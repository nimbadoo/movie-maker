"""Synthetic local checks; no real approval, account connection or paid operation."""
import json,unittest,tempfile
from pathlib import Path
from shot_workflow import submission_gate,bundle_for_request,Blocked,CHECKS,selected_plan
class WorkflowChecks(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)/'EP02-SH13';self.take=self.root/'takes/take-09';self.take.mkdir(parents=True)
  (self.root/'frame.png').write_bytes(b'synthetic image bytes');(self.take/'prompt.txt').write_text('Synthetic prompt',encoding='utf8')
  self.card=self.root/'shot.md';self.report=self.take/'preflight.md'
  self.state={'shot':'EP02-SH13','send_request':{'take':'take-09','prompt':'prompt.txt','preflight':'preflight.md','input_files':['frame.png'],'settings':{'model':'synthetic','seconds':5,'quality':'test','aspect_ratio':'9:16','audio':True,'outputs':1},'cost':{'per_attempt':4,'attempts':1,'ceiling':4,'unit':'test-credit','price_source':'synthetic test fixture','verified_at':'test'}}}
  self.write_card();self.data={'shot':'EP02-SH13','take':'take-09','ready':True,'open_issues':[],'checks':{k:{'status':'pass','evidence':'Synthetic test evidence'} for k in CHECKS},'consumed_attempts':0}
  self.write_report();fingerprint=bundle_for_request(self.card)[-1];self.data['bundle_sha256']=fingerprint
  for key in ['content_approval','cost_approval']:self.data[key]={'approved':True,'bundle_sha256':fingerprint,'user_reply':'SYNTHETIC, NOT A REAL APPROVAL','evidence_ref':'test fixture only'}
  self.write_report()
 def tearDown(self):self.temp.cleanup()
 def write_card(self):self.card.write_text('<!-- shot-state -->\n```json\n'+json.dumps(self.state)+'\n```\n<!-- /shot-state -->\n## متن و دستور اجرا\nSynthetic creative text\n## برداشت‌ها و تاریخچه\n',encoding='utf8')
 def write_report(self):self.report.write_text('<!-- preflight-state -->\n```json\n'+json.dumps(self.data)+'\n```\n<!-- /preflight-state -->',encoding='utf8')
 def test_complete_synthetic_bundle_passes(self):self.assertTrue(submission_gate(self.card)['ready_for_live_verification'])
 def test_prompt_change_invalidates_approval(self):
  (self.take/'prompt.txt').write_text('Changed',encoding='utf8')
  with self.assertRaises(Blocked):submission_gate(self.card)
 def test_missing_cost_approval_blocks(self):
  self.data['cost_approval']['approved']=False;self.write_report()
  with self.assertRaises(Blocked):submission_gate(self.card)
 def test_incomplete_check_blocks(self):
  self.data['checks']['eyeline']['status']='unchecked';self.write_report()
  with self.assertRaises(Blocked):submission_gate(self.card)
 def test_cost_change_blocks(self):
  self.state['send_request']['cost']['ceiling']=8;self.write_card()
  with self.assertRaises(Blocked):submission_gate(self.card)
 def test_frame_change_blocks(self):
  (self.root/'frame.png').write_bytes(b'changed')
  with self.assertRaises(Blocked):submission_gate(self.card)
 def test_consumed_attempt_blocks_retry(self):
  self.data['consumed_attempts']=1;self.write_report()
  with self.assertRaises(Blocked):submission_gate(self.card)
 def test_explicit_take_survives_newer_take(self):
  rows=selected_plan(2);row=next(x for x in rows if x['shot']=='EP02-SH13');self.assertEqual(row['take'],'take-07')
 def test_creative_change_blocks(self):
  self.card.write_text(self.card.read_text(encoding='utf8').replace('Synthetic creative text','Changed delivery'),encoding='utf8')
  with self.assertRaises(Blocked):submission_gate(self.card)
 def test_settings_change_blocks(self):
  self.state['send_request']['settings']['seconds']=6;self.write_card()
  with self.assertRaises(Blocked):submission_gate(self.card)
 def test_missing_request_blocks(self):
  self.state['send_request']=None;self.write_card()
  with self.assertRaises(Blocked):submission_gate(self.card)
 def test_approval_without_evidence_blocks(self):
  self.data['content_approval']['evidence_ref']='';self.write_report()
  with self.assertRaises(Blocked):submission_gate(self.card)
 def test_zero_duration_blocks(self):
  self.state['send_request']['settings']['seconds']=0;self.write_card()
  with self.assertRaises(Blocked):submission_gate(self.card)
if __name__=='__main__':unittest.main()
