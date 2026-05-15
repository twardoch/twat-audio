"""Deterministic audio-file operations for twat-audio."""
# this_file: src/twat_audio/operations.py

from __future__ import annotations

from pathlib import Path

from twat_audio.ffmpeg import CommandResult, probe_audio, run_ffmpeg


def normalize_audio(input_path: str | Path, output_path: str | Path, *, target_i: float = -16.0, dry_run: bool = False) -> CommandResult:
    """Normalize loudness with ffmpeg's loudnorm filter."""
    return run_ffmpeg(["-y", "-i", str(input_path), "-af", f"loudnorm=I={target_i:g}:TP=-1.5:LRA=11", str(output_path)], dry_run=dry_run)


def trim_audio(input_path: str | Path, output_path: str | Path, *, start: float = 0.0, duration: float | None = None, dry_run: bool = False) -> CommandResult:
    """Trim an audio segment."""
    args = ["-y", "-ss", f"{start:g}", "-i", str(input_path)]
    if duration is not None:
        args += ["-t", f"{duration:g}"]
    args += ["-c", "copy", str(output_path)]
    return run_ffmpeg(args, dry_run=dry_run)


def extract_audio(input_path: str | Path, output_path: str | Path, *, codec: str = "pcm_s16le", dry_run: bool = False) -> CommandResult:
    """Extract audio from a media file."""
    return run_ffmpeg(["-y", "-i", str(input_path), "-vn", "-acodec", codec, str(output_path)], dry_run=dry_run)


def replace_audio(video_path: str | Path, audio_path: str | Path, output_path: str | Path, *, dry_run: bool = False) -> CommandResult:
    """Replace a media file's audio stream with a separate audio file."""
    return run_ffmpeg(["-y", "-i", str(video_path), "-i", str(audio_path), "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy", "-shortest", str(output_path)], dry_run=dry_run)


def simple_effect(input_path: str | Path, output_path: str | Path, effect: str, *, dry_run: bool = False) -> CommandResult:
    """Apply a caller-provided ffmpeg audio filter string."""
    if not effect.strip():
        msg = "effect filter must not be empty"
        raise ValueError(msg)
    return run_ffmpeg(["-y", "-i", str(input_path), "-af", effect, str(output_path)], dry_run=dry_run)


def audio_metadata(path: str | Path, *, dry_run: bool = False) -> dict[str, object] | CommandResult:
    """Return audio/media metadata via ffprobe."""
    return probe_audio(path, dry_run=dry_run)
