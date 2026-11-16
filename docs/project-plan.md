# Project Plan

## Metadata
| Key | Value |
| --- | --- |
| ID | PP-001 |
| CrossReference | [BC-001], [SA-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] |
| Language | en |
| Domain | education |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Deprecated | Claude (AI) for S01 | AI as stand-in for S01 | Initial version; reviewed in RC-003, Mode: autonomous, not independent | [1f11ab0] |
| 2026-11-16 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added the baseline gateway G5 (MIL-005) with its schedule row, scope coverage, dependency, risk and Gantt entries; recorded the move of the end date, the domain and the open pull request #31 in the Planning Assumptions and Open Issues; set the domain to education; reviewed in autonomous mode, not independent | [8dc3193] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Recorded task 6 of MIL-005 (one behaviour-neutral source change for the OpenGrep check) in the schedule row and the Open Issues; reviewed in autonomous mode, not independent | pending |

---

## Purpose

The plan schedules four gateways (and, since the baseline gateway [MIL-005], a fifth) that deliver the Day 59 blog over the Business
Case constraint "the work ends by 2026-11-16" ([BC-001]). Each gateway is one
branch, one pull request, one review record and one Milestone on the git host.

## Planning Assumptions

- Week 1 starts 2026-11-09; the plan ends by 2026-11-16, per the Business Case constraint.
- The baseline gateway G5 (MIL-005) starts 2026-11-16 and ends 2026-11-23, one week (source: [BC-001], Constraints). It brings the finished project to the baseline of the framework, a decision of S01. The decision dates of the earlier gateways stay as they were, so the end date of the plan moves from 2026-11-16 to 2026-11-23.
- For MIL-005 S01 has authorised the assistant to commit, push, open the pull request and merge it, and the review is done by an AI stand-in for S01 (source: [BC-001], Constraints and Risks).
- The PO language is English; the domain is IT until [MIL-005] and education since.
- Phase length: one to two days; the gateways follow the lecture's own order.
- The Product Owner, developer and reviewer is S01; in autonomous mode the AI
  is the stand-in reviewer (`Mode: autonomous, not independent`), and S01
  confirms the language criteria of `QC-LANG-001` that need a person who reads
  English and knows the IT domain when accepting this plan.
- Presentation pattern: the user interface is a server-rendered web UI, so the
  `clean-architecture` default applies in a light form: Jinja templates are the
  view, the Flask routes in the presentation layer are the controllers, and
  post data is passed as plain objects (view models). No wireframes exist
  beyond the lecture's screenshots, which serve as the first edition.
- Branches: `mil-001-project-setup`, `mil-002-site-skeleton`,
  `mil-003-dynamic-posts`, `mil-004-docs-wiki-screenshots`. Commits carry no
  AI attribution lines. Screenshots are taken in a Docker container.
- The repository is the existing remote
  `Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2` on
  `git.tirsystem.com`.

## Gateway Schedule

| Gateway | Document | Window | Decision date | Owner | Stories | Main deliverable | Milestone |
| --- | --- | --- | --- | --- | --- | --- | --- |
| G1 Project setup and tooling | [MIL-001] | 2026-11-09 to 2026-11-10 | 2026-11-10 | S01 | none (technical) | `pyproject.toml`, layout, README, repository metadata | [Milestone 384][ms-384] |
| G2 Site skeleton (Steps 1-5) | [MIL-002] | 2026-11-10 to 2026-11-12 | 2026-11-12 | S01 | none (lecture steps) | Bootstrap site with shared header and footer, About, Contact | [Milestone 385][ms-385] |
| G3 Dynamic posts (Steps 6-7) | [MIL-003] | 2026-11-12 to 2026-11-14 | 2026-11-14 | S01 | none (lecture steps) | Posts from the API and post pages | [Milestone 386][ms-386] |
| G4 Docs and wiki | [MIL-004] | 2026-11-14 to 2026-11-16 | 2026-11-16 | S01 | none (documentation) | README, trilingual wiki, screenshots | [Milestone 387][ms-387] |
| G5 Framework baseline | [MIL-005] | 2026-11-16 to 2026-11-23 | 2026-11-23 | S01 | none (technical tasks) | Branch `mil-005-framework-baseline` merged: the adopted framework release, the README, project URL metadata, `.editorconfig`, `.env.example`, review records and one behaviour-neutral source change (task 6) | [Milestone 580][ms-580] |

```plantuml
@startgantt
Project starts 2026-11-09
[G1 Project setup] starts 2026-11-09 and ends 2026-11-10
[G1 Go/No-Go] happens 2026-11-10
[G2 Site skeleton] starts 2026-11-10 and ends 2026-11-12
[G2 Go/No-Go] happens 2026-11-12
[G3 Dynamic posts] starts 2026-11-12 and ends 2026-11-14
[G3 Go/No-Go] happens 2026-11-14
[G4 Docs and wiki] starts 2026-11-14 and ends 2026-11-16
[G4 Go/No-Go] happens 2026-11-16
[G5 Framework baseline] starts 2026-11-16 and ends 2026-11-23
[G5 Go/No-Go] happens 2026-11-23
@endgantt
```

## Scope Coverage

| Business Case scope item | Gateway |
| --- | --- |
| Flask application with the Clean Blog template, header and footer includes | G2 |
| Routes for home, about, contact and individual posts | G2, G3 |
| Posts from a configurable JSON endpoint with a bundled copy | G3 |
| pytest tests | G2, G3 |
| `pyproject.toml`, `.gitignore`, `Doxyfile`, `constants.py`, `.venv` instructions | G1 |
| README and three-language wiki with screenshots | G1 (first README), G4 |
| Repository description and topics | G1 |
| The baseline: framework release, README, project URL metadata, editor settings, environment template, review records (objective O6) | G5 |

## Dependencies

```
G1 → G2 → G3 → G4 → G5
```

A No-Go at a gateway moves every later date by the rework time; the end date of
2026-11-16 is then re-planned with S01, not silently exceeded.

## Plan Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Docker image for the headless browser is slow to build | G2 and G3 screenshots late | Build the image once in G2 and reuse it |
| Translation volume (27 wiki pages) is larger than expected | G4 slips | English first; Danish and Bahasa Malaysia follow page by page; start them as soon as each English step page is final |
| Review stand-in cannot close the language criteria | Milestones stay `Go-with-conditions` and block the gate | S01 confirms criteria 3, 5 and 9 of `QC-LANG-001` at plan acceptance |
| A continuous integration (CI) check fails on the pull request of MIL-005 | The merge is delayed past 2026-11-23 | The failure is fixed on the same branch and the checks run again; after three failed rounds on one cause the work stops and S01 decides (trace: success criterion SC10 of [BC-001]) |

## Open Issues

- The requested repository URL `Tirsvad-Udemy-100_days_of_code` differs from the
  configured remote `Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2`;
  the plan uses the remote and its token.
- The course's own npoint document is used as the default endpoint; creating a
  personal bin needs a browser sign-up and is left to S01 (the endpoint is a constant).
- The Governance (`GOV`) and Dictionary (`DICT`) documents are not created: the
  project has one person and no domain terms beyond the framework's; the
  traceability matrix and the review records carry the quality trail.
- Domain: since [MIL-005] the plan, the Business Case and the baseline milestone have the domain `education`. The other documents (Stakeholder Analysis, milestones MIL-001 to MIL-004 and the review records RC-001 to RC-011) keep the domain `it` they were accepted with; they are not changed by the baseline, and a change of their domain would need a new review of each.
- The git host also has the open pull request #31 (framework submodule URL in lowercase); the baseline delivers the same change in the pull request of MIL-005, and S01 closes #31 after the merge.
- The earlier review record RC-011 checked the wiki; MIL-005 checks it again against the current checklist (including the published wiki, criterion 14) and changes no page.
- The source file `api_post_repository.py` carried two `nosemgrep` markers from MIL-003 whose rule names no longer match the rule names of the shared OpenGrep ruleset, so the check on the pull request of MIL-005 reported the `importlib.resources` import as a blocking finding. Task 6 of MIL-005 removes the import and its marker and reads the bundled posts file with `pathlib` (same behaviour, tests unchanged). The second marker (the `urllib` call, reported as a warning only) is left as it is; no suppression is added.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[MIL-001]: ./milestones/mil-001-project-setup.md
[MIL-002]: ./milestones/mil-002-site-skeleton.md
[MIL-003]: ./milestones/mil-003-dynamic-posts.md
[MIL-004]: ./milestones/mil-004-docs-wiki-screenshots.md
[1f11ab0]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/commit/1f11ab05fc7d3af6f6694514dc6b103f9b7d557f
[ms-384]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/milestone/384
[ms-385]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/milestone/385
[ms-386]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/milestone/386
[ms-387]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/milestone/387
[MIL-005]: ./milestones/mil-005-framework-baseline.md
[ms-580]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/milestone/580
[8dc3193]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/commit/8dc3193b6ef18b8c03044408ae0fa5be595873a3
