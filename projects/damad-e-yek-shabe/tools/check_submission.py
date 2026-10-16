"""Read-only local gate; never sends anything to Flow."""
import argparse,json
from pathlib import Path
from shot_workflow import P,submission_gate,bundle_for_request,Blocked
ap=argparse.ArgumentParser();ap.add_argument('--shot',required=True);ap.add_argument('--fingerprint',action='store_true');args=ap.parse_args()
matches=list(P.glob('episodes/episode-*/shots/'+args.shot+'/shot.md'))
if len(matches)!=1:raise SystemExit('BLOCKED: unique shot card not found')
try:
 if args.fingerprint:
  result={'bundle_sha256':bundle_for_request(matches[0])[-1],'submission_authorized':False,'note':'Fingerprint only; does not constitute review or approval.'}
 else:result=submission_gate(matches[0])
 print(json.dumps(result,ensure_ascii=False,indent=2))
except (Blocked,KeyError,TypeError,ValueError) as e:raise SystemExit('BLOCKED: '+str(e))
