"""Tests for twat_audio ffmpeg command construction."""
# this_file: tests/test_audio_operations.py

import pytest

from twat_audio import extract_audio, normalize_audio, replace_audio, simple_effect, trim_audio


def test_normalize_trim_extract_replace_commands() -> None:
    normalized = normalize_audio("in.wav", "out.wav", target_i=-18, dry_run=True)
    assert any("loudnorm=I=-18" in part for part in normalized.command)
    trimmed = trim_audio("in.wav", "clip.wav", start=1.25, duration=2.5, dry_run=True)
    assert "-ss" in trimmed.command and "1.25" in trimmed.command
    extracted = extract_audio("movie.mp4", "voice.wav", dry_run=True)
    assert "-vn" in extracted.command
    replaced = replace_audio("movie.mp4", "voice.wav", "muxed.mp4", dry_run=True)
    assert replaced.command.count("-i") == 2


def test_simple_effect_rejects_empty_filter() -> None:
    with pytest.raises(ValueError, match="must not be empty"):
        simple_effect("in.wav", "out.wav", "  ", dry_run=True)


def test_simple_effect_builds_filter_command() -> None:
    result = simple_effect("in.wav", "out.wav", "volume=0.5", dry_run=True)
    assert "volume=0.5" in result.command
