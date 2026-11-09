# README, screenshots and trilingual wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Claude (AI) for S01 | AI as stand-in for S01 | Initial version; reviewed in RC-007, Mode: autonomous, not independent | [1f11ab0] |

---

## Purpose

Decide whether the project is ready to share: the README is complete with screenshots and the wiki exists in English, Danish and Bahasa Malaysia and explains what each lecture step teaches.

## Deliverable

A pull request on branch `mil-004-docs-wiki-screenshots` with the final `README.md`, a flat `docs/wiki/` with the same page set in `en`, `da` and `ms`, a `_Sidebar.md`, screenshots for every step in README and wiki, and the review records of the wiki.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `README.md` follows the framework template sections and `check-readme.sh` reports no error | Met | Not met |
| 2 | README and every wiki language show one screenshot per lecture step (7 of 7) | Met | Not met |
| 3 | `docs/wiki/` holds `Home`, `Getting-Started` and `Step-1` to `Step-7` pages in English, with `-da` and `-ms` twins for each (27 pages) and a `_Sidebar.md` | Met | Not met |
| 4 | Each wiki page starts with the language line and every step page has a section "What we gained" | Met | Not met |
| 5 | `check-languages.sh` and `check-qc-tags.sh` report no error | Met | Not met |
| 6 | A fresh clone follows the README and gets HTTP 200 on `/` and a green `pytest` | Met | Not met |
| 7 | `RC-*` for the wiki (`QC-WIKI-001`) and for this milestone have the verdict `Go` | Met | Not met |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | All seven steps and their screenshots must exist |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| [BC-001] O4 | README and trilingual wiki |
| [BC-001] SC4, SC5, SC6 | Wiki languages, screenshots, clean-clone run |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in in autonomous mode) |

## Target Date

2026-11-16 — the Business Case constraint (end by 2026-11-16).

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Finalise README with screenshots | Add the seven screenshots, the final run, test and Doxygen instructions and the appendix of project documents to `README.md`, from the framework template. | No | BC-001 O4 |
| 2 | Write the English wiki | Write `Home`, `Getting-Started` and `Step-1` to `Step-7` pages in `docs/wiki/`, each step with its screenshot, the code that matters and a section "What we gained". Add `_Sidebar.md` as `framework/process/wiki.md` defines. | No | BC-001 O4 |
| 3 | Write the Danish wiki | Translate every English wiki page to Danish as `<Page>-da.md`, page by page, with the language line; code, commands and file names stay in English. | No | BC-001 SC4 |
| 4 | Write the Bahasa Malaysia wiki | Translate every English wiki page to Bahasa Malaysia as `<Page>-ms.md`, page by page, with the language line; code, commands and file names stay in English. | No | BC-001 SC4 |
| 5 | Run documentation and language checks | Run `check-readme.sh`, `check-languages.sh`, `check-qc-tags.sh`, link checks on the wiki and `doxygen Doxyfile`; review the wiki against `QC-WIKI-001`; fix findings. | No | BC-001 SC8 |
| 6 | Verify the clean-clone run and success criteria | Clone the branch into an empty folder, follow only the README, confirm HTTP 200 on `/`, green tests and the dependency count, and record the result for each success criterion SC1 to SC9 in the milestone review. | No | BC-001 SC6 |

---

[BC-001]: ../business-case.md
[1f11ab0]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/commit/1f11ab05fc7d3af6f6694514dc6b103f9b7d557f
