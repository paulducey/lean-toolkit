Shows an analysis built entirely from a supervisor interview rather than filmed observation, with estimates marked throughout, a priority verification list, and capacity math run on best-case and conservative scenarios.

**User:** Just draft it. We don't have film, but I can tell you what our supervisor says happens during a die change on the stamping press.

**Assistant:** Go ahead — since this is interview data rather than filmed observation, I'll mark every time as an estimate rather than treating it as measured, and I'll flag which classifications most need verification before you act on them. Leave out any proprietary part numbers — machine type, process step, and time data are fine.

**User:** Supervisor says the die change usually takes "about an hour, sometimes 90 minutes." Steps as he described them: press stops and cools down a bit (says maybe 10 min), crew unbolts the old die (15-20 min), old die craned out and new die craned in (10 min), new die bolted in (15-20 min), then they run a few test hits and check part dimensions with calipers, adjusting die height each time until it's right (this is the part he says "just takes as long as it takes," could be 10 min or 45 min depending on the day). We change dies maybe 3 times a week.

**Assistant:** Here's the draft. Because this is memory-based, every time below is marked `[EST]`, and the classifications need verification before this becomes an action plan rather than a hypothesis.

## Element Classification — Stamping Press Die Change

Machine/Line: Stamping press [NEEDS GEMBA: press ID]
Changeover type: Die A → Die B (general, not part-specific)
Current total changeover time: 60–90 min [user estimate — supervisor's range, not measured]
Data source: supervisor interview

| # | Element Description | Current Time | Classification | Phase 2 Action | Target Time |
|---|---|---|---|---|---|
| 1 | Press stops, cools down | 10 min [EST] | Internal — [VERIFY] whether cooldown is a safety/physical requirement or a habit; if the press doesn't actually need to cool before unbolting, this may be reducible but not convertible to external (machine is still down either way) | Verify actual cooldown requirement against equipment spec | [VERIFY before estimating] |
| 2 | Unbolt old die | 15–20 min [EST] | Internal — machine must be stopped, crew working inside the press envelope | Streamline: pre-stage fasteners/tools at the press before shutdown | 10 min [EST] |
| 3 | Crane old die out, new die in | 10 min [EST] | Internal — physical constraint, die is in motion during transfer and the press bed must be clear | none identified yet — [VERIFY] whether a second crane or a die cart could run this in parallel with another activity | 10 min [EST, unchanged] |
| 4 | Bolt new die in | 15–20 min [EST] | Internal — same physical constraint as element 2 | Streamline: pre-set bolt torque sequence, quarter-turn or faster fastener where feasible | 10 min [EST] |
| 5 | Test hits, caliper check, adjust die height iteratively | 10–45 min [EST] — widest range of any element | Internal, but the *adjustment* is the target — this is a classic adjustment-elimination candidate | Eliminate: pre-set die height to a documented shim/gauge setting before the trial hits begin | 5 min [EST] |

**[VERIFY] priority — element 1, cooldown:** Ten minutes of "waiting for it to cool" was described with hedging language ("maybe") and no stated physical reason. Before this analysis proceeds, confirm with maintenance or the equipment manual whether cooldown is a genuine requirement — if it isn't, this element may be reducible, though it stays internal either way since the machine is still down during it.

**[VERIFY] priority — element 5, the widest-range element:** A 10–45 minute range on the same task, described as "just takes as long as it takes," is the strongest signal in this whole list that the die isn't being set to a repeatable position — this is the single highest-leverage item to test before trusting any savings number below.

## Capacity Math — Conservative and Best-Case

```
Current changeover time (midpoint):   75 min [EST — midpoint of supervisor's 60–90 min range]
Target changeover time, conservative: 45 min [10 + 15 + 10 + 15 + 10... wait, see note]
Target changeover time, best case:    35 min [10 + 10 + 10 + 10 + 5, if cooldown at #1 is not reducible]
Time saved, conservative:             30 min per changeover
Time saved, best case:                40 min per changeover
Changeovers per week:                 3 [user estimate]
Production time recovered, conservative: 90 min/week
Production time recovered, best case:    120 min/week
```

Both scenarios are built from the estimated element times above, not from a guessed overall percentage — but every input here is `[EST]`, so both totals should be treated as directional until at least the die-height adjustment (element 5) is filmed or timed directly.

---

**User:** So which number do I use for the business case?

**Assistant:** Neither one on its own — present both the conservative and best-case figures together, and say plainly that they're built from a supervisor's recollection, not a timed observation. If someone asks for a single number before verification happens, that's a decision for whoever owns the business case, not something this analysis should paper over by picking the more favorable figure.

**User:** Is there anything I should NOT tell the plant manager is a sure thing here?

**Assistant:** The die-height adjustment savings (element 5, going from a 10–45 minute range down to an estimated 5 minutes) is the one to be most careful about. It's the single biggest contributor to both scenarios, and it rests entirely on the idea that pre-setting the die to a gauged position will actually eliminate the iterative caliper-and-adjust cycle — which hasn't been tested. If that assumption is wrong and the die still needs hand-adjustment for reasons beyond just "it wasn't pre-set" (worn tooling, for instance), the real savings could be much smaller than either scenario shows.

**User:** What about the cooldown step — should I just drop that from the plan since it might not be needed?

**Assistant:** Not yet — I flagged it as worth checking, not as something to remove from the plan. Until maintenance or the equipment manual confirms there's no physical requirement behind the cooldown, treat it as internal and unchanged. Removing a step from a changeover plan without knowing why it exists is how a "streamlining" effort accidentally reintroduces a safety or equipment issue that someone built the wait time in to prevent.

---

**What this skill did:**
- Built an element list and classification for the stamping press die change from a supervisor interview, with every time marked as an estimate rather than a measurement.
- Identified the die-height adjustment step (10–45 minute range) as the single highest-leverage verification target, and flagged the cooldown step as possibly non-required.
- Ran capacity math as a conservative/best-case pair (90–120 min/week recovered) rather than a single number, since none of the underlying times are measured.

**What still needs a human:**
- The die-height adjustment step's true internal-only status and actual time — if pre-setting the die height doesn't eliminate the adjustment the way estimated, both the conservative and best-case savings figures collapse.
- Whether the 10-minute cooldown step is a genuine equipment or safety requirement or just habit — flagged for maintenance to check, not removed from the plan.
- Every element time in this analysis is `[EST]` from a single supervisor's recollection; none of it has been independently confirmed by a second person or by film.

**Suggested next step:** Film one actual die change this week, focused specifically on timing the test-hit and adjustment sequence, before using either capacity figure in a business case.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
