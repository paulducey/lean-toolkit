# Example: scoping a delivery-performance problem to shift and route, rejecting a too-broad opening claim

**User:** Our deliveries are always late. Need a problem statement for this.

**Assistant:** Before you share any data — leave out names of employees and anything confidential; roles and initials are fine. Tell me what you're seeing — what, where, how often, since when — and I'll scope it and write the one sentence.

"Deliveries are always late" is too broad to act on — it would produce a root cause too broad to fix. Let's narrow it. Do late deliveries happen on all routes, or particular ones? All times of day?

**User:** Now that you mention it — it's really the second-shift route to the east distribution center. The morning routes are basically fine.

**Assistant:** That's the scope. Do you have a rate or count, and since when?

**User:** Over the last month, about 30% of east-route second-shift deliveries have missed their scheduled window, versus maybe 5% for the same route on first shift.

**Assistant:** That contrast — same route, different shift, very different rate — is exactly the kind of IS-NOT signal that narrows where the cause lives. Let's build the table.

## IS / IS-NOT

| Dimension | IS (observed) | IS NOT (not observed, but plausible) |
|---|---|---|
| Object | East distribution center route deliveries | Other routes — not reported as a problem |
| Location | East route, second shift | East route, first shift — ~5% miss rate [user estimate] |
| Time | Past month | `[Unknown]` — no data on whether this predates the past month |
| Magnitude | ~30% missed window [user estimate] | First shift, same route: ~5% [user estimate] |

**Assistant:** Good — the scope is now narrow enough to investigate. I won't guess at why second shift differs (that's for root-cause work), but I'll flag it as the obvious lead.

**User:** My manager keeps saying it's because the second-shift drivers are slower. Should that go in the statement?

**Assistant:** No — that's a cause claim about people, not an observation, and it's exactly the kind of thing that ends analysis before it starts. If I write "second-shift drivers are slower" into the problem statement, it reads as settled, and nobody will ask what's actually different about second shift's load times, routing, or dispatch timing. Keep the statement to the observed rate gap; bring "drivers are slower" to root-cause as a claim to test, not a fact to record — and root-cause will likely ask what would make any driver slower on that shift specifically, not just this one.

---

## Problem Statement

> East distribution center deliveries on the second-shift route are missing their scheduled delivery window at approximately 30% [user estimate] over the past month, against a first-shift rate of approximately 5% [user estimate] on the same route, and a target of on-time delivery [NEEDS GEMBA: confirm the formal on-time-delivery target with the logistics manager].

## SMART validation

| Criterion | Result |
|---|---|
| Specific | Pass — names the exact route (east DC), shift (second), and contrasts against first shift. |
| Measurable | Pass, with caveat — both the 30% and 5% figures are user estimates; `[NEEDS GEMBA: pull actual on-time delivery percentages from the dispatch/TMS system for both shifts over the same period]` |
| Actionable | Pass — within the logistics team's scope to investigate (staffing, routing, load times on second shift). |
| Relevant | Pass — customer delivery commitment and downstream cost. |
| Time-bound | Pass — "past month," with the caveat that how far back the pattern goes is unconfirmed. |

The original framing ("deliveries are always late") failed Specific and Actionable — it named no route, shift, or scope. The narrowed version passes all five, contingent on confirming the estimated rates against system data.

---

**What this skill did:**
- Rejected "deliveries are always late" as too broad, and narrowed it with the user to the east-route, second-shift pattern using IS/IS-NOT.
- Wrote a one-sentence problem statement built on the shift-vs-shift contrast, and validated it against SMART, flagging Measurable as resting on user estimates.
- Left the "why second shift differs" question explicitly open for root-cause work rather than guessing.

**What still needs a human:**
- Pull actual on-time delivery percentages from the dispatch/TMS system for both shifts over the same period — the 30%/5% figures are estimates.
- Confirm the formal on-time-delivery target with the logistics manager.
- Confirm how far back this pattern goes — the scoping only covers the past month.

**Suggested next step:** Have the dispatch supervisor pull one month of on-time-delivery data split by shift for the east route before this goes to root-cause analysis.

**On the "drivers are slower" claim:** it's worth testing, not repeating as fact. A defensible root-cause pass would compare load times, dispatch timing, and route conditions between the two shifts before concluding anything about driver pace — otherwise the fix stops at "manage the drivers harder," which rarely holds.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
