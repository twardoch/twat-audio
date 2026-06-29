# twat-audio Style Guide

This document describes the coding conventions for `twat-audio`. All contributions should follow these guidelines. The automated enforcement is via [Ruff](https://docs.astral.sh/ruff/) and [mypy](https://mypy.readthedocs.io/).

## Python Version Target

Python 3.10+. Use modern syntax:

- Union types: `str | Path` not `Union[str, Path]`
- Optional: `str | None` not `Optional[str]`
- `from __future__ import annotations` in every module (enables forward references)

## Type Annotations

Every public function signature must be fully annotated:

```python
def trim_audio(
    input_path: str | Path,
    output_path: str | Path,
    *,
    start: float = 0.0,
    duration: float | None = None,
    dry_run: bool = False,
) -> CommandResult:
```

Private helpers (prefixed `_`) should also be annotated.

## Docstrings

Use Google-style docstrings on all public symbols:

```python
def resample_audio(config: AudioProcessConfig, *, debug: bool = False) -> dict[str, Any]:
    """Load an audio file, resample it, and save to the output path.

    Args:
        config: Processing parameters (input/output paths, target sample rate).
        debug: Enable DEBUG-level logging for this call.

    Returns:
        Dict with keys: input_file, output_file, original_samplerate,
        target_samplerate, num_channels, duration_seconds, status.

    Raises:
        FileNotFoundError: If config.input_file does not exist.
        RuntimeError: If the audio backend fails.
    """
```

## File Path Parameters

Accept both `str` and `Path` — annotate as `str | Path`. Convert to `str` only when passing to subprocess or a library that does not accept `Path` directly.

## The `dry_run` Pattern

Every ffmpeg-backed public function must support `dry_run: bool = False` as a keyword-only argument. When `True`, forward it to `run_ffmpeg(..., dry_run=True)`, which builds and returns the command without executing it. This keeps functions testable without requiring ffmpeg on the test host.

## Error Handling

| Situation | Exception |
|---|---|
| Input file missing | `FileNotFoundError` |
| Invalid parameter value | `ValueError` |
| Subprocess failure | `RuntimeError` (include stderr) |
| Optional dependency absent | `RuntimeError` with install hint |

Never use bare `except:` or `except Exception:` to silently swallow errors.

## Logging

Use `logging.getLogger(__name__)`. Never use `print()` for diagnostic output in library code. Log at `INFO` for high-level milestones, `DEBUG` for detail.

## Line Length

120 characters maximum (set in `[tool.ruff]` `line-length`).

## Import Order

1. `from __future__ import annotations`
2. Standard library
3. Third-party (`numpy`, `pedalboard`, `fire`, …)
4. Local (`from twat_audio.ffmpeg import …`)

Ruff `I` rules enforce this automatically.

## Naming

- Functions: `snake_case`
- Classes / dataclasses: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private helpers: `_leading_underscore`

## Module Headers

Every module starts with:

```python
"""One-line module summary.

Optional extended description.
"""
# this_file: src/twat_audio/module.py

from __future__ import annotations
```

## Tests

- Test files: `tests/test_<module>.py`
- Test functions: `test_<function>_<scenario>` e.g. `test_trim_audio_with_duration`
- Use `dry_run=True` for command-construction tests (no ffmpeg required)
- Use `tmp_path` fixture for file I/O tests
- Assert with descriptive messages where the failure would be ambiguous

## Ruff Rules

The active ruleset is declared in `pyproject.toml` `[tool.ruff.lint]`. Run:

```bash
ruff check --fix src/ tests/
ruff format src/ tests/
```

before every commit (or install pre-commit hooks).
