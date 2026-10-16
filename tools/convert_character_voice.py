#!/usr/bin/env python3
"""Local OpenVoice tone conversion; outputs are experiments until reviewed."""
import argparse
import hashlib
import json
import sys
import time
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('engine-dir', 'checkpoint', 'config', 'source', 'reference', 'output'):
        p.add_argument('--' + name, type=Path, required=True)
    args = p.parse_args()
    for path in (args.checkpoint, args.config, args.source, args.reference):
        if not path.is_file():
            p.error(f'Missing input: {path}')
    if args.output.exists() or args.output.with_suffix('.json').exists():
        p.error('Output already exists; choose a new attempt filename.')
    sys.path.insert(0, str(args.engine_dir.resolve()))
    import torch
    import soundfile as sf
    from openvoice.api import ToneColorConverter

    def asset(path):
        audio, rate = sf.read(path)
        return dict(path=str(path.resolve()), sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                    samples=len(audio), sample_rate=rate, duration_seconds=len(audio) / rate)

    source, reference = asset(args.source), asset(args.reference)
    started = time.monotonic()
    torch.manual_seed(42)
    torch.set_num_threads(4)
    converter = ToneColorConverter(str(args.config), device='cpu', enable_watermark=False)
    converter.load_ckpt(str(args.checkpoint))
    source_embedding = converter.extract_se(str(args.source))
    reference_embedding = converter.extract_se(str(args.reference))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    converter.convert(str(args.source), source_embedding, reference_embedding,
                      str(args.output), tau=0.3)
    output = asset(args.output)
    record = dict(status='experimental_not_approved', model='OpenVoiceV2 ToneColorConverter',
                  source=source, reference=reference, output=output, seed=42, tau=0.3,
                  checkpoint_sha256=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest(),
                  elapsed_seconds=time.monotonic() - started, external_generation_credits=0,
                  duration_delta_seconds=output['duration_seconds'] - source['duration_seconds'],
                  human_listening_verified=False, speaker_identity_verified=False,
                  phoneme_alignment_verified=False, clipped_word_repair=False,
                  notes=['No text synthesis, pitch shift, time stretch, or missing-word repair.',
                         'Optional watermark encoder not loaded; no existing watermark removal.',
                         'Duration alone does not prove lip synchronization.'])
    assert source == asset(args.source) and reference == asset(args.reference), 'Input changed'
    args.output.with_suffix('.json').write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(record, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
