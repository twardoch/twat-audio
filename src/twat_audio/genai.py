"""Thin optional adapters from twat-audio to twat-genai audio providers."""
# this_file: src/twat_audio/genai.py

from __future__ import annotations

from importlib import import_module
from pathlib import Path
from typing import Any


def generate_audio(prompt: str, *, output_dir: str | Path = "generated_audio", **kwargs: Any) -> Any:
    """Call a twat_genai audio provider without embedding provider clients here."""
    try:
        twat_genai = import_module("twat_genai")
    except ImportError as exc:
        msg = "twat_genai is required for AI audio generation. Install twat-genai and configure a provider."
        raise RuntimeError(msg) from exc
    generator = getattr(twat_genai, "generate_audio", None)
    if generator is None:
        msg = "Installed twat_genai does not expose an audio generation API yet."
        raise NotImplementedError(msg)
    return generator(prompt=prompt, output_dir=output_dir, **kwargs)
