# Team Charter

**Exploring E. coli Risk Patterns Using Rainfall and Environmental Data**

Client: Water Services Authority – Taumata Arowai
University of Canterbury – Virtual Internship 2026

> **How to use this file:** Anything marked `[TODO]` needs filling in. Fill in
> *your own row only* — do not edit other people's entries. Pull before you
> edit, commit, and push.

---

## 1. Project Overview

| Field | Detail |
| --- | --- |
| Project name | Exploring E. coli Risk Patterns Using Rainfall and Environmental Data |
| Client | Water Services Authority – Taumata Arowai (taumataarowai.govt.nz) |
| Project type | Proof-of-concept data analysis (not a complete predictive tool) |
| Duration | `[TODO — charter says 18 Jun–17 Jul 2026; confirm actual dates]` |
| Deliverable 1 | Team-written report, 2,500–3,000 words including citations |
| Deliverable 2 | 10-minute team presentation |
| Submission dates | `[TODO — confirm with Program Organiser / Mentor]` |

---

## 2. Team Purpose & Shared Goals

Our purpose is to explore whether simple data analysis can reveal patterns in
E. coli risk following rainfall events, and to communicate our findings clearly
to the client. As a team we commit to:

- Deliver both a high-quality report and presentation on time and within scope.
- Produce honest, defensible analysis — we will be clear about what the data
  can and cannot show.
- Contribute equitably, so every member learns and the workload is shared fairly.
- Score well against all six rubric criteria (Section 11).
- Work professionally and supportively, treating this as a real client engagement.

---

## 3. Team Members & Roles

Five members, each leading one area. Leads coordinate their area; everyone
contributes to the report and presentation.

**Fill in your own row: email, GitHub username, and tick the box.**

| Member | Role | Email | GitHub username | Charter accepted |
| --- | --- | --- | --- | --- |
| Ahmed Masoom | Project Lead | ama778@uclive.ac.nz | `[TODO]` | [ ] |
| Hanna Hautea | Visualisation / GIS Lead | hanapatriciahautea@gmail.com | `[TODO]` | [ ] |
| Rupika | Analysis Lead | `[TODO]` | `[TODO]` | [ ] |
| Rex | Data Lead | `[TODO]` | `[TODO]` | [ ] |
| Max | Report & Comms Lead | `[TODO]` | `[TODO]` | [ ] |
| Weiyu Liu | Support | wli115@uclive.ac.nz | WeiyuLiu1 | [x] |

---

## 4. Roles & Responsibilities

**Project Lead (Ahmed)**
- Owns the timeline and ClickUp board; keeps the team on track to deadlines.
- Runs meetings, records decisions, and is the main point of contact.
- Coordinates final submission; drafts limitations and recommendations.

**Data Lead (Rex)**
- Sources rainfall, E. coli and environmental datasets; documents licences.
- Cleans, structures and joins the data into an analysis-ready set.

**Analysis Lead (Rupika)**
- Runs the exploratory analysis (rainfall vs E. coli, location, features).
- Designs, builds and tests the low/medium/high risk score.

**Visualisation / GIS Lead (Hanna)**
- Creates charts, tables, maps and the dashboard-style summary.
- Ensures visuals are clear, accurate and presentation-ready.

**Report & Comms Lead (Max)**
- Owns report structure, formatting, citations (Zotero) and word count.
- Coordinates the slide deck and presentation logistics.

**All members**
- Attend meetings, update ClickUp tasks, contribute to writing, rehearse the talk.

---

## 5. Communication Plan

| Channel | Used for | Expected response time |
| --- | --- | --- |
| WhatsApp | Quick questions, day-to-day chat | Within 1 hour on weekdays |
| Email | Formal / external comms, tutor | Within 24 hours |
| ClickUp comments | Task-specific discussion & decisions | When working on the task |
| Zoom | Team meetings | Confirm or decline 24 hours before |
| GitHub | Code, scripts, documents, version history | Review PRs within 24 hours |
| OneDrive | Raw data files too large for Git | N/A |

**Norm:** if you are unavailable or cannot meet a deadline, tell the team as
early as possible.

---

## 6. Meeting Cadence

- **Weekly internal team meeting** — Fridays 8:30 pm, ~45 min. Review progress,
  plan the week, unblock issues.
- **Weekly mentor meeting** — Sundays, ~1 hour. Review progress.
- **Mid-week check-in** — async update in WhatsApp / ClickUp.
- Each meeting has a brief agenda; the Project Lead records decisions and action
  items in ClickUp.
- Ad-hoc working sessions as needed near deliverable dates.

---

## 7. Decision-Making

- Routine decisions are made by the relevant role lead.
- Decisions affecting scope, methods or deliverables are made by the team,
  aiming for consensus.
- If consensus cannot be reached, we decide by majority vote; the Project Lead
  breaks a tie.
- All significant decisions are recorded (ClickUp or meeting notes) so they are
  not relitigated.

---

## 8. Ways of Working — Team Norms

- Treat each other with respect; everyone's input is valued.
- Keep tasks in ClickUp up to date — status, blockers, links to outputs.
- Deliver your tasks by the agreed date, or flag early if you cannot.
- Give feedback on the work, not the person; assume good intent.
- Reference everything — capture sources as you go for citations.

---

## 9. Version Control & File Management

Replaces the earlier "save files in the shared drive with clear names" approach.

**What lives where**
- **GitHub** — all code, scripts, notebooks, report drafts, and this charter.
  GitHub is the single source of truth for anything text-based.
- **OneDrive** — raw data files too large for Git (>50 MB), and any data we are
  not licensed to publish.

**Branch and commit conventions**
- Branch names: `feature/yourname-short-description`
  (e.g. `feature/rex-rainfall-cleaning`)
- Commit messages: present tense, one line, says what changed
  (e.g. `Add rainfall data source documentation`)
- **Pull before you start work.** `git pull origin main` every time.
- After this deliverable, no direct pushes to `main` — all changes go through a
  pull request.
- Every PR is reviewed by at least one other member before merging.
- Delete your branch after it's merged.

**Keep out of the repo** (add to `.gitignore`)
- Large or restricted datasets, `.Rhistory`, `.RData`, `__pycache__/`,
  `.DS_Store`, `.env`, credentials of any kind.

---

## 10. Task & Project Management

We manage the project in ClickUp using the imported plan (8 phases, 49 subtasks).

- Every task has an owner, a due date and a status
  (To Do / In Progress / In Review / On Hold / Done).
- Update your task status before each meeting.
- Board view for standups, Gantt/Timeline for the critical path, Calendar for
  the week.
- Raise blockers as ClickUp comments and @mention the people involved.
- The board must be visible to the tutor/mentor — check sharing settings.

---

## 11. Accountability & Deadlines

- Internal deadlines are set a few days before any official due date, to allow
  review and buffer.
- If a member repeatedly misses commitments, the team discusses it openly and
  supportively first.
- Persistent issues are escalated to the program tutor/coordinator as a last
  resort.
- We track contribution fairly, so peer/teamwork assessment reflects reality.

---

## 12. Quality Standards — Definition of Done

| Rubric criterion | What "good" looks like for us |
| --- | --- |
| Written Communication / Structure | Clear, well-organised report within 2,500–3,000 words, proofread. |
| Getting Information | Relevant, credible data sources identified and documented. |
| Analysing Data & Information | Sound, reproducible analysis; conclusions supported by evidence. |
| Critical Thinking | Honest about limitations; thoughtful recommendations and next steps. |
| Teamwork | Equitable contribution; decisions and workload shared. |
| Presentation Skills | Clear, well-rehearsed 10-minute talk; everyone presents. |

Every report section and the deck get a peer review before submission.

---

## 13. Conflict Resolution

- Raise the issue early and directly with the people involved, in private and
  respectfully.
- If unresolved, bring it to the full team to discuss and agree a way forward.
- If still unresolved, the Project Lead facilitates a decision per Section 7.
- As a last resort, escalate to the program tutor/coordinator.

---

## 14. Risks & Contingencies

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Data hard to find or access | Delays analysis | Start sourcing in week 1; have a backup catchment/sample dataset. |
| A member unavailable / drops out | Workload imbalance | Cross-share knowledge; document work in ClickUp; redistribute early. |
| Report over word limit / late | Marks lost | Word-count check task before submission. |
| Merge conflicts / lost work | Rework, wasted time | Pull before editing; small commits; edit only your own sections. |

---

## 15. Agreement & Sign-Off

By adding your name and the date below, you agree to uphold this charter for
the duration of the project. Commit this change yourself — your commit is your
signature.

| Name | Date signed |
| --- | --- |
| `[TODO]` | `[TODO]` |
| `[TODO]` | `[TODO]` |
| `[TODO]` | `[TODO]` |
| `[TODO]` | `[TODO]` |
| `[TODO]` | `[TODO]` |
