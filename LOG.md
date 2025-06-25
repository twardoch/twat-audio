---
this_file: LOG.md
---

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [v0.0.1] - 2025-02-15

Initial release of the twat-audio package.

### Added

- Basic project structure with modern Python packaging (PEP 621 compliance)
- Initial implementation of `twat_audio.py` with:
  - Configuration management using dataclasses
  - Basic logging setup
  - Type hints and runtime type checking
  - Process data function skeleton
- Comprehensive development setup:
  - Hatch for development workflow management
  - Pre-commit hooks for code quality
  - Ruff for linting and formatting
  - MyPy for type checking
  - Pytest for testing with coverage and benchmarking support
- GitHub Actions workflows for:
  - Build and test on multiple Python versions (3.10, 3.11, 3.12)
  - Code quality checks
  - Automated releases to PyPI
- Project documentation:
  - Basic README.md with installation and usage instructions
  - MIT License

## [Unreleased]

### MVP Streamlining and Core Feature Implementation
- **Project Focus & Cleanup:**
    - Clarified project scope as `twat-audio`, removing conflicting `twat-fs` references (e.g., deleted `.cursor/rules/0project.mdc`).
    - Removed unused and redundant files (`VERSION.txt`, `package.toml`).
    - Fixed initial errors reported by `cleanup.py status` (mypy, pytest version access).
- **Development Tooling:**
    - Simplified `cleanup.py`:
        - Aligned its quality checks to use `hatch` tasks (`lint:all`, `default:test-cov`).
        - Removed git auto-commit/push features and unused `repomix` call.
        - Streamlined available commands to `status`, `venv`, `install`.
- **Core Functionality (Resampling MVP):**
    - Added `pedalboard` as a core dependency.
    - Implemented audio resampling functionality in `src/twat_audio/twat_audio.py`:
        - Loads an audio file.
        - Resamples to a target sample rate using `pedalboard.Resample`.
        - Saves the processed audio.
    - Added `AudioProcessConfig` for managing processing parameters.
    - Included basic error handling and logging.
- **Testing:**
    - Added unit tests for the new resampling logic, covering various scenarios including successful resampling, same sample rate handling, and file errors.
- **Documentation:**
    - Created `PLAN.md` and `TODO.md` for tracking the streamlining effort.
    - Maintained a detailed `CHANGELOG.md` for this specific set of changes.
    - Performed an initial update of `README.md` to reflect project scope and MVP features.

[unreleased]: https://github.com/twardoch/twat-audio/compare/v0.0.1...HEAD
[v0.0.1]: https://github.com/twardoch/twat-audio/releases/tag/v0.0.1 
