"""Command-line interface for twat-audio."""
# this_file: src/twat_audio/__main__.py

from __future__ import annotations

import argparse

from twat_audio.operations import extract_audio, normalize_audio, replace_audio, simple_effect, trim_audio
from twat_audio.twat_audio import AudioProcessConfig, resample_audio


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="twat-audio", description="Audio processing helpers.")
    sub = parser.add_subparsers(dest="command")

    resample = sub.add_parser("resample", help="Resample an audio file with Pedalboard.")
    resample.add_argument("input")
    resample.add_argument("output")
    resample.add_argument("--samplerate", type=float, default=22050.0)

    normalize = sub.add_parser("normalize", help="Normalize loudness.")
    normalize.add_argument("input")
    normalize.add_argument("output")
    normalize.add_argument("--target-i", type=float, default=-16.0)
    normalize.add_argument("--dry-run", action="store_true")

    trim = sub.add_parser("trim", help="Trim an audio file.")
    trim.add_argument("input")
    trim.add_argument("output")
    trim.add_argument("--start", type=float, default=0.0)
    trim.add_argument("--duration", type=float)
    trim.add_argument("--dry-run", action="store_true")

    extract = sub.add_parser("extract", help="Extract audio from media.")
    extract.add_argument("input")
    extract.add_argument("output")
    extract.add_argument("--codec", default="pcm_s16le")
    extract.add_argument("--dry-run", action="store_true")

    replace = sub.add_parser("replace", help="Replace video audio.")
    replace.add_argument("video")
    replace.add_argument("audio")
    replace.add_argument("output")
    replace.add_argument("--dry-run", action="store_true")

    effect = sub.add_parser("effect", help="Apply an ffmpeg audio filter.")
    effect.add_argument("input")
    effect.add_argument("output")
    effect.add_argument("filter")
    effect.add_argument("--dry-run", action="store_true")
    return parser


def _print(result: object) -> None:
    command = getattr(result, "command", None)
    if command:
        print(" ".join(command))
    elif result is not None:
        print(result)


def main() -> None:
    """Run the twat-audio CLI."""
    parser = _parser()
    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        return
    if args.command == "resample":
        _print(resample_audio(AudioProcessConfig(args.input, args.output, args.samplerate)))
    elif args.command == "normalize":
        _print(normalize_audio(args.input, args.output, target_i=args.target_i, dry_run=args.dry_run))
    elif args.command == "trim":
        _print(trim_audio(args.input, args.output, start=args.start, duration=args.duration, dry_run=args.dry_run))
    elif args.command == "extract":
        _print(extract_audio(args.input, args.output, codec=args.codec, dry_run=args.dry_run))
    elif args.command == "replace":
        _print(replace_audio(args.video, args.audio, args.output, dry_run=args.dry_run))
    elif args.command == "effect":
        _print(simple_effect(args.input, args.output, args.filter, dry_run=args.dry_run))


if __name__ == "__main__":
    main()
