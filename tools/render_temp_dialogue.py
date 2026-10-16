"""Make temporary Persian TTS takes from canonical scene text using local eSpeak NG."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile
import wave


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('episode', type=Path)
parser.add_argument('--ffmpeg', required=True)
args = parser.parse_args()
root = args.episode.resolve()

def main():
    entries = []
    prior_file = root / 'audio/dialogue/takes-v1.json'
    prior = {line['id']: line for line in json.loads(prior_file.read_text())['takes']} if prior_file.exists() else {}
    for scene in sorted(root.glob('scenes/*/scene.md')):
        text = scene.read_text()
        pattern = r'### `(EP\d+-D\d+)` — ([^\n]+)\n(.*?)(?=\n<a id=|\n## |\Z)'
        for match in re.finditer(pattern, text, re.S):
            ident, speaker, block = match.groups()
            words = re.search(r'- متن: «(.*?)»', block).group(1)
            window = re.search(r'جای پیشنهادی: `(\d+:\d+)–(\d+:\d+)`', block)
            def seconds(s):
                minute, sec = map(int, s.split(':'))
                return minute * 60 + sec
            start, end = map(seconds, window.groups())
            who = 'girl' if speaker == 'دختر' else 'younes'
            voice = 'fa+f3' if who == 'girl' else 'fa+m3'
            dest = root / 'audio/dialogue' / f'{ident}-{who}-t01.wav'
            dest.parent.mkdir(parents=True, exist_ok=True)
            fingerprint = hashlib.sha256(words.encode()).hexdigest()
            if dest.exists() and (ident not in prior or prior[ident]['text_sha256'] != fingerprint):
                raise ValueError(f'{ident}: existing take does not match canonical text; create a new take version')
            # Never overwrite an existing take. Retakes require a new filename.
            if not dest.exists():
                with tempfile.TemporaryDirectory(prefix='movie-tts-') as folder:
                    media = Path(folder) / 'speech.wav'
                    subprocess.run(['espeak-ng', '-v', voice, '-s', '160', '-p', '45' if who == 'younes' else '58', '-w', str(media), words], check=True)
                    subprocess.run([args.ffmpeg, '-y', '-loglevel', 'error', '-i', str(media), '-af', 'silenceremove=start_periods=1:start_duration=0.02:start_threshold=-45dB', '-ar', '24000', '-ac', '1', str(dest)], check=True)
            with wave.open(str(dest)) as wav:
                duration = wav.getnframes() / wav.getframerate()
            entries.append(dict(id=ident, speaker=who, voice=voice, file=dest.relative_to(root).as_posix(), source=scene.relative_to(root).as_posix() + '#' + ident.lower(), text_sha256=hashlib.sha256(words.encode()).hexdigest(), start=start, planned_end=end, duration=round(duration, 4), fits_planned_window=duration <= end-start, auditioned=False, approved_voice=False))
            print(f'{ident}: {duration:.2f}s, window {end-start:.2f}s', flush=True)
    (root / 'audio/dialogue/takes-v1.json').write_text(json.dumps(dict(provider='eSpeak NG 1.52.0; robotic Persian timing placeholders, not actor performances', no_paid_generation_used=True, takes=entries), ensure_ascii=False, indent=2) + '\n')

main()
