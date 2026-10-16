"""Local EP02 pause review. Preserve speech speed/sync; cover internal cuts with silent live listener footage."""
from pathlib import Path
import argparse,json,subprocess,sys,hashlib,os
ap=argparse.ArgumentParser();ap.add_argument('--deps-dir',required=True);ap.add_argument('--ffmpeg-deps-dir',required=True);ap.add_argument('--version',default='v2');args=ap.parse_args()
sys.path[:0]=[args.deps_dir,args.ffmpeg_deps_dir]
import numpy as np,av,imageio_ffmpeg
from PIL import Image,ImageDraw
from shot_workflow import P,selected_plan,sha
import re
assert re.fullmatch(r'v\d+',args.version)
E=P/'episodes/episode-02';out=E/'edit'/args.version
assert not out.exists(),'Output version already exists'
old=json.loads((E/'edit/v1/timeline.json').read_text(encoding='utf8'))
original_hash=sha(E/'edit/v1/EP02-SC02-review-v1.mp4')
plan=selected_plan(2);byshot={r['shot']:r for r in old['timeline']}
assert [r['shot'] for r in plan]==[r['shot'] for r in old['timeline']]
for row in plan:assert row['sha256']==byshot[row['shot']]['sha256'],'Selected source changed; review pauses again'
out.mkdir(parents=True);ff=imageio_ffmpeg.get_ffmpeg_exe();pieces=[];timeline=[];cursor=0.;sheet=Image.new('RGB',(1200,15*420),'#eeeeee');draw=ImageDraw.Draw(sheet)
listeners={'EP02-SH01':('EP02-SH02',.05),'EP02-SH02':('EP02-SH01',1.55),'EP02-SH04':('EP02-SH05',.20),'EP02-SH07':('EP02-SH08',.20),'EP02-SH08':('EP02-SH05',.20)}
base_encode=['-vf','scale=360:640:force_original_aspect_ratio=decrease,pad=360:640:(ow-iw)/2:(oh-ih)/2,fps=30,setsar=1','-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-c:a','aac','-ar','48000','-ac','2','-b:a','160k','-movflags','+faststart']
def audio(src):return np.frombuffer(subprocess.run([ff,'-v','error','-i',str(src),'-vn','-ac','1','-ar','16000','-f','f32le','-'],capture_output=True,check=True).stdout,dtype=np.float32)
def db_peak(a,start,end):
 chunk=a[max(0,int(start*16000)):int(end*16000)]
 if not len(chunk):return -120.
 windows=np.array_split(chunk,max(1,len(chunk)//320));return float(20*np.log10(max(float(np.sqrt(np.mean(w*w)+1e-12)) for w in windows)))
def encode(src,start,end,dest,listener=None):
 dur=end-start;cmd=[ff,'-v','error','-n']
 if listener:
  lsrc,lstart=listener;cmd+=['-ss',str(lstart),'-i',str(lsrc),'-ss',str(start),'-i',str(src),'-t',str(dur),'-map','0:v:0','-map','1:a:0']
 else:cmd+=['-ss',str(start),'-i',str(src),'-t',str(dur)]
 cmd+=base_encode+['-af',f'afade=t=in:d=0.003,afade=t=out:st={max(0,dur-.003)}:d=0.003',str(dest)]
 subprocess.run(cmd,check=True)
 c=av.open(str(dest));actual=c.duration/av.time_base;c.close();return actual
for index,row in enumerate(plan):
 sid=row['shot'];record=byshot[sid];src=P/row['source'];a=audio(src)
 speech=[(x['start']/16000,x['end']/16000) for x in record['speech_ranges']]
 start=max(row['in'],speech[0][0]-.10);end=min(row['out'],speech[-1][1]+.14)
 # Trim outer audio only if the removed samples are quiet; uncertain material stays.
 if db_peak(a,row['in'],start)>-32:start=row['in']
 if db_peak(a,end,row['out'])>-32:end=row['out']
 cuts=[]
 if sid in listeners:
  for left,right in zip(speech,speech[1:]):
   if right[0]-left[1]<.65:continue
   lo=left[1]+.12;hi=right[0]-.12
   if db_peak(a,lo,hi)>-32:continue
   lid,li=listeners[sid];lsrc=P/byshot[lid]['source'];la=audio(lsrc)
   assert db_peak(la,li,li+.25)<-30,'Listener region is not silent'
   cuts.append({'remove_in':lo,'remove_out':hi,'original_gap':right[0]-left[1],'replacement_seconds':.25,'listener_shot':lid,'listener_source':lsrc.relative_to(P).as_posix(),'listener_in':li,'listener_out':li+.25,'silence_peak_db':db_peak(a,lo,hi),'saved_seconds':hi-lo-.25})
 root=E/'shots'/sid/'takes'/row['take']/'edits'/args.version;assert not root.exists();root.mkdir(parents=True)
 segments=[];pos=start;part=0
 def add(lo,hi,cut=None):
  global part,cursor
  part+=1;dest=root/f'part-{part:02d}.mp4';listener=(P/cut['listener_source'],cut['listener_in']) if cut else None
  seconds=encode(src,lo,hi,dest,listener)
  segments.append({'kind':'silent_listener_cutaway' if cut else 'original_synced_speech','source':row['source'],'in':lo,'out':hi,'file':dest.relative_to(P).as_posix(),'output_seconds':seconds,'listener':cut,'timeline_in':cursor,'timeline_out':cursor+seconds});pieces.append(dest);cursor+=seconds
 for cut in cuts:
  add(pos,cut['remove_in']);add(cut['remove_in'],cut['remove_in']+.25,cut);pos=cut['remove_out']
 add(pos,end)
 concat=root/'concat.txt';concat.write_text('\n'.join("file '"+Path(s['file']).name+"'" for s in segments),encoding='utf8')
 shotvideo=root/(sid+'-pause-review.mp4');subprocess.run([ff,'-v','error','-n','-f','concat','-safe','0','-i',str(concat),'-c','copy','-movflags','+faststart',str(shotvideo)],check=True)
 entry={'shot':sid,'take':row['take'],'source':row['source'],'sha256':row['sha256'],'original_in':row['in'],'original_out':row['out'],'in':start,'out':end,'pause_cuts':cuts,'segments':segments,'review_video':shotvideo.relative_to(P).as_posix(),'speed':1.0,'status':'local review only; user acceptance pending'}
 (root/'pause-review.json').write_text(json.dumps(entry,ensure_ascii=False,indent=2)+'\n',encoding='utf8');timeline.append(entry)
 c=av.open(str(shotvideo));frames=list(c.decode(video=0));c.close()
 for j,frac in enumerate([0,.2,.4,.6,.8,.98]):
  fr=frames[min(len(frames)-1,int(len(frames)*frac))];im=fr.to_image();im.thumbnail((195,375));sheet.paste(im,(j*200,index*420+30));draw.text((j*200+5,index*420+5),sid+f' {fr.time:.2f}s',fill='black')
 print(sid,'removed',round(row['out']-row['in']-sum(s['out']-s['in'] for s in segments),3),'internal cuts',len(cuts),flush=True)
(out/'concat.txt').write_text('\n'.join("file '"+os.path.relpath(x,out).replace('\\','/')+"'" for x in pieces),encoding='utf8')
final=out/'EP02-faster-pause-review.mp4';subprocess.run([ff,'-v','error','-n','-f','concat','-safe','0','-i',str(out/'concat.txt'),'-vf','fps=30','-c:v','libx264','-preset','fast','-crf','19','-pix_fmt','yuv420p','-c:a','aac','-ar','48000','-ac','2','-b:a','160k','-movflags','+faststart',str(final)],check=True)
for k in range(5):sheet.crop((0,k*3*420,1200,(k+1)*3*420)).save(out/f'motion-review-{k+1}.jpg',quality=90)
c=av.open(str(final));seconds=c.duration/av.time_base;vf=sum(1 for _ in c.decode(video=0));c.close();c=av.open(str(final));af=sum(1 for _ in c.decode(audio=0));c.close();assert vf and af
assert sha(E/'edit/v1/EP02-SC02-review-v1.mp4')==original_hash
report={'episode':'EP02','output':final.relative_to(P).as_posix(),'status':'faster local review; not final approval','original_seconds':old['actual_seconds'],'actual_seconds':seconds,'saved_seconds':old['actual_seconds']-seconds,'decoded_video_frames':vf,'decoded_audio_frames':af,'speed':1.0,'paid_actions':0,'timeline':timeline,'limitations':['No regenerated speech or completed words. SH13 remains the selected old take02.','Speech spans retained using existing VAD plus low-energy boundary checks; this is not proof of exact pronunciation.','Silent live listener cutaways cover internal discontinuities; visual samples and user review still required.']}
(out/'timeline.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf8');print('FINAL',seconds,'SAVED',report['saved_seconds'],flush=True)
