# this_file: tests/test_cli.py
"""CLI smoke tests for twat-audio Fire entry points."""

from __future__ import annotations

import subprocess
import sys


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "twat_audio", *args],
        capture_output=True,
        text=True,
        check=False,
    )


def test_help_exits_zero() -> None:
    """twat_audio --help exits 0."""
    result = _run("--help")
    assert result.returncode == 0, result.stderr


def test_help_lists_commands() -> None:
    """--help output mentions known subcommands."""
    result = _run("--help")
    assert result.returncode == 0
    out = result.stdout + result.stderr
    assert "version" in out
    assert "info" in out
    assert "transcode" in out
    assert "normalize" in out


def test_version_exits_zero() -> None:
    """twat_audio version exits 0."""
    result = _run("version")
    assert result.returncode == 0, result.stderr


def test_version_prints_semver() -> None:
    """version subcommand prints a semver-ish string."""
    result = _run("version")
    assert result.returncode == 0
    out = (result.stdout + result.stderr).strip()
    assert out, "version output must not be empty"
    # semver has at least one dot
    assert "." in out, f"Expected semver, got: {out!r}"


def test_info_help_exits_zero() -> None:
    """twat_audio info --help exits 0."""
    result = _run("info", "--help")
    assert result.returncode == 0, result.stderr


def test_transcode_help_exits_zero() -> None:
    """twat_audio transcode --help exits 0."""
    result = _run("transcode", "--help")
    assert result.returncode == 0, result.stderr


def test_normalize_help_exits_zero() -> None:
    """twat_audio normalize --help exits 0."""
    result = _run("normalize", "--help")
    assert result.returncode == 0, result.stderr


def test_silence_trim_help_exits_zero() -> None:
    """twat_audio silence-trim --help exits 0."""
    result = _run("silence-trim", "--help")
    assert result.returncode == 0, result.stderr


def test_resample_help_exits_zero() -> None:
    """twat_audio resample --help exits 0."""
    result = _run("resample", "--help")
    assert result.returncode == 0, result.stderr


def test_effect_help_exits_zero() -> None:
    """twat_audio effect --help exits 0."""
    result = _run("effect", "--help")
    assert result.returncode == 0, result.stderr


def test_replace_help_exits_zero() -> None:
    """twat_audio replace --help exits 0."""
    result = _run("replace", "--help")
    assert result.returncode == 0, result.stderr
