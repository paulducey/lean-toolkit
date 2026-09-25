# Example: chartering a 5-day kaizen event to cut changeover time on a stamping line, readiness questions first

**User:** We want to run a kaizen event on our stamping line changeover — it's too slow and we want to fix it next month.

**Assistant:** Leave out names of employees and anything confidential when you share details; roles and initials are fine. I'll ask a few questions a coach would ask — including whether this is the right event to run at all — then draft the charter. Say *just draft it* at any point and I'll work from what you've given me.

First, the readiness questions: has anyone actually watched a changeover on this line recently, or is the pain mostly from complaints and reports?

**User:** The line supervisor, T., has watched a few. Nobody's timed the steps though.

**Assistant:** Good — some observation, no step-level data yet. Is the process stable right now — running its normal way most days — or is it currently in some kind of crisis (short-staffed, mid-transition to new tooling, a one-off spike)?

**User:** It's stable. Same crew, same press, same tooling for the last six months.

**Assistant:** Good. Will the sponsor actually free the team for the full week, no pulling people back for an hour here and there? Has that been tried before?

**User:** We tried a kaizen event two years ago and lost half the team back to firefighting by day 3. Plant manager says this time it's committed.

**Assistant:** I'll note that history as a real risk in the charter rather than assume this time is different. Last one: is the changeover problem understood well enough to scope a week around it, or does it need a root-cause pass first?

**User:** We know changeover averages way too long. We don't know exactly where the time goes.

**Assistant:** That's actually two negative-leaning readiness signals — no step-level data, and a history of the team getting pulled back. I'd normally suggest a short pre-work pass (a time study, and firming up the backfill commitment in writing) before the week. Do you want that pre-work step built in, or draft the charter as a 5-day event anyway?

**User:** Build the pre-work in, but let's go ahead and draft the full charter.

**Assistant:** Good — I'll default to 5-day since the process hasn't been step-timed yet, and I'll put the pre-work (time study, backfill commitment) as day-zero prerequisites, not day-1 work.

---

## Kaizen Charter: Stamping Line Changeover Reduction

**1. Business case**
Stamping line changeover currently averages 74 minutes [from system: setup crew changeover log] against a target of 40 minutes, contributing to missed takt on shifts following a changeover [NEEDS GEMBA: quantify takt cycles lost per changeover]. This charter supports the plant manager's decision to commit a dedicated week to this line rather than incremental fixes.

**2. Scope**
Starts at last-good-part of the outgoing die; ends at first-good-part approval of the incoming die on the stamping press. Limited to this one press.

**3. Boundaries and constraints**
- Press cannot be taken offline during first shift — changeover work and testing happen on second/third shift or scheduled downtime windows only [ASSUMED — verify with production planning].
- No capital tooling purchases approved for this event; solutions must use existing equipment.

**3a. Readiness assumptions and risks**
- No step-level time study exists yet — pre-work must include one before day 1, or day 1 becomes the time study instead of design work.
- A prior kaizen event on this line lost half its team to firefighting by day 3 — the plant manager says backfill commitment is firm this time, but this should be confirmed in writing before the week, not assumed. `[NEEDS GEMBA: get the backfill commitment in writing]`

**4. Team**
| Role | Who |
|---|---|
| Sponsor | Plant manager |
| Facilitator | `[NEEDS GEMBA: assign]` |
| Team lead | Line supervisor, T. |
| Members | Setup crew (2–3), maintenance technician |
| Subject-matter experts | Die shop lead (by function) |

**5. Baseline metrics**
| Metric | Baseline | Source |
|---|---|---|
| Changeover time | 74 minutes average | [from system: setup crew changeover log, last 20 changeovers] |
| Step-level breakdown | Not available | `[NEEDS GEMBA: pre-work time study]` |

**6. Targets**
| Metric | Baseline | Target | By when |
|---|---|---|---|
| Changeover time | 74 min | 40 min | End of event week + confirmation at 30 days |

**7. Pre-work checklist**
- [ ] Time-study the next 3 changeovers step-by-step before the event week `[NEEDS GEMBA]`
- [ ] Get backfill commitment for the full team in writing from the plant manager `[NEEDS GEMBA]`
- [ ] Stage a video camera or stopwatch kit for day 1 confirmation runs
- [ ] Pull current tooling storage layout near the press

**8. Agenda — 5-day**
| Day | Focus |
|---|---|
| 1 | Confirm current-state changeover steps against pre-work time study; validate baseline |
| 2 | Identify internal vs. external work (SMED), waste in each step |
| 3 | Design future-state sequence, convert internal work to external where possible |
| 4 | Implement changes, run test changeovers, adjust |
| 5 | Stabilize, document new standard changeover procedure, report-out |

**9. Deliverables**
Updated changeover standard procedure, tooling staging layout change (if any), before/after time data, and an owner for sustaining the gain.

**10. Report-out plan**
Team lead T. presents before/after changeover times and the new procedure to the plant manager and shift supervisors on day 5 afternoon.

**11. 30/60/90-day follow-up**
| Checkpoint | Date | Owner | What's checked |
|---|---|---|---|
| 30-day | `[NEEDS GEMBA: set date]` | T. | Changeover time holding at/near 40 min |
| 60-day | `[NEEDS GEMBA: set date]` | T. | New procedure still being followed as documented |
| 90-day | `[NEEDS GEMBA: set date]` | Plant manager | Sign-off that gain is sustained; retrospective on backfill commitment |

---

**Self-critique:** The readiness risk most likely to derail the week is the backfill commitment — it failed once already on this exact line. The boundary most likely to get tested is "no capital tooling purchases" once the team finds a fixture-related root cause. The report-out will need actual before/after times from confirmation runs, not just the day-1 baseline, which isn't nailed down yet since pre-work hasn't happened.

**What this skill did:**
- Ran the readiness questions before drafting and surfaced two negative-leaning risks: no step-level data yet, and a prior backfill failure on this same line.
- Built pre-work (time study, written backfill commitment) into the charter as day-zero prerequisites rather than silently assuming they'd happen.
- Drafted a full 5-day charter with baseline, targets, agenda, and 30/60/90 follow-up as requested.

**What still needs a human:**
- Get the backfill commitment in writing from the plant manager before day 1 — this event failed once already for exactly this reason.
- Complete the pre-work time study; the current-state breakdown does not exist yet.
- Assign a facilitator — not yet named.

**Suggested next step:** Have the line supervisor, T., run the pre-work time study on the next three changeovers and get the plant manager's backfill commitment in writing before scheduling the event week.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
