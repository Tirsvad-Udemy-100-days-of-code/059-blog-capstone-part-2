# Dynamic posts from the API (Steps 6-7)

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Claude (AI) for S01 | AI as stand-in for S01 | Initial version; reviewed in RC-006, Mode: autonomous, not independent | pending |

---

## Purpose

Decide whether the blog renders its posts from the JSON API and shows each post on its own page (lecture Steps 6 and 7).

## Deliverable

A pull request on branch `mil-003-dynamic-posts` with `get_posts`, a Jinja loop on the home page, the `show_post` route and `post.html`, a bundled local copy of the sample posts, tests that need no network and screenshots for Steps 6 and 7.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `get_posts` returns the posts from the endpoint in `constants.py` and, when the request fails, from the bundled copy, verified by a test with a fake client | Met | Not met |
| 2 | The home page lists each post with title, subtitle, author and date from the data | Met | Not met |
| 3 | `GET /post/<id>` returns HTTP 200 with title, subtitle, image, date, author and body, and HTTP 404 for an unknown id | Met | Not met |
| 4 | No test opens a network connection | Met | Not met |
| 5 | Runtime dependencies in `pyproject.toml` are still exactly one (Flask); the API is read with the standard library | Met | Not met |
| 6 | `docs/screenshots/` holds one image each for Step 6 and Step 7 | Met | Not met |
| 7 | `pytest` exits with code 0 with at least 90 % line coverage of `src/`, and `doxygen Doxyfile` has 0 warnings | Met | Not met |
| 8 | `RC-*` for this milestone and for the code have the verdict `Go` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | Pages, header and footer must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] O1, O2 | Steps 6 and 7 with the assignment's function names |
| [BC-001] SC1, SC2, SC3, SC5 | Steps shown, tests, dependency count, screenshots |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in in autonomous mode) |

## Target Date

2026-11-14 — inside the Business Case constraint (end by 2026-11-16).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Step 6: fetch posts from the API | Implement `get_posts` behind a repository port in the application layer and an infrastructure adapter that reads the JSON endpoint from `constants.py` with the standard library `urllib` and falls back to a bundled copy of the course's sample data. Needed so tests and offline runs never depend on npoint. | No | BC-001 O1, O2 |
| 2 | Step 6: render posts on the home page | Pass the posts to `index.html` and use a Jinja `for` loop to show title, subtitle, author and date of each post with a link to its page, using dot notation on the data. | No | BC-001 O1 |
| 3 | Step 7: add show_post route and post.html | Add the `show_post` route for `/post/<int:index>`, find the post by id, return 404 when it does not exist, and render `post.html` with full-screen title, subtitle, image, date, author and body. | No | BC-001 O1 |
| 4 | Write repository, route and 404 tests | Add pytest tests with a fake client for `get_posts` success, failure and fallback, for the home loop and for `show_post` including the 404 case; measure coverage. | No | BC-001 SC2 |
| 5 | Capture Step 6-7 screenshots in Docker | Extend the Docker based screenshot script with the home page showing posts and an individual post page (the cactus post), written to `docs/screenshots/`. | No | BC-001 SC5 |

---

[BC-001]: ../business-case.md
