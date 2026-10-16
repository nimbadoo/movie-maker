from pathlib import Path
import json,math,re,html,os,hashlib
import numpy as np
P=Path(__file__).resolve().parents[3];E=P/'episodes/episode-05';R=E/'references';R.mkdir(exist_ok=True)
plan=json.loads((E/'edit/timing-plan-sandwich-v1.json').read_text(encoding='utf-8'))
# Coordinates are local design units; no claim of measured apartment dimensions.
people={'M':{'name':'مادر','p':[-.8,1.6],'color':'#80364a','standing':False},'F':{'name':'فرهاد','p':[.8,1.6],'color':'#d4bd98','standing':False},'N':{'name':'نازلی','p':[-1.1,-1.05],'color':'#207a78','standing':True},'S':{'name':'سامان','p':[1.1,-1.05],'color':'#3a6497','standing':True}}
cameras={'F':{'p':[2.8,-1.3,1.95],'target':[.8,1.6,1.75],'vfov':28,'label':'کنار بیرونی سامان، رو به فرهاد؛ شرق محور','background':'آشپزخانه و دیوار شمالی پشت فرهاد؛ جوان‌ها خارج برش، نه حذف‌شده.'},'B':{'p':[2.6,2.6,2.5],'target':[0,-1.05,1.55],'vfov':56,'label':'کنار بیرونی فرهاد، رو به دو جوان ایستاده','background':'آشپزخانه پشت دوربین؛ دیوار جنوب، تلویزیون در چپ تصویر و پنجره در راست.'},'N':{'p':[2.6,1.8,2.55],'target':[-1.1,-1.05,2.25],'vfov':26,'label':'همان نیم‌صفحهٔ شرقی، نزدیک نازلی','background':'سمت جنوب/غرب؛ پنجره در حاشیهٔ راست ممکن، آشپزخانه پشت دوربین و ممنوع در پس‌زمینه.'},'S':{'p':[2.8,.8,2.5],'target':[1.1,-1.05,2.25],'vfov':34,'label':'شرق سامان، نزدیک با ارتفاع چشم ایستاده','background':'دیوار جنوب؛ فقط لبهٔ تلویزیون شرق اگر در میدان واقعی جا شد؛ آشپزخانه پشت دوربین.'},'M':{'p':[2.6,-.7,1.95],'target':[-.8,1.6,1.75],'vfov':27,'label':'شرق و جنوب کاناپه، رو به مادر نشسته','background':'آشپزخانه پشت مادر؛ فرهاد در سمت ثابت دیگر کاناپه خارج برش است.'},'FW':{'p':[3,-1.6,1.95],'target':[.8,1.6,1.35],'vfov':42,'label':'ایستگاه فرهاد، کمی بازتر برای آغاز بلندشدن','background':'کاناپه و آشپزخانه؛ دست‌ها روی ران خود فرهاد، هیچ دست همراه از خارج قاب.'}}
# All cameras are on the east half-plane; no furniture is moved for framing.
specs=[('EP05-SH02','F','F','S','ثابت؛ بازپخش منبع موجود','فرهاد نشسته، نگاه بالا به سامان ایستاده؛ هیچ پاسخ دختر در این بازپخش نباشد.'),('EP05-SH03','N','N','F','ثابت','نازلی ایستاده؛ پاسخ کوتاه رو به فرهاد، سپس نگاه کوتاه به سامان؛ دست‌ها پایین.'),('EP05-SH05','B','S','M','ثابت؛ معرفی رابطهٔ فضایی','سامان چپ تصویر و نازلی راست؛ هر دو جلوی صندلی خود ایستاده؛ سامان از فرهاد به مادر و نازلی نگاه می‌برد.'),('EP05-SH06','N','N','S','ثابت','نازلی شوخی را به سامان می‌گوید؛ فقط سر و چشم به او بچرخد، پا و صندلی ثابت.'),('EP05-SH07','S','S','N','پیشروی بسیار کوتاه روی محور لنز، حداکثر ۴درصد تغییر اندازه؛ اجرای واقعی هنوز بررسی نشده','سامان با خجالت مختصر جواب می‌دهد؛ دست به دهان نمی‌برد، آب یا ساندویچ در زمان حال ظاهر نمی‌شود.'),('EP05-SH08','M','M','S','ثابت','مادر نشسته، نگاه بالا به چشم سامان؛ دست‌های خودش روی پا، روسری تک‌لایه و بدون حرکت نمایشی.'),('EP05-SH10','S','S','M','ثابت؛ همان سوی محور نمای جواب سامان','سامان مؤدبانه رو به مادر؛ پایان جمله لب‌ها بسته و لبخند کوتاه؛ سپس خندهٔ مادر و نازلی خارج قاب در همان دنباله.'),('EP05-SH14','FW','F','M','ثابت','فرهاد ابتدا نشسته؛ نگاه به مادر و جمع؛ در پایان به جلو متمایل و شروع به بلندشدن می‌کند، بدون اخم. خروج کامل در این نما الزام ندارد.'),('EP05-SH15','M','M','F','ثابت؛ تغییر مخاطب با سر و چشم','مادر اول به فرهاد در حال بلندشدن، سپس به سامان نگاه کند. فرهاد از کنارهٔ شرقی میز به سمت راهرو برود؛ گذر از وسط میز و نشان‌دادن در ممنوع.')]
shots=[]
for sid,cam,sp,listener,movement,action in specs:
 card=E/f'shots/{sid}/shot.md';s=card.read_text(encoding='utf-8');text=re.search(r'^- متن: «(.*)»$',s,re.M)[1]
 t=next(x for x in plan['timeline'] if x.get('shot')==sid)
 shots.append({'shot':sid,'camera':cam,'speaker':sp,'listener':listener,'text':text,'start':t['start_seconds'],'end':t['end_seconds'],'movement':movement,'action':action,'schematic':f'shots/{sid}/images/{sid}-blocking-v1.svg','kind':'diagram_not_production_image','status':'proposed_camera_and_blocking_only','inputs':{'space':'house/apartment-cutaway-v2.png','plan':'house/apartment-plan-v1.svg','appearance':'references/visuals/character-bible.md'},'active_frame_changed':False})
# End reaction remains inside SH15 owner; no renumbering of dialogue shots.
shots.append({'shot':'EP05-SH15-END','camera':'B','speaker':None,'listener':None,'text':'بدون دیالوگ؛ نگاه نگران نازلی به سامان','start':43.291667,'end':44.541667,'movement':'ثابت؛ برش به دونفره با همان جای پا','action':'نازلی سمت راست تصویر نگاه را به سامانِ چپ می‌برد؛ سامان نگاه او را می‌بیند. صندلی‌ها خالی و ثابت‌اند؛ دست‌ها پایین و هیچ نشستن مجددی نیست.','schematic':'shots/EP05-SH15/images/EP05-SH15-ending-blocking-v1.svg','kind':'diagram_not_production_image','status':'proposed_camera_and_blocking_only','active_frame_changed':False})
W,H=360,640

def project(points,c):
 pos=np.array(c['p']);forward=np.array(c['target'])-pos;forward=forward/np.linalg.norm(forward);right=np.cross(forward,[0,0,1]);right=right/np.linalg.norm(right);up=np.cross(right,forward);f=H/2/math.tan(math.radians(c['vfov'])/2)
 out=[]
 for pt in points:
  v=np.array(pt)-pos;z=float(v@forward)
  if z<=.08:return None
  out.append((W/2+float(v@right)*f/z,H/2-float(v@up)*f/z,z))
 return out

def face(points,c,color,stroke='#584f46'):
 p=project(points,c)
 if p is None:return ''
 return '<polygon points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y,z in p)+f'" fill="{color}" stroke="{stroke}" stroke-width="1.2"/>'

def box(x,y,z,w,dep,h,c,col,angle=0):
 a=math.radians(angle)
 def pt(dx,dy,dz):return [x+dx*math.cos(a)-dy*math.sin(a),y+dx*math.sin(a)+dy*math.cos(a),z+dz]
 pts=[pt(dx,dy,dz) for dx,dy,dz in [(-w/2,-dep/2,0),(w/2,-dep/2,0),(w/2,dep/2,0),(-w/2,dep/2,0),(-w/2,-dep/2,h),(w/2,-dep/2,h),(w/2,dep/2,h),(-w/2,dep/2,h)]]
 surfaces=[[0,1,5,4],[1,2,6,5],[2,3,7,6],[3,0,4,7],[4,5,6,7]]
 surfaces.sort(key=lambda f:sum((np.array(pts[i])-np.array(c['p']))@(np.array(c['target'])-np.array(c['p'])) for i in f),reverse=True)
 return ''.join(face([pts[i] for i in inds],c,col) for inds in surfaces)

def line(points,c,color,width=2,dash=False):
 p=project(points,c)
 if p is None:return ''
 return '<polyline points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y,z in p)+f'" fill="none" stroke="{color}" stroke-width="{width}" stroke-linecap="round"'+(' stroke-dasharray="5 4"' if dash else '')+'/>'

def person(key,c,speaker,listener,end=False):
 info=people[key];x,y=info['p'];standing=info['standing'];head=2.65 if standing else 1.8;neck=head-.24;hip=1.2 if standing else .65;shoulder=neck-.12
 s=face([[x-.23,y,shoulder],[x+.23,y,shoulder],[x+.20,y,hip],[x-.20,y,hip]],c,info['color'],'#27394a')
 # Simplified figures deliberately omit face identity, fingers and fabric detail.
 for side in [-1,1]:
  s+=line([[x+side*.23,y,shoulder],[x+side*.30,y-.02,hip+.10],[x+side*.26,y-.02,hip-.08]],c,info['color'],9)
  legs=[[x+side*.12,y,hip],[x+side*.16,y, .63],[x+side*.16,y-.03,.07]] if standing else [[x+side*.12,y,hip],[x+side*.17,y-.5,.58],[x+side*.17,y-.5,.07]]
  s+=line(legs,c,'#26313c',9)
 pts=project([[x,y,head],[x+.2,y,head]],c)
 if pts:
  cx,cy,z=pts[0];radius=max(5,abs(pts[1][0]-cx));s+=f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{radius:.2f}" fill="#c9b59c" stroke="#28323a" stroke-width="2"/>'
  if speaker==key:s+=f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{radius+5:.2f}" fill="none" stroke="#d2a743" stroke-width="2"/>'
  if -80<cx<440 and -50<cy<700:s+=f'<text x="{cx:.1f}" y="{cy+radius+20:.1f}" text-anchor="middle" fill="#11293d" font-size="15" font-weight="700">{info["name"]}</text>'
 if speaker==key and listener:
  lx,ly=people[listener]['p'];lh=2.65 if people[listener]['standing'] else 1.8;v=np.array([lx-x,ly-y,lh-head]);v=v/np.linalg.norm(v)*.45
  s+=line([[x,y,head],np.array([x,y,head])+v],c,'#007d89',3)
 return s

def render(shot):
 c=cameras[shot['camera']];shapes=[];cp=np.array(c['p']);fw=np.array(c['target'])-cp;fw=fw/np.linalg.norm(fw)
 def add(center,draw):shapes.append((float((np.array(center)-cp)@fw),draw))
 # Fixed architecture; drawn only when physically in front of camera.
 add([0,4,1.3],box(-1,4,0,3.4,.6,2.5,c,'#a4b0a0'))
 add([0,1.65,.5],box(0,1.65,0,3.3,1, .65,c,'#c7b79a')+box(0,2.0,.65,3.3,.25,.7,c,'#d0bfa0'))
 add([0,0,.6],box(0,0,0,2.0,1.0,.7,c,'#a97f53'))
 # Table props have fixed positions and never enter hands.
 add([0,0,.85],box(.40,.05,.70,.40,.30,.12,c,'#b49656')+box(-.62,0,.70,.50,.36,.03,c,'#825f3c')+box(.72,-.18,.70,.12,.12,.18,c,'#a66539'))
 for x,angle in [(-1.1,-45),(1.1,45)]:
  add([x,-1.95,.6],box(x,-1.95,0,1.0,1.0,.65,c,'#7e967a',angle)+box(x+.425*math.sin(math.radians(angle)),-1.95-.425*math.cos(math.radians(angle)),.65,1.0,.15,.85,c,'#8fa383',angle))
 add([-3.8,-.5,1.6],box(-3.8,-.5,.5,.08,2.1,2.0,c,'#b6d1d3'))
 add([3.8,-.5,1.2],box(3.8,-.5,.7,.08,1.7,1.2,c,'#2b3e44'))
 for k,info in people.items():add([*info['p'],1.3],person(k,c,shot['speaker'],shot['listener']))
 shapes.sort(key=lambda x:x[0],reverse=True)
 s=f'<svg xmlns="http://www.w3.org/2000/svg" width="360" height="640" viewBox="0 0 360 640"><defs><linearGradient id="bg" x2="0" y2="1"><stop stop-color="#eee4d3"/><stop offset="1" stop-color="#c8ac87"/></linearGradient><clipPath id="fr"><rect width="360" height="640"/></clipPath></defs><rect width="360" height="640" fill="url(#bg)"/><g clip-path="url(#fr)">'
 for yy in np.arange(-3,5,.5):s+=line([[-4,float(yy),0],[4,float(yy),0]],c,'#c3ae92',.6)
 s+=''.join(draw for depth,draw in shapes if depth>0)+'</g>'
 s+='<rect x="12" y="12" width="336" height="35" rx="8" fill="#142f3c"/><text x="180" y="35" text-anchor="middle" font-family="Tahoma,Arial" fill="white" font-size="14">طرح شماتیک؛ عکس تولید نیست</text>'
 s+=f'<rect x="12" y="586" width="336" height="42" rx="8" fill="#142f3c"/><text x="180" y="613" text-anchor="middle" fill="white" font-size="15" font-family="Tahoma,Arial">{shot["start"]:.2f} – {shot["end"]:.2f} | {shot["camera"]}</text>'
 return s+'</svg>'
for shot in shots:
 f=E/shot['schematic'];f.parent.mkdir(exist_ok=True);f.write_text(render(shot),encoding='utf-8',newline='\n')
# Shared overhead plan: same fixed world, independent of shot projection.
def topmap():
 def xy(x,y):return (380+x*70,390-y*70)
 s='<svg xmlns="http://www.w3.org/2000/svg" width="820" height="800" viewBox="0 0 820 800"><defs><marker id="a" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0 0L6 3L0 6Z" fill="#278591"/></marker></defs><rect width="820" height="800" fill="#f5efe1"/><g font-family="Tahoma,Arial" text-anchor="middle" fill="#173748"><text x="410" y="32" font-size="23">پلان دوربین قسمت پنج؛ واحد طرح، بدون مقیاس</text>'
 s+='<rect x="100" y="70" width="560" height="600" fill="#eee1c8" stroke="#384d54" stroke-width="4"/><rect x="230" y="80" width="260" height="60" fill="#a6b7a0"/><text x="360" y="118">آشپزخانه</text><text x="60" y="380" transform="rotate(-90 60 380)">پنجره؛ غرب</text><text x="697" y="405" transform="rotate(90 697 405)">تلویزیون؛ شرق</text><text x="730" y="130">راهرو</text>'
 x,y=xy(0,1.65);s+=f'<rect x="{x-116}" y="{y-38}" width="232" height="70" rx="12" fill="#c5ad89" stroke="#806e54"/>'
 x,y=xy(0,0);s+=f'<rect x="{x-70}" y="{y-35}" width="140" height="70" fill="#b28c5d"/>'
 for xworld,angle in [(-1.1,45),(1.1,-45)]:
  x,y=xy(xworld,-1.95);s+=f'<g transform="translate({x},{y}) rotate({angle})"><rect x="-32" y="-32" width="64" height="64" fill="#92a58b" stroke="#71634f"/><path d="M-32 26H32" stroke="#71634f" stroke-width="7"/></g>'
 for key,info in people.items():
  x,y=xy(*info['p']);s+=f'<circle cx="{x}" cy="{y}" r="18" fill="{info["color"]}" stroke="#173748"/><text x="{x}" y="{y-26}" font-size="16">{info["name"]}</text>'
 for key,c in cameras.items():
  x,y=xy(*c['p'][:2]);tx,ty=xy(*c['target'][:2]);s+=f'<path d="M{x},{y}L{tx},{ty}" stroke="#278591" stroke-width="2" stroke-dasharray="5 5" marker-end="url(#a)"/><circle cx="{x}" cy="{y}" r="15" fill="#173748"/><text x="{x}" y="{y+5}" fill="white" font-size="12">{key}</text>'
 x1,y1=xy(.8,1.6);x2,y2=xy(2.8,1.1);x3,y3=xy(3.1,3.2);s+=f'<path d="M{x1},{y1}L{x2},{y2}L{x3},{y3}" fill="none" stroke="#ad673e" stroke-width="4" stroke-dasharray="6 5"/><text x="610" y="260" font-size="13">مسیر خروج پیشنهادی</text>'
 s+='<text x="410" y="719" font-size="17">جوان‌ها ایستاده؛ صندلی‌ها خالی و ثابت با زاویهٔ ۹۰درجه</text><text x="410" y="754" font-size="15">مسیر تا راهرو؛ هندسهٔ در نمایش داده نمی‌شود</text></g></svg>'
 return s
(R/'camera-plan-v1.svg').write_text(topmap(),encoding='utf-8',newline='\n')
refs={'house':P/'house/apartment-cutaway-v2.png','plan':P/'house/apartment-plan-v1.svg','identity':P/'episodes/episode-01/references/01-casting-and-living-room-concept-v1.png','saman':P/'episodes/episode-02/references/01-saman-portrait-v1.png','standing':P/'episodes/episode-04/shots/EP04-SH14/images/EP04-SH14-start-v2.png','mother_pose':P/'episodes/episode-04/shots/EP04-SH03/images/EP04-SH03-start-v2.png','farhad':P/'episodes/episode-04/shots/EP04-SH12/images/EP04-SH12-start-v3.png'}
manifest={'status':'proposed_schematic_storyboard_not_generation_inputs','date':'2026-10-17','duration_seconds':plan['duration_seconds'],'references':{k:{'path':str(v.relative_to(P)),'sha256':hashlib.sha256(v.read_bytes()).hexdigest()} for k,v in refs.items()},'design_units':'arbitrary; not apartment measurements','people':people,'cameras':cameras,'chair_forward_axes':[[1,1],[-1,1]],'chair_dot_product':0,'shots':shots,'video_generated':False,'credits_used':0,'open_items':['photoreal start frames not created','exact human appearance and spatial output review require actual generated or accepted image','mother revised scarf and fitted costume must be checked in actual output','standing entrance and exit movements need video review','reconstructed question and recording06 still lack auditory acceptance']}
(R/'shot-design-v1.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
# Offline HTML report; all diagram SVG is inline, all photographic references remain unchanged.
esc=html.escape
parts=['<!doctype html><html lang="fa" dir="rtl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>طرح نماهای قسمت پنج</title><style>body{margin:0;background:#102830;color:#f1eadc;font:16px Tahoma,Arial;line-height:1.9}main{max-width:1240px;margin:auto;padding:28px}h1{font-size:29px;margin:0}h2{font-size:23px}.note{background:#26434a;border-right:4px solid #d8af62;padding:16px;border-radius:10px}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px}.card{background:#f4eedf;color:#18343e;border-radius:14px;overflow:hidden;padding:16px}.card svg{display:block;width:100%;height:auto;max-height:540px;border-radius:10px}.small{font-size:13px;opacity:.85}.pill{background:#d8af62;color:#17313a;padding:4px 10px;border-radius:8px;display:inline-block}details{background:#e8dfcc;padding:9px;border-radius:8px}summary{cursor:pointer;font-weight:bold}blockquote{margin:12px 0;padding:10px;border-right:3px solid #b18843;font-size:18px}a{color:#e5c17c}.card a{color:#236175}figure{margin:0}.refs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.refs img{width:100%;height:auto;border-radius:9px}.plan svg{width:100%;max-width:820px;display:block;margin:auto}.status{font-size:14px;color:#f2d79e}.controls{display:flex;gap:12px;flex-wrap:wrap;margin:20px 0}button{background:#d4ac61;color:#132d36;padding:9px 15px;border:0;border-radius:7px;font:inherit;cursor:pointer}button:focus-visible,summary:focus-visible,a:focus-visible{outline:3px solid #03bcc5;outline-offset:4px}@media(max-width:760px){main{padding:16px}.grid,.refs{grid-template-columns:1fr}h1{font-size:24px}.card svg{max-height:620px}}@media print{body{background:white;color:black}.grid{grid-template-columns:repeat(3,1fr)}.controls{display:none}.card{break-inside:avoid}details{display:block}}</style><main><span class="pill">پیشنهادی • بدون تولید ویدیو • بدون مصرف اعتبار</span><h1>قسمت پنج؛ خاطرهٔ ساندویچی</h1><p>۹نوبت گفتار، خندهٔ کوتاه و نگاه پایانی؛ زمان هدف ۴۴٫۵۴ثانیه. متن و زمان‌بندی مصوب مبناست؛ این بسته طرح قاب و بازی است، نه عکس آمادهٔ ارسال.</p><p class="note">جوان‌ها در تمام بدنه ایستاده‌اند؛ مادر و فرهاد روی کاناپه‌اند. صندلی‌ها برای نشان‌دادن صورت نمی‌چرخند. آشپزخانه پشت کاناپه است و در نمای رو به جوان‌ها پشت دوربین می‌ماند. خاطرهٔ ساندویچی در همین خانه روایت می‌شود؛ بازگشت تصویری به گذشته اضافه نشده.</p><p class="status">پیکره‌های رنگی فقط جای بدن، قاب و لباس را نشان می‌دهند؛ چهره، مو و روسری واقعی را بازسازی نمی‌کنند. مرجع‌های تصویری واقعی پایین صفحه‌اند. قاب تولیدی تازه هنوز ساخته نشده و هیچ قاب معتبری جایگزین نشده است.</p><div class="controls"><button id="open">بازکردن همهٔ جزئیات</button><button id="close">بستن جزئیات</button><a href="#refs">دیدن مرجع‌های واقعی</a><a href="#plan">پلان دوربین‌ها</a></div><section class="grid">']
for i,shot in enumerate(shots,1):
 c=cameras[shot['camera']];svg=(E/shot['schematic']).read_text(encoding='utf-8');cardpath='shots/EP05-SH15/shot.md' if shot['shot'].endswith('END') else f'shots/{shot["shot"]}/shot.md'
 parts.append(f'<article class="card"><div class="small" dir="ltr">{esc(shot["shot"])} · {shot["start"]:.2f}–{shot["end"]:.2f}s</div><h2>{i:02} · {esc(people[shot["speaker"]]["name"] if shot["speaker"] else "نگاه پایان")}</h2>{svg}<blockquote>{esc(shot["text"])}</blockquote><p>{esc(shot["action"])}</p><details><summary>دوربین، اتصال و بررسی</summary><p>{esc(c["label"])}</p><p>{esc(c["background"])}</p><p>حرکت: {esc(shot["movement"])}</p><p>گوینده فقط صاحب همین جمله است؛ دیگران شنونده‌اند. نور شب و ظاهر روزاول ثابت است.</p><p>وضعیت: طرح هندسی پیشنهادی؛ تطبیق چهره و حرکت واقعی بررسی نشده، چون خروجی تولیدی وجود ندارد.</p><a href="{cardpath}">کارت مالک نما</a></details></article>')
parts+=['</section><p class="note">خندهٔ ۰٫۶۲۵ثانیه‌ای در انتهای جواب سامان، با همان قاب و بدون برش تازه نگه داشته می‌شود؛ خندهٔ مادر و نازلی خارج قاب و لب‌های سامان پس از جمله بسته‌اند. در بدرقه، فرهاد از کنار شرقی میز به سمت راهرو می‌رود؛ در و مسیر لولا نشان داده نمی‌شوند. واکنش پایانی ۱٫۲۵ثانیه است و منبع واقعی آن هنوز تولید نشده.</p><h2 id="plan">پلان ثابت و دوربین‌ها</h2><div class="plan">'+(R/'camera-plan-v1.svg').read_text(encoding='utf-8')+'</div><h2 id="refs">مرجع‌های واقعی؛ نقش‌ها جداست</h2><section class="refs">']
labels={'house':'خانهٔ مرجع؛ چیدمان فعال، نه اندازه‌برداری','identity':'چهره‌های مصوب؛ پس‌زمینه و مدل قدیمی روسری مرجع اجرای تازه نیست','saman':'هویت سامان؛ تی‌شرت متعلق به قسمت۲است، پیراهن دیدار باید آبی بماند','standing':'قاب تاریخی پایان۴؛ مرجع وضعیت ایستاده و رنگ لباس، نه تأیید خودکار قاب تازه','mother_pose':'قاب تاریخی مادر؛ شانهٔ نشستهٔ نازلی برای قسمت۵ناسازگار است و نباید کپی شود','farhad':'مرجع تاریخی فرهاد؛ هم‌جهتی نگاه به سامان ایستاده'}
for key in ['house','identity','saman','standing','mother_pose','farhad']:
 link=os.path.relpath(refs[key],E).replace('\\','/');parts.append(f'<figure><a href="{link}"><img src="{link}" alt="{esc(labels[key])}" loading="lazy"></a><figcaption>{esc(labels[key])}</figcaption></figure>')
parts+=['</section><h2>موارد باقی‌مانده پیش از تولید</h2><p>عکس‌های نهایی چهره‌دار، تطبیق مستقل هر عکس با مرجع خانه و ظاهر، کنترل پیوستگی ابتدا/انتها، شنیدن ضبط‌ها و نسخهٔ سؤال، و سپس بستهٔ کامل پرامپت و قیمت لازم‌اند. آماده‌سازی این طرح مجوز تولید یا مصرف اعتبار نیست.</p><p><a href="timing-plan.md">برنامهٔ زمان</a> · <a href="references/shot-design-v1.json">دادهٔ دقیق طرح</a> · <a href="references/camera-plan-v1.svg">پلان کامل</a></p></main><script>document.getElementById("open").onclick=()=>document.querySelectorAll("details").forEach(x=>x.open=true);document.getElementById("close").onclick=()=>document.querySelectorAll("details").forEach(x=>x.open=false);</script></html>']
(E/'storyboard.html').write_text(''.join(parts),encoding='utf-8',newline='\n')
# Cards own design; no schematic is set as active_frame or approved input.
for shot in shots:
 if shot['shot'].endswith('END'):continue
 f=E/f'shots/{shot["shot"]}/shot.md';s=f.read_text(encoding='utf-8').split('\n## طرح قاب و بازی قسمت پنج')[0];local=Path(shot['schematic']).name
 s+='\n## طرح قاب و بازی قسمت پنج — نسخهٔ۱، پیشنهادی\n\n[![قاب شماتیک، نه عکس تولید](images/'+local+')](images/'+local+')\n\n- زمان پیشنهادی: '+f'{shot["start"]:.3f} تا {shot["end"]:.3f}'+' ثانیه؛ مطابق برنامهٔ زمان، نه زمان خروجی تولیدشده.\n- ایستگاه دوربین: '+cameras[shot['camera']]['label']+'؛ مختصات و مخروط دید در [دادهٔ مشترک](../../references/shot-design-v1.json).\n- انتظار پس‌زمینه: '+cameras[shot['camera']]['background']+'\n- حرکت و دلیل: '+shot['movement']+'\n- ابتدا، کنش و پایان: '+shot['action']+'\n- وضعیت ظاهر: هویت از مرجع مصوب، لباس روزاول؛ تصویر شماتیک چهره ندارد و عکس نهایی هنوز ساخته نشده.\n- [بررسی مستقل طراحی](design-review-v1.md) · [بستهٔ یک‌جای قاب‌ها](../../storyboard.html). این طرح ورودی تولید نیست؛ قاب فعال یا اجازهٔ ارسال عوض نشده است.\n'
 if shot['shot']=='EP05-SH10':s+='\nدنبالهٔ۰٫۶۲۵ثانیه‌ای خنده در همین اندازه و زاویه ادامه دارد؛ مادر و نازلی خارج قاب‌اند، سامان لبخند کوتاه دارد و جملهٔ دیگری نمی‌گوید.\n'
 if shot['shot']=='EP05-SH15':s+='\n[![طرح دونفرهٔ پایان](images/EP05-SH15-ending-blocking-v1.svg)](images/EP05-SH15-ending-blocking-v1.svg)\n\nواکنش آخر از۴۳٫۲۹۲تا۴۴٫۵۴۲، همان جای بدن و صندلی‌ها؛ سامان چپ و نازلی راستِ تصویر.\n'
 f.write_text(s,encoding='utf-8',newline='\n')
print('Created 10 schematic frames, per-shot camera design, fixed-space camera map and offline storyboard report. Review status remains proposed.')
