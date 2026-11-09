# Project setup and tooling

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Claude (AI) for S01 | AI as stand-in for S01 | Initial version; reviewed in RC-004, Mode: autonomous, not independent | [1f11ab0] |

---

## Purpose

Decide whether the project foundation is ready for feature work: configuration, tooling, folder layout, repository metadata and the first README exist and run on a clean clone.

## Deliverable

A pull request on branch `mil-001-project-setup` that adds `pyproject.toml`, `.gitignore`, `Doxyfile`, `constants.py`, the `src/` and `tests/` skeleton, a passing smoke test, the README from the framework template with `.venv` instructions, and the repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` declares `requires-python >=3.13`, one runtime dependency (Flask) and pytest as a development dependency | Met | Not met |
| 2 | `python -m venv .venv`, `python -m pip install --upgrade pip` and `pip install -e .[dev]` succeed as the README describes | Met | Not met |
| 3 | `pytest` exits with code 0 | Met | Not met |
| 4 | `doxygen Doxyfile` finishes with 0 warnings | Met | Not met |
| 5 | `.gitignore` ignores `.venv/`, `__pycache__/`, `.env` and Doxygen output | Met | Not met |
| 6 | `check-readme.sh` reports no error for `README.md` | Met | Not met |
| 7 | The git host shows a non-empty description and at least 5 topics | Met | Not met |
| 8 | `.env` is neither tracked nor referenced by any file under `src/` or `tests/` | Met | Not met |
| 9 | `RC-*` for this milestone has the verdict `Go` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [PP-001] plan accepted | The plan-first gate needs an accepted plan before code |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] O3, O5 | Project hygiene and repository metadata |
| [BC-001] SC2, SC3, SC7, SC8 | Tests, dependency count, metadata and Doxygen |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in in autonomous mode) |

## Target Date

2026-11-10 — inside the Business Case constraint (end by 2026-11-16).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml | Configure the project in `pyproject.toml`: name, version, `requires-python >=3.13`, Flask as the only runtime dependency, pytest as a `dev` extra, pytest settings and the `src` layout. Needed so S02 can install and run the project with standard tools. | No | BC-001 O3 |
| 2 | Add Python .gitignore | Add a Python `.gitignore` that also covers `.venv/`, `.env`, caches, coverage and Doxygen output so secrets and build files never reach the repository. | No | BC-001 O3 |
| 3 | Create src and tests skeleton with constants.py | Create the Clean Architecture folders under `src/` (domain, application, infrastructure, presentation), a `constants.py` that holds all constants (endpoint URL, host, port, titles), and an empty `tests/` package with a smoke test that imports the package. | No | BC-001 O2, O3 |
| 4 | Add Doxyfile and Doxygen comment style | Add a `Doxyfile` for the Python sources and write the Doxygen comment convention (`##` and `@brief`, `@param`, `@return`) used in every module so `doxygen Doxyfile` runs with 0 warnings. | No | BC-001 SC8 |
| 5 | Write README with venv and test instructions | Create `README.md` from the framework template with how to create and use a local `.venv`, run `python -m pip install --upgrade pip`, install, run the site, run pytest and generate Doxygen. Screenshots are added in MIL-004. | No | BC-001 O4 |
| 6 | Set repository description, topics and wiki flag | Use the Gitea API with the token from `.env` (read by hand in the shell, never imported by the project) to set the repository description and topics and to make sure the wiki is enabled. Record the values in the pull request. | No | BC-001 O5 |

---

[BC-001]: ../business-case.md
[1f11ab0]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/commit/1f11ab05fc7d3af6f6694514dc6b103f9b7d557f
