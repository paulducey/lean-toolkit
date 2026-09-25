# Example: coaching an A3 through recurring on-time delivery misses in a fabrication cell, escape hatch used

**User:** Just draft it. Our fab cell keeps missing on-time delivery to the paint line and I need an A3 for the value stream review tomorrow.

**Assistant:** Got it — one thing before I draft: leave out names of employees and anything the company treats as confidential; roles and initials are fine. I'll draft all eight sections now from what you've given me and mark anything I don't know as `[NEEDS GEMBA]`. Tell me what you do have — a number, a date range, anything.

**User:** On-time delivery from the fab cell to paint has been below 90% for about 5 weeks. Target is 98%. Cell lead is J.

**Assistant:** That's enough to start. Before I draft — even on "just draft it," I want to flag one thing rather than silently paper over it: you haven't told me *why* deliveries are missing, and I'm not going to guess at a cause to make Section 4 look complete. I'll draft the whole A3 now, but Root Cause and everything to its right will carry `[NEEDS GEMBA]` rather than an invented mechanism.

**User:** That's fine, I know it's rough — the review is just to get the team looking at this seriously.

**Assistant:** Understood — that's actually a reasonable use of a mostly-yellow-tag A3. It's the to-do list for the floor, not a finished analysis. Drafting now.

---

## A3: Fab Cell → Paint On-Time Delivery

**1. Background**
On-time delivery from the fab cell to the paint line has run below 90% [user estimate] for approximately 5 weeks, against a target of 98%. Late delivery to paint risks starving the paint line and pushing schedule pressure downstream `[NEEDS GEMBA: confirm downstream impact — has paint actually gone idle, or is this a near-miss so far]`.

**2. Current Condition**
`[NEEDS GEMBA: pull the actual weekly on-time percentages and a Pareto of which part numbers or shifts are missing most often — a single "below 90%" estimate is not enough to show where in the process the problem occurs]`. No process map or run chart is available yet.

**3. Goal / Target Condition**
Raise fab cell → paint on-time delivery from below 90% [user estimate] to 98% by `[NEEDS GEMBA: confirm target date with cell lead J. and the value stream owner]`.

**4. Root Cause Analysis**
Not yet started — no current-condition data exists to trace a cause back to. `[NEEDS GEMBA: this section cannot be drafted responsibly until Section 2 has real data; do not skip to countermeasures]`. When data is available, do not accept these as final answers — ask the systemic question instead:

- "The cell falls behind" → ask what specifically causes it to fall behind: changeover, starved input, machine reliability, or staffing.
- "Operators run late" → ask what made running on time harder than running late — a symptom claim about people is never a root cause here.
- "It's always been like this" → ask what changed, or whether it has simply never been measured before now.

### Right side — not started

Sections 5–8 are placeholders only. Countermeasures cannot be drafted responsibly without a verified root cause, and no root cause work has happened yet — only an estimate of the symptom. Presenting countermeasures tomorrow without this would be presenting a guess as a plan.

**5. Countermeasures:** `[NEEDS GEMBA: pending root cause]`
**6. Implementation Plan:** `[NEEDS GEMBA: pending root cause]`
**7. Effect Confirmation:** Will use the same on-time-delivery metric as Section 3 once real data exists.
**8. Follow-up / Standardize:** `[NEEDS GEMBA: pending root cause]`

---

**What this skill did:**
- Drafted all eight A3 sections on request ("just draft it") from a single estimated figure (below 90%, 5 weeks).
- Found the current condition and root cause cannot honestly be completed without real data — flagged rather than invented a Pareto or a cause.
- Left the right side as explicit placeholders rather than filling it with plausible-sounding countermeasures.

**What still needs a human:**
- Pull the actual weekly on-time percentages and a breakdown by part number or shift before the review — the "below 90%" figure is a placeholder for real data.
- Confirm whether paint has actually gone idle or this is a near-miss.
- No root cause work has happened; this A3 is not ready to present countermeasures tomorrow — say so at the review rather than presenting a guess.

**Suggested next step:** Have J., the cell lead, pull five weeks of on-time data from the scheduling system before the review, and walk the review with Section 2 still open rather than presenting invented countermeasures.

**A note on framing for tomorrow:** presenting an A3 that is mostly `[NEEDS GEMBA]` tags is not a weak showing — it is an honest one. A polished-looking A3 built on a single estimated percentage and no cause data would look better in the room and be worth less. The value of tomorrow's review is getting the team to agree that Section 2 needs real data before anyone commits to a fix, not walking out with a countermeasure that addresses a guess.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
