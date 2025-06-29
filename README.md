# twat-audio: Audio Processing for Python

**`twat-audio` is a versatile Python package for audio processing, designed as a powerful and easy-to-use component within the [TWAT (The Twardoch Workflow Automation Tools) collection](https://pypi.org/project/twat/).**

It aims to provide robust functionalities for common audio manipulation and analysis tasks, leveraging modern Python practices and high-quality underlying libraries. This initial version focuses on providing a solid foundation for audio resampling.

## Who is `twat-audio` for?

*   **Python Developers:** Seamlessly integrate audio processing capabilities into your Python applications.
*   **Audio Researchers & Engineers:** A practical tool for experimenting with and applying audio transformations.
*   **Hobbyists & Creatives:** Easily perform tasks like sample rate conversion for your audio projects.
*   **Users of the TWAT Ecosystem:** Enhance your workflow automation scripts with audio processing steps.

## Why use `twat-audio`?

*   **Simplicity:** Offers a straightforward API for complex audio tasks.
*   **Extensibility:** Built with future expansion in mind, aiming to cover a wider range of audio effects and analyses.
*   **Modern Tooling:** Utilizes `pedalboard` for efficient and high-quality audio operations, `Hatch` for project and environment management, `pytest` for rigorous testing, and `Ruff` for code quality.
*   **TWAT Integration:** Designed to work well within the broader TWAT ecosystem, facilitating comprehensive automation pipelines.

## Installation

### Standard Installation

To install the latest stable version of `twat-audio` from PyPI, run:

```bash
pip install twat-audio
```

### Development Setup

If you want to contribute to `twat-audio` or need the latest development version:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/twardoch/twat-audio.git
    cd twat-audio
    ```
2.  **Set up the development environment using Hatch:**
    Ensure you have [Hatch](https://hatch.pypa.io/latest/install/) installed (`pip install hatch`). Then, from the project root directory, run:
    ```bash
    hatch shell
    ```
    This command creates a virtual environment, installs all dependencies (including development tools), and activates it.

## Usage

`twat-audio` can be used programmatically as a Python library. While the current `main()` function in the source code serves as a demo, a dedicated CLI is a potential future enhancement.

### Programmatic Usage (Python Library)

The core functionality is exposed through functions that you can import into your Python scripts. The primary function available in the current version is `resample_audio`.

**Example: Resampling an Audio File**

```python
from pathlib import Path
from twat_audio import resample_audio, AudioProcessConfig

# 1. Define the processing configuration
# Ensure your input file exists. For this example, let's assume 'input.wav'.
# You might need to create a dummy 'input.wav' or use your own audio file.
input_audio_path = Path("input.wav") # Replace with your actual input file
output_audio_path = Path("output_resampled.wav")

# Create a dummy input file if it doesn't exist for this example to run
if not input_audio_path.exists():
    try:
        import numpy as np
        from pedalboard.io import AudioFile as PedalboardAudioFile
        print(f"Creating dummy file: {input_audio_path}")
        samplerate = 44100
        duration = 1
        frequency = 440
        t = np.linspace(0, duration, int(samplerate * duration), endpoint=False)
        dummy_signal = 0.5 * np.sin(2 * np.pi * frequency * t)
        with PedalboardAudioFile(str(input_audio_path), "w", samplerate, 1, len(dummy_signal)) as f:
            f.write(dummy_signal.reshape(1, -1))
    except Exception as e:
        print(f"Could not create dummy input file for example: {e}")
        # Exit or handle error as appropriate for your application

config = AudioProcessConfig(
    input_file=input_audio_path,
    output_file=output_audio_path,
    target_samplerate=22050.0  # Target sample rate in Hz (e.g., CD quality to half)
)

# 2. Process the audio
try:
    result = resample_audio(config=config, debug=True) # Enable debug for more verbose logs
    print("Audio resampling successful!")
    print(f"  Input File: {result['input_file']}")
    print(f"  Output File: {result['output_file']}")
    print(f"  Original Samplerate: {result['original_samplerate']:.0f} Hz")
    print(f"  Target Samplerate: {result['target_samplerate']:.0f} Hz")
    print(f"  Duration: {result['duration_seconds']:.2f}s")
    print(f"  Channels: {result['num_channels']}")
except FileNotFoundError:
    print(f"Error: Input file not found at {config.input_file}")
except Exception as e:
    print(f"An error occurred during processing: {e}")

```

**Configuration (`AudioProcessConfig`)**

The `AudioProcessConfig` dataclass is used to specify the parameters for audio processing tasks. For `resample_audio`, its fields are:

*   `input_file (str | Path)`: Path to the input audio file.
*   `output_file (str | Path)`: Path where the processed audio file will be saved.
*   `target_samplerate (float)`: The desired sample rate for the output audio in Hertz (e.g., `44100.0`, `22050.0`, `16000.0`). Defaults to `22050.0`.

### Command-Line Interface (CLI)

Currently, `twat-audio` does not offer a dedicated command-line interface for direct execution with arbitrary file paths via command-line arguments. The `main()` function within `src/twat_audio/twat_audio.py` serves as a demonstration that processes a pre-defined (or self-created dummy) audio file.

To run this demonstration:

1.  Ensure you have the package installed or are in an active Hatch development environment.
2.  Execute the main script:
    ```bash
    python src/twat_audio/twat_audio.py
    ```
    This will create `sample_audio/input.wav` (if it doesn't exist) and then resample it to `sample_audio/output_resampled.wav`.

A future enhancement could involve adding a more robust CLI using libraries like `argparse` or `typer`, allowing users to specify input/output files and parameters directly from the terminal.

## Technical Details

### How the Code Works

The primary logic resides in `src/twat_audio/twat_audio.py`.

*   **`AudioProcessConfig` Dataclass:**
    *   Defined using Python's `dataclasses`.
    *   Holds configuration parameters for audio processing tasks, such as input/output file paths and target sample rates. This makes it easy to extend with more parameters for future effects.

*   **`resample_audio(config: AudioProcessConfig, *, debug: bool = False) -> dict` Function:**
    *   **Inputs:**
        *   `config`: An `AudioProcessConfig` instance.
        *   `debug`: A boolean flag (keyword-only argument) to enable more verbose logging.
    *   **Core Logic:**
        1.  **File Handling:** Converts input and output file paths to `pathlib.Path` objects. Checks if the input file exists, raising `FileNotFoundError` if not.
        2.  **Audio Loading:** Uses `pedalboard.io.AudioFile` to open and read the input audio file. It extracts metadata like the original sample rate, number of channels, and duration.
        3.  **Resampling Decision:** Compares the original sample rate with `config.target_samplerate`.
            *   If they are the same, no resampling is performed; the original audio data is used directly.
            *   If different, it logs the intent to resample.
        4.  **Resampling with Pedalboard:**
            *   A `pedalboard.Pedalboard` instance is created, containing a `pedalboard.Resample` effect initialized with `target_sample_rate=config.target_samplerate`.
            *   The audio data is processed by calling the `board(audio_data, original_samplerate)` method.
        5.  **Output Directory & Saving:** Ensures the output directory exists (creates it if necessary). Uses `pedalboard.io.AudioFile` in write mode (`"w"`) to save the (potentially resampled) audio data to the specified output file, using the target sample rate and original number of channels.
    *   **Return Value:** Returns a dictionary containing details of the operation, such as file paths, sample rates, duration, and status.
    *   **Error Handling:** Includes a `try...except` block to catch and log general exceptions during processing, then re-raises them.

*   **`main()` Function:**
    *   Serves as an example and entry point for demonstrating the `resample_audio` functionality.
    *   It attempts to create a dummy stereo WAV file (`sample_audio/input.wav`) if one doesn't exist, using `numpy` for signal generation and `pedalboard.io.AudioFile` for saving. This is primarily for testing and demonstration.
    *   Then, it calls `resample_audio` with a predefined configuration.

### Key Libraries and Technologies

*   **[Pedalboard](https://github.com/spotify/pedalboard):** The core audio processing library. `twat-audio` uses it for:
    *   Reading and writing a wide variety of audio file formats.
    *   Applying audio effects, with `Resample` being the primary one used in the current version.
*   **[Hatch](https://hatch.pypa.io/latest/):** The build backend and project management tool. It handles:
    *   Dependency management.
    *   Virtual environment creation and management (`hatch shell`).
    *   Running scripts for testing, linting, formatting (`hatch run ...`).
    *   Building the package for distribution.
    *   Version management via `hatch-vcs` (dynamically sets version from Git tags).
*   **[pytest](https://docs.pytest.org/):** The testing framework used for writing and running unit tests (see `tests/` directory).
*   **[Ruff](https://github.com/astral-sh/ruff):** An extremely fast Python linter and formatter, used to enforce code style and quality. Configuration is in `pyproject.toml`.
*   **[mypy](http://mypy-lang.org/):** A static type checker for Python, helping to catch type errors before runtime. Configuration is in `pyproject.toml`.

## Coding and Contribution Rules

We welcome contributions to `twat-audio`! Please follow these guidelines to ensure a smooth development process.

### Coding Conventions

*   **Style and Quality:** The project uses `Ruff` for linting and formatting, and `mypy` for static type checking. Configurations are defined in `pyproject.toml`. Please ensure your contributions adhere to these standards.
*   **PEP 8:** Code should generally follow PEP 8 guidelines (largely enforced by Ruff).
*   **Type Hints:** All new functions and methods should include type hints.
*   **Imports:** Imports are managed by Ruff's `isort` integration. Relative imports within the `src/twat_audio` package are banned in favor of absolute imports (e.g., `from twat_audio.module import ...`).

### Development Workflow (using Hatch)

1.  **Set up Environment:**
    ```bash
    hatch shell
    ```
2.  **Running Tests:**
    *   Run all tests:
        ```bash
        hatch run test
        ```
    *   Run tests with coverage report:
        ```bash
        hatch run test-cov
        ```
3.  **Running Linters, Formatters, and Type Checkers:**
    *   Run all checks and apply automatic fixes:
        ```bash
        hatch run lint:all
        ```
    *   Specific checks (see `pyproject.toml` under `[tool.hatch.envs.lint.scripts]` for more):
        *   Style checking and formatting: `hatch run lint:style` or `hatch run lint:fmt`
        *   Type checking: `hatch run lint:typing`
        *   Apply more extensive fixes (including `pyupgrade`): `hatch run lint:fix`

    It's recommended to run `hatch run lint:all` before committing changes.

### Contributing

1.  **Fork the Repository:** Create your own fork of the `twat-audio` repository on GitHub.
2.  **Create a Feature Branch:** Create a new branch in your fork for your changes (e.g., `git checkout -b feature/my-new-feature`).
3.  **Make Changes:** Implement your feature or bug fix.
4.  **Add Tests:** Write unit tests for any new functionality or to cover bug fixes.
5.  **Ensure Checks Pass:** Run `hatch run lint:all` and `hatch run test-cov` to ensure all quality checks and tests pass.
6.  **Update Changelog:** If your changes are notable (new features, significant bug fixes, breaking changes), add an entry to `CHANGELOG.md` under the `[Unreleased]` section.
7.  **Commit and Push:** Commit your changes with a clear and descriptive commit message. Push the changes to your fork.
8.  **Submit a Pull Request:** Open a pull request from your feature branch to the `main` branch of the `twardoch/twat-audio` repository. Provide a clear description of your changes in the pull request.

### `AGENTS.md` / `CLAUDE.md`

If a file named `AGENTS.md` or `CLAUDE.md` exists in the root of the repository or relevant subdirectories, it may contain specific instructions or guidelines for AI agents working with this codebase. Contributors (human or AI) should consult these files if present.

## License

`twat-audio` is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
