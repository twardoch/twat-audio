# Plan for Streamlining `twat-audio` to MVP

This document outlines the steps to streamline the `twat-audio` codebase, focusing on creating a performant, focused v1.0 (MVP).

1.  **Project Definition Consistency (Completed):**
    *   Removed `.cursor/rules/0project.mdc`.
    *   Ensured `README.md` and `pyproject.toml` consistently refer to `twat-audio`.

2.  **Create Initial Documentation and Tracking Files:**
    *   *Action:* Create `PLAN.md` (this file).
    *   *Action:* Create `TODO.md` with an initial list of tasks.
    *   *Action:* Create `CHANGELOG.md` for user-facing changes.
    *   *Goal:* Proper planning and change tracking.

3.  **Fix Immediate Errors (identified by `cleanup.py status`):**
    *   *Action:* Address `mypy` error in `tests/test_twat_audio.py`: `Function is missing a return type annotation`. Add `-> None` to `test_version()`.
    *   *Action:* Address `pytest` `AttributeError: module 'twat_audio' has no attribute '__version__'` in `tests/test_twat_audio.py`. Modify the test to use `importlib.metadata.version('twat-audio')`.
    *   *Goal:* A stable baseline with passing checks.

4.  **Review and Simplify `cleanup.py` (Initial Pass):**
    *   *Goal:* Reduce redundancy, simplify its role for MVP, and align with `hatch`.
    *   *Action:* Modify `cleanup.py`'s `_run_checks` method to primarily use `hatch run` commands (e.g., `hatch run lint:all`, `hatch run test-cov`) for linting, type-checking, and tests.
    *   *Action:* In `cleanup.py`, temporarily comment out the `repomix()` call within the `main()` function.
    *   *Action:* Ensure `cleanup.py status` remains functional for reporting, with underlying checks leveraging `hatch`.
    *   *Note:* Defer major removal of `cleanup.py` features until after core MVP functionality.

5.  **Evaluate `VERSION.txt`:**
    *   *Goal:* Determine if `VERSION.txt` is necessary.
    *   *Action:* Use `grep` to search for usages of "VERSION.txt". If none critical, plan for removal.

6.  **Review `package.toml`:**
    *   *Goal:* Ensure settings in `package.toml` are relevant for `twat-audio` MVP.
    *   *Action:* Verify impact of settings like `include_cli`, `use_pydantic`. Consider simplification/removal later if not core to MVP.

7.  **Update `README.md` (Initial Pass):**
    *   *Goal:* Clear, concise information about `twat-audio`.
    *   *Action:* Initial update to `README.md` to remove placeholder content and reflect `twat-audio` project name. Detailed rewrite after core functionality definition.

8.  **Define Core Audio Processing Task:**
    *   *Goal:* Specify a simple, concrete audio processing task for the MVP.
    *   *Action:* Request user input for a simple audio task (e.g., "Load WAV, apply gain, save"). Propose a default if no input.

9.  **Implement Core Logic in `src/twat_audio/twat_audio.py`:**
    *   *Goal:* Implement the defined audio processing task.
    *   *Actions:* Update `Config` dataclass if needed; implement logic in `process_data`; add dependencies (e.g., `soundfile`) to `pyproject.toml`; ensure basic error handling/logging.

10. **Write Unit Tests for Core Logic:**
    *   *Goal:* Ensure core functionality is well-tested.
    *   *Action:* Add new test cases in `tests/test_twat_audio.py` for the audio processing.

11. **Refine `cleanup.py` (Second Pass):**
    *   *Goal:* Make final decisions on `cleanup.py`'s role.
    *   *Action:* Based on MVP state, decide on further simplification or removal if `hatch` and manual git are sufficient.

12. **Update Documentation (`LOG.md`, `CHANGELOG.md`, `README.md`):**
    *   *Action:* Document all significant changes in `LOG.md` and `CHANGELOG.md`.
    *   *Action:* Finalize `README.md` with comprehensive MVP details.

13. **Run Full Checks and Ensure Stability:**
    *   *Action:* Execute all checks (e.g., `cleanup.py status` or `hatch` scripts) to confirm everything passes.
    *   *Action:* Manually verify MVP functionality.

14. **Submit Changes:**
    *   *Action:* Commit all changes with a clear message to a dedicated branch.
