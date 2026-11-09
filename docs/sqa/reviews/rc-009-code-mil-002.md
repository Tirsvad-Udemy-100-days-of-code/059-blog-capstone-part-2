# Code review of MIL-002

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; Mode: autonomous, not independent | [330c9a8] |

---

## Artifact Under Review

- Instance reviewed: source code and tests delivered for MIL-002 (Flask app, templates, tests and screenshot tooling)
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | ruff (pycodestyle, pyflakes, isort, bugbear, pyupgrade, annotations) reports no naming finding. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (posts, repository, show_post); the assignment's function names are kept. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format` applied and `ruff check` reports no finding; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `ANN` rules of ruff are enabled and pass; `-> None` used. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; failures are caught as specific exceptions and the cause is kept or handled by the fallback. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | ruff bugbear (B006, A) reports nothing. |
| 7 | Files, locks and connections are managed with context managers | Pass | Network and file access use `with` blocks. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public module, class and function has a Doxygen docstring; `doxygen Doxyfile` has 0 warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No print calls in src/; no secrets handled. `.env` is not referenced by src/ or tests/. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists; the milestone's Tasks table is the design (route and template rows of MIL-002). |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 29 tests with the Flask test client; no network; order independent. The Docker screenshot script is excluded from pytest by design (e2e, runs only in a container). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `mypy --strict src` reports no issues. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Flask is the only runtime dependency; pytest, pytest-cov, ruff and mypy are development tools. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Constants are defined once in `blog/constants.py`; the posts format is defined once in the domain. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports nothing from the other layers; application imports domain; infrastructure and presentation import inward only. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Use cases receive the repository protocol; the adapter is chosen in the composition root `create_app`. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Layers `domain`, `application`, `infrastructure`, `presentation` under `src/blog`; `unit`, `integration`, `e2e` under `tests/` as needed. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All new file names are English, snake_case or well-known names. |

## Overall Verdict

Go — every Mandatory criterion passes. Checks run: `ruff check`, `ruff format --check`, `mypy --strict src`, `pytest` (97% line coverage) and `doxygen Doxyfile` (0 warnings). Mode: autonomous, not independent.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-16 |

---

[MIL-002]: ../../milestones/mil-002-site-skeleton.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[330c9a8]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/commit/330c9a8098170bc4c6f8a31cb5544bc4479d3462
