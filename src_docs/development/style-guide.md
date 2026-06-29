# Style Guide

See also [STYLE_GUIDE.md](../../STYLE_GUIDE.md) in the repository root.

## Python Version

Target Python 3.10+. Use union syntax (`X | Y`) instead of `Optional[X]` or `Union[X, Y]`.

## Type Hints

All public functions must have full type annotations on parameters and return values. Use `str | Path` for file path parameters.

## Docstrings

Use Google-style docstrings for public functions:

```python
def normalize_audio(
    input_path: str | Path,
    output_path: str | Path,
    *,
    target_i: float = -16.0,
    dry_run: bool = False,
) -> CommandResult:
    """Normalize loudness with ffmpeg's loudnorm filter.

    Args:
        input_path: Path to the input audio file.
        output_path: Path where the normalized file will be saved.
        target_i: Integrated loudness target in LUFS (EBU R128).
        dry_run: If True, construct the command but do not execute it.

    Returns:
        A CommandResult with the executed (or dry-run) command details.

    Raises:
        RuntimeError: If ffmpeg exits with a non-zero status.
    """
```

## Error Handling

- Raise `FileNotFoundError` for missing input files (checked before calling ffmpeg).
- Raise `ValueError` for invalid parameter values (e.g. empty filter string).
- Raise `RuntimeError` (with `stderr` content) when a subprocess fails.
- Never silently swallow exceptions in public API functions.

## `dry_run` Pattern

Every ffmpeg-backed function must accept a `dry_run: bool = False` keyword argument. When `dry_run=True`, call `run_ffmpeg(..., dry_run=True)` which returns a `CommandResult` with `returncode=0` and empty stdout/stderr without actually executing.

## Imports

- Standard library first, then third-party, then local (`from twat_audio.x import y`).
- Use `from __future__ import annotations` in every module.
- Prefer absolute imports within the package.

## Line Length

120 characters (configured in `pyproject.toml` `[tool.ruff]`).

## Linter

[Ruff](https://docs.astral.sh/ruff/) with the rule set defined in `pyproject.toml`. Run `ruff check --fix src/ tests/` before committing.
