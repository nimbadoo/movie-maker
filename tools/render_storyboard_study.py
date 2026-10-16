"""Render a silent still-frame study from a JSON timeline; no AI motion is created."""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('timeline', type=Path)
parser.add_argument('--ffmpeg', default='ffmpeg')
args = parser.parse_args()
timeline = args.timeline.resolve()
data = json.loads(timeline.read_text())
output = timeline.parent / data['output']
with tempfile.TemporaryDirectory(prefix='movie-storyboard-') as folder:
    concat = Path(folder) / 'frames.ffconcat'
    lines = ['ffconcat version 1.0']
    for item in data['frames']:
        source = (timeline.parent / item['image']).resolve()
        if not source.is_file():
            raise FileNotFoundError(source)
        escaped = str(source).replace("'", "'\\''")
        lines.extend([f"file '{escaped}'", f"duration {item['seconds']}"])
    lines.append(lines[-2])
    concat.write_text('\n'.join(lines) + '\n')
    duration = sum(item['seconds'] for item in data['frames'])
    subprocess.run([args.ffmpeg, '-y', '-hide_banner', '-loglevel', 'warning',
        '-f', 'concat', '-safe', '0', '-i', str(concat),
        '-vf', 'scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24,tpad=stop_mode=clone:stop_duration=5',
        '-r', '24', '-frames:v', str(round(duration * 24)), '-an', '-c:v', 'libx264',
        '-preset', 'medium', '-crf', '20', '-pix_fmt', 'yuv420p',
        '-movflags', '+faststart', str(output)], check=True)
print(output)
print(f'{duration} seconds; silent still-frame study, not finished episode')
