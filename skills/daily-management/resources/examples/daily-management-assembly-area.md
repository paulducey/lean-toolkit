Shows a three-tier daily management design for a mixed-model assembly area, hourly plan vs. actual on the T1 board, OEE moved off T1 to T2, a response-to-abnormality protocol with defined escalation thresholds, and meeting agendas specified.

**User:** We're setting up daily management for our mixed-model assembly area for the first time. No tiers exist yet.

**Assistant:** Tell me about the current state — which tiers exist, what's on the boards, how long the meetings run, and where the system isn't working. Sounds like this is a design from scratch rather than a diagnosis — that changes how I approach it. Leave out personnel names when you describe the area; roles and shift designations are fine.

**User:** Just draft it. We run 4 models on one line, one shift, 8 people plus a supervisor. Right now the only thing anyone sees is an end-of-shift report the supervisor emails out.

**Assistant:** Here's a three-tier design. I don't know your specific model mix takt times or historical OEE, so those pieces are marked for you to fill in.

## Daily Management Design — Mixed-Model Assembly Area

### Tier 1 — Team Level
**Who:** Assembly team (8), team lead
**Where:** At the line, in front of the hour-by-hour board
**Frequency:** Start of shift, then every hour
**Duration target:** ≤15 min at shift start, 5 min hourly check-ins

**T1 board content:**
- Hourly plan vs. actual by model (4 rows, one per model) — updated by the team lead each hour [ASSUMED — verify: confirm the team can realistically update this without pulling someone off the line]
- Top abnormalities from the prior hour: what happened, what was done, status
- Safety cross (daily) — filled in by the team
- Today's standard work items and completion status, referencing `standard-work` documents at each station
- One quality indicator measurable each hour: first-pass yield by model, if station-level pass/fail is already tracked [NEEDS GEMBA: confirm whether this data exists today or needs a new tally sheet]

**What does NOT go on this board:** end-of-shift OEE (that's a lag metric, moves to T2), and the current end-of-shift email report is retired in favor of the hourly board.

### Tier 2 — Supervisor Level
**Who:** Supervisor, plus maintenance/quality on rotation
**Where:** Area board
**Frequency:** Once per shift (end of shift, given this is a single-shift operation)
**Duration target:** ≤30 min

**T2 board content:**
- T1 summary: which models hit plan for the day, which didn't
- Escalations raised from T1 during the shift and resolution status
- OEE for the shift, by model — moved here from T1 because it's only measurable once per shift, which fails the T1 lead-metric test [ASSUMED — verify: confirm your OEE data can actually be broken out by model, not just by line]
- Downtime log with root-cause status for anything over 10 minutes

### Tier 3 — Value Stream Level
**Who:** [NEEDS GEMBA: who above the supervisor owns this area — plant manager, value stream manager]
**Where:** Plant-level board
**Frequency:** Daily
**Duration target:** ≤60 min

**T3 board content:**
- T2 summary across all areas reporting into this value stream, not just this one assembly area
- Open escalations and any A3s in progress, with owner and status
- Delivery, quality, and safety KPIs [NEEDS GEMBA: which specific KPIs this plant already tracks at this level]

### Response-to-Abnormality Protocol (Tier 1)

| Step | What happens | Threshold / trigger |
|---|---|---|
| 1. Detect | Hourly board shows actual below plan for that model | Any hour where actual < 90% of planned units [ASSUMED — verify this threshold with the supervisor; drafted, not confirmed] |
| 2. Contain | Team lead identifies immediate cause and takes damage-limiting action (reroute WIP, pull backup part, notify next station) | Applied immediately on detection |
| 3. Escalate | Team lead escalates to supervisor if the same model misses plan two hours in a row, or if any single hour falls below 75% of plan | Two consecutive hours below 90%, or one hour below 75% |
| 4. Analyze | Supervisor assigns root-cause investigation for any abnormality that recurs 2+ times in a week; referenced to `root-cause` | Recurrence, not first occurrence |

### Meeting Agendas

**T1 shift-start (10–15 min):** Safety cross check-in (2 min) → yesterday's carryover items (3 min) → today's plan by model (3 min) → standard work or staffing notes (5 min).
**T1 hourly (5 min):** Actual vs. plan this hour → any abnormality and its status → nothing new opened unless it's an escalation.
**T2 end-of-shift (30 min):** T1 escalations review (10 min) → shift OEE and downtime (10 min) → quality/safety trend (5 min) → next-shift handoff notes (5 min).

---

**User:** What if the team can't realistically update the board every hour with only 8 people?

**Assistant:** That's exactly the kind of thing I flagged as needing your confirmation rather than assumed — if pulling someone off the line hourly isn't workable, the alternative is a rotating scribe duty (each person takes one hour) or a simpler tally the team lead updates without leaving their post. That's a decision that needs your knowledge of the floor, not something I'd guess at.

---

**What this skill did:**
- Designed a three-tier daily management system from scratch for a mixed-model assembly area with no prior tiers, replacing the end-of-shift-only email report with an hourly T1 board.
- Applied the lead/lag rule to move OEE off the T1 board (only measurable once per shift) to T2, and defined a four-step response-to-abnormality protocol with numeric escalation thresholds.
- Meeting agendas specified for T1 shift-start, T1 hourly, and T2 end-of-shift, each within the tier duration maximum.

**What still needs a human:** The escalation threshold (90%/75% of plan) is drafted, not confirmed — the supervisor's knowledge of what actually predicts a bad shift on this line is what should set the real number.

**Suggested next step:** Take the draft T1 board and escalation thresholds to the supervisor and the team lead together, and confirm hourly board updates are workable with the current headcount before the design goes live.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
