"""Render deterministic synthetic timing cues; not recorded foley or actor audio."""
import argparse
from array import array
import json
import math
from pathlib import Path
import random
import sys
import wave

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('cues', type=Path)
args = parser.parse_args()
source = args.cues.resolve()
spec = json.loads(source.read_text())
rate = 22050
rng = random.Random(42)
samples = array('f', [0.0]) * round(spec['duration_seconds'] * rate)
filtered = 0.0
for n in range(len(samples)):
    filtered = filtered * 0.985 + rng.uniform(-1, 1) * 0.015
    samples[n] = filtered * 0.035
for cue in spec['events']:
    start = round(cue['start'] * rate)
    count = round(cue['duration'] * rate)
    kind = cue['kind']
    for n in range(count):
        if start + n >= len(samples):
            break
        t = n / rate
        envelope = math.sin(math.pi * n / max(1, count - 1)) ** 2
        noise = rng.uniform(-1, 1)
        if kind == 'soil':
            signal = noise * (0.35 + 0.65 * math.sin(2 * math.pi * 13 * t) ** 2)
        elif kind == 'tool':
            signal = math.exp(-t * 17) * (math.sin(2 * math.pi * 1300 * t) + noise * 0.25)
            envelope = 1.0
        elif kind == 'stone':
            signal = noise * math.exp(-t * 12) + math.sin(2 * math.pi * 170 * t) * math.exp(-t * 23)
            envelope = 1.0
        elif kind == 'water':
            signal = noise * 0.25 + math.sin(2 * math.pi * 750 * t) * math.sin(2 * math.pi * 37 * t) * 0.12
        else:
            raise ValueError(kind)
        samples[start + n] += signal * envelope * cue['gain']
peak = max(abs(x) for x in samples) or 1.0
scale = min(1.0, 0.24 / peak)
pcm = array('h', (round(max(-1, min(1, x * scale)) * 32767) for x in samples))
if sys.byteorder != 'little':
    pcm.byteswap()
output = source.parent / spec['output']
with wave.open(str(output), 'wb') as audio:
    audio.setnchannels(1)
    audio.setsampwidth(2)
    audio.setframerate(rate)
    audio.writeframes(pcm.tobytes())
print(f'{output}: {len(pcm) / rate:.2f}s, synthetic cues; no speech or human breath')
