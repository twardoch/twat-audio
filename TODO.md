# TODO for twat-audio MVP Streamlining

## Phase 1: Cleanup and Clarification
- [x] Project Definition Consistency: Ensure all project documentation and configuration (`README.md`, comments in `pyproject.toml`) consistently refer to `twat-audio`. (`.cursor/rules/0project.mdc` removed).
- [ ] Create `PLAN.md`.
- [x] Create `TODO.md` (this file).
- [x] Create `CHANGELOG.md`.
- [x] Fix `mypy` error in `tests/test_twat_audio.py` (add `-> None` to `test_version()`).
- [x] Fix `pytest` `AttributeError` for `__version__` in `tests/test_twat_audio.py` (use `importlib.metadata.version`).
- [x] Updated `cleanup.py` to no longer require `.cursor/rules/0project.mdc`.
- [x] Review `cleanup.py`: Modify `_run_checks` to use `python -m hatch run` commands.
- [x] Review `cleanup.py`: Temporarily comment out `repomix()` call.
- [x] Investigate usage of `VERSION.txt` (potential removal). (Done: Removed file)
- [x] Review `package.toml` for relevance to MVP (potential simplification/removal). (Done: Removed file)
- [x] Update `README.md` (Initial Pass): Remove placeholders, reflect `twat-audio` name. (Done)

## Phase 2: Core MVP Functionality
- [x] Define a specific, simple audio processing task for MVP. (Done: Load, resample, export with `pedalboard`)
- [x] Add `pedalboard` dependency to `pyproject.toml`.
- [x] Implement the core audio processing logic in `src/twat_audio/twat_audio.py` using `pedalboard`.
    - [x] Update `Config` dataclass (now `AudioProcessConfig`).
    - [x] Implement loading, resampling, saving in `resample_audio` function.
    - [x] Add basic error handling and logging.
- [x] Write unit tests for the new core audio logic.

## Phase 3: Finalizing MVP
- [x] Refine `cleanup.py` (Second Pass): Make final decisions on simplifying or removing parts. (Done: Removed prefix, update, push, repomix. Kept status, venv, install.)
- [x] Update `LOG.md` with all changes. (Done: Added summary of MVP streamlining)
- [x] Update `CHANGELOG.md` with all changes. (Done: Incremental updates finalized)
- [x] Finalize `README.md` with comprehensive MVP details. (Done)
- [x] Run all checks (`cleanup.py status` or equivalent `hatch` scripts) and ensure they pass. (Done)
- [x] Manually verify MVP functionality. (Done via `main()` in `twat_audio.py` and unit tests)
- [ ] Submit all changes.
