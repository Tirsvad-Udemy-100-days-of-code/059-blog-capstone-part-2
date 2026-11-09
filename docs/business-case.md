# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Claude (AI) for S01 | AI as stand-in for S01 | Initial version; reviewed in RC-001, Mode: autonomous, not independent | [1f11ab0] |

---

## Executive Summary

The project upgrades the simple blog built on Day 57 of the Udemy course
"100 Days of Code: The Complete Python Pro Bootcamp" into a Bootstrap-based,
mobile-responsive blog on the Start Bootstrap "Clean Blog" template (Day 59,
"Blog capstone part 2"). A Flask application serves a multi-page site (home,
about, contact, post) whose header and footer are shared Jinja templates and
whose posts are fetched from a JSON API. The result is a readable, runnable
repository that other course participants can compare with their own solutions,
documented in a README and in a trilingual wiki (English, Danish, Bahasa
Malaysia) with one screenshot per lecture step.

## Methodological and Standards Foundation

- Planning-first workflow of the SQA and QC framework mounted at `framework/`
  (Business Case, Stakeholder Analysis, Project Plan, milestones, tasks as
  issues, then code), with one reviewed pull request per milestone.
- ISO/IEC 25010:2023 characteristics tag every QC criterion; ISO/IEC 25002 and
  25019 frame the quality model used by the reviews.
- Python code follows the project's Python coding conventions and Clean
  Architecture ("Folder structure" of the `clean-architecture` skill), tested
  with pytest.
- Larman, *Applying UML and Patterns*, is the reference for the design
  artifacts; this project is small enough that none are needed beyond the
  milestones.

## Problem Statement

1. The Day 57 blog has plain CSS, no animation and no mobile layout.
2. Course participants who finish Day 59 lack one clean, runnable reference
   against which to compare their solution; the assignment's function names and
   steps are scattered over gists and videos.
3. A repository without a description, topics and instructions is hard for
   visitors to judge or to run.

## Business Opportunity

A single repository that follows the seven lecture steps in order, with a
screenshot and an explanation for each, lets S02 compare and learn quickly and
lets S03 judge the work at a glance. It also practises the full planning, review
and delivery workflow on a small, bounded project.

## Objectives

| # | Objective |
| --- | --- |
| O1 | Deliver the Day 59 blog (Steps 1 to 7) as a Flask application with Bootstrap styling, shared header and footer, About and Contact pages, posts from an API and individual post pages. |
| O2 | Keep the code readable and runnable with the assignment's function names (`home`, `about`, `contact`, `show_post`, `get_posts`), a single runtime dependency (Flask) and tested with pytest. |
| O3 | Provide complete project hygiene: `pyproject.toml`, local `.venv` instructions, Python `.gitignore`, `constants.py`, Doxygen comments and a `Doxyfile`. |
| O4 | Document the work: README from the framework template and a wiki in English, Danish and Bahasa Malaysia, each with a screenshot per lecture step and an explanation of what that step teaches. |
| O5 | Publish the repository with a description and topics on the git host. |

## Scope

### In Scope

- Flask application under `src/` with the Clean Blog template files in
  `templates/` and `static/`, `header.html` and `footer.html` included with
  Jinja `{% include %}`.
- Routes for home, about, contact and individual posts; `url_for` for static
  files and links.
- Fetching posts from a configurable JSON endpoint (default: the course's
  npoint document) with a bundled local copy for offline use and tests.
- pytest unit and integration tests under `tests/`.
- Project configuration: `pyproject.toml`, `.gitignore`, `Doxyfile`,
  `constants.py`, local `.venv` instructions.
- README and the three-language wiki with screenshots for Steps 1 to 7.
- Repository description and topics on the git host.

### Out of Scope

- Contact form submission, e-mail sending, comments, authentication and a
  database (not part of Day 59).
- Deployment to a hosting service.
- Editing the framework mounted at `framework/`.
- Creating the user's own npoint account or bin (the public course document is
  used; the endpoint is configurable).

## Expected Benefits

### Tangible Benefits

- A working, tested blog repository that runs with three commands.
- A README and a trilingual wiki that S02 can follow without the videos.
- A repository page with description and topics that S03 can find and judge.

### Intangible Benefits

- Practice in Flask templating, Bootstrap reuse and API consumption.
- A worked example of the planning-first, review-gated workflow.
- Reusable structure for the next days of the course.

## Strategic Alignment

The project supports S01's goal of completing the 100 Days of Code course with
repositories of consistent quality, and the sharing goal of S02 and S03:
readable code, clear documentation and no needless dependencies.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| SC1 | Every lecture step (1 to 7) is reproduced | 7 of 7 steps implemented and shown in a screenshot | Count of steps with code and screenshot in the README |
| SC2 | Automated tests pass | 100 % pass; at least 90 % line coverage of `src/` | `pytest` exit code 0 and the coverage report |
| SC3 | Runtime dependencies | Exactly 1 (Flask) | `dependencies` list in `pyproject.toml` |
| SC4 | Wiki languages | 3 languages (en, da, ms) with the same page set | File list of `docs/wiki/` |
| SC5 | Screenshots | At least 1 per lecture step in README and in each wiki language | Image links per page |
| SC6 | Run instructions work from a clean clone | Site answers HTTP 200 on `/` within 5 steps of the README | Manual run in a fresh `.venv` |
| SC7 | Repository metadata | Description set and at least 5 topics | Git host API response |
| SC8 | Doxygen documentation | `doxygen Doxyfile` finishes with 0 warnings | Doxygen log |
| SC9 | Review gates | Every milestone has an `RC-*` with `Go` before its pull request | `docs/sqa/reviews/` |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The npoint endpoint is offline or changes | Home and post pages empty; tests flaky | Bundle a local copy of the posts, fall back to it on error and test with it, never with the network |
| The Clean Blog template download changes or is unavailable | Step 1 blocked | Fetch the tagged release from the template's repository and keep the needed files in `src/` under its MIT licence |
| Screenshots taken on the host desktop disturb the user | Violates `framework/process/gui-testing.md` | Capture them with a headless browser in a Docker container, written to a shared folder |
| Danish or Bahasa Malaysia text contains errors | Reduced value for S02 | English is authoritative; translations follow it page by page and are flagged for native review |
| Language criteria need a person who reads the language | A stand-in review stays `Go-with-conditions` | The Product Owner confirms those criteria in chat when accepting the plan |
| A token leaks into the repository | Security defect | Tokens stay in the untracked `.env`; it is in `.gitignore` and never read by project code |

## Assumptions

- S01 is Product Owner, developer and reviewer; S02 and S03 are not contacted.
- The PO language is English and the PO domain is IT.
- The remote `git.tirsystem.com` accepts the token in `.env` for repository
  settings, pull requests and milestones.
- Docker is available for headless screenshots.
- Python 3.13 or newer is installed.

## Constraints

- Python 3.13 or newer, a local `.venv`, pytest, `pyproject.toml`, `constants.py`
  for constants and Doxygen comments in the source.
- Folder structure `src/`, `tests/` and `docs/`.
- One branch and one pull request per milestone; no merge without green checks.
- The work ends by 2026-11-16.
- `.env` is for the maintainer only: it is not imported, tested or committed.
- Runtime dependencies are avoided unless needed (only Flask is needed).

## Cost–Benefit Assessment

The assessment is qualitative: the project is a learning exercise with no
revenue and no budget beyond the maintainer's time, so a monetary return on
investment would be invented.

| Costs | Benefits |
| --- | --- |
| About one week of S01's part-time effort plus AI assistance | A complete, documented Day 59 solution for S02 and S03 |
| Maintenance of three wiki languages | Wider reach, including Danish and Malaysian readers |
| Docker for screenshots | No disturbance of the user's desktop |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Finishes the lesson with a repository of consistent quality |
| S02 | Runnable, readable code and run instructions to compare with their own |
| S03 | Clear repository description, topics and README, and no extra dependencies |

## Recommendation

Proceed — the scope is small and well defined, the risks are mitigated and the
repository gives S01, S02 and S03 a reusable result.

---

[SA-001]: ./stakeholder-analysis.md
[1f11ab0]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/commit/1f11ab05fc7d3af6f6694514dc6b103f9b7d557f
