"""Render a silent MVP using existing photos and explicitly simulated camera moves."""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('timeline', type=Path)
parser.add_argument('--ffmpeg', default='ffmpeg')
args = parser.parse_args()
path = args.timeline.resolve()
data = json.loads(path.read_text())
def run(argv):
    subprocess.run([args.ffmpeg, '-y', '-hide_banner', '-loglevel', 'error', *argv], check=True)
with tempfile.TemporaryDirectory(prefix='movie-mvp-') as folder:
    work = Path(folder)
    start = 0
    clips = []
    for index, shot in enumerate(data['frames'], 1):
        frames = shot['seconds'] * 24
        label = work / f'{index:02d}.txt'
        label.write_text(f'EP01 / SH{index:02d}   {start:02d}-{start+shot["seconds"]:02d}s\n{shot["label"]}\n{shot["coverage"]}\nMVP / SILENT / DIGITAL MOVE / NOT FINAL\n')
        z = '1+0.06*on/' + str(frames-1)
        if shot['motion'] == 'pull_out':
            z = '1.06-0.06*on/' + str(frames-1)
        if shot['motion'] == 'pan_right':
            z = '1.06'
        x = f'(iw-iw/zoom)*on/{frames-1}' if shot['motion'] == 'pan_right' else '(iw-iw/zoom)/2'
        filters = [shot['crop']] if shot.get('crop') else []
        filters += ['scale=720:1280:force_original_aspect_ratio=decrease',
                    'pad=720:1280:(ow-iw)/2:(oh-ih)/2', 'setsar=1',
                    'scale=1440:2560',
                    f"zoompan=z='{z}':x='{x}':y='(ih-ih/zoom)/2':d={frames}:s=720x1280:fps=24",
                    'drawbox=x=0:y=1080:w=iw:h=200:color=black@0.86:t=fill',
                    f"drawtext=fontfile='/System/Library/Fonts/Supplemental/Arial.ttf':textfile='{label}':x=24:y=1100:fontsize=23:fontcolor=white:line_spacing=14"]
        clip = work / f'{index:02d}.mp4'
        run(['-i',str((path.parent/shot['image']).resolve()),'-vf',','.join(filters),
             '-frames:v',str(frames),'-an','-c:v','libx264','-preset','fast','-crf','25','-pix_fmt','yuv420p',str(clip)])
        clips.append(clip)
        start += shot['seconds']
    concat = work/'clips.ffconcat'
    concat.write_text('ffconcat version 1.0\n'+'\n'.join(f"file '{p}'" for p in clips)+'\n')
    run(['-f','concat','-safe','0','-i',str(concat),'-c','copy','-movflags','+faststart',str(path.parent/data['output'])])
print(f'{start}s; {len(clips)} reference shots; digital motion only; zero cloud credits')
