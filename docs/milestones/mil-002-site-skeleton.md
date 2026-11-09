# Clean Blog site skeleton (Steps 1-5)

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Claude (AI) for S01 | AI as stand-in for S01 | Initial version; reviewed in RC-005, Mode: autonomous, not independent | [1f11ab0] |

---

## Purpose

Decide whether the Bootstrap site skeleton (lecture Steps 1 to 5) works: template laid out, home page served, assets fixed, header and footer shared, About and Contact pages reachable.

## Deliverable

A pull request on branch `mil-002-site-skeleton` with the Clean Blog template in `templates/` and `static/`, routes `home`, `about` and `contact`, shared `header.html` and `footer.html`, tests, and one screenshot for each of Steps 1 to 5 in `docs/screenshots/`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `GET /`, `GET /about` and `GET /contact` return HTTP 200 in the pytest client | Met | Not met |
| 2 | No template contains a hard-coded `static/` path or an `href` to a `.html` page (all use `url_for`) | Met | Not met |
| 3 | `index.html`, `about.html` and `contact.html` include `header.html` and `footer.html` with Jinja `include` and contain no duplicated `<head>` or `<footer>` | Met | Not met |
| 4 | The Clean Blog licence notice (MIT) is kept with the copied files | Met | Not met |
| 5 | `docs/screenshots/` holds one image for each of Steps 1 to 5, created in a Docker container | Met | Not met |
| 6 | `pytest` exits with code 0 and `doxygen Doxyfile` has 0 warnings | Met | Not met |
| 7 | `RC-*` for this milestone and for the code (`qc-programming-python`) have the verdict `Go` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Tooling, layout and constants must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] O1 | Steps 1 to 5 of the lecture |
| [BC-001] SC1, SC2, SC5 | Steps shown, tests, screenshots |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in in autonomous mode) |

## Target Date

2026-11-12 — inside the Business Case constraint (end by 2026-11-16).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Step 1: add Clean Blog template and lay out folders | Download the Clean Blog template release into a new empty folder outside the repository, treat it as untrusted data, copy the HTML files to `templates/` and the `css`, `js` and `assets` folders to `static/`, keep the licence notice and add empty `header.html`, `footer.html` and the application entry point. Screenshot: the resulting file tree. | No | BC-001 O1 |
| 2 | Step 2: render the home page | Create the Flask application and the `home` route that renders `index.html` at `http://localhost:5000`. The page is still unstyled. Screenshot: the unstyled home page. | No | BC-001 O1 |
| 3 | Step 3: fix header, footer and background image | Replace relative asset paths with `url_for('static', filename=...)` so Bootstrap CSS, the navbar script and `home-bg.jpg` load. Screenshot: the styled home page. | No | BC-001 O1 |
| 4 | Step 4: share header and footer with Jinja include | Move `<head>` and navigation into `header.html` and `<footer>` and scripts into `footer.html`, and include them from `index.html` so the site renders identically. Screenshot: the home page rendered from the includes. | No | BC-001 O1 |
| 5 | Step 5: About and Contact pages | Remove the Sample Post link, point the navigation to `about` and `contact` with `url_for`, add the routes, use the shared header and footer and fix the header images with `url_for`. Screenshots: About and Contact pages. | No | BC-001 O1 |
| 6 | Write route and template tests | Add pytest tests with the Flask test client for the three routes, the navigation links and the absence of hard-coded static paths. | No | BC-001 SC2 |
| 7 | Capture Step 1-5 screenshots in Docker | Write `tests/e2e/capture_screenshots.py` and a Dockerfile that start the app and a headless browser inside a Docker container (never on the host desktop, as `framework/process/gui-testing.md` requires) and write PNG files to a folder shared with the host. | No | BC-001 SC5 |

---

[BC-001]: ../business-case.md
[1f11ab0]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/commit/1f11ab05fc7d3af6f6694514dc6b103f9b7d557f
