# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- Created `PLAN.md` with steps for MVP streamlining.
- Created `TODO.md` with initial task list.
- Created `CHANGELOG.md` (this file).

### Removed
- Deleted `.cursor/rules/0project.mdc` as its content conflicted with the project's scope (twat-audio vs. twat-fs).

### Fixed
- Ensured project identity is consistently `twat-audio` in `README.md` and `pyproject.toml`.
- Corrected `mypy` errors in `tests/test_twat_audio.py` by adding return type hints.
- Resolved `pytest` `AttributeError` for `__version__` in `tests/test_twat_audio.py` by using `importlib.metadata.version` and ensuring top-level imports.
- Updated `cleanup.py` to no longer require the deleted `.cursor/rules/0project.mdc` file.
- Modified `cleanup.py` to use `python -m hatch run ...` for executing linting, formatting, type checks, and tests, centralizing quality checks via Hatch.
- Temporarily commented out the `repomix()` call in `cleanup.py` to prevent `REPO_CONTENT.txt` generation.

### Removed
- Deleted `VERSION.txt` as it was found to be unused and redundant with `hatch-vcs` versioning.
- Deleted `package.toml` as it was found to be unused by any current project scripts or build processes and likely a remnant of a scaffolding tool.

### Changed
- Updated `README.md` with a project title, specific description for `twat-audio`, and more detailed development environment/testing instructions.
- Defined core MVP audio processing task: Load, resample, and export audio using the `pedalboard` library. Plan updated to reflect this.

### Added
- `pedalboard` dependency to `pyproject.toml`.
- Core audio resampling logic to `src/twat_audio/twat_audio.py` using `pedalboard`, including:
    - `AudioProcessConfig` dataclass for configuration.
    - `resample_audio` function for loading, resampling, and saving audio.
    - Basic error handling and logging.
    - Example usage in `main()` with dummy audio file creation.
- Unit tests for the `resample_audio` function in `tests/test_twat_audio.py`, covering:
    - Successful resampling.
    - Handling of same input/output sample rates.
    - File not found errors.
    - Basic stereo file processing.

### Changed
- Simplified `cleanup.py` by removing:
    - `prefix()` function (as `.cursor/rules/0project.mdc` was deleted).
    - `update()` and `push()` commands and their associated methods (git operations to be manual).
    - `repomix()` function (functionality already commented out and not required for MVP).
- Updated `cleanup.py` usage information to reflect removed commands.
