Shows an assessment of an existing daily management system, identifying three failure modes (a 45-minute T1 standup, lag metrics on T1, no escalation protocol), a redesign, and a standard-work reference added for the new T1 standup format.

**User:** Our daily standup on the fabrication line is a mess. It runs 45 minutes and nothing gets resolved.

**Assistant:** Tell me about the current state — which tiers exist, what's on the boards, how long the meetings run, and where the system isn't working. This sounds like a diagnosis of an existing system rather than a fresh design — is that right?

**User:** Right, we just need to fix what we have. Before I paste the details — I know, leave out names.

**Assistant:** That's the right instinct — roles and shift designations are enough.

**User:** One tier only, called it "daily standup," whole fab team plus supervisor, 45 minutes every morning. Board shows yesterday's total output, yesterday's scrap count, and yesterday's OEE. When something goes wrong the team just talks about it in the meeting until someone has an idea, no defined next step, and it's not written anywhere who's supposed to do what. Half the meeting is people debating root cause of yesterday's scrap.

**Assistant:** Here's the assessment — I found three specific failure modes, not just "meetings run long."

## Daily Management Assessment — Fabrication Line

### Failure Mode 1: T1 board shows only lag metrics
**Observation:** Output, scrap, and OEE are all yesterday's totals — end-of-shift numbers with no in-shift visibility [from user].
**Root cause:** No hourly or per-cycle tracking exists; the team only finds out how the day went after it's over — by definition, this fails the T1 lead-metric test ("can the team act on this in the next 30–60 minutes?").
**Fix:** Replace with hourly plan vs. actual by the fabrication step, and move yesterday's OEE and scrap total to a new T2-level review (see below — this line currently has no T2).

### Failure Mode 2: Meeting runs 45 minutes with no agenda
**Observation:** No time-boxing; the meeting expands to fill available time with open-ended discussion [from user].
**Root cause:** No structure separates "report status" from "solve the problem" — both happen in the same freeform conversation.
**Fix:** Time-box the meeting to 15 minutes maximum (T1 target). Root-cause discussion moves out of the standup entirely — see Failure Mode 3.

### Failure Mode 3: No response-to-abnormality protocol
**Observation:** When something goes wrong, the team discusses it live until someone proposes an idea; nothing is written down about who does what [from user].
**Root cause:** No four-step protocol (detect, contain, escalate, analyze) exists — the standup is being used as an ad hoc problem-solving session instead of a status-and-assignment session.
**Fix:** Adopt the four-step protocol below; root cause analysis gets assigned during the standup, not conducted during it — reference `root-cause` for the actual investigation.

## Redesigned T1 Standup — Fabrication Line

**Frequency:** Start of shift, plus hourly check-ins at the line (new — didn't exist before)
**Duration target:** ≤15 min for shift-start, ≤5 min hourly

**New T1 board content:**
- Hourly plan vs. actual by fabrication step [NEEDS GEMBA: confirm what unit of output is trackable hourly — pieces, weight, or cycles, depending on the step]
- Today's abnormalities: what happened, containment action, status — carried hour to hour, not just discussed once
- Safety cross
- Standard work completion status, referencing `standard-work` documents once they exist for each fab step [NEEDS GEMBA: confirm standard work documents currently exist for this line — not stated]

**Moved off T1, to a new T2 review (once per shift, ≤30 min):**
- Yesterday's total output, scrap count, OEE — these stay valuable, just at the tier where they're actionable within a day's planning horizon rather than an hour's

### Response-to-Abnormality Protocol (new)

| Step | What happens | Threshold / trigger |
|---|---|---|
| 1. Detect | Hourly actual falls short of plan | [ASSUMED — verify: draft threshold of actual < 85% of hourly plan; supervisor should confirm against real variation] |
| 2. Contain | Team lead takes immediate action — flag the piece, hold the batch, notify next step | Immediate |
| 3. Escalate | To supervisor if the same abnormality recurs within the shift, or containment isn't possible with team authority | Second occurrence in a shift |
| 4. Analyze | Assigned during standup, conducted afterward — not during the 15-minute window | Any abnormality tagged for `root-cause` gets an owner and a due date in the standup, not a resolution in the room |

**New standup agenda (target 15 min):**
1. Safety cross (2 min)
2. Yesterday's carryover abnormalities — status only, not new discussion (3 min)
3. Today's plan by fab step (3 min)
4. Open abnormalities — assign owner and next step for anything not yet contained (5 min)
5. Standard work notes (2 min)

Root-cause debate — the thing that was consuming half the old 45-minute meeting — is explicitly removed from this agenda and reassigned to whoever owns the investigation, outside the standup.

---

**User:** Will 15 minutes actually be enough once we stop debating root cause in the room?

**Assistant:** That's the working hypothesis behind this redesign, but it's untested at your line specifically — worth timing the first two weeks of the new format and confirming it holds, rather than assuming 15 minutes is the answer on paper alone.

---

**What this skill did:**
- Assessed the fabrication line's existing single-tier "daily standup" and identified three specific failure modes: lag-only metrics on the working board, a 45-minute unstructured meeting, and no response-to-abnormality protocol.
- Redesigned the format into a proper T1 (hourly, 15-minute) plus a new T2 review that now carries the lag metrics (output, scrap, OEE) that don't belong on T1.
- Added a four-step response-to-abnormality protocol with a draft escalation threshold, and referenced `standard-work` for the fab-step documentation this board now points to.

**What still needs a human:** The 85%-of-plan escalation threshold is a placeholder — the supervisor's knowledge of what's normal shift-to-shift variation on this line is what should set the real number, and it's the piece most likely to change the whole protocol if it's wrong.

**Suggested next step:** Run the new 15-minute standup format for two weeks and confirm with the supervisor whether it actually holds the time box once root-cause debate is removed from the room.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
