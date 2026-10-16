"""Make exact 9:16 crops at native resolution; never resample or overwrite sources."""
from pathlib import Path
import json,hashlib,html
from PIL import Image

P=Path(__file__).resolve().parents[1]; E=P/'episodes/episode-05'
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
assets=json.loads((E/'references/photo-frame-package-v1.json').read_text(encoding='utf-8-sig'))['assets']
rise='shots/EP05-SH14/images/EP05-SH14-rise-reference-v1.png'
if (E/rise).exists():assets['EP05-SH14-RISE']={'path':rise,'role':'planned_cut_pose_reference_not_start_frame'}
out={};cache={}
for key,a in assets.items():
    rel=a['path']; src=E/rel
    if rel not in cache:
        with Image.open(src) as im:
            im.load();w,h=im.size;k=min(w//9,h//16);cw,ch=k*9,k*16
            x=(w-cw)//2
            # Tall standing references: remove only excess floor below the table.
            y=0 if w/h<0.55 else (h-ch)//2
            dst=src.with_name(src.stem+'-input-9x16-v1.png')
            im.crop((x,y,x+cw,y+ch)).save(dst)
        with Image.open(dst) as result:
            assert result.size==(cw,ch) and cw*16==ch*9
        cache[rel]={'source':rel,'source_sha256':digest(src),'source_size':[w,h],'path':dst.relative_to(E).as_posix(),'sha256':digest(dst),'size':[cw,ch],'crop_xywh':[x,y,cw,ch],'resampled':False,'exact_9_16':True,'visual_review':'pending','role':a.get('role','proposed_input')}
    out[key]=dict(cache[rel])
data={'date':'2026-10-17','status':'native_resolution_exact_crop_pending_visual_review','method':'Pillow crop only; no scaling, stretching, generative fill or new detail','user_scope':'prepare exact image format; no video','assets':out,'source_files_unchanged':True,'video_generated':False,'credits_spent':0}
(E/'references/input-frames-9x16-v1.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
names={'EP05-SH03':'نازلی؛ پاسخ','EP05-SH05':'سامان؛ خاطره','EP05-SH06':'نازلی؛ شوخی','EP05-SH07':'سامان؛ جواب','EP05-SH08':'مادر؛ پرسش','EP05-SH14':'فرهاد؛ آغاز نشسته','EP05-SH15':'مادر؛ بدرقه','EP05-SH02':'سؤال بازیافتی','EP05-SH10':'سامان؛ پاسخ به مادر','EP05-SH15-END':'پایان؛ نگاه متقابل','EP05-SH15-END-START':'پایان؛ نگاه به مادر','EP05-SH14-RISE':'فرهاد؛ مرجع لحظهٔ قطع'}
cards=[]
for key,a in out.items():
    cards.append(f'<figure><a href="{a["path"]}"><img src="{a["path"]}" alt="{names[key]}"></a><figcaption>{names[key]}<br><bdi>{a["size"][0]} × {a["size"][1]}</bdi> · ۹:۱۶ دقیق</figcaption></figure>')
body='''<!doctype html><html lang="fa" dir="rtl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>قالب دقیق عکس‌های قسمت پنج</title><style>body{background:#112a32;color:#f3ead8;font:16px Tahoma;line-height:1.9;margin:0}main{padding:24px;max-width:1250px;margin:auto}a{color:#edc983}.grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}figure{margin:0;padding:10px;background:#f1e9d8;color:#193540;border-radius:8px;text-align:center}img{width:100%;height:auto;display:block}.note{padding:14px;background:#29464e;border-right:4px solid #d9ac61}@media(max-width:650px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}main{padding:12px}}</style><main><h1>قالب دقیق عکس‌های قسمت پنج</h1><p class="note">همهٔ عکس‌ها برش دقیق۹:۱۶دارند؛ هیچ تصویری کشیده یا بزرگ نشده است. در نماهای باز فقط بخش اضافهٔ کف پایین تصویر کوتاه شده؛ سرها، بدن‌ها، پاها و میز در قاب باقی‌اند. فایل‌های اصلی حفظ شده‌اند. این صفحه عکس ثابت است و تولید ویدیو یا مجوز ارسال نیست.</p><p><a href="production-review.html">بستهٔ تولید و موارد باز</a> · <a href="references/input-frames-9x16-v1.json">ابعاد، برش و اثرانگشت‌ها</a></p><section class="grid">'''
(E/'input-frames.html').write_text(body+''.join(cards)+'</section></main></html>',encoding='utf-8')
print(f'{len(out)} roles; {len(cache)} unique exact9:16 crops, no resampling')
