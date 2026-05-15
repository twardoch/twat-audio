"""twat-audio: audio-file processing utilities for TWAT."""
# this_file: src/twat_audio/__init__.py

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

from twat_audio.__main__ import main as cli_main

try:
    __version__ = version("twat-audio")
except PackageNotFoundError:
    __version__ = "0.0.0-dev"

from twat_audio.ffmpeg import CommandResult, probe_audio, run_command, run_ffmpeg
from twat_audio.genai import generate_audio
from twat_audio.operations import audio_metadata, extract_audio, normalize_audio, replace_audio, simple_effect, trim_audio
from twat_audio.twat_audio import AudioProcessConfig, resample_audio


def main() -> None:
    """CLI entry point for twat-audio."""
    cli_main()


__all__ = [
    "AudioProcessConfig",
    "CommandResult",
    "__version__",
    "audio_metadata",
    "extract_audio",
    "generate_audio",
    "main",
    "normalize_audio",
    "probe_audio",
    "replace_audio",
    "resample_audio",
    "run_command",
    "run_ffmpeg",
    "simple_effect",
    "trim_audio",
]
