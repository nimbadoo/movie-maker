"""Render a reproducible scratch mix. All non-speech sounds are synthetic placeholders."""
import argparse
import json
from pathlib import Path
import subprocess
import wave
import numpy as np

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('spec', type=Path)
parser.add_argument('--ffmpeg', required=True)
args = parser.parse_args()
source = args.spec.resolve()
spec = json.loads(source.read_text())
episode = source.parent.parent
rate = 24000
count = round(spec['duration_seconds'] * rate)
rng = np.random.default_rng(spec['seed'])
stems = {name: np.zeros(count, dtype=np.float64) for name in ['dialogue', 'breath', 'ambience', 'water', 'foley']}

def noise(length, low, high):
    n = round(length * rate)
    signal = rng.normal(size=n)
    freq = np.fft.rfftfreq(n, 1 / rate)
    mask = np.minimum(1, freq / max(low, 1)) ** 3 / (1 + (freq / high) ** 6)
    filtered = np.fft.irfft(np.fft.rfft(signal) * mask, n=n)
    return filtered / max(np.sqrt(np.mean(filtered ** 2)), 1e-8)

def sound(kind, length):
    n = round(length * rate)
    t = np.arange(n) / rate
    env = np.sin(np.pi * np.arange(n) / max(n - 1, 1)) ** 2
    if kind == 'wind':
        return noise(length, 40, 400) * (.6 + .2 * np.sin(2*np.pi*.13*t))
    if kind in ('breath-younes', 'breath-girl'):
        return noise(length, 180 if kind.endswith('younes') else 450, 1400) * env * (.85 + .15*np.sin(2*np.pi*9*t))
    if kind == 'water':
        return noise(length, 650, 2600) * (.4 + .1*np.sin(2*np.pi*31*t))
    if kind == 'drop':
        return np.sin(2*np.pi*(950*t - 130*t*t)) * np.exp(-t*24)
    if kind == 'tool':
        return (np.sin(2*np.pi*1250*t) + .3*noise(length, 700, 4000)) * np.exp(-t*22)
    if kind in ('soil', 'cloth'):
        return noise(length, 500 if kind == 'soil' else 150, 3000 if kind == 'soil' else 1000) * env * (.6+.4*np.sin(2*np.pi*12*t)**2)
    if kind in ('stone','step','pot','support'):
        return (noise(length, 80, 1200) + .3*np.sin(2*np.pi*(180 if kind == 'pot' else 100)*t)) * np.exp(-t*18)
    raise ValueError(kind)

def wav_write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    pcm = np.round(np.clip(data, -1, 1)*32767).astype('<i2')
    with wave.open(str(path), 'wb') as wav:
        wav.setnchannels(1); wav.setsampwidth(2); wav.setframerate(rate); wav.writeframes(pcm.tobytes())

def place(stem, start, data, gain=1):
    at = round(start * rate)
    end = at + len(data)
    if at < 0 or end > count:
        raise ValueError(f'Audio exceeds timeline: {start} to {end / rate}')
    stems[stem][at:end] += data * gain

# Bank files allow the temporary breathing to be replaced without rewriting the mix.
for who in ['younes','girl']:
    file = episode / 'audio/foley' / f'breath-{who}-synthetic-t01.wav'
    wav_write(file, sound('breath-'+who, 1.0)*.04)

manifest = json.loads((episode / 'audio/dialogue/takes-v1.json').read_text())
placements = []
for line in manifest['takes']:
    with wave.open(str(episode / line['file'])) as wav:
        if wav.getframerate() != rate or wav.getnchannels() != 1:
            raise ValueError('Dialogue must be mono 24 kHz')
        data = np.frombuffer(wav.readframes(wav.getnframes()), dtype='<i2').astype(float)/32768
    if line['start'] + len(data)/rate > line['planned_end']:
        raise ValueError(f"Dialogue overflows its planned window: {line['id']}")
    data *= .32 / max(np.max(np.abs(data)), 1e-8)
    if line['speaker'] == 'girl':
        # Muted interior perspective without an invented large-cave echo.
        freq = np.fft.rfftfreq(len(data), 1/rate)
        data = np.fft.irfft(np.fft.rfft(data)/(1+(freq/2200)**4), n=len(data))
    place('dialogue', line['start'], data)
    placements.append(dict(id=line['id'],start=line['start'],end=round(line['start']+len(data)/rate,4)))
for cue in spec['events']:
    place(cue['stem'], cue['start'], sound(cue['kind'],cue['duration']),cue['gain'])
# Smooth relative ducking under speech; preserve quiet water through every pause.
duck = np.ones(count)
for cue in placements:
    a=max(0,round((cue['start']-.15)*rate)); b=round(cue['start']*rate)
    c=round(cue['end']*rate); d=min(count,round((cue['end']+.2)*rate))
    duck[a:b] = np.minimum(duck[a:b],np.linspace(1,.35,b-a))
    duck[b:c] = .35
    duck[c:d] = np.minimum(duck[c:d],np.linspace(.35,1,d-c))
for name in ['ambience','water','foley','breath']:
    stems[name] *= duck
mix = sum(stems.values())
peak = float(np.max(np.abs(mix)))
if peak > .9:
    raise ValueError(f'Mix needs a gain revision; peak={peak}')
output = source.parent / spec['output']
wav_write(output,mix)
for name, data in stems.items():
    wav_file=source.parent/f'{spec["id"]}-{name}-scratch-v1.wav'
    wav_write(wav_file,data)
    flac_file=wav_file.with_suffix('.flac')
    subprocess.run([args.ffmpeg,'-y','-loglevel','error','-i',str(wav_file),str(flac_file)],check=True)
    wav_file.unlink()
report=dict(duration_seconds=count/rate,peak_linear=peak,dialogue_placements=placements,auditioned=False,synthetic_non_speech=True,natural_actor_timing_verified=False)
(source.parent / f'{spec["id"]}-scratch-report-v1.json').write_text(json.dumps(report,indent=2)+'\n')
print(output)
print(json.dumps(report))
