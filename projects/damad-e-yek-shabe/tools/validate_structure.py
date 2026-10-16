"""Check current project links, selected media and publication manifests without archives."""
from pathlib import Path
import re,json,urllib.parse,ast
from shot_workflow import P,sha,read_card,selected_plan,submission_gate,Blocked
links=selected=blocked=publications=0
for f in P.rglob('*.md'):
 for url in re.findall(r'\]\(([^)\n]+)\)',f.read_text(encoding='utf8')):
  url=url.strip('<>').split('#')[0]
  if not url or re.match(r'^[a-z]+:',url,re.I):continue
  assert (f.parent/urllib.parse.unquote(url)).exists(),(f,url)
  links+=1
for card in P.glob('episodes/episode-*/shots/*/shot.md'):
 text,state=read_card(card)
 if state.get('active_frame'):assert (card.parent/state['active_frame']).exists(),card
 if state.get('selected_video'):
  assert sha(card.parent/state['selected_video'])==state['selected_sha256'],card
  selected+=1
 if state.get('send_request') is None:
  try:submission_gate(card)
  except Blocked:blocked+=1
  else:raise AssertionError('Missing request passed the gate')
for ep in [1,2]:
 plan=selected_plan(ep)
 if ep==1:
  rows=json.loads((P/'episodes/episode-01/edit/v3/timeline.json').read_text())['timeline']
  expected=[(r['shot'],f"take-{r['take']:02d}") for r in rows]
 else:
  rows=json.loads((P/'episodes/episode-02/edit/v5/selected-plan.json').read_text())['selected_plan']
  expected=[(r['shot'],r['selected_take']) for r in rows]
 assert [(r['shot'],r['take']) for r in plan]==expected,ep
for f in P.glob('episodes/episode-*/publishing/manifest.json'):
 data=json.loads(f.read_text())
 for key,digest in [('source','source_sha256'),('output','output_sha256')]:
  if data.get(key):assert sha(f.parent/data[key])==data[digest],f
 if data.get('cover'):assert (f.parent/data['cover']).exists(),f
 if data.get('caption'):assert (f.parent/data['caption']).exists(),f
 if data.get('posted_to_instagram'):assert data['instagram']['url'].startswith('https://www.instagram.com/'),f
 publications+=1
for f in P.glob('episodes/episode-*/cover/cover-v*.json'):
 data=json.loads(f.read_text())
 if data.get('sha256'):assert sha(f.parent/data['image'])==data['sha256'],f
for f in P.glob('episodes/episode-*/edit/v*/concat.txt'):
 for url in re.findall(r"file '([^']+)'",f.read_text()):assert (f.parent/url).exists(),(f,url)
for f in (P/'tools').glob('*.py'):ast.parse(f.read_text())
assert not list(P.rglob('history')),'Unused archives remain'
print(f'OK: {links} links; {selected} selected media hashes; {publications} publication packages; {blocked} shots blocked from unapproved generation.')
