# Quick Start

## Python API

```python
from twat_audio import (
    AudioProcessConfig,
    resample_audio,
    normalize_audio,
    trim_audio,
    extract_audio,
    replace_audio,
    simple_effect,
    audio_metadata,
)

# Resample to 16 kHz
result = resample_audio(
    AudioProcessConfig("input.wav", "output_16k.wav", target_samplerate=16000.0)
)
print(result)  # dict with input/output paths, samplerates, status

# Normalize loudness (EBU R128, target -16 LUFS)
normalize_audio("input.wav", "normalized.wav", target_i=-16.0)

# Trim: start at 2 s, take 5 s
trim_audio("input.wav", "clip.wav", start=2.0, duration=5.0)

# Extract audio from a video file
extract_audio("movie.mp4", "soundtrack.wav")

# Replace a video's audio track
replace_audio("silent.mp4", "voice.wav", "dubbed.mp4")

# Apply any ffmpeg audio filter
simple_effect("input.wav", "eq.wav", "equalizer=f=1000:width_type=o:width=2:g=5")

# Read media metadata via ffprobe
info = audio_metadata("input.wav")
print(info["format"]["duration"])
```

## CLI

```bash
# Show available subcommands
python -m twat_audio --help

# Resample
twat-audio resample input.wav output.wav --samplerate 16000

# Normalize (dry-run prints the command without running it)
twat-audio normalize input.wav output.wav --dry-run

# Trim
twat-audio silence-trim input.wav clip.wav --start 2 --duration 5

# Extract audio from video
twat-audio transcode movie.mp4 voice.wav

# Replace audio
twat-audio replace silent.mp4 voice.wav dubbed.mp4

# Apply ffmpeg filter
twat-audio effect input.wav eq.wav --audio-filter "volume=0.5"

# Metadata
twat-audio info input.wav

# Version
twat-audio version
```

## Dry-Run Mode

Most ffmpeg-backed commands accept `--dry-run` (CLI) or `dry_run=True` (API).
In dry-run mode the `ffmpeg`/`ffprobe` command is constructed and returned as a
`CommandResult` but never executed — useful for testing or logging the intended
operation.
