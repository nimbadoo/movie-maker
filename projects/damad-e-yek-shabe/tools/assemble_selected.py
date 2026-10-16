"""Local assembly from explicit card selections, never the latest take record."""
import argparse,json,subprocess,sys
from pathlib import Path
from shot_workflow import P,selected_plan
def main(default_episode=None):
 ap=argparse.ArgumentParser();ap.add_argument('--episode',type=int,default=default_episode,required=default_episode is None);ap.add_argument('--output-version',required=True);ap.add_argument('--ffmpeg-deps-dir',required=True);args=ap.parse_args()
 import re
 if not re.fullmatch(r'v\d+',args.output_version):raise SystemExit('Use a fresh vNN output version')
 plan=selected_plan(args.episode)
 out=P/f'episodes/episode-{args.episode:02d}/edit'/args.output_version
 if out.exists():raise SystemExit('Refusing to overwrite existing assembly')
 for entry in plan:
  root=P/f'episodes/episode-{args.episode:02d}/shots/{entry["shot"]}/takes'/entry['take']/'edits'/args.output_version
  if root.exists():raise SystemExit('Refusing to overwrite existing shot edit: '+str(root))
 sys.path.insert(0,args.ffmpeg_deps_dir);import imageio_ffmpeg
 ff=imageio_ffmpeg.get_ffmpeg_exe();out.mkdir(parents=True);pieces=[]
 for entry in plan:
  sid=entry['shot'];root=P/f'episodes/episode-{args.episode:02d}/shots/{sid}/takes'/entry['take']/'edits'/args.output_version
  if root.exists():raise SystemExit('Refusing to overwrite shot edit')
  root.mkdir(parents=True);dest=root/(sid+'.mp4');dur=entry['out']-entry['in']
  subprocess.run([ff,'-v','error','-n','-ss',str(entry['in']),'-i',str(P/entry['source']),'-t',str(dur),'-vf','scale=360:640:force_original_aspect_ratio=decrease,pad=360:640:(ow-iw)/2:(oh-ih)/2,fps=30,setsar=1','-c:v','libx264','-crf','19','-pix_fmt','yuv420p','-c:a','aac','-ar','48000','-ac','2','-movflags','+faststart',str(dest)],check=True);pieces.append(dest)
 import os
 (out/'concat.txt').write_text('\n'.join("file '"+os.path.relpath(x,out).replace('\\','/')+"'" for x in pieces),encoding='utf8')
 final=out/f'EP{args.episode:02d}-review.mp4'
 subprocess.run([ff,'-v','error','-n','-f','concat','-safe','0','-i',str(out/'concat.txt'),'-c','copy','-movflags','+faststart',str(final)],check=True)
 (out/'timeline.json').write_text(json.dumps({'output':final.name,'status':'new local review; final acceptance pending','timeline':plan},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
 print(final)
if __name__=='__main__':main()
