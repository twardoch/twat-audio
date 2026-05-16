# this_file: src/twat_audio/__main__.py
"""Fire CLI entry point for twat-audio."""

from __future__ import annotations

import fire


def _version() -> str:
    """Print the installed twat-audio version."""
    from twat_audio.__version__ import __version__  # noqa: PLC0415

    return __version__


def _info(path: str) -> object:
    """Return audio/media metadata via ffprobe."""
    from twat_audio.operations import audio_metadata  # noqa: PLC0415

    return audio_metadata(path)


def _transcode(
    input_path: str,
    output_path: str,
    codec: str = "pcm_s16le",
    *,
    dry_run: bool = False,
) -> object:
    """Extract/transcode audio from a media file."""
    from twat_audio.operations import extract_audio  # noqa: PLC0415

    return extract_audio(input_path, output_path, codec=codec, dry_run=dry_run)


def _normalize(
    input_path: str,
    output_path: str,
    target_i: float = -16.0,
    *,
    dry_run: bool = False,
) -> object:
    """Normalize loudness with ffmpeg's loudnorm filter."""
    from twat_audio.operations import normalize_audio  # noqa: PLC0415

    return normalize_audio(input_path, output_path, target_i=target_i, dry_run=dry_run)


def _silence_trim(
    input_path: str,
    output_path: str,
    start: float = 0.0,
    duration: float | None = None,
    *,
    dry_run: bool = False,
) -> object:
    """Trim an audio segment."""
    from twat_audio.operations import trim_audio  # noqa: PLC0415

    return trim_audio(input_path, output_path, start=start, duration=duration, dry_run=dry_run)


def _resample(
    input_path: str,
    output_path: str,
    samplerate: float = 22050.0,
) -> object:
    """Resample an audio file with Pedalboard."""
    from twat_audio.twat_audio import AudioProcessConfig, resample_audio  # noqa: PLC0415

    return resample_audio(AudioProcessConfig(input_path, output_path, samplerate))


def _effect(
    input_path: str,
    output_path: str,
    audio_filter: str,
    *,
    dry_run: bool = False,
) -> object:
    """Apply a caller-provided ffmpeg audio filter string."""
    from twat_audio.operations import simple_effect  # noqa: PLC0415

    return simple_effect(input_path, output_path, audio_filter, dry_run=dry_run)


def _replace(
    video: str,
    audio: str,
    output_path: str,
    *,
    dry_run: bool = False,
) -> object:
    """Replace a media file's audio stream with a separate audio file."""
    from twat_audio.operations import replace_audio  # noqa: PLC0415

    return replace_audio(video, audio, output_path, dry_run=dry_run)


COMMANDS: dict[str, object] = {
    "version": _version,
    "info": _info,
    "transcode": _transcode,
    "normalize": _normalize,
    "silence-trim": _silence_trim,
    "resample": _resample,
    "effect": _effect,
    "replace": _replace,
}


def main() -> None:
    """Fire CLI dispatcher for twat-audio."""
    fire.Fire(COMMANDS, name="twat-audio")


def cmd_version() -> None:
    """Print the installed twat-audio version."""
    fire.Fire(_version, name="twat-audio-version")


def cmd_info() -> None:
    """Return audio/media metadata via ffprobe."""
    fire.Fire(_info, name="twat-audio-info")


def cmd_transcode() -> None:
    """Extract/transcode audio from a media file."""
    fire.Fire(_transcode, name="twat-audio-transcode")


def cmd_normalize() -> None:
    """Normalize loudness with ffmpeg's loudnorm filter."""
    fire.Fire(_normalize, name="twat-audio-normalize")


def cmd_silence_trim() -> None:
    """Trim an audio segment."""
    fire.Fire(_silence_trim, name="twat-audio-silence-trim")


def cmd_resample() -> None:
    """Resample an audio file with Pedalboard."""
    fire.Fire(_resample, name="twat-audio-resample")


def cmd_effect() -> None:
    """Apply a caller-provided ffmpeg audio filter string."""
    fire.Fire(_effect, name="twat-audio-effect")


def cmd_replace() -> None:
    """Replace a media file's audio stream with a separate audio file."""
    fire.Fire(_replace, name="twat-audio-replace")


if __name__ == "__main__":
    main()
