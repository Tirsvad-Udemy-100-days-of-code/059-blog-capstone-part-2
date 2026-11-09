# 🚀 Blog Capstone Part 2 (Day 59, upgraded blog)

A Flask blog on the Start Bootstrap "Clean Blog" template, built for Day 59 of
Udemy's "100 Days of Code: The Complete Python Pro Bootcamp". It is written for
fellow course participants who want to compare solutions and for visitors who
browse the repository for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The project upgrades the Day 57 blog with Bootstrap. It has a multi-page site
(home, about, contact, post), a header and footer shared with Jinja `include`,
and posts that come from a JSON API. The seven lecture steps are explained, each
with a screenshot, in the project wiki.

| Folder | Purpose |
| --- | --- |
| `src/blog/` | The application: domain, application, infrastructure and presentation layers; `constants.py` holds all constants |
| `tests/` | pytest tests (`unit/`, `integration/`, and `e2e/` for the Docker screenshot script) |
| `docs/` | Project documents (business case, plan, reviews), the wiki and the screenshots |

### The seven lecture steps

Each step has a page in the [wiki][wiki] that explains what it teaches.

| Step | What it adds | Screenshot |
| --- | --- | --- |
| 1 | Clean Blog template sorted into `templates/` and `static/` | ![Step 1][step-1] |
| 2 | `home` route renders `index.html` (the page is still unstyled) | ![Step 2][step-2] |
| 3 | `url_for('static', ...)` restores CSS, JavaScript and the background image | ![Step 3][step-3] |
| 4 | `header.html` and `footer.html` shared with Jinja `include` | ![Step 4][step-4] |
| 5 | About and Contact pages and navigation links built with `url_for` | ![Step 5 About][step-5a] ![Step 5 Contact][step-5b] |
| 6 | Posts fetched from a JSON API and listed with a Jinja `for` loop | ![Step 6][step-6] |
| 7 | One page per post (`show_post`, `/post/<id>`) | ![Step 7][step-7] |

## 📋 Requirements

- Python 3.13 or newer (the language and `venv`).
- Flask, the only runtime dependency (web server, routing and Jinja templates).
- pytest and pytest-cov for the tests (installed with the `dev` extra).
- Doxygen, only to build the API documentation (optional).

## 🛠️ Setup

Create and use a local virtual environment named `.venv`, upgrade `pip`, and
install the project with its test tools.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Leave the environment with `deactivate`. The folder `.venv/` is ignored by git.

## ▶️ Run

```bash
python -m blog.main
```

Open <http://127.0.0.1:5000> in a browser. Posts are read from the endpoint in
`src/blog/constants.py` (`POSTS_API_URL`); when it is not reachable, the site
uses the copy of the sample posts that ships with the package.

## 🧪 Tests

```bash
python -m pytest
```

The tests need no network. Build the API documentation with `doxygen Doxyfile`;
the HTML is written to `docs/doxygen/`.

## 📄 License

GNU Affero General Public License v3.0, see [LICENSE][license]. The Clean Blog
template files are MIT licensed by Start Bootstrap.

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [AGENTS.md][agents] | The rules AI agents follow in this repository |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[license]: ./LICENSE
[wiki]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/wiki
[step-1]: ./docs/screenshots/step-1-file-structure.png
[step-2]: ./docs/screenshots/step-2-unstyled-home.png
[step-3]: ./docs/screenshots/step-3-styled-home.png
[step-4]: ./docs/screenshots/step-4-includes.png
[step-5a]: ./docs/screenshots/step-5-about.png
[step-5b]: ./docs/screenshots/step-5-contact.png
[step-6]: ./docs/screenshots/step-6-home-posts.png
[step-7]: ./docs/screenshots/step-7-post.png
[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/issues
[agents]: ./AGENTS.md
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
