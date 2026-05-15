# twat-audio

`twat-audio` is the audio-file domain package for the `twat` ecosystem. It preserves the existing Pedalboard resampling API and adds deterministic ffmpeg-backed helpers for common audio-file workflows.

## Requirements

- Python 3.10+
- `pedalboard` for resampling
- `ffmpeg`/`ffprobe` for metadata, trimming, extraction, normalization, and muxing helpers

## Python API

```python
from twat_audio import AudioProcessConfig, resample_audio, normalize_audio, trim_audio

resample_audio(AudioProcessConfig("input.wav", "speech-16k.wav", target_samplerate=16000.0))
normalize_audio("input.wav", "normal.wav")
trim_audio("input.wav", "intro.wav", start=0, duration=5)
```

Implemented helpers:

- `resample_audio`: existing Pedalboard resampling behavior.
- `audio_metadata`: ffprobe metadata.
- `normalize_audio`, `trim_audio`, `extract_audio`.
- `replace_audio`: import/replace media audio tracks.
- `simple_effect`: explicit ffmpeg audio filter helper for deterministic effects.
- `generate_audio`: optional thin adapter to `twat_genai` audio providers.

Speech-specific STT, TTS, and dubbing orchestration belong in `twat_speech`; this package stays focused on audio files and signals.

## CLI

```bash
python -m twat_audio --help
python -m twat_audio resample input.wav speech.wav --samplerate 16000
python -m twat_audio normalize input.wav normal.wav --dry-run
python -m twat_audio trim input.wav clip.wav --start 2 --duration 5 --dry-run
python -m twat_audio extract movie.mp4 voice.wav --dry-run
python -m twat_audio replace silent.mp4 voice.wav dubbed.mp4 --dry-run
```

## Reference scripts

The audio portions of `vidimportaudio`, `vidpredub.py`, `viddub-*`, and `vidreverb.py` are represented here only where they are deterministic audio-file operations. Dubbing plans, speech provider calls, transcript handling, and subtitle work live in `twat_speech`.
