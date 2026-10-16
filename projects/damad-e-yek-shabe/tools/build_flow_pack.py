"""Local draft export from canonical cards, with no network calls or take overwrite."""
import argparse,re
from shot_workflow import cards
ap=argparse.ArgumentParser();ap.add_argument('--episode',type=int,required=True);ap.add_argument('--check',action='store_true');ap.add_argument('--take');args=ap.parse_args()
if not args.check and (not args.take or not re.fullmatch(r'take-\d{2,}',args.take)):raise SystemExit('Use --check or explicitly name a fresh --take take-NN')
for card,text,state in cards(args.episode):
 sid=state['shot']
 created=False
 for kind,title in [('start-frame','قالب قاب شروع'),('video','قالب ویدئو')]:
  match=re.search(r'#### '+title+' '+sid+r'\n```text\n(.*?)\n```',text,re.S)
  if not match:continue
  def fill(m):
   ident=m[1];b=re.search(r'### `'+re.escape(ident)+r'` — ([^\n]+)\n(.*?)(?=\n<a id=|\n## |\n### |\Z)',text,re.S)
   if not b:raise ValueError('Missing dialogue '+ident)
   line=re.search(r'^- متن: «(.*)»$',b[2],re.M)
   if not line:raise ValueError('Missing spoken text '+ident)
   return 'DIRECTIONS — NOT SPOKEN:\n'+'\n'.join(x for x in b[2].splitlines() if x.startswith('- ') and not x.startswith('- متن:'))+'\nSPOKEN DIALOGUE ONLY — '+b[1]+': «'+line[1]+'»'
  prompt=re.sub(r'\{\{DIALOGUE:([^}]+)\}\}',fill,match[1])
  if '{{' in prompt:raise ValueError('Unresolved template '+sid)
  if args.check:print('OK',sid,kind);continue
  folder=card.parent/'takes'/args.take
  if folder.exists() and not created:raise SystemExit('Refusing existing take: '+str(folder))
  # Export templates only; still requires completed review and cost/content approval.
  folder.mkdir(parents=True,exist_ok=True);created=True
  dest=folder/('prompt.txt' if kind=='video' else 'frame-prompt.txt')
  dest.write_text(prompt+'\n',encoding='utf8');print(dest)
