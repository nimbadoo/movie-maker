"""Build an offline, explicitly blocked production review from canonical cards."""
from pathlib import Path
import re,json,hashlib,html
from PIL import Image

P=Path(__file__).resolve().parents[1]
E=P/'episodes/episode-05'
def readj(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def savej(p,d):p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
frames=readj(E/'references/photo-frame-package-v1.json')['assets']
timing=readj(E/'edit/timing-plan-sandwich-v1.json')
normalized_path=E/'references/input-frames-9x16-v1.json'
normalized=readj(normalized_path) if normalized_path.exists() else {'assets':{}}
inputs_ready=normalized.get('status')=='exact_crops_visually_reviewed_not_submission_approval'
if inputs_ready:
    for key,asset in normalized['assets'].items():
        if key in frames:
            frames[key]={**frames[key], 'original_path':frames[key]['path'], 'path':asset['path'], 'sha256':asset['sha256'], 'size':asset['size']}

# Directions are stage instructions, never speech. Existing dialogue stays in cards.
actions={
'EP05-SH03':('فرهادِ نشسته، راست و پایین تصویر','روان و مطمئن، لبخند کوچک؛ پاسخ کوتاه بدون مکث نمایشی.','نازلی ایستاده در جای ثابت، نگاه راست و پایین به فرهاد؛ دست‌ها پایین. تنها خودش حرف می‌زند.'),
'EP05-SH05':('مادر و فرهادِ نشسته، خارج قاب','خودمانی و ساده؛ قصد توضیح آشنایی و دعوت جمعی.','سامان چپ و نازلی راست با فاصله ثابت؛ سامان به جمع جواب می‌دهد، سپس نگاه کوتاه به مادر و نازلی؛ نازلی و فرهاد ساکت و بدون حرکت لب گفتاری.'),
'EP05-SH06':('سامانِ ایستاده، چپ و کمی بالای تصویر','شوخی ملایم و صمیمی، بدون تمسخر.','نازلی فقط سر و چشم را به سامان می‌برد؛ بدن در جای ثابت، سامان بیرون قاب ساکت.'),
'EP05-SH07':('نازلی، راست تصویر','کمی خجالت‌زده و خندان؛ اعتراف ساده و خبری.','سامان از نگاه به جمع با چرخش کوچک سر و چشم به نازلیِ ایستاده نگاه کند؛ برای خطاب به نازلی نگاه عمودیِ پایین به فرد نشسته نماند. هیچ لیوان یا غذای خاطره وارد قاب نشود.'),
'EP05-SH08':('سامانِ ایستاده، چپ و بالای تصویر','پرسش گرم و شوخ؛ تلفظ روشن «تُندِه»، پایان پرسشی.','مادر نشسته، دست‌های خودش روی پا، سر و چشم چپ و بالا به سامان؛ دیگران خارج قاب و ساکت.'),
'EP05-SH10':('مادرِ نشسته، راست و پایین تصویر','مؤدب و خودمانی، لبخند کم؛ «غُر نَزَنَم» خبری و روشن.','سامان به مادر نگاه کند؛ پس از جمله دهان بسته و لبخند کوچک. خنده کوتاه مادر و نازلی خارج قاب فقط پس از تمام‌شدن جمله و بدون گفتار اضافه؛ اگر هویت خنده درست اجرا نشد در تدوین از منبع پذیرفته استفاده شود، منبع خنده فعلاً موجود نیست.'),
'EP05-SH14':('جمع، سپس مادر','خوش‌برخورد و عادی؛ دلخوری با اخم یا مکث سنگین نشان داده نشود.','آغاز نشسته با دو دست روی ران خود. ابتدا جمله کامل؛ نزدیک پایانِ بخش «مُرَخَّص بِشَم» آرام به جلو خم شود، کف پا روی زمین، وزن به پاها و آغاز بلندشدن. در پایان هنوز حرکت رو به بالا ادامه دارد؛ جهش یا برگشت به نشستن ممنوع. خروج کامل لازم نیست.'),
'EP05-SH15':('ابتدا فرهادِ درحال برخاستن در راست، سپس سامانِ ایستاده در چپ','بدرقه گرم، سپس پیگیری دعوت با لحن عادی و روشن.','در «بُرو بِه سَلامَت، عَزیزَم» مادر نگاه راست را همراه صاف‌شدن فرهاد آرام بالا ببرد، نه از ابتدا سر شدیداً عقب. پس از پایان بدرقه، گردش طبیعی چشم و سر به چپ و بالای تصویر، سپس جمله خطاب به سامان. فرهاد خارج کادر از کنار شرقی میز به راهرو می‌رود؛ در و عبور از وسط میز نشان داده نشود. مادر نشسته و دست‌ها روی پای خودش بماند.')}

common='''دستورها خوانده نشوند. عکس واقع‌گرایانهٔ مرجع و ظاهر و لباس شب روزاول حفظ شود. دوربین ثابت، بدون زوم و تغییر محور. فقط گوینده تعیین‌شده همان جمله را به فارسی بگوید؛ هیچ نریشن، موسیقی، زیرنویس یا جمله اضافه نباشد. صدای شخصیت باید با مرجع صوتی مصوب او تطبیق داشته باشد؛ توصیف متن تضمین هویت صدا نیست. شنونده‌ها حرف نزنند و لب نزنند. اشیا و دست‌ها مالک مشخص داشته باشند. آشپزخانه پشت کاناپه مادر و فرهاد است؛ پشت جوان‌ها دیوار جنوبی و سمت پنجره راست است. صندلی‌ها رو به داخل و ثابت، چای چپ تصویر رو به جوان‌ها، کاسه وسط و سینی خالی راست؛ در زاویه معکوس جای تصویری معکوس است. هیچ آب یا ساندویچ یا صحنه گذشته ظاهر نشود.'''
actions['EP05-SH14']=(actions['EP05-SH14'][0],actions['EP05-SH14'][1],'آغاز نشسته، دو دست روی ران خود. در آخرین بخش جمله، حدود ثانیه۲٫۹تا۴٫۱۲۵ِ سهم تدوین، به جلو متمایل شود، وزن روی پاها و لگن از نشیمن جدا شود؛ روی ادامهٔ حرکت رو به بالا قطع شود، نه پس از بازگشت به نشستن. مرجع ثابت برخاستن فقط راهنمای حالت است و فریم واقعی خروجی نیست. هر دو دست روی ران خود بمانند، تماس با میز و عبور اندام از کاناپه ممنوع؛ نگاه به جمع و سپس مادر، بدون اخم. زمان‌های کنش پیشنهادی‌اند و با اجرای واقعی تطبیق می‌خواهند.')
actions['EP05-SH15']=(actions['EP05-SH15'][0],actions['EP05-SH15'][1],'آغاز با نگاه ملایم به راست و کمی بالا به فرهادِ درحال برخاستن؛ مادر در «بُرو بِه سَلامَت، عَزیزَم» چشم و سر را آرام با ادامهٔ بالا رفتن او دنبال کند، نه جهش ناگهانی گردن. بعدِ پایان بدرقه و در مکث موجود، حدود ثانیه۲٫۰تا۲٫۵ِ سهم تدوین، نگاه به چپ و بالا برای سامان برگردد؛ بخش خطاب به سامان پس از گردش نگاه شروع شود. مکث و زمان‌ها بر پایهٔ تشخیص فعالیت گفتار پیشنهادی‌اند، نه تطبیق شنیداری قطعی. مادر نشسته و دست‌ها روی پای خودش؛ فرهاد خارج قاب از کنار شرقی میز می‌رود، در و عبور از وسط میز نشان داده نشود.')
rows=[]
for t in timing['timeline']:
    if t['kind']!='reference_dialogue':continue
    sid=t['shot']; card=E/'shots'/sid/'shot.md'; text=card.read_text(encoding='utf-8')
    spoken=re.search(r'- متن: «(.*?)»',text).group(1)
    assert spoken==t['text'],sid
    recipient,tone,action=actions[sid]
    asset=frames[sid]; image=E/asset['path']; assert sha(image)==asset['sha256']
    audio=E/t['source']; assert sha(audio)==t['source_sha256']
    take=E/'shots'/sid/'takes/take-01'; take.mkdir(parents=True,exist_ok=True)
    duration=t['duration_seconds']+(0.625 if sid=='EP05-SH10' else 0)
    prompt=f'''نما: {sid}؛ زمان حال در پذیرایی، شب روزاول.
وضعیت متن: مصوب؛ دستور بازی: پیشنهادی برای مرور بسته.
گوینده: {t['speaker']}، داخل قاب. مخاطب: {recipient}.
لحن و قصد: {tone}
رفتار و ابتدا/پایان: {action}
زمان هدف در تدوین: {duration:.3f}ثانیه، بر اساس ضبط مرجع و تشخیص فعالیت گفتار؛ پذیرش شنیداری مرزها هنوز باز است. زمان تولید پیشنهادی۸ثانیه با یک خروجی؛ جمله طبیعی و کامل باشد، برای پرکردن۸ثانیه کشیده نشود. حاشیه کوتاه قبل و بعد، بدون بریدن واژه؛ برش نهایی محلی است.
{common}

فقط این دیالوگ گفته شود:
«{spoken}»
'''
    (take/'prompt.txt').write_text(prompt,encoding='utf-8')
    w,h=Image.open(image).size
    k=min(w//9,h//16); cw,ch=9*k,16*k
    # Crop spec only; the ending image needs top anchoring to retain heads/table.
    crop={'x':(w-cw)//2,'y':0 if w/h<0.55 else (h-ch)//2,'width':cw,'height':ch,'status':'proposal_not_applied_or_visually_approved'}
    issues=['شنیدن واقعی متن، لحن، تلفظ و سلامت مرزهای ضبط انجام نشده است.','نسخه دقیق۹:۱۶و برش واقعی ورودی هنوز اعمال و بازبینی نشده است.','امکان حفظ هویت صدای مصوب با مدل و روش جاری تأیید نشده است.','مدت و کیفیت و هزینهٔ همین ارسال در رابط زنده تأیید نشده؛ مجوز هزینه نداریم.']
    if inputs_ready:
        issues=[x for x in issues if not x.startswith('نسخه دقیق۹:۱۶')]
        crop['status']='exact_crop_applied_and_visually_reviewed'
    if sid=='EP05-SH15' and not (E/'references/farewell-connection-v1.json').exists():issues.append('قاب مادر از ابتدا رو به بالا است؛ برای نمایش دنبال‌کردنِ حرکت فرهاد، قاب آغاز با نگاهِ میانهٔ برخاستن باید آماده و دیده شود، یا اتصال واقعی برداشت بر اساس پایان حرکت فرهاد بررسی شود.')
    if sid=='EP05-SH07':issues.append('ارتفاع نگاه آغاز به فرد نشسته است؛ تغییر مخاطب به نازلی باید با گردش کوچک نگاه در اجرای واقعی کنترل شود.')
    checks={k:{'status':'unchecked','evidence':v} for k,v in {
      'dialogue':'متن با کارت تطبیق داده شد؛ تلفظ واقعی شنیده نشده.',
      'delivery':'دستور بازی نوشته شده؛ ضبط شنیداری پذیرفته نیست.',
      'duration':'بازه بر پایه تشخیص فعالیت گفتار است، نه تأیید شنیداری.',
      'identity':'گزارش عکس موجود است؛ قالب نهایی ارسال و هویت صدا هنوز بررسی لازم دارند.',
      'eyeline':'جهت پیشنهادی ثبت است؛ نگاه واقعی و قاب ورودی نهایی کنترل می‌خواهد.',
      'geometry':'گزارش ثابت عکس وجود دارد؛ بررسی نسخهٔ ورودی نهایی باز است.',
      'continuity':'ابتدا و پایان در پرامپت ثبت است؛ رسانه حرکت تولید نشده.',
      'settings':'Omni 1.1 Flash در فهرست زنده دیده شد؛ انتخاب مدل/مدت/قالب همین ارسال انجام نشده.',
      'cost':'قیمت زندهٔ این ارسال نمایش داده نشده؛ مقدار null است.'}.items()}
    checks['speaker']={'status':'pass','evidence':'تنها گوینده و سکوت شنونده‌ها در متن و پرامپت مشخص‌اند؛ خروجی واقعی هنوز وجود ندارد.'}
    checks['performance']={'status':'pass','evidence':action+' وضعیت پیشنهادی؛ قبول دستور به معنی قبول خروجی نیست.'}
    checks['camera']={'status':'pass','evidence':'دوربین ثابت و محور عکس حفظ می‌شود.'}
    checks['prompt']={'status':'pass','evidence':'متن کارت و متن پرامپت ماشینی تطبیق شدند، دستورها از جمله جداست.'}
    checks['local_alternative']={'status':'pass','evidence':'برداشت گفتاری پذیرفته برای متن جدید موجود نیست؛ سؤال از منبع موجود استفاده می‌شود؛ تدوین و میکس محلی است.'}
    if inputs_ready:
        checks['geometry']={'status':'pass','evidence':'نسخهٔ دقیق۹:۱۶دیده شد، بدون تغییر مقیاس؛ گزارش input-format-review-v1.md. این قبولی عکس ثابت است؛ حرکت واقعی هنوز تولید نشده.'}
    state={'shot':sid,'take':'take-01','ready':False,'open_issues':issues,'checks':checks,'bundle_sha256':None,'content_approval':{'approved':False,'bundle_sha256':None,'user_reply':'','evidence_ref':''},'cost_approval':{'approved':False,'bundle_sha256':None,'user_reply':'','evidence_ref':''},'consumed_attempts':0}
    report=f'# بررسی پیش از ارسال — {sid}\n\nوضعیت: آماده‌سازی انجام‌شده؛ ارسال مسدود.\n\n[پرامپت کامل](prompt.txt) · [قاب پیشنهادی](../../../../'+asset['path']+')\n\nگوینده: '+t['speaker']+'؛ مخاطب: '+recipient+'\n\n'+action+'\n\nزمان مرجع با مکث‌های داخلی: '+str(t['duration_seconds'])+'ثانیه؛ بازهٔ ضبط '+str(t['source_in_seconds'])+'تا'+str(t['source_out_seconds'])+'ثانیه. این مرز شنیداری تأیید نشده.\n\n'+ '\n'.join('- '+x for x in issues)+'\n\n<!-- preflight-state -->\n```json\n'+json.dumps(state,ensure_ascii=False,indent=2)+'\n```\n<!-- /preflight-state -->\n'
    (take/'preflight.md').write_text(report,encoding='utf-8')
    settings={'status':'proposed_not_live_verified','model':'Omni 1.1 Flash','mode':'Frames','seconds':8,'quality':'360p','aspect_ratio':'9:16','audio':True,'outputs':1,'cost':{'per_attempt':None,'ceiling':None,'attempts':1,'approved':False}}
    row={'shot':sid,'speaker':t['speaker'],'text':spoken,'recipient':recipient,'tone':tone,'action':action,'frame':asset['path'],'frame_sha256':sha(image),'frame_size':[w,h],'crop_proposal':crop,'audio':t['source'],'audio_sha256':sha(audio),'source_in':t['source_in_seconds'],'source_out':t['source_out_seconds'],'start':t['start_seconds'],'end':t['end_seconds'],'edit_seconds':duration,'settings':settings,'prompt':str((take/'prompt.txt').relative_to(E)).replace('\\','/'),'prompt_sha256':sha(take/'prompt.txt'),'preflight':str((take/'preflight.md').relative_to(E)).replace('\\','/'),'open_issues':issues}
    rows.append(row)
    marker='## بستهٔ پیشنهادی تولید — نسخهٔ۱'
    if marker not in text:
        card.write_text(text+'\n\n'+marker+'\n\n[پرامپت کامل](takes/take-01/prompt.txt) · [بررسی مستقل و موارد باز](takes/take-01/preflight.md) · [مرور بسته](../../production-review.html)\n\nاین آماده‌سازی مجوز ارسال نیست؛ قاب فعال، درخواست ارسال و برداشت منتخب تغییر نکرده‌اند.\n',encoding='utf-8')

endframe=frames['EP05-SH15-END']['path']
endstart=frames.get('EP05-SH15-END-START',{}).get('path','shots/EP05-SH15/images/EP05-SH15-ending-start-v2.png')
has_endstart=(E/endstart).exists()
enddir=E/'shots/EP05-SH15/takes/take-02';enddir.mkdir(parents=True,exist_ok=True)
endprompt='''واکنش بی‌کلام پایان قسمت پنج، پس از دعوت مادر. وضعیت بازی پیشنهادی. زمان هدف۱٫۲۵ثانیه؛ زمان تولید پیشنهادی۴ثانیه اگر در مدل جاری قابل‌انتخاب باشد، وگرنه۸ثانیه فقط پس از مرور قیمت تازه. دوربین و فاصله و جای بدن همان نمای باز سامان، بدون قدم یا نزدیک‌شدن یا تماس. آغاز: نگاه دو نفر هنوز به مادر خارج قاب است. سپس نازلی فقط سر و چشم به سامان ببرد و سامان نگاهش را بگیرد؛ نگرانی ظریف، لب‌ها بسته. میز، چای چپ، کاسه وسط و سینی راست و صندلی‌های مورب ثابت. فرهاد پس از خداحافظی از این محدوده خارج شده است. صدای محیط آرام، بدون گفتار، موسیقی یا خندهٔ اضافه. عکس پایان پذیرفته‌شده مرجع حالت مقصد است و نباید به جای قاب شروع وارد شود. تا قاب شروعِ بدون فرهاد با نگاه رو به مادر آماده و بازبینی نشده، ارسال انجام نشود.'''
(enddir/'prompt.txt').write_text(endprompt,encoding='utf-8')
endissues=['روش ورودی پایان/دو قاب، مدت و قیمت مدل باید در رابط واقعی بررسی شوند.','قالب دقیق۹:۱۶و نسخهٔ برش باید قبل از ارسال دیده شوند.','مجوز تولید و هزینه وجود ندارد.']
if not has_endstart:endissues.insert(0,'قاب شروعِ بدون فرهاد و با نگاه به مادر آماده نشده؛ عکس موجود حالت مقصد است.')
else:
    endprompt=endprompt.replace('تا قاب شروعِ بدون فرهاد با نگاه رو به مادر آماده و بازبینی نشده، ارسال انجام نشود.','قاب آغاز جداگانه با نگاه هر دو به مادر و بدون فرهاد آماده و بررسی ثابت شده است؛ نقش عکس مقصد با عکس آغاز عوض نشود. حرکت واقعی هنوز بررسی نشده است.')
    (enddir/'prompt.txt').write_text(endprompt,encoding='utf-8')
if inputs_ready:endissues=[x for x in endissues if not x.startswith('قالب دقیق۹:۱۶')]
endstate={'shot':'EP05-SH15','take':'take-02','purpose':'separate_silent_ending_not_alternative_mother_dialogue','ready':False,'open_issues':endissues,'checks':{'settings':{'status':'unchecked','evidence':'روش ورودی و مدت در رابط واقعی تأیید نشده.'},'geometry':{'status':'unchecked','evidence':'قالب نهایی۹:۱۶و حرکت واقعی باز است.'},'cost':{'status':'unchecked','evidence':'مجوز و قیمت جاری نداریم.'},'continuity':{'status':'pass' if has_endstart else 'unchecked','evidence':'قاب آغاز و مقصد جدا شدند؛ گزارش leg-depth-review-v1.md بررسی ثابت و محدودیت حرکت را ثبت می‌کند.' if has_endstart else 'قاب آغاز موجود نیست.'}},'bundle_sha256':None,'consumed_attempts':0,'content_approval':{'approved':False},'cost_approval':{'approved':False}}
if inputs_ready:
    endstate['checks']['geometry']={'status':'pass','evidence':'قاب‌های آغاز و مقصد با برش دقیق۹:۱۶واقعاً دیده شدند؛ بدون تغییر مقیاس. حرکت واقعی هنوز تولید نشده است.'}
(enddir/'preflight.md').write_text('# واکنش پایان؛ برداشت جداگانه برای قطعهٔ بی‌کلام\n\n'+ '\n'.join('- '+x for x in endissues)+'\n\n<!-- preflight-state -->\n```json\n'+json.dumps(endstate,ensure_ascii=False,indent=2)+'\n```\n<!-- /preflight-state -->\n',encoding='utf-8')
bundle={'version':'production-preparation-v1','date':'2026-10-17','status':'blocked_pending_auditory_review_final_inputs_provider_and_cost','duration_seconds':timing['duration_seconds'],'dialogue_jobs':rows,'ending':{'frame_role':'destination_only_not_start','frame':endframe,'prompt':'shots/EP05-SH15/takes/take-02/prompt.txt','preflight':'shots/EP05-SH15/takes/take-02/preflight.md','open_issues':endissues},'question_replay':{'source':'shots/EP05-SH02/sources/EP04-SH12-question-restored-v1.mp4','status':'reuse_candidate_not_auditioned_or_selected','new_generation':False},'cost':{'live_price':None,'approved_ceiling':None,'approved':False,'spent':0},'provider_observation':'2026-10-17: existing episode4 project loaded; Omni1.1Flash visible in model dropdown; defaults16:9 and1 output; no settings saved, no upload, no generation; cost for these jobs not displayed','video_generated':False,'source_audio_edited':False}
if has_endstart:
    bundle['ending']['start_frame']=endstart
    bundle['ending']['start_frame_sha256']=sha(E/endstart)
    bundle['ending']['start_frame_role']='start_pose_both_look_at_mother_no_farhad'
savej(E/'references/production-preparation-v1.json',bundle)
esc=html.escape
parts=['''<!doctype html><html lang="fa" dir="rtl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>بستهٔ تولید قسمت پنج</title><style>body{margin:0;background:#112a32;color:#f3ead8;font:16px Tahoma,Arial;line-height:1.9}main{max-width:1150px;margin:auto;padding:24px}a{color:#dfbe7d}.notice{padding:16px;border-right:4px solid #dda955;background:#29464e;border-radius:8px}.card{background:#f1e9d8;color:#193540;padding:20px;border-radius:12px;margin:20px 0;display:grid;grid-template-columns:260px minmax(0,1fr);gap:24px}.card a{color:#216476}img{width:100%;height:auto;border-radius:8px}audio,video{width:100%;max-width:100%}blockquote{font-size:20px;border-right:3px solid #b18a50;margin:12px 0;padding:10px}pre{white-space:pre-wrap;overflow-wrap:anywhere;font:15px Tahoma;line-height:1.9;background:#e5dac3;padding:12px}summary{cursor:pointer;font-weight:bold}code{direction:ltr;unicode-bidi:isolate}a:focus-visible,summary:focus-visible{outline:3px solid #048b9c;outline-offset:4px}@media(max-width:650px){main{padding:14px}.card{display:block}img{max-width:330px;display:block;margin:auto}}</style><main><h1>بستهٔ تولید قسمت پنج</h1><p class="notice"><strong>پرامپت‌ها و طرح اتصال آمادهٔ مرورند؛ ارسال هنوز مسدود است.</strong> شنیدن ضبط‌ها، قاب آغاز پایان، قاب دقیقِ آغاز بدرقه، قالب نهایی ورودی و هزینهٔ جاری هنوز باید تکمیل شوند. هیچ تولید ویدیو یا مصرف اعتبار انجام نشده.</p><p>زمان هدف۴۴٫۵۴۲ثانیه؛۸گفتار تازه، سؤال بازیافتی و یک واکنش بی‌کلام. همهٔ دستورهای بازی پیشنهادی‌اند. ضبط کاربر مرجع زمان و اجراست؛ ورودی صوتیِ قابل‌قبول ابزار یا صدای نهایی شخصیت فرض نشده است.</p><p><a href="photo-frames.html">مرور همهٔ عکس‌ها</a> · <a href="references/production-preparation-v1.json">ثبت نسخه و اثرانگشت‌ها</a></p><h2>اتصال خداحافظی</h2><p>فرهاد نزدیک پایان جمله‌اش شروع به بلندشدن می‌کند. مادر در بدرقه نگاه را آرام همراه او بالا می‌برد؛ سپس نگاهش را به سامان می‌چرخاند. فرهاد هنگام گفتار بعدی مادر از محدوده می‌رود. در پایان، جای بدن و فاصلهٔ نازلی و سامان ثابت است و فقط سر و چشم‌ها می‌چرخند.</p><h2>قیمت و تنظیمات</h2><p>مدل پیشنهادی <code>Omni 1.1 Flash</code>، روش <code>Frames</code>، قالب۹:۱۶، کیفیت پیشنهادی <code>360p</code>، یک خروجی؛ برای هر گفتار۸ثانیه و برش محلی. این تنظیمات همین ارسال هنوز زنده تأیید نشده‌اند. رابط فعلی پیش‌فرض۱۶:۹نشان می‌دهد؛ پیش‌فرض نباید خودکار پذیرفته شود. قیمت و سقف مجوز تعیین نشده؛ اعداد قسمت قبل قیمت این بسته نیستند.</p><h2>سؤال آغاز؛ استفاده از منبع موجود</h2><video controls preload="metadata" src="shots/EP05-SH02/sources/EP04-SH12-question-restored-v1.mp4"></video><p>بازسازی۴٫۵۸۳ثانیه‌ای هنوز شنیده و منتخب نشده؛ تولید تازه برای سؤال پیشنهاد نشده.</p>''']
for i,r in enumerate(rows,1):
    prompt=(E/r['prompt']).read_text(encoding='utf-8')
    issues=''.join('<li>'+esc(x)+'</li>' for x in r['open_issues'])
    parts.append(f'''<article class="card" id="{r['shot']}"><div><img src="{r['frame']}" alt="قاب پیشنهادی {esc(r['speaker'])}"><p>قاب موجود؛ برش نهایی هنوز باز است.</p></div><div><h2>{i} · {esc(r['speaker'])}</h2><p>از{r['start']:.3f}تا{r['end']:.3f}ثانیه؛ سهم تدوین با واکنش همراه{r['edit_seconds']:.3f}ثانیه</p><blockquote>{esc(r['text'])}</blockquote><p><strong>مخاطب:</strong> {esc(r['recipient'])}</p><p><strong>لحن پیشنهادی:</strong> {esc(r['tone'])}</p><p><strong>کنش:</strong> {esc(r['action'])}</p><audio controls preload="metadata" src="{r['audio']}"></audio><p>اصل ضبط؛ بازهٔ پیشنهادی{r['source_in']:.3f}تا{r['source_out']:.3f}ثانیه. این بازه از تشخیص فعالیت گفتار است و هنوز شنیداری تأیید نشده.</p><details><summary>موارد باز و بررسی مستقل</summary><ul>{issues}</ul><a href="{r['preflight']}">گزارش پیش از ارسال</a></details><details><summary>پرامپت کامل؛ دستورها خوانده نشوند</summary><pre>{esc(prompt)}</pre></details></div></article>''')
parts.append(f'''<article class="card"><div><img src="{endframe}" alt="مرجع حالت مقصد نگاه پایانی"></div><div><h2>پایان بی‌کلام؛ فاصله ثابت</h2><p>۴۳٫۲۹۲تا۴۴٫۵۴۲ثانیه. عکس موجود حالت مقصد نگاه است؛ قاب شروعِ بدون فرهاد و با نگاه به مادر هنوز لازم است. استفاده از این عکس به‌عنوان آغاز چرخش نگاه تناقض ایجاد می‌کند.</p><details><summary>پرامپت کامل پایان</summary><pre>{esc(endprompt)}</pre></details><a href="shots/EP05-SH15/takes/take-02/preflight.md">گزارش پایان</a></div></article><p>تأیید قبلی عکس‌ها مجوز ارسال یا هزینه نیست. پس از رفع موارد باز، بستهٔ نهایی با هزینهٔ همان نوبت برای تأیید ارائه می‌شود.</p></main></html>''')
output=''.join(parts)
if has_endstart:
    output=output.replace('شنیدن ضبط‌ها، قاب آغاز پایان، قاب دقیقِ آغاز بدرقه، قالب نهایی ورودی','شنیدن ضبط‌ها، قاب دقیقِ آغاز بدرقه، قالب نهایی ورودی')
    output=output.replace('عکس موجود حالت مقصد نگاه است؛ قاب شروعِ بدون فرهاد و با نگاه به مادر هنوز لازم است.','قاب آغاز جداگانه آماده شد: نگاه هر دو به مادر و بدون فرهاد؛ عکس مقصد نگاه متقابل را نشان می‌دهد.')
    output=output.replace('استفاده از این عکس به‌عنوان آغاز چرخش نگاه تناقض ایجاد می‌کند.','قاب آغاز و مقصد در ابزار جابه‌جا انتخاب نشوند؛ مسیر واقعی چرخش نگاه هنوز تولید نشده.')
    needle=f'<img src="{endframe}" alt="مرجع حالت مقصد نگاه پایانی">'
    output=output.replace(needle,f'<p>آغاز؛ نگاه به مادر</p><img src="{endstart}" alt="قاب آغاز؛ نگاه به مادر بدون فرهاد"><p>مقصد؛ نگاه متقابل</p>'+needle)
if inputs_ready:
    output=output.replace('شنیدن ضبط‌ها، قاب دقیقِ آغاز بدرقه، قالب نهایی ورودی و هزینهٔ جاری هنوز باید تکمیل شوند.','قاب‌های دقیق۹:۱۶و طرح اتصال بدرقه آماده و بررسی ثابت شدند؛ بررسی شنیداری، روش و تنظیمات مدل و قیمت جاری هنوز بازند.')
    output=output.replace('قاب موجود؛ برش نهایی هنوز باز است.','قاب ورودی دقیق۹:۱۶؛ بدون بزرگ‌نمایی یا کشیدگی.')
    output=output.replace('<h2>قیمت و تنظیمات</h2>','<p><a href="input-frames.html">دیدن همهٔ عکس‌های دقیق۹:۱۶</a> · <a href="farewell-connection.html">دیدن اتصال برخاستن و نگاه مادر</a></p><h2>قیمت و تنظیمات</h2>')
    output=output.replace('نسخهٔ برش باید قبل از ارسال دیده شوند.','نسخهٔ برش دیده شده‌اند؛ تطبیق رابط قبل از ارسال لازم است.')
output=output.replace('<h2>پایان بی‌کلام؛ فاصله ثابت</h2>','<h2 id="ending">پایان بی‌کلام؛ فاصله ثابت</h2>')
(E/'production-review.html').write_text(output,encoding='utf-8')
print('Built 8 dialogue prompts, separate silent-ending prompt, 9 blocking reports and offline review')
