# Supported Formats

## Resampling (Pedalboard backend)

The `resample_audio` function uses [Pedalboard](https://github.com/spotify/pedalboard) (Spotify's libsndfile wrapper). Supported formats:

| Format | Read | Write | Notes |
|--------|------|-------|-------|
| WAV | Yes | Yes | All bit depths; recommended for lossless work |
| AIFF | Yes | Yes | macOS native lossless |
| FLAC | Yes | Yes | Lossless compression |
| OGG Vorbis | Yes | Yes | Lossy open format |
| MP3 | Yes | Yes | Lossy; write requires libmp3lame |

## ffmpeg-backed Operations

`normalize_audio`, `trim_audio`, `extract_audio`, `replace_audio`, `simple_effect`, and `audio_metadata` delegate to `ffmpeg`/`ffprobe`. Every format ffmpeg supports is therefore available, including:

- **Lossless:** WAV, AIFF, FLAC, ALAC
- **Lossy:** MP3, AAC, OGG, Opus, AC3, EAC3
- **Video containers (audio extraction):** MP4, MKV, MOV, AVI, WebM

The `extract_audio` function defaults to `pcm_s16le` (uncompressed 16-bit WAV). Pass `codec=` to override:

```python
from twat_audio import extract_audio

extract_audio("movie.mp4", "voice.aac", codec="aac")
extract_audio("movie.mp4", "voice.opus", codec="libopus")
```

## Sample Rate Notes

Common target sample rates for reference:

| Rate | Use Case |
|------|----------|
| 8 000 Hz | Telephony (narrow-band) |
| 16 000 Hz | Speech recognition / ML models |
| 22 050 Hz | Legacy multimedia |
| 44 100 Hz | CD audio |
| 48 000 Hz | Video / broadcast standard |

`resample_audio` uses linear interpolation. For professional quality, pass the audio
through a high-quality resampler (e.g. SoX, `soxr`) after extraction.
