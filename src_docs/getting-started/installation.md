# Installation

## Requirements

- Python 3.10 or later
- `ffmpeg` and `ffprobe` on `PATH` (for all operations except `resample`)

## Install from PyPI

```bash
pip install twat-audio
```

Or with [uv](https://github.com/astral-sh/uv):

```bash
uv add twat-audio
```

## Install ffmpeg

=== "macOS"
    ```bash
    brew install ffmpeg
    ```

=== "Ubuntu / Debian"
    ```bash
    sudo apt-get install ffmpeg
    ```

=== "Windows"
    Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add the `bin/` directory to `PATH`.

## Verify the Installation

```bash
python -c "import twat_audio; print(twat_audio.__version__)"
ffmpeg -version
ffprobe -version
```

## Optional: AI Audio Generation

To use `generate_audio()`, install a `twat-genai` provider:

```bash
pip install "twat-audio[all]"
```
