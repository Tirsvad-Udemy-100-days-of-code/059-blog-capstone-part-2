# Review of the wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-004], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; Mode: autonomous, not independent | pending |

---

## Artifact Under Review

- Instance reviewed: the wiki in `docs/wiki/` (27 pages and `_Sidebar.md`) delivered for MIL-004
- Checklist used: [QC-WIKI-001]
- Scope: full review
- Language and domain: en, da and ms pages; the wiki is not an artifact with Language and Domain rows
- Language reviewer: none
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | `docs/wiki/_Sidebar.md` exists. |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Bold title, one English page list, Home first. |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | The structure check (page sets, links, sidebar) found no dead link and every English page is listed. |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | Pass | No related wiki exists and there is no Related section. |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages section is last: English Home, Dansk Hjem, Bahasa Malaysia Utama. |
| 6 | The sidebar does not repeat the page list per language | Pass | Page list appears once. |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is hand-written, not generated; the criterion applies to generated sidebars only. |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Each page has the language line. |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English plus Danish and Bahasa Malaysia; the PO language is English. |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | 9 English pages, 9 `-da` and 9 `-ms` pages; verified by script. |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Every page starts with the language line, the current language in bold. |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | `<Page>-da.md` and `<Page>-ms.md`; English has no suffix. |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Code blocks and reference definitions are byte-identical to English (verified by script). |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | The wiki is published by the host workflow after the merge; the published sidebar and links are checked then (action item). |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | No layout rule changed. |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | `docs/wiki/` is flat; no subfolder. |

## Overall Verdict

Go-with-conditions — every Mandatory criterion passes except criterion 14, which only the published wiki can answer (Pending). The Danish and Bahasa Malaysia texts were written by the AI and have not been read by a native speaker; they follow the English page by page.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| After the merge, check the published sidebar and every link on the host, then close criterion 14 | S01 | 2026-11-16 |
| Native review of the Danish and Bahasa Malaysia text | S01 | 2026-11-16 |

---

[MIL-004]: ../../milestones/mil-004-docs-wiki-screenshots.md
[QC-WIKI-001]: ../../../framework/qc/artifacts/qc-wiki.md
