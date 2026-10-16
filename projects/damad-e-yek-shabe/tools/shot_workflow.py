"""Single-source shot cards, explicit edit selection and local submission checks.

This module never contacts Flow or spends credits. A passing gate is evidence to
check against the live interface, not a capability to generate automatically.
"""
from pathlib import Path
import re,json,hashlib
P=Path(__file__).resolve().parents[1]
CHECKS=('dialogue','delivery','duration','performance','speaker','identity','eyeline','geometry','continuity','camera','prompt','local_alternative','settings','cost')
class Blocked(ValueError):pass
def sha(path):
 h=hashlib.sha256()
 with Path(path).open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()
def block(text,name):
 m=re.search(r'<!-- '+re.escape(name)+r' -->\s*```json\s*(.*?)\s*```\s*<!-- /'+re.escape(name)+r' -->',text,re.S)
 if not m:raise Blocked('Missing '+name+' block')
 return json.loads(m[1])
def read_card(path):
 path=Path(path).resolve();text=path.read_text(encoding='utf8');state=block(text,'shot-state')
 if state['shot']!=path.parent.name:raise Blocked('Wrong shot identifier')
 return text,state
def owned(root,path):
 result=(root/path).resolve()
 if not result.is_relative_to(root.resolve()) or not result.is_file():raise Blocked('Missing or unowned file: '+str(path))
 return result
def cards(episode):
 folder=P/f'episodes/episode-{episode:02d}'
 result=[]
 for path in folder.glob('shots/*/shot.md'):
  text,state=read_card(path)
  if state['active']:result.append((path,text,state))
 result.sort(key=lambda x:x[2]['order'])
 orders=[x[2]['order'] for x in result]
 if len(orders)!=len(set(orders)):raise Blocked('Duplicate shot order')
 return result
def selected_plan(episode):
 result=[]
 for card,text,state in cards(episode):
  if not state['selected_take'] or not state['selected_video']:raise Blocked(state['shot']+': no explicitly selected take')
  video=owned(card.parent,state['selected_video'])
  if not video.is_relative_to(card.parent/'takes'/state['selected_take']):raise Blocked('Selected video is outside selected take')
  if sha(video)!=state['selected_sha256']:raise Blocked('Selected media changed')
  trim=state['trim']
  if not trim or trim['in']<0 or trim['out']<=trim['in']:raise Blocked('Invalid selected trim')
  result.append({'shot':state['shot'],'take':state['selected_take'],'source':video.relative_to(P).as_posix(),'sha256':state['selected_sha256'],'in':trim['in'],'out':trim['out'],'order':state['order'],'acceptance':state['selection_status']})
 return result
def bundle_for_request(card):
 card=Path(card).resolve();text,state=read_card(card);req=state.get('send_request')
 if state.get('active') is False:raise Blocked('Retired shot is not active for production')
 if not req:raise Blocked('No active submission request or new cost approval')
 take=req['take']
 if not re.fullmatch(r'take-\d{2,}',take):raise Blocked('Invalid take identifier')
 root=card.parent/'takes'/take
 prompt=owned(root,req['prompt']);preflight=owned(root,req['preflight'])
 inputs=[owned(card.parent,x) for x in req['input_files']]
 if not inputs:raise Blocked('No confirmed input files')
 report=block(preflight.read_text(encoding='utf8'),'preflight-state')
 creative=text.split('## متن و دستور اجرا',1)[-1].split('## برداشت‌ها و تاریخچه',1)[0]
 bundle={'shot':state['shot'],'take':take,'creative_sha256':hashlib.sha256(creative.encode()).hexdigest(),'prompt_sha256':sha(prompt),'inputs':[{ 'path':f.relative_to(card.parent).as_posix(),'sha256':sha(f)} for f in inputs],'settings':req['settings'],'cost':req['cost']}
 fingerprint=hashlib.sha256(json.dumps(bundle,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
 return state,req,report,bundle,fingerprint
def submission_gate(card):
 state,req,report,bundle,fingerprint=bundle_for_request(card)
 take=req['take']
 if report['shot']!=state['shot'] or report['take']!=take:raise Blocked('Report belongs to another take')
 if report.get('open_issues')!=[] or report.get('ready') is not True:raise Blocked('Review incomplete or open issues')
 for key in CHECKS:
  check=report.get('checks',{}).get(key,{})
  if check.get('status') not in ('pass','not_applicable') or not str(check.get('evidence','')).strip():raise Blocked('Unchecked item: '+key)
  if check.get('status')=='not_applicable' and not str(check.get('reason','')).strip():raise Blocked('Missing exemption reason: '+key)
 # Bind approval to everything sent, plus the current canonical creative text.
 required=('model','seconds','quality','aspect_ratio','audio','outputs')
 if any(k not in bundle['settings'] for k in required):raise Blocked('Incomplete generation settings')
 settings=bundle['settings']
 if not settings['model'] or not settings['quality'] or settings['seconds']<=0 or not isinstance(settings['outputs'],int) or settings['outputs']<1 or not isinstance(settings['audio'],bool) or not re.fullmatch(r'\d+:\d+',settings['aspect_ratio']):raise Blocked('Invalid generation settings')
 cost=bundle['cost']
 if not isinstance(cost.get('attempts'),int) or isinstance(cost.get('attempts'),bool):raise Blocked('Invalid attempt count')
 if not cost.get('unit') or not cost.get('price_source') or not cost.get('verified_at'):raise Blocked('Unverified current price')
 if cost.get('per_attempt',-1)<0 or cost.get('attempts',0)<1 or cost.get('ceiling',-1)<cost['per_attempt']*cost['attempts']:raise Blocked('Invalid cost ceiling')
 if report.get('bundle_sha256')!=fingerprint:raise Blocked('Reviewed bundle is stale')
 for key in ('content_approval','cost_approval'):
  approval=report.get(key,{})
  if approval.get('approved') is not True or approval.get('bundle_sha256')!=fingerprint or not approval.get('user_reply') or not approval.get('evidence_ref'):raise Blocked('Missing explicit user approval: '+key)
 if report.get('consumed_attempts',0)>=cost['attempts']:raise Blocked('Approved attempt limit exhausted')
 return {'ready_for_live_verification':True,'bundle_sha256':fingerprint,'cost_ceiling':cost['ceiling'],'unit':cost['unit'],'note':'Recheck live files/settings/price and human approval evidence before any paid action. No action was sent.'}
