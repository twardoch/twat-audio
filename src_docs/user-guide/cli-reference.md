# CLI Reference

`twat-audio` ships a [Fire](https://github.com/google/python-fire)-based CLI. Every subcommand is also available as a standalone entry point (e.g. `twat-audio-resample`).

## Global Usage

```
python -m twat_audio [COMMAND] [ARGS...]
twat-audio [COMMAND] [ARGS...]
```

## Commands

### `version`

Print the installed version string.

```bash
twat-audio version
```

### `info`

Return audio/media metadata via `ffprobe`.

```
twat-audio info PATH
```

| Argument | Type | Description |
|----------|------|-------------|
| `PATH` | str | Path to audio or video file |

### `resample`

Resample an audio file using Pedalboard (high-quality linear interpolation).

```
twat-audio resample INPUT OUTPUT [--samplerate RATE]
```

| Argument | Default | Description |
|----------|---------|-------------|
| `INPUT` | — | Input audio file |
| `OUTPUT` | — | Output audio file |
| `--samplerate` | `22050.0` | Target sample rate in Hz |

### `normalize`

Normalize loudness with ffmpeg's `loudnorm` filter (EBU R128).

```
twat-audio normalize INPUT OUTPUT [--target-i DB] [--dry-run]
```

| Argument | Default | Description |
|----------|---------|-------------|
| `INPUT` | — | Input audio file |
| `OUTPUT` | — | Output audio file |
| `--target-i` | `-16.0` | Integrated loudness target (LUFS) |
| `--dry-run` | `False` | Print command without executing |

### `silence-trim`

Trim an audio segment by time range.

```
twat-audio silence-trim INPUT OUTPUT [--start S] [--duration D] [--dry-run]
```

| Argument | Default | Description |
|----------|---------|-------------|
| `INPUT` | — | Input audio file |
| `OUTPUT` | — | Output audio file |
| `--start` | `0.0` | Start offset in seconds |
| `--duration` | `None` | Duration in seconds (omit for end of file) |
| `--dry-run` | `False` | Print command without executing |

### `transcode`

Extract (and optionally re-encode) audio from a media file.

```
twat-audio transcode INPUT OUTPUT [--codec CODEC] [--dry-run]
```

| Argument | Default | Description |
|----------|---------|-------------|
| `INPUT` | — | Input file (audio or video) |
| `OUTPUT` | — | Output audio file |
| `--codec` | `pcm_s16le` | ffmpeg audio codec |
| `--dry-run` | `False` | Print command without executing |

### `effect`

Apply any ffmpeg audio filter string.

```
twat-audio effect INPUT OUTPUT --audio-filter FILTER [--dry-run]
```

| Argument | Default | Description |
|----------|---------|-------------|
| `INPUT` | — | Input audio file |
| `OUTPUT` | — | Output audio file |
| `--audio-filter` | — | ffmpeg `-af` filter expression |
| `--dry-run` | `False` | Print command without executing |

**Example:**

```bash
twat-audio effect input.wav loud.wav --audio-filter "volume=2.0"
```

### `replace`

Replace a media file's audio stream with a separate audio file.

```
twat-audio replace VIDEO AUDIO OUTPUT [--dry-run]
```

| Argument | Default | Description |
|----------|---------|-------------|
| `VIDEO` | — | Input video file |
| `AUDIO` | — | Replacement audio file |
| `OUTPUT` | — | Output file with replaced audio |
| `--dry-run` | `False` | Print command without executing |
