# Example: scoping a solder-defect problem statement with IS/IS-NOT, stripping cause language

**User:** I need a problem statement for solder bridging on our PCB line. It's because the operators aren't cleaning the stencil enough between prints.

**Assistant:** Before you paste any data — leave out names of employees and anything confidential; roles and initials are fine. Tell me what you're seeing — what, where, how often, since when — and I'll scope it and write the one sentence.

One thing up front: "operators aren't cleaning the stencil enough" is a cause, not an observation — I'm going to set that aside for now and come back to it as a hypothesis for root-cause work later, not put it in the problem statement.

**User:** Fair. We're seeing solder bridging on PCB-12 at Station 7. It's been going on about three weeks.

**Assistant:** Good, that's specific. Do you have a rate — a percentage or count — and does it happen on all shifts or lines, or just some?

**User:** Around 4% of units on Line 3, and it seems to only happen morning shift, not afternoon.

**Assistant:** That IS-NOT contrast (afternoon shift clean) is useful — it points toward something specific to morning shift setup, not the board or component itself. Let's build the table, then I'll write the sentence and check it against SMART.

## IS / IS-NOT

| Dimension | IS (observed) | IS NOT (not observed, but plausible) |
|---|---|---|
| Object | Solder bridging defects on PCB-12 | Other board types on the same line — not reported |
| Location | Line 3, Station 7 | Other stations on Line 3 — not reported |
| Time | Morning shift, past 3 weeks | Afternoon shift — clean [user estimate] |
| Magnitude | ~4% of units [user estimate] | Afternoon shift: near 0% [user estimate] |

**Assistant:** One more thing — you mentioned stencil cleaning as the cause. I'm setting that aside from the statement itself, but it's a good hypothesis to bring to `root-cause` once this statement is done, especially given the morning-only pattern.

**User:** Should I just write "stencil cleaning" into the problem statement so people know what to fix?

**Assistant:** I'd hold off — if we write the cause into the statement, whoever reads it will treat it as settled and stop looking. If the morning-only pattern turns out to be about warm-up time, humidity, or a first-run material difference instead of cleaning frequency, a statement that already names stencil cleaning has closed off those other leads before anyone checked them. Keep the statement to what's observed; bring the stencil-cleaning idea to root-cause as the first hypothesis to test, not as a settled fact.

---

## Problem Statement

> Solder bridging defects on PCB-12 are occurring at approximately 4% of units [user estimate] on Line 3, Station 7, morning shift only, over the past three weeks, against a target of [NEEDS GEMBA: confirm the defect rate target/spec with quality] .

## SMART validation

| Criterion | Result |
|---|---|
| Specific | Pass — names exact board (PCB-12), station (7), line (3), shift. |
| Measurable | Pass, with caveat — 4% is a user estimate, not yet a counted/system-confirmed rate. `[NEEDS GEMBA: pull actual solder-bridging counts from the AOI or inspection log for the past 3 weeks]` |
| Actionable | Pass — within Line 3's own team to investigate; the morning/afternoon contrast is something they control. |
| Relevant | Pass — quality/scrap and potential rework cost. |
| Time-bound | Pass — "past three weeks," morning shift only. |

The statement is directionally SMART but Measurable is flagged: the 4% figure should be confirmed against an actual count before this goes further, and a formal target/spec value is missing.

---

**What this skill did:**
- Scoped a solder-bridging complaint to a specific board, station, shift, and duration using IS/IS-NOT, and stripped out the stated cause ("operators aren't cleaning the stencil") rather than embedding it in the statement.
- Wrote a one-sentence problem statement and validated it against all five SMART criteria, flagging Measurable as needing a system-confirmed count.
- Preserved the stencil-cleaning hypothesis as a lead for root-cause work rather than discarding it.

**What still needs a human:**
- Pull the actual AOI or inspection log count for the past three weeks — the 4% figure is a user estimate, not yet confirmed.
- Confirm the formal defect-rate target/spec with quality — none was given.
- Confirm the afternoon-shift contrast is real and not just an impression, before treating it as a lead.

**Suggested next step:** Have the Line 3 quality technician pull three weeks of AOI solder-bridging counts split by shift before bringing this to root-cause analysis.

**On the stencil-cleaning hypothesis:** it is a reasonable first thing to check once root-cause work starts, precisely because the morning-only pattern points at something specific to shift start-up. But it should be tested against the data, not assumed — a stencil-cleaning fix that doesn't address the real cause would leave the 4% rate in place while looking resolved on paper.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
