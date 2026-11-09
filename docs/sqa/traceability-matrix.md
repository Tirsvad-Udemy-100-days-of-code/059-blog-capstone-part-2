# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | <reviewer S-ID> | Initial version | [1f11ab0] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| BC-001 | BC | en | it | - | SA-001, PP-001, MIL-001..004 | RC-001 |
| SA-001 | SA | en | it | BC-001 | PP-001 | RC-002 |
| PP-001 | PP | en | it | BC-001, SA-001 | MIL-001..004 | RC-003 |
| MIL-001 | MIL | en | it | BC-001, PP-001 | - | RC-004, RC-008 |
| MIL-002 | MIL | en | it | BC-001, MIL-001 | - | RC-005, RC-009 |
| MIL-003 | MIL | en | it | BC-001, MIL-002 | - | RC-006, RC-010 |
| MIL-004 | MIL | en | it | BC-001, MIL-003 | - | RC-007 |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | MIL-002, MIL-003 | - | - | Covered |
| CN-002 | MIL-001 | - | - | Covered |
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
