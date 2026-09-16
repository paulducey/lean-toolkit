# Example: narrowing "machine downtime" from a broad complaint to a specific failure mode, escape hatch used

**User:** Just draft it — machine downtime on our CNC line is killing us.

**Assistant:** One line first — leave out names of employees and anything confidential when you share anything further; roles and initials are fine. "Machine downtime is killing us" is too broad to draft a usable statement from — I'll draft what I can now and mark the gaps rather than invent a rate or a machine.

**User:** It's mostly Mill 2. Breaks down a few times a week.

**Assistant:** That's a start — I'll use it, but "a few times a week" and "breaks down" aren't yet a rate or a specific failure mode. I'll draft with placeholders for what's missing.

**User:** Can't you just say it's the spindle? That's usually what it is on these machines.

**Assistant:** I won't put "spindle" in the statement — that would be the tool's general idea of how a mill like this usually fails, not something anyone has actually confirmed on Mill 2. If I write it in, whoever reads this statement will treat the failure mode as known and skip the CMMS pull that would tell us for certain — and if it turns out to be a fixture or coolant issue instead, the whole downstream analysis is aimed at the wrong thing. I'll leave the failure mode as a gap to fill from the maintenance log.

---

## IS / IS-NOT

| Dimension | IS (observed) | IS NOT (not observed, but plausible) |
|---|---|---|
| Object | Mill 2 | Other mills on the CNC line — `[Unknown]`, not reported as a problem |
| Location | CNC line, Mill 2 | `[Unknown]` — no station-level detail given |
| Time | "A few times a week" [user estimate] | `[Unknown]` — no baseline period stated |
| Magnitude | `[Unknown — go look]` — no rate, count, or duration given | `[Unknown]` |

The IS-NOT column is nearly empty — a sign the scope is still too broad to act on. In particular, no failure mode (spindle fault, tool break, fixture jam, alarm code) has been named yet.

## Problem Statement (draft)

> Mill 2 on the CNC line experiences unplanned downtime events at a frequency of approximately "a few times a week" [user estimate], failure mode [NEEDS GEMBA: pull the maintenance/CMMS log for Mill 2 downtime events and alarm codes over the last 4–6 weeks], since [NEEDS GEMBA: confirm when this pattern started or whether it has always been this way], against a target of [NEEDS GEMBA: confirm the acceptable downtime target with the maintenance or production manager].

## SMART validation

| Criterion | Result |
|---|---|
| Specific | Fail — no failure mode named yet; "breaks down" could be five different mechanisms with five different fixes. |
| Measurable | Fail — "a few times a week" is not a counted baseline. `[NEEDS GEMBA: pull actual downtime event count and total minutes from the CMMS or MES for Mill 2]` |
| Actionable | Pass, tentatively — within the maintenance/production team's scope once the failure mode is known. |
| Relevant | Pass — downtime affects throughput and cost. |
| Time-bound | Fail — no start date or baseline period given. |

This statement fails three of five SMART criteria as drafted. It is not ready for root-cause analysis — the scope needs the CMMS pull before drilling further, or the fishbone in `root-cause` will spend the first hour just re-deriving what a data pull would give in five minutes.

---

**What this skill did:**
- Drafted a problem statement immediately on "just draft it," from a genuinely broad complaint ("machine downtime is killing us") narrowed only as far as "Mill 2."
- Validated against SMART and found it fails Specific, Measurable, and Time-bound — stated this plainly rather than smoothing over the gaps to make the sentence read well.
- Did not invent a failure mode, rate, or start date to complete the picture.

**What still needs a human:**
- Pull the CMMS/maintenance log for Mill 2 covering the last 4–6 weeks — this is the single blocking gap; without it there is no real failure mode or rate.
- Confirm when this downtime pattern started, or whether it has always been roughly this frequent.
- Confirm the acceptable downtime target with the maintenance or production manager.

**Suggested next step:** Have the maintenance lead pull Mill 2's downtime event log (with alarm codes if available) for the last 4–6 weeks before this problem statement is used for root-cause work.

**On the spindle guess:** it may well turn out to be right, but it should come from the alarm codes, not from what's typical on similar mills. Writing an unconfirmed failure mode into a problem statement is the same trap as writing an unconfirmed cause into it — it looks specific without actually being known, and it can send root-cause work down the wrong path for a week before anyone checks the log.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
