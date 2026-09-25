# Example: coaching an A3 through chronic scrap on an assembly line, left side before right side

**User:** We've got a scrap problem on our assembly line and I need to write this up as an A3 for the plant manager.

**Assistant:** Before you paste anything — leave out names of employees and anything your company treats as confidential; roles and initials are fine. Tell me the problem and who the A3 is for, and I'll coach it left to right — say *just draft it* any time and I'll draft from what you've given me.

**User:** It's for our plant manager, K. Scrap rate on the Line 3 sub-assembly has been running high for a couple months. Everyone says it's operator error on second shift.

**Assistant:** Let's build the left side first. Three questions:
1. What metric is off, and by how much — do you have a number and where it comes from?
2. Where in the process does it actually show up — which station or step?
3. What does "good" look like, with a date?

Also — "operator error" is where people stop looking, not where the cause usually is. We'll come back to that in root cause.

**User:** Scrap rate has been 6.8% for the last 6 weeks per the MES scrap log, versus a target of 2%. It shows up at the final crimp station. We'd want it back to 2% by end of next quarter.

**Assistant:** Good, that's enough for a solid Background and Goal. For Current Condition, do you have anything beyond the MES number — a Pareto by defect type, or has anyone watched the crimp station directly?

**User:** No one's watched it directly yet. We just have the MES totals by defect code — most are coded "crimp separation."

**Assistant:** That's real data, so I'll use it, and I'll tag the direct-observation gap as `[NEEDS GEMBA]` rather than guess at what's happening at the station. Let's talk root cause before countermeasures — walk me through why crimp separation happens, as far as you know it today.

**User:** Honestly the shift supervisor just says the second-shift crew isn't careful.

**Assistant:** That's a symptom claim, not a cause — I won't put "operator carelessness" in Section 4. Ask instead: what made a correct crimp harder to achieve than an incorrect one on second shift specifically? Is there anything different about second shift's tooling, parts lot, or crimp fixture versus first shift?

**User:** Actually — now that you ask, I think second shift got a batch of a different terminal supplier a few months back. Not certain.

**Assistant:** That's a real lead. I'll mark it `[CANDIDATE — verify at gemba]` since it isn't confirmed. That's enough for the left side — I'll draft now and mark what's unverified.

---

## A3: Line 3 Sub-Assembly Crimp Scrap

**1. Background**
Line 3 sub-assembly scrap has run 6.8% [from system: MES scrap log] over the last 6 weeks, against a 2% target, driven mostly by the "crimp separation" defect code. At current volume this represents a meaningful daily yield loss and rework burden [NEEDS GEMBA: rework hours/cost not yet quantified]. The plant manager, K., needs this resolved before next quarter's audit.

**2. Current Condition**
| Defect code | Share of scrap (last 6 weeks) | Source |
|---|---|---|
| Crimp separation | 71% | [from system: MES scrap log] |
| Other | 29% | [from system: MES scrap log] |

Crimp separation occurs at the final crimp station. No one has yet directly observed the station in operation — `[NEEDS GEMBA: observe crimp station both shifts, compare fixture setup]`.

**3. Goal / Target Condition**
Reduce Line 3 sub-assembly scrap rate from 6.8% [from system: MES scrap log] to 2% by end of next quarter (date: `[NEEDS GEMBA: confirm exact quarter-end date with K.]`).

**4. Root Cause Analysis**
Second shift reported a terminal supplier change several months ago `[CANDIDATE — verify at gemba]`. "Second-shift crew isn't careful" was raised but rejected as a root cause — it does not explain why crimp separation is concentrated on one shift's output, and it isn't something the team can act on directly. Candidate systemic cause: a terminal dimensional or plating difference between suppliers is causing marginal crimps that separate under vibration `[CANDIDATE — verify at gemba: pull terminal lot numbers against scrap timestamps]`.

### Right side — not started

Sections 5–8 (Countermeasures, Implementation Plan, Effect Confirmation, Follow-up) are not drafted. The root cause above is a candidate, not verified — starting countermeasures now would repeat the exact failure mode this skill exists to prevent. Verify the terminal-supplier hypothesis at gemba first.

---

**What this skill did:**
- Coached the left side of an A3 on Line 3 crimp scrap, using MES scrap-log data the user provided.
- Found a candidate root cause (terminal supplier change on second shift) after rejecting "operator carelessness" as unverifiable.
- Declined to draft the right side because the root cause is unverified — left side must be solid first.

**What still needs a human:**
- Verify whether the terminal-supplier change lines up with the scrap timestamps — pull lot numbers against the MES log.
- Direct observation of the crimp station on both shifts has not happened yet.
- Confirm the exact quarter-end target date with K.

**Suggested next step:** Have the second-shift lead, R., pull three days of terminal lot numbers and walk the crimp station with you before the next A3 review.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
