"""ffmpeg command helpers for twat-audio."""
# this_file: src/twat_audio/ffmpeg.py

from __future__ import annotations

from collections.abc import Sequence
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class CommandResult:
    """Result from a command execution or dry run."""

    command: list[str]
    returncode: int
    stdout: str
    stderr: str


def run_command(command: Sequence[str], *, dry_run: bool = False) -> CommandResult:
    """Run a command or return its constructed form in dry-run mode."""
    cmd = [str(part) for part in command]
    if dry_run:
        return CommandResult(cmd, 0, "", "")
    completed = subprocess.run(cmd, check=False, capture_output=True, text=True)
    if completed.returncode != 0:
        msg = completed.stderr.strip() or f"command failed with exit code {completed.returncode}"
        raise RuntimeError(msg)
    return CommandResult(cmd, completed.returncode, completed.stdout, completed.stderr)


def run_ffmpeg(args: Sequence[str], *, dry_run: bool = False) -> CommandResult:
    """Run ffmpeg with a small stable prefix."""
    return run_command(["ffmpeg", "-hide_banner", *args], dry_run=dry_run)


def probe_audio(path: str | Path, *, dry_run: bool = False) -> dict[str, Any] | CommandResult:
    """Return ffprobe JSON metadata for an audio/media file."""
    command = ["ffprobe", "-hide_banner", "-v", "error", "-show_format", "-show_streams", "-of", "json", str(path)]
    result = run_command(command, dry_run=dry_run)
    if dry_run:
        return result
    data = json.loads(result.stdout)
    if not isinstance(data, dict):
        msg = "ffprobe did not return a JSON object"
        raise RuntimeError(msg)
    return data
