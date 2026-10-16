"""Build copyable Flow prompts from scene-owned templates and canonical dialogue. No media/API calls."""
import argparse
import hashlib
import json
from pathlib import Path
import re

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('pack', type=Path)
args = parser.parse_args()
pack = args.pack.resolve()
manifest = json.loads((pack/'manifest.json').read_text())
output = pack/'prompts'
output.mkdir(exist_ok=True)
look = ('Photorealistic Iranian rural drama, vertical 9:16. Soft angled morning light, muted earth and stone, natural skin and fabric textures. '
        'Maintain the approved identity, prop shapes, screen direction and location geometry. No glamour treatment, extra characters, fantasy glow, titles, logos or subtitles. ')
build = {'kind':'derived prompt export; edit scene.md, then rebuild', 'media_generated':False, 'shots':[]}
for shot in manifest['shots']:
    source = (pack/shot['source']).resolve()
    text = source.read_text()
    details = {'id':shot['id'], 'source':shot['source'], 'source_sha256':hashlib.sha256(text.encode()).hexdigest(), 'exports':[]}
    for kind,heading in [('start-frame','قالب قاب شروع'),('video','قالب ویدئو')]:
        pattern = rf'### {heading} `{re.escape(shot["id"])}`\s+```text\n(.*?)\n```'
        match = re.search(pattern,text,re.S)
        if not match:
            raise ValueError(f'Missing {kind} template: {shot["id"]}')
        prompt = match.group(1)
        dialogue_sources=[]
        def replace_dialogue(match):
            ident = match.group(1)
            canonical = re.search(rf'### `{re.escape(ident)}` — [^\n]+\n(.*?)(?=\n<a id=|\n## |\Z)',text,re.S)
            if not canonical:
                raise ValueError(f'Dialogue source missing: {ident}')
            words = re.search(r'- متن: «([^»]+)»',canonical.group(1)).group(1)
            dialogue_sources.append(ident)
            return words
        prompt = re.sub(r'\{\{DIALOGUE:([^}]+)\}\}',replace_dialogue,prompt)
        if '{{' in prompt:
            raise ValueError(f'Unresolved template: {shot["id"]}')
        if kind == 'video':
            prompt = look + '\n\nAnimate the approved starting frame. ' + prompt
        else:
            prompt = look + '\n\n' + prompt
        dest = output / f'{shot["id"]}-{kind}.txt'
        dest.write_text(prompt+'\n')
        details['exports'].append({'file':dest.relative_to(pack).as_posix(), 'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'dialogue_sources':dialogue_sources})
    build['shots'].append(details)
(pack/'build-manifest.json').write_text(json.dumps(build,ensure_ascii=False,indent=2)+'\n')
print(f'{len(build["shots"])} shot cards, {len(build["shots"])*2} prompt files. No generation submitted.')
