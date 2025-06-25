# twat-audio

**twat-audio** is a Python package designed as an audio processing plugin for the TWAT ecosystem. It provides functionalities for various audio manipulation and analysis tasks.

This current version implements a core MVP (Minimum Viable Product) focused on audio resampling using the `pedalboard` library.

## Features

- **Audio Resampling:** Load an audio file, resample it to a specified target sample rate, and save the output.
- **Powered by Pedalboard:** Utilizes the `pedalboard` library for robust audio file I/O and effects processing.
- **Modern Python Development:**
    - Packaged with Hatch, compliant with PEP 621.
    - Type hints for improved code quality.
    - Comprehensive test suite using Pytest.
    - Linting and formatting with Ruff.
    - CI/CD pipeline via GitHub Actions for automated testing and releases.

## Installation

To install the latest stable version:
```bash
pip install twat-audio
```

For development, clone the repository and use Hatch:
```bash
git clone https://github.com/twardoch/twat-audio # Replace with your actual repo URL if different
cd twat-audio
hatch shell
# Further development commands below
```

## Usage Example: Resampling Audio

Here's how to use the `resample_audio` function:

```python
from pathlib import Path
from twat_audio import resample_audio, AudioProcessConfig

# Define configuration for resampling
config = AudioProcessConfig(
    input_file="path/to/your/input.wav",  # Replace with actual input file path
    output_file="path/to/your/output_resampled.wav", # Replace with desired output path
    target_samplerate=22050.0  # Target sample rate in Hz
)

try:
    # Process the audio
    result = resample_audio(config=config, debug=True)
    print(f"Audio resampling successful!")
    print(f"Input: {result['input_file']}")
    print(f"Output: {result['output_file']}")
    print(f"Original Samplerate: {result['original_samplerate']} Hz")
    print(f"Target Samplerate: {result['target_samplerate']} Hz")
    print(f"Duration: {result['duration_seconds']:.2f} s, Channels: {result['num_channels']}")
except FileNotFoundError:
    print(f"Error: Input file not found at {config.input_file}")
except Exception as e:
    print(f"An error occurred during processing: {e}")

```
The `main()` function in `src/twat_audio/twat_audio.py` also provides a runnable example that creates a dummy input file.

## Development

This project uses [Hatch](https://hatch.pypa.io/) for development workflow management.

### Setup Development Environment

1.  **Install Hatch** (if you haven't already):
    ```bash
    pip install hatch
    ```
2.  **Activate Development Environment**:
    Navigate to the project root and run:
    ```bash
    hatch shell
    ```
    This command creates a virtual environment (if it doesn't exist) and activates it. This will also install all dependencies, including `pedalboard`.

### Running Quality Checks & Tests

Once the Hatch shell is active:

-   **Run tests**:
    ```bash
    hatch run test
    ```
-   **Run tests with coverage report**:
    ```bash
    hatch run test-cov
    ```
-   **Run linting, formatting, and type checks (and apply fixes)**:
    ```bash
    hatch run lint:all
    ```
    (See `pyproject.toml` for definitions of `test`, `test-cov`, and `lint:all` scripts under `[tool.hatch.envs...]`)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
.
