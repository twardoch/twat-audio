# twat-audio

**Audio processing utilities for the [twat](https://github.com/twardoch/twat) ecosystem.**

`twat-audio` provides deterministic, file-level audio helpers built on two backends:

- **[Pedalboard](https://github.com/spotify/pedalboard)** (Spotify) — fast, high-quality resampling via `libsndfile`/`libresample`.
- **[ffmpeg](https://ffmpeg.org/)** — normalization, trimming, audio extraction, muxing, and arbitrary filter application.

Speech-specific concerns (STT, TTS, dubbing orchestration, transcript handling) belong in `twat_speech`. This package stays focused on audio *files* and *signals*.

## Key Features

| Feature | Backend | CLI command |
|---|---|---|
| Resample to any sample rate | Pedalboard | `twat-audio resample` |
| Loudness normalization (EBU R128) | ffmpeg loudnorm | `twat-audio normalize` |
| Trim / cut segments | ffmpeg | `twat-audio silence-trim` |
| Extract audio from video | ffmpeg | `twat-audio transcode` |
| Replace audio track in video | ffmpeg | `twat-audio replace` |
| Apply any ffmpeg filter | ffmpeg | `twat-audio effect` |
| Read media metadata | ffprobe | `twat-audio info` |
| AI audio generation (optional) | twat-genai | Python API only |

## Quick Example

```python
from twat_audio import AudioProcessConfig, resample_audio, normalize_audio

# Resample to 16 kHz (common ML model input rate)
resample_audio(AudioProcessConfig("speech.wav", "speech_16k.wav", target_samplerate=16000.0))

# Normalize loudness in-place
normalize_audio("speech_16k.wav", "speech_norm.wav", target_i=-16.0)
```

## Installation

```bash
pip install twat-audio
```

Requires `ffmpeg` and `ffprobe` on `PATH` for all operations except resampling.

See [Installation](getting-started/installation.md) for details.
