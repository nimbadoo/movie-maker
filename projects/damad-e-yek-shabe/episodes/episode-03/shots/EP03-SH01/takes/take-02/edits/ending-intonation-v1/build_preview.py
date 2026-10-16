"""Bounded local PSOLA intonation audition; never overwrites the source take."""
from pathlib import Path
import hashlib
import json
import subprocess
import numpy as np
import parselmouth
from parselmouth.praat import call
import soundfile as sf
import imageio_ffmpeg

out = Path(__file__).resolve().parent
take = out.parents[1]
source = take / 'video.mp4'
source_wav = take / 'edits/source-audio.wav'
recording = take.parents[1] / 'audio/user-performance-v1/nazli-mother-original.m4a'
selected = take / 'edits/EP03-SH01-review-v1.mp4'
ff = imageio_ffmpeg.get_ffmpeg_exe()
wav = out / 'mother-original-ending-question-v1.wav'
video = out / 'EP03-SH01-original-voice-question-preview-v1.mp4'
assert not wav.exists() and not video.exists(), 'Choose a new version.'
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
before = {str(p): sha(p) for p in [source, source_wav, selected, recording]}
assert before[str(source)] == 'dafa81e028033c2213909f965970f5572b11b3b46ce4f0269e5f0b93fa7e0af6'
x, sr = sf.read(source_wav, dtype='float64', always_2d=True)
y = x.copy()
start, end, outer_end = 5.30, 5.77, 5.88
pitch_records = []
for c in range(x.shape[1]):
    sound = parselmouth.Sound(x[:, c], sampling_frequency=sr)
    manipulation = call(sound, 'To Manipulation', 0.005, 100, 500)
    tier = call(manipulation, 'Extract pitch tier')
    n = call(tier, 'Get number of points')
    points = [(call(tier, 'Get time from index', i), call(tier, 'Get value at index', i)) for i in range(1, n+1)]
    anchor = float(call(tier, 'Get value at time', start))
    call(tier, 'Remove points between', start, outer_end)
    changed = []
    for t, f in points:
        if start <= t <= outer_end:
            progress = np.clip((t-start)/(end-start), 0, 1)
            ease = progress*progress*(3-2*progress)
            target = anchor * 2**((3.5*ease)/12)
            # Keep the original start continuous; preserve 10% of micro variation.
            target *= (f/anchor)**(0.1*(1-progress))
            call(tier, 'Add point', t, float(target))
            changed.append([float(t), float(f), float(target)])
    call([tier, manipulation], 'Replace pitch tier')
    resynth = call(manipulation, 'Get resynthesis (overlap-add)').values[0]
    assert len(resynth) == len(x)
    times = np.arange(len(x))/sr
    mask = np.zeros(len(x))
    zone = (times >= start) & (times < outer_end)
    mask[zone] = 1
    a = (times >= start) & (times < start+.04)
    mask[a] = .5-.5*np.cos(np.pi*(times[a]-start)/.04)
    b = (times >= outer_end-.06) & (times < outer_end)
    mask[b] = .5+.5*np.cos(np.pi*(times[b]-(outer_end-.06))/.06)
    y[:, c] = x[:, c]*(1-mask)+resynth*mask
    pitch_records.append({'channel':c,'anchor_hz':anchor,'changed_pitch_points':changed})
assert np.array_equal(x[:int(start*sr)], y[:int(start*sr)])
assert np.array_equal(x[int(outer_end*sr)+1:], y[int(outer_end*sr)+1:])
assert np.isfinite(y).all() and np.abs(y).max()<1
sf.write(wav, y, sr, subtype='PCM_16')
def run(args):
    return subprocess.run([ff,'-nostdin','-hide_banner','-v','error',*args],check=True,capture_output=True)
run(['-i',str(source),'-i',str(wav),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-t','8','-movflags','+faststart',str(video)])
run(['-i',str(video),'-f','null','-'])
def vhash(p):
    return run(['-i',str(p),'-map','0:v:0','-c:v','copy','-f','hash','-hash','sha256','-']).stdout.decode().strip()
assert vhash(source)==vhash(video)
assert before=={str(p):sha(p) for p in [source,source_wav,selected,recording]}
new_samples, new_sr = sf.read(wav, always_2d=True)
assert new_sr==sr and new_samples.shape==x.shape
unchanged = np.ones(len(x), dtype=bool)
unchanged[int(start*sr):int(outer_end*sr)+1] = False
assert np.max(np.abs(new_samples[unchanged]-x[unchanged])) <= 1/32768
record = {'skill':'review-and-assemble','status':'experimental_not_selected',
 'authorization':'همون صدای طبیعی قبلی مادر رو نگه دار و فقط آخر جمله رو متعجب و سوالی کن؛ ضبط من فقط مرجع لحن باشه. نسخهٔ اصلی بمونه و اگر هزینه‌ای داره، قبلش بگو.',
 'source_video':{'path':str(source),'sha256':sha(source)},'source_audio':{'path':str(source_wav),'sha256':sha(source_wav)},
 'intonation_reference_only':{'path':str(recording),'sha256':sha(recording),'not_voice_conversion_input':True},
 'method':'Praat PSOLA overlap-add, terminal pitch-tier edit only',
 'parselmouth_version':parselmouth.__version__,'edit_start_seconds':start,'edit_end_seconds':outer_end,
 'target_rise_semitones':3.5,'pitch_analysis':pitch_records,'source_audio_duration_seconds':len(x)/sr,
 'output_audio_duration_seconds':len(y)/sr,'speed_change':False,'voice_conversion':False,'word_synthesis':False,
 'audio_outside_edit_equal_within_pcm_quantization':True,'video_packet_hash_unchanged':True,
 'inputs_unchanged':True,'full_decode_passed':True,'samples_at_digital_limit':int((np.abs(y)>=1).sum()),
 'human_listening_verified':False,'expressive_success_verified':False,'precise_lip_sync_verified':False,
 'external_credits':0,'free_generation_slots_used':0,'external_uploads':0,
 'outputs':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in [wav,video]],
 'notes':['Source is raw original take, not Seed-VC converted user performance.','Pitch change is a local audition, not a claim of natural surprise performance.','Recording informs requested performance only; its pitch contour is not cloned.','Original source and previous selected media preserved; no acceptance state changed.']}
(out/'review-package.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'video':str(video),'audio':str(wav),'edit_seconds':[start,outer_end],'duration':len(y)/sr,'source_preserved':True},ensure_ascii=False,indent=2))
