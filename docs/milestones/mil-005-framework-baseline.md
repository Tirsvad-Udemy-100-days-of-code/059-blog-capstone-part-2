# MIL-005 Framework baseline

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001], [PP-001], [MIL-004] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; accepted with the Go verdict of the review record (autonomous, not independent) | [8dc3193] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added task 6 (a behaviour-neutral source change that clears the blocking finding of the OpenGrep check) and changed criterion 2 and the Deliverable to allow that one file; reviewed in autonomous mode, not independent | [faf4c22] |

---

## Purpose

This gate decides whether the project has the baseline of the framework: the adopted framework release, the README in the framework template with an appendix that lists only the documents of the repository, project URL metadata, the editor settings of the baseline, the environment template of the framework, a passing test suite, an updated plan and reviewed documents, merged to the default branch with a green build. The wiki in English, Danish and Bahasa Malaysia already has a sidebar in the framework's shape and the language line on the first line of each page; this gate checks it again against the current checklist and does not change a page. The work is delivered on the branch `mil-005-framework-baseline` and one pull request. It changes no behaviour of the program.

## Deliverable

A merged pull request that holds: the updated Business Case, Project Plan, Traceability Matrix and Artifact Registry, this milestone and the review records of the changed documents and of the wiki; the README without the private framework files in its appendix; `pyproject.toml` with the project URLs and the build requirement for a licence expression; `.editorconfig` and `.env.example` of the framework baseline; and the framework release adopted by the project. The tests (`tests/`), the screenshots and the wiki pages do not change; the program (`src/`) changes only in `src/blog/infrastructure/api_post_repository.py` (task 6: the bundled posts file is read with `pathlib` instead of `importlib.resources`).

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | BC-001, PP-001 and MIL-005 each have an `Accepted` Version History row and a review record, and the wiki has a review record | Verdict `Go` | Any missing or `No-Go` |
| 2 | `python -m pytest` runs (the tests stub the posts API and need no network) and `git diff origin/main --stat -- src tests docs/screenshots docs/wiki` lists only `src/blog/infrastructure/api_post_repository.py` (task 6) | Exit code 0 and only that file in the diff | Any failure or any other change |
| 3 | `docs/wiki/` has `_Sidebar.md` and the nine English pages (Home, Getting-Started and Step-1 to Step-7) in en, da and ms (27 pages), directly in the folder, each page starting with the language line, and the sidebar has the title, one list of the English pages and the Languages section last; the published wiki is the same as the folder | 27 pages, the sidebar and the same content on the host | A page or language missing, a subfolder, a sidebar of another shape or a difference on the host |
| 4 | `framework/scripts/check-readme.sh`, `framework/scripts/check-languages.sh` and `framework/scripts/check-editorconfig.sh` run | Exit code 0 | Any finding |
| 5 | `pyproject.toml` sets the licence as an SPDX expression with `license-files`, requires a setuptools release that reads it and sets the project URLs for the repository, the documentation and the issue tracker | All set | Any missing |
| 6 | `.env.example` is tracked and holds empty placeholders for the framework tokens; `.env` is not tracked | Present, no real value | Missing, a real value present or `.env` tracked |
| 7 | All CI checks of the pull request | Green | Red or pending |
| 8 | The pull request carries one `Closes #N` line per task of this milestone | Every issue is closed after the merge | An issue stays open |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] accepted | Documents and baselines the finished program, its tests, its README and its wiki |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives O1 to O5 | Criterion 2 (the behaviour is unchanged, its tests pass and the one source change is task 6) |
| Objective O6 | Criteria 1, 3, 4, 5, 6 and 8 (documents, wiki, README, metadata, environment template and issues) |
| Success criterion SC10 | Criteria 1, 2, 3, 4 and 7 |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, autonomous mode, not independent) |

## Target Date

2026-11-23: one week after the start, as the Business Case constraint for this milestone requires.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Adopt the framework release | Move the `framework/` submodule to the newest release, track `.gitmodules` (lowercase repository URL), install the skills and hooks, add the framework baseline `.editorconfig`, bring `.env.example` to the framework's template, so the project follows the same rules as the other projects of the portfolio. | No | BC-001 objective O6 |
| 2 | Update and review the planning documents | Add this milestone to the Business Case, Project Plan and Traceability Matrix, set the domain of the changed documents and of the registry to education, name the PlantUML server in the Artifact Registry and review each changed document against its QC checklist, so the plan-first gate is met. | No | BC-001 objective O6 |
| 3 | Check the wiki against the current checklist | Compare the pages and the sidebar with the wiki checklist of the adopted framework release, read the published wiki back from the host and add a review record for the wiki. No page changes. | No | BC-001 objectives O4 and O6 |
| 4 | Bring the README to the framework template | Keep the text of the README, describe the framework files in the overview, name the licence expression and give the appendix only the documents that are in the repository, so the README is complete and checkable. | No | BC-001 objectives O4 and O6 |
| 5 | Complete the package metadata | Add the repository, documentation and issue tracker URLs to `pyproject.toml`, replace the licence file reference by the SPDX expression with `license-files` and the author, and raise the build requirement to the setuptools release that reads a licence expression, so package tools can read them. | No | BC-001 objective O6 |
| 6 | Clear the blocking OpenGrep finding | Read the bundled posts file in `api_post_repository.py` with `pathlib` instead of `importlib.resources`, remove the import together with its `nosemgrep` marker and keep the behaviour and the tests as they are, so the shared OpenGrep check passes without any suppression. | No | BC-001 objective O6 |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-004]: ./mil-004-docs-wiki-screenshots.md
[8dc3193]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/commit/8dc3193b6ef18b8c03044408ae0fa5be595873a3
[faf4c22]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/commit/faf4c222a7f7eeda241ec05143b8d87ba5d2dcd6
