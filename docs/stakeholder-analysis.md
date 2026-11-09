# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Claude (AI) for S01 | AI as stand-in for S01 | Initial version; reviewed in RC-002, Mode: autonomous, not independent | pending |

---

## Purpose

The analysis names the people who use, judge or decide on the Day 59 blog
repository, classifies them by power and interest (Mendelow grid) and records
their concerns with a FURPS+ attribute, so that owners, reviewers and
acceptance can be assigned by stakeholder ID.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Self (Udemy course participant) | HIGH | HIGH | Manage Closely | Finish the lesson with a correct, tidy and well documented repository |
| S02 | Udemy coursists | Fellow participants of the course | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public internet | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, accepts the plan and every
  artifact, and is the only person who talks to others.
- **Keep Informed (S02):** cannot change the project but depends on its
  clarity; kept informed through the README and the wiki.
- **Monitor (S03):** casual visitors with no influence; served by repository
  metadata and the README.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The blog reproduces all seven lecture steps correctly | Functionality |
| CN-002 | S01 | Every artifact follows the framework and is reviewed before code | Supportability |
| CN-003 | S02 | Code is readable and uses the assignment's function names | Supportability |
| CN-004 | S02 | The README tells how to create the `.venv`, run the site and run the tests | Usability |
| CN-005 | S03 | The repository page shows a description, topics and a README | Usability |
| CN-006 | S03 | Nothing beyond what is needed is installed (no extra runtime dependencies) | Performance (footprint) |
| CN-007 | S01 | Each lecture step is explained and shown in a screenshot in three wiki languages | Usability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat with S01 | At plan acceptance and at the end of a run | Plan dry run, run summary | All milestones |
| CR-002 | Pull request on the git host | Once per milestone | Reviewed change set | MIL-001 to MIL-004 |
| CR-003 | README and wiki | At the last milestone | Run instructions, screenshots, explanations | MIL-004 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S03 wants no runtime dependencies, but Flask, `url_for` and Jinja are the assignment | S03, S01 | Flask is the one allowed runtime dependency (everything else uses the standard library); the README states it |
| S02 wants the assignment's function names, but clean layering suggests other names | S02, S01 | Keep the assignment's names for routes and helpers and place them in small modules under `src/` |
| Wiki in three languages costs effort, but only English is authoritative | S01 | English is written first; Danish and Bahasa Malaysia follow it page by page |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | [BC-001] O1 |
| S01 | CN-002 | [BC-001] O3 |
| S02 | CN-003 | [BC-001] O2 |
| S02 | CN-004 | [BC-001] O4 |
| S03 | CN-005 | [BC-001] O5 |
| S03 | CN-006 | [BC-001] O2 |
| S01 | CN-007 | [BC-001] O4 |

## Sign-Off

| Stakeholder | Role | Date |
| --- | --- | --- |
| S01 | Product Owner and reviewer (AI as stand-in, autonomous mode; plan accepted in chat) | 2026-11-09 |

---

[BC-001]: ./business-case.md
