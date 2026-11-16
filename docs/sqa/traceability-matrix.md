# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-005] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [1f11ab0] |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Added MIL-005 and its review records RC-012 to RC-015; set the domain of BC-001 and PP-001 to education; replaced the reviewer placeholder of the first row; reviewed in autonomous mode, not independent | pending |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| BC-001 | BC | en | education | - | SA-001, PP-001, MIL-001..005 | RC-012, RC-001 |
| SA-001 | SA | en | it | BC-001 | PP-001 | RC-002 |
| PP-001 | PP | en | education | BC-001, SA-001 | MIL-001..005 | RC-013, RC-003 |
| MIL-001 | MIL | en | it | BC-001, PP-001 | - | RC-004, RC-008 |
| MIL-002 | MIL | en | it | BC-001, MIL-001 | - | RC-005, RC-009 |
| MIL-003 | MIL | en | it | BC-001, MIL-002 | - | RC-006, RC-010 |
| MIL-004 | MIL | en | it | BC-001, MIL-003 | MIL-005 | RC-007, RC-011 |
| MIL-005 | MIL | en | education | BC-001, PP-001, MIL-004 | - | RC-014, RC-015 |

The domain of BC-001, PP-001 and MIL-005 is `education` since MIL-005; the other documents keep the domain `it` they were accepted with (see the Open Issues of PP-001). MIL-005 changes no source, test, screenshot or wiki file. The wiki is reviewed again in RC-015 (it has no row of its own in this matrix, as before).

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | MIL-002, MIL-003 | - | - | Covered |
| CN-002 | MIL-001, MIL-005 | - | - | Covered |
| CN-003 | MIL-003 | - | - | Covered |
| CN-004 | MIL-001, MIL-004 | - | - | Covered |
| CN-005 | MIL-001 | - | - | Covered |
| CN-006 | MIL-001 | - | - | Covered |
| CN-007 | MIL-004 | - | - | Covered |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | None found | - | Closed | - |

---

[BC-001]: ../business-case.md
[1f11ab0]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/059-blog-capstone-part-2/commit/1f11ab05fc7d3af6f6694514dc6b103f9b7d557f
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-005]: ../milestones/mil-005-framework-baseline.md
[RC-012]: ./reviews/rc-012-business-case-baseline.md
[RC-013]: ./reviews/rc-013-project-plan-baseline.md
[RC-014]: ./reviews/rc-014-milestone-005.md
[RC-015]: ./reviews/rc-015-wiki-baseline.md
