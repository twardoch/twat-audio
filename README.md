# twat-audio

**Audio processing utilities for the [twat](https://github.com/twardoch/twat) ecosystem.**

`twat-audio` provides deterministic, file-level audio helpers built on two backends:

- **[Pedalboard](https://github.com/spotify/pedalboard)** (Spotify) — fast, high-quality resampling via libsndfile/libresample.
- **[ffmpeg](https://ffmpeg.org/)** — normalization, trimming, audio extraction, muxing, and arbitrary filter application.

Speech-specific concerns (STT, TTS, dubbing orchestration, transcript handling) belong in `twat_speech`. This package stays focused on audio *files* and *signals*.

## Requirements

- Python 3.10+
- `ffmpeg` and `ffprobe` on `PATH` (for all operations except `resample_audio`)

## Installation

```bash
pip install twat-audio
```

Or with [uv](https://github.com/astral-sh/uv):

```bash
uv add twat-audio
```

## Python API

```python
from twat_audio import AudioProcessConfig, resample_audio, normalize_audio, trim_audio

# Resample to 16 kHz (common ML model input rate)
result = resample_audio(
    AudioProcessConfig("speech.wav", "speech_16k.wav", target_samplerate=16000.0)
)
print(result["status"])  # "success"

# Normalize loudness (EBU R128, target -16 LUFS)
normalize_audio("speech.wav", "speech_norm.wav", target_i=-16.0)

# Trim: start at 2 s, take 5 s
trim_audio("speech.wav", "clip.wav", start=2.0, duration=5.0)
```

### All Public Functions

| Function | Backend | Description |
|---|---|---|
| `resample_audio(config)` | Pedalboard | Resample to any sample rate |
| `normalize_audio(in, out, ...)` | ffmpeg | Loudness normalization (EBU R128) |
| `trim_audio(in, out, ...)` | ffmpeg | Trim by time range |
| `extract_audio(in, out, ...)` | ffmpeg | Extract audio from video |
| `replace_audio(video, audio, out)` | ffmpeg | Replace audio track in video |
| `simple_effect(in, out, filter)` | ffmpeg | Apply any ffmpeg `-af` filter |
| `audio_metadata(path)` | ffprobe | Read media metadata as dict |
| `generate_audio(prompt, ...)` | twat_genai | AI audio generation (optional) |

## CLI

```bash
# Show all subcommands
python -m twat_audio --help

# Resample
twat-audio resample input.wav output.wav --samplerate 16000

# Normalize (--dry-run prints the command without running it)
twat-audio normalize input.wav output.wav --dry-run

# Trim: 5-second clip starting at 2 s
twat-audio silence-trim input.wav clip.wav --start 2 --duration 5

# Extract audio from video
twat-audio transcode movie.mp4 voice.wav

# Replace audio track
twat-audio replace silent.mp4 voice.wav dubbed.mp4

# Apply ffmpeg filter
twat-audio effect input.wav loud.wav --audio-filter "volume=2.0"

# Read metadata
twat-audio info input.wav

# Print version
twat-audio version
```

## Supported Formats

Resampling (Pedalboard): **WAV, AIFF, FLAC, OGG, MP3**.

ffmpeg operations: all formats ffmpeg supports, including MP4/MKV/MOV/AVI/WebM containers for audio extraction.

## Role in the twat Ecosystem

`twat-audio` is a plugin for the [twat](https://github.com/twardoch/twat) host package. It registers under the `twat.plugins` entry point as `audio`. Other twat plugins can import it to gain audio file operations without depending on ffmpeg directly.

```python
# Via twat plugin discovery
import twat
twat.audio.normalize_audio("in.wav", "out.wav")
```

## Development

```bash
git clone https://github.com/twardoch/twat-audio
cd twat-audio
uv venv --python 3.12
uv pip install -e ".[dev,test]"
python -m pytest tests/ -v
```

Lint and format:

```bash
ruff check src/twat_audio tests
ruff format src/twat_audio tests
```

See [STYLE_GUIDE.md](STYLE_GUIDE.md) for coding conventions and [CONTRIBUTING](src_docs/development/contributing.md) for the full development workflow.

## License

MIT — see [LICENSE](LICENSE).
