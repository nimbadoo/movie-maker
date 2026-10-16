"""Build navigation, dialogue reading views and galleries from canonical shot cards."""
from pathlib import Path
import os,re,html,argparse
from shot_workflow import P,cards,submission_gate,Blocked
def link(path,base):return os.path.relpath(path,base).replace('\\','/')

def dialogue_view(ep,active):
 """Derive readable dialogue without creating a second editable source."""
 def fa_number(value):return str(value).translate(str.maketrans('0123456789','۰۱۲۳۴۵۶۷۸۹'))
 entries=[]
 for card,text,state in active:
  lines=text.splitlines();spoken=[]
  for i,line in enumerate(lines):
   if re.match(r'### `EP\d{2}-D\d{2}`',line):
    spoken+=['',line,'']
   elif line.startswith(('- متن:', '- مالک گفتار:', '- حالت:', '- وضعیت متن', '- دستور اجرا؛ خوانده نشود:', '- وضعیت جهت بازی:')):
    spoken.append(line)
   elif re.match(r'^- [^:«\n]+: «',line):
    # New arrival dialogue can precede the numbered dialogue section.
    spoken.append(line)
    for following in lines[i+1:]:
     if not following.startswith('  '):break
     spoken.append(following)
  if spoken:entries.append((card,state,spoken))
 number=fa_number(int(ep.name[-2:]))
 lines=[f'# دیالوگ‌های قسمت {number}','','این صفحه خودکار از کارت‌های جاری نماها ساخته می‌شود؛ برای اصلاح متن و بازی، کارت همان نما را ویرایش کنید. اعراب و وضعیت‌های ثبت‌شده از منبع حفظ شده‌اند.','','ترتیب نمایش مطابق روایت است؛ شناسه‌های نما ثابت‌اند. نماهای بی‌گفتار در این صفحه نیامده‌اند.','','## لینک‌های نماها','']
 for card,state,_ in entries:
  lines.append(f'- `{state["shot"]}` — [خواندن دیالوگ در همین صفحه](#dialogue-{state["shot"].lower()}) · [کارت نما]({link(card,ep)})')
 lines+=['','## متن کامل به‌ترتیب نماها','']
 for card,state,spoken in entries:
  lines += [f'<a id="dialogue-{state["shot"].lower()}"></a>',f'## `{state["shot"]}`','',f'[منبع متن و دستور بازی]({link(card,ep)})','']
  speaker=''
  for line in spoken:
   if line.startswith('### '):
    # Preserve the speaker beside the text without extra heading identifiers.
    speaker=line.partition(' — ')[2]
    continue
   if line.startswith('- متن:') and speaker:
    line=line.replace('- متن:',f'- {speaker}:',1)
   if line.startswith('- مالک گفتار:'):
    line=re.sub(r'؛ نوبت\s*[۰-۹0-9]+\s*از\s*[۰-۹0-9]+','',line)
   # Keep Latin identifiers isolated in Persian prose, preserving existing code.
   parts=re.split(r'(`[^`]*`)',line)
   lines.append(''.join(part if n%2 else re.sub(r'[A-Za-z][A-Za-z0-9_-]*',r'`\g<0>`',part) for n,part in enumerate(parts)))
  lines.append('')
 return re.sub(r'\n{3,}','\n\n','\n'.join(lines)).rstrip()+'\n'

parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--episode',type=int,help='Rebuild only this episode')
parser.add_argument('--dialogue-only',action='store_true',help='Refresh dialogue reading views without changing cards or galleries')
args=parser.parse_args()
episodes=[P/'episodes'/f'episode-{args.episode:02d}'] if args.episode is not None else sorted((P/'episodes').glob('episode-*'))
for ep in episodes:
 number=int(ep.name[-2:]);active=cards(number)
 if args.dialogue_only:
  (ep/'dialogue.md').write_text(dialogue_view(ep,active),encoding='utf8')
  continue
 shots=['# نماها و وضعیت جاری — '+ep.name,'','این فهرست خودکار از کارت اصلی نماها ساخته می‌شود؛ متن، انتخاب برداشت و اجازهٔ ارسال را در همان کارت ویرایش کنید.','','| ترتیب | نما | برداشت منتخب | وضعیت | ارسال تازه |','|---|---|---|---|---|']
 frames=['# قاب‌های فعال — '+ep.name,'','این گالری از قاب فعال کارت نما ساخته شده؛ نسخه‌های قدیمی در پوشهٔ همان نما محفوظ‌اند.','']
 for card,text,state in active:
  url=link(card,ep);sid=state['shot']
  try:submission_gate(card);permit='بسته تأییدشده؛ کنترل زنده لازم'
  except (Blocked,KeyError,ValueError,TypeError):permit='مسدود؛ مجوز بستهٔ تازه کامل نیست'
  status={'accepted_episode_cut':'در خروجی پذیرفته‌شده','accepted_standalone_edit':'اصلاح همین نما پذیرفته و منتخب است','existing_review_cut_not_final':'در تدوین بازبینی؛ نهایی نیست','not_selected':'انتخاب نشده'}[state['selection_status']]
  # Human summary is derived from the state in the same card, never a second owner.
  text=re.sub(r'^- برداشت منتخب: .*$',f'- برداشت منتخب: {state["selected_take"] or "انتخاب نشده"} — {status}.',text,flags=re.M)
  text=re.sub(r'^- اجازهٔ ارسال تازه: .*$',f'- اجازهٔ ارسال تازه: **{permit}**.',text,flags=re.M)
  for label,key in [('ویدیوی منتخب','selected_video'),('قاب فعال','active_frame')]:
   if state[key]:text=re.sub(r'^- \['+label+r'\]\([^\n]+\)$',f'- [{label}]({state[key]})',text,flags=re.M)
  # All images displayed by the current card follow its canonical active frame.
  # Historical image reviews remain separate linked documents.
  if state['active_frame']:
   active_image=state['active_frame']
   text=re.sub(r'\[!\[([^\]]*)\]\([^)]+\)\]\([^)]+\)',lambda m:f'[![{m[1]}]({active_image})]({active_image})',text)
  card.write_text(text,encoding='utf8')
  shots.append(f'| {state["order"]} | [{sid}]({url}) | {state["selected_take"] or "انتخاب نشده"} | {status} | {permit} |')
  if state['active_frame']:
   frame=card.parent/state['active_frame'];furl=link(frame,ep);frames+=['### '+sid,'',f'[![{sid}]({furl})]({furl})',f'[متن، بازی و وضعیت]({url})','']
 inactive=[]
 for card in ep.glob('shots/*/shot.md'):
  from shot_workflow import read_card
  if not read_card(card)[1]['active']:inactive.append(f'- [سابقهٔ {card.parent.name}]({link(card,ep)})')
 if inactive:shots+=['','## نماهای خارج از تدوین فعال','']+sorted(inactive)
 (ep/'dialogue.md').write_text(dialogue_view(ep,active),encoding='utf8')
 for name,lines in [('shots.md',shots),('frames.md',frames)]:
  (ep/name).write_text('\n'.join(lines)+'\n',encoding='utf8')
 # HTML is a derived view too; never maintain its order, image or prose separately.
 page=['<!doctype html><html lang="fa" dir="rtl"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>قاب‌های فعال قسمت</title><style>body{background:#171918;color:#f0eae0;font:16px/1.8 Tahoma,Arial;margin:0}header,main{max-width:1100px;margin:auto;padding:20px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px}article{background:#242723;padding:14px;border-radius:12px}img{width:100%;aspect-ratio:9/16;object-fit:contain}a{color:#e6c589}code{direction:ltr;unicode-bidi:isolate}p{font-size:14px}</style>',f'<header><h1>قاب‌های فعال قسمت {number}</h1><p>ترتیب و تصاویر از کارت‌های فعال ساخته شده‌اند؛ این گالری تأیید حرکت، صدا یا مجوز هزینه نیست.</p><a href="timing-rehearsal.md">برگهٔ تمرین</a> · <a href="frames.md">فهرست قاب‌ها</a></header><main>']
 for card,_,state in active:
  if not state['active_frame']:continue
  url=html.escape(link(card,ep),quote=True);furl=html.escape(link(card.parent/state['active_frame'],ep),quote=True)
  current=card.read_text(encoding='utf8')
  table_rows=[row for row in current.splitlines() if row.startswith('| ') and re.match(r'\| \d+ \|',row)]
  caption=''
  if table_rows:
   cells=table_rows[0].split('|');caption='؛ '.join(c.strip() for c in cells[3:6])
  page.append(f'<article data-shot="{state["shot"]}"><h2>{state["order"]}. <code>{state["shot"]}</code></h2><a href="{furl}"><img loading="lazy" src="{furl}" alt="قاب فعال نما"></a><p>{html.escape(caption)}</p><a href="{url}">متن و بازی و وضعیت همین نما</a></article>')
 page.append('</main></html>')
 (ep/'frames.html').write_text('\n'.join(page)+'\n',encoding='utf8')
 review=ep/'review.md'
 if review.exists():review.write_text('# مرور قسمت\n\n[وضعیت و برداشت‌های منتخب](shots.md) · [فهرست ضبط](dialogue.md) · [قاب‌های فعال](frames.md)\n\nمتن و بازی هر نما فقط در کارت خودش است؛ این صفحه نسخهٔ مستقل دیالوگ ندارد.\n',encoding='utf8')
print(('Dialogue views' if args.dialogue_only else 'Indexes and HTML')+' regenerated from shot.md for '+str(len(episodes))+' episode(s).')
