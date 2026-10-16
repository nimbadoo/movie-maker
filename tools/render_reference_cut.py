"""Lay out numbered reference cards, then render a silent timing cut. No generation."""
import argparse
import json
from pathlib import Path
import subprocess
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('timeline', type=Path)
parser.add_argument('--ffmpeg', default='ffmpeg')
parser.add_argument('--font', default='/System/Library/Fonts/Supplemental/Arial.ttf')
args = parser.parse_args()
timeline = args.timeline.resolve()
data = json.loads(timeline.read_text())
cards = timeline.parent / data['cards_dir']
cards.mkdir(parents=True, exist_ok=True)
render_data = {'output': data['output'], 'frames': []}
start = 0
for index, shot in enumerate(data['frames'], 1):
    source = (timeline.parent / shot['image']).resolve()
    seconds = shot['seconds']
    heading = f"EP01 / SH{index:02d}     {start:02d}-{start+seconds:02d}s     {seconds}s"
    label = cards / f'SH{index:02d}.txt'
    label.write_text(heading + '\n' + shot['label'] + '\n' + shot['coverage'] + '\nSILENT REFERENCE STUDY - NOT FINAL FOOTAGE\n')
    image = cards / f'SH{index:02d}.png'
    filters = []
    if shot.get('crop'):
        filters.append(shot['crop'])
    filters += ['scale=720:1280:force_original_aspect_ratio=decrease',
                'pad=720:1280:(ow-iw)/2:(oh-ih)/2', 'setsar=1',
                'drawbox=x=0:y=1080:w=iw:h=200:color=black@0.86:t=fill',
                f"drawtext=fontfile='{args.font}':textfile='{label}':x=24:y=1100:fontsize=23:fontcolor=white:line_spacing=14"]
    subprocess.run([args.ffmpeg, '-y', '-hide_banner', '-loglevel', 'error',
                    '-i', str(source), '-vf', ','.join(filters), '-frames:v', '1',
                    '-update', '1', str(image)], check=True)
    render_data['frames'].append({'image': str(image.relative_to(timeline.parent)),
                                 'seconds': seconds})
    start += seconds
render_file = cards / 'render-timeline.json'
render_data['output'] = '../' + data['output']
# Render helper resolves paths relative to its own JSON.
for item in render_data['frames']:
    item['image'] = Path(item['image']).name
render_file.write_text(json.dumps(render_data, indent=2) + '\n')
subprocess.run([sys.executable, str(Path(__file__).with_name('render_storyboard_study.py')),
                str(render_file), '--ffmpeg', args.ffmpeg], check=True)
print(f'{len(data["frames"])} shots / {start} seconds / no sound / no cloud credits')
