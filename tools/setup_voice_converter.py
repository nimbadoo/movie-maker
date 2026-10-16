#!/usr/bin/env python3
"""Prepare an isolated, pinned OpenVoice converter without generation credits."""
import hashlib
import json
import subprocess
import urllib.request
from pathlib import Path

REVISION = '74a1d147b17a8c3092dd5430504bd83ef6c7eb23'
MODEL_SHA = '9652c27e92b6b2a91632590ac9962ef7ae2b712e5c5b7f4c34ec55ee2b37ab9e'


def main():
    root = Path.home() / '.cache/movie-maker/openvoice-v2'
    (root / 'openvoice').mkdir(parents=True, exist_ok=True)
    (root / 'converter').mkdir(exist_ok=True)
    files = ['openvoice/' + x for x in (
        '__init__.py', 'api.py', 'utils.py', 'commons.py', 'mel_processing.py',
        'models.py', 'modules.py', 'attentions.py', 'transforms.py')] + ['LICENSE']
    for name in files:
        url = f'https://raw.githubusercontent.com/myshell-ai/OpenVoice/{REVISION}/{name}'
        with urllib.request.urlopen(url, timeout=60) as response:
            data = response.read()
        if name == 'openvoice/api.py':
            data = data.replace(b'from openvoice.text import text_to_sequence',
                                b'# Unused TTS frontend excluded in conversion-only adapter.')
            data = data.replace(b"device='cuda:0'):", b"device='cuda:0', **kwargs):")
        (root / name).write_bytes(data)
    for name in ('config.json', 'checkpoint.pth'):
        path = root / 'converter' / name
        if name == 'checkpoint.pth' and path.exists() and hashlib.sha256(path.read_bytes()).hexdigest() == MODEL_SHA:
            continue
        url = f'https://huggingface.co/myshell-ai/OpenVoiceV2/resolve/main/converter/{name}'
        temporary = path.with_suffix('.download')
        urllib.request.urlretrieve(url, temporary)
        if name == 'checkpoint.pth' and hashlib.sha256(temporary.read_bytes()).hexdigest() != MODEL_SHA:
            raise RuntimeError('Checkpoint hash mismatch; refusing to load it.')
        temporary.replace(path)
    (root / 'source.json').write_text(json.dumps(dict(repository='https://github.com/myshell-ai/OpenVoice',
        revision=REVISION, checkpoint_sha256=MODEL_SHA,
        local_adaptations=['Exclude unused TTS frontend', 'Accept optional converter kwargs']), indent=2))
    environment = root / 'venv'
    if not (environment / 'bin/python').exists():
        subprocess.run(['uv', 'venv', '--python', '3.10', str(environment)], check=True)
    subprocess.run(['uv', 'pip', 'install', '--python', str(environment / 'bin/python'),
                    'torch==2.5.1', 'numpy==2.2.6', 'scipy==1.13.1',
                    'librosa==0.10.2', 'soundfile==0.14.0'], check=True)
    print(root)


if __name__ == '__main__':
    main()
