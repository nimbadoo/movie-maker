"""Read-only local transcription of replacement06, no reference-text hint."""
from pathlib import Path
import sys,json,hashlib,subprocess
sys.path.insert(0,'C:/Users/momen/.codex/visualizations/2026/10/12/01a13208-3576-7443-b60d-b2202e3e3738/video-review-deps')
import numpy as np
from faster_whisper import WhisperModel
from faster_whisper.vad import get_speech_timestamps,VadOptions
P=Path(__file__).resolve().parents[1]/'episodes/episode-05/dialogs-input'
source=P/'06.m4a'
ffmpeg='C:/Users/momen/.codex/tmp/ep03-media-review-deps/imageio_ffmpeg/binaries/ffmpeg-win-x86_64-v7.1.exe'
decoded=subprocess.run([ffmpeg,'-v','error','-i',str(source),'-ar','16000','-ac','1','-f','f32le','-'],capture_output=True,check=True)
samples=np.frombuffer(decoded.stdout,dtype=np.float32).copy()
model=WhisperModel('C:/Users/momen/.codex/visualizations/2026/10/12/01a13208-3576-7443-b60d-b2202e3e3738/video-review/models/models--Systran--faster-whisper-small/snapshots/536b0662742c02347bc0e980a01041f333bce120',device='cpu',compute_type='int8',local_files_only=True)
segments,info=model.transcribe(samples,language='fa',beam_size=5,temperature=0,word_timestamps=True,vad_filter=False,condition_on_previous_text=False)
segments=list(segments)
vad=get_speech_timestamps(samples,vad_options=VadOptions(threshold=.35,min_speech_duration_ms=100,min_silence_duration_ms=250,speech_pad_ms=0))
r={'file':'06.m4a','sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'decoded_duration_seconds':len(samples)/16000,'method':'local faster-whisper small int8, fa, beam5, no prompt/reference text, no external service; same model not independent audition','audition_performed':False,'text':''.join(s.text for s in segments).strip(),'segments':[{'start':s.start,'end':s.end,'text':s.text,'words':[{'start':w.start,'end':w.end,'word':w.word,'probability':w.probability} for w in (s.words or [])]} for s in segments],'speech_ranges':[{'start':v['start']/16000,'end':v['end']/16000} for v in vad],'peak_dbfs':float(20*np.log10(max(float(np.max(np.abs(samples))),1e-12))),'clip_samples':int(np.sum(np.abs(samples)>=.999)),'audio_modified':False,'video_generated':False}
(P/'06-rerecord-check-v1.json').write_text(json.dumps(r,ensure_ascii=False,indent=2),encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8');print(json.dumps(r,ensure_ascii=False,indent=2))
