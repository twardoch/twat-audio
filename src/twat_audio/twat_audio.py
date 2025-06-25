#!/usr/bin/env python3
"""twat_audio:

Created by Adam Twardoch
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import Any
from pathlib import Path

from pedalboard import Pedalboard, Resample
from pedalboard.io import AudioFile


__version__ = "0.1.0" # This will be overwritten by hatch-vcs

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@dataclass
class AudioProcessConfig:
    """Configuration settings for audio processing."""
    input_file: str | Path
    output_file: str | Path
    target_samplerate: float = 22050.0
    # Example of how other pedalboard effects could be configured:
    # effects: list[Any] = field(default_factory=list)


def resample_audio(
    config: AudioProcessConfig, *, debug: bool = False
) -> dict[str, Any]:
    """
    Loads an audio file, resamples it, and saves it to the output path.

    Args:
        config: Configuration for the audio processing.
        debug: Enable debug mode for more verbose logging.

    Returns:
        A dictionary containing information about the operation.

    Raises:
        FileNotFoundError: If the input audio file does not exist.
        Exception: For other processing errors.
    """
    if debug:
        logger.setLevel(logging.DEBUG)
    logger.debug("Starting audio resampling process with config: %s", config)

    input_path = Path(config.input_file)
    output_path = Path(config.output_file)

    if not input_path.exists():
        msg = f"Input audio file not found: {input_path}"
        logger.error(msg)
        raise FileNotFoundError(msg)

    try:
        logger.info("Loading audio from: %s", input_path)
        with AudioFile(str(input_path)) as af:
            original_samplerate = af.samplerate
            num_channels = af.num_channels
            duration_seconds = af.duration
            logger.debug(
                "Original audio details: Samplerate=%.2f Hz, Channels=%d, Duration=%.2f s",
                original_samplerate,
                num_channels,
                duration_seconds,
            )
            audio_data = af.read(af.frames)

        if original_samplerate == config.target_samplerate:
            logger.info(
                "Input samplerate (%.2f Hz) matches target. No resampling needed.",
                original_samplerate,
            )
            resampled_audio = audio_data
        else:
            logger.info(
                "Resampling audio from %.2f Hz to %.2f Hz",
                original_samplerate,
                config.target_samplerate,
            )
            # Pedalboard's Resample effect processes audio in a Pedalboard chain
            board = Pedalboard([Resample(target_sample_rate=config.target_samplerate)])
            resampled_audio = board(audio_data, original_samplerate)
            logger.debug("Resampling completed.")

        output_path.parent.mkdir(parents=True, exist_ok=True)
        logger.info("Saving processed audio to: %s", output_path)
        with AudioFile(str(output_path), "w", config.target_samplerate, resampled_audio.shape[0]) as of:
            of.write(resampled_audio)
        logger.info("Audio successfully saved.")

        result = {
            "input_file": str(input_path),
            "output_file": str(output_path),
            "original_samplerate": original_samplerate,
            "target_samplerate": config.target_samplerate,
            "num_channels": num_channels,
            "duration_seconds": duration_seconds,
            "status": "success",
        }
        return result

    except Exception as e:
        logger.exception("Error during audio processing for file %s: %s", input_path, e)
        raise # Re-raise the exception after logging


def main() -> None:
    """Main entry point for demonstrating twat_audio functionality."""
    logger.info("twat-audio MVP demo started.")
    # Create a dummy WAV file for testing if it doesn't exist
    # Note: For real CLI, argument parsing (e.g., argparse) would be used.
    sample_dir = Path("sample_audio")
    sample_dir.mkdir(exist_ok=True)
    dummy_input_file = sample_dir / "input.wav"
    dummy_output_file = sample_dir / "output_resampled.wav"

    if not dummy_input_file.exists():
        logger.info("Creating a dummy input WAV file: %s", dummy_input_file)
        try:
            import numpy as np # Local import for dummy file creation
            samplerate = 44100
            duration = 1 # second
            frequency = 440 # Hz (A4 note)
            t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
            dummy_signal = 0.5 * np.sin(2 * np.pi * frequency * t)
            # Make it stereo
            dummy_stereo_signal = np.vstack([dummy_signal, dummy_signal]).T

            with AudioFile(str(dummy_input_file), "w", samplerate, dummy_stereo_signal.shape[0]) as f:
                 f.write(dummy_stereo_signal)
            logger.info("Dummy input file created successfully.")
        except Exception as e:
            logger.error("Could not create dummy input file: %s. Please provide a valid WAV file.", e)
            return


    # Example usage of the resampling function
    try:
        process_config = AudioProcessConfig(
            input_file=dummy_input_file,
            output_file=dummy_output_file,
            target_samplerate=16000.0,
        )
        result = resample_audio(config=process_config, debug=True)
        logger.info("Resampling process completed: %s", result)

    except FileNotFoundError:
        logger.error("Demo failed: Input file not found. Please ensure %s exists or can be created.", dummy_input_file)
    except Exception as e:
        logger.exception("An error occurred during the demo: %s", str(e))
        raise


if __name__ == "__main__":
    main()
