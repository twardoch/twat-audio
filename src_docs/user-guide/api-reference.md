# Python API Reference

All public symbols are importable from `twat_audio` directly.

```python
from twat_audio import (
    AudioProcessConfig,
    CommandResult,
    resample_audio,
    normalize_audio,
    trim_audio,
    extract_audio,
    replace_audio,
    simple_effect,
    audio_metadata,
    probe_audio,
    run_ffmpeg,
    run_command,
    generate_audio,
)
```

## Data Classes

### `AudioProcessConfig`

Configuration for `resample_audio`.

```python
@dataclass
class AudioProcessConfig:
    input_file: str | Path
    output_file: str | Path
    target_samplerate: float = 22050.0
```

### `CommandResult`

Immutable result from a command execution or dry run.

```python
@dataclass(frozen=True)
class CommandResult:
    command: list[str]   # Full command as list of strings
    returncode: int       # Exit code (0 = success)
    stdout: str
    stderr: str
```

In `dry_run=True` mode, `returncode` is `0` and `stdout`/`stderr` are empty strings.

## Functions

### `resample_audio(config, *, debug=False) -> dict`

Load an audio file, resample it, and save to the output path using Pedalboard.

Returns a dict with keys: `input_file`, `output_file`, `original_samplerate`, `target_samplerate`, `num_channels`, `duration_seconds`, `status`.

Raises `FileNotFoundError` if the input file does not exist.

### `normalize_audio(input_path, output_path, *, target_i=-16.0, dry_run=False) -> CommandResult`

Normalize loudness with ffmpeg's `loudnorm` filter (EBU R128 standard). `target_i` is the integrated loudness target in LUFS.

### `trim_audio(input_path, output_path, *, start=0.0, duration=None, dry_run=False) -> CommandResult`

Trim an audio segment. `start` is the offset in seconds; `duration` is the clip length in seconds (omit to trim to end of file).

### `extract_audio(input_path, output_path, *, codec='pcm_s16le', dry_run=False) -> CommandResult`

Extract audio from a media file. `codec` is any ffmpeg audio codec name.

### `replace_audio(video_path, audio_path, output_path, *, dry_run=False) -> CommandResult`

Replace a media file's audio stream with a separate audio file. Video stream is stream-copied; output duration is the shortest of the two inputs.

### `simple_effect(input_path, output_path, effect, *, dry_run=False) -> CommandResult`

Apply any ffmpeg `-af` filter expression. Raises `ValueError` if `effect` is blank.

### `audio_metadata(path, *, dry_run=False) -> dict | CommandResult`

Return `ffprobe` JSON metadata for an audio/media file. In normal mode returns a dict with `format` and `streams` keys. In `dry_run` mode returns a `CommandResult`.

### `probe_audio(path, *, dry_run=False) -> dict | CommandResult`

Low-level alias for `audio_metadata`.

### `run_ffmpeg(args, *, dry_run=False) -> CommandResult`

Run `ffmpeg -hide_banner` with the provided argument list.

### `run_command(command, *, dry_run=False) -> CommandResult`

Run an arbitrary command. Raises `RuntimeError` on non-zero exit.

### `generate_audio(prompt, *, output_dir='generated_audio', **kwargs) -> Any`

Optional thin adapter to a `twat_genai` audio provider. Requires `twat-genai` to be installed. Raises `RuntimeError` if `twat_genai` is not available.
