Shows a material handler's kitting route documented with separated walk time and manual time, and a "just draft it" request producing placeholders for untimed steps.

**User:** Just draft it. Kitting route for the line-side material handler, I don't have great timing data yet.

**Assistant:** Leave out names of employees before you paste anything — roles and initials are fine. Go ahead with what you have, and I'll mark anything untimed rather than guess at it.

**User:** Handler (materials role, one FTE) walks a fixed loop: stockroom, then stations 1 through 4, then back to stockroom. I know the stockroom pick takes about 90 seconds because I've watched it a few times, roughly. I have no real timing on the walk segments or the drop-offs. Demand is one kit per station every 12 minutes, 4 stations, 8-hour shift with a 30-minute lunch and one 15-minute break.

**Assistant:** Here's the draft. Since walk and drop-off segments weren't timed, I'm marking those `[NEEDS GEMBA: time this step]` rather than estimating them — filling them from general practice would be a fact I don't have. One thing to flag up front: with only one of ten segments timed, this sheet is really a route map with one confirmed data point, not a working combination sheet yet — I'd treat what follows as the skeleton to fill in, not something to laminate and post as-is.

## Standard Work Combination Sheet — Line-Side Kitting Route

**Operator:** Material handler (materials role, 1 FTE)
**Date drafted:** 2026-09-16 — draft only, pending timing
**Cycles observed:** 0 formally timed; stockroom pick time from repeated casual observation [user estimate]

**Takt time:** 3 min/kit-station-cycle — 445 min available (480 min shift − 30 min lunch − 15 min break — this reflects one continuous loop covering all 4 stations, so takt is calculated per station visit: 445 min ÷ (4 stations × 1 kit per 12 min ÷ 12 min... — restated below) [ASSUMED — verify: confirm whether takt should be calculated per full loop or per station drop]

Restated more simply: each station needs a kit every 12 minutes, 4 stations, so the route must complete one full loop within 12 minutes to keep every station supplied without a station waiting. **Takt time for the full loop = 12 min = 720 sec.** [from user: demand]

**Cycle time:** [NEEDS GEMBA: time the full loop end to end, at least 5 cycles] — cannot state a modal cycle time without observation.

| Step # | Step Description | Manual Time | Walk Time | Machine Time | Cumulative |
|---|---|---|---|---|---|
| 1 | Pick kit components at stockroom | 90 sec [user estimate, casual repeated observation] | — | — | 90 sec |
| 2 | Walk stockroom → Station 1 | [NEEDS GEMBA: time this step] | [NEEDS GEMBA] | — | — |
| 3 | Drop kit at Station 1 | [NEEDS GEMBA: time this step] | — | — | — |
| 4 | Walk Station 1 → Station 2 | [NEEDS GEMBA: time this step] | [NEEDS GEMBA] | — | — |
| 5 | Drop kit at Station 2 | [NEEDS GEMBA: time this step] | — | — | — |
| 6 | Walk Station 2 → Station 3 | [NEEDS GEMBA: time this step] | [NEEDS GEMBA] | — | — |
| 7 | Drop kit at Station 3 | [NEEDS GEMBA: time this step] | — | — | — |
| 8 | Walk Station 3 → Station 4 | [NEEDS GEMBA: time this step] | [NEEDS GEMBA] | — | — |
| 9 | Drop kit at Station 4 | [NEEDS GEMBA: time this step] | — | — | — |
| 10 | Walk Station 4 → Stockroom | [NEEDS GEMBA: time this step] | [NEEDS GEMBA] | — | — |

**Standard WIP:** [NEEDS GEMBA] — likely 1 kit per station between drops, but this needs confirmation against how many kits the handler stages ahead of the loop, if any.

**Preliminary check:** Only the stockroom pick (90 sec) is timed; that alone is 12.5% of the 720-second loop takt. The remaining 87.5% of the loop — four walk segments and four drop-offs — is unmeasured. No conclusion about whether this route meets takt can be drawn yet.

---

**User:** Okay, I'll get someone to time the walk segments this week.

**Assistant:** Good — once you have those, send the times and I'll fill in the modal values and calculate whether the full loop fits inside the 12-minute takt. Until then, treat every blank cell above as unverified, not as zero.

**User:** Who should actually do the timing — should it be the handler themselves, or someone watching them?

**Assistant:** A separate observer watching the handler run the loop is more reliable than the handler self-timing — self-timed cycles tend to compress under the pressure of being measured, or the handler unconsciously changes pace. Time at least 5 full loops, ideally on different days if the route varies by which stations are running which models that day, and note the modal time for each segment rather than the average — the same rule that applies to any cycle-time measurement in this toolkit.

**User:** What if the times come back and the loop doesn't fit inside 12 minutes?

**Assistant:** Then the route as designed can't keep every station supplied without one of them waiting — that's a real finding, not a failure of the sheet. The next step in that case is usually one of: reduce the loop's walk distance (relocate the stockroom or restage material closer to the stations), split the loop between two handlers, or reconfirm the 12-minute demand figure is actually right. I wouldn't recommend any of those changes now, though — that's premature until the actual times come back.

**User:** You marked standard WIP as [NEEDS GEMBA] too — why can't you just say it's 1 kit per station?

**Assistant:** Because I don't actually know how many kits the handler stages ahead of the loop versus delivering one at a time as they pass each station. If the handler pre-builds two kits before leaving the stockroom and drops one, then continues with a spare on the cart, standard WIP could be 2, not 1 — and that changes what "the minimum needed to avoid waiting" actually is at each station. Saying 1 without checking would be a guess dressed up as a documented fact, which is exactly what this toolkit's numbers aren't supposed to do.

---

**What this skill did:**
- Drafted a standard work combination sheet skeleton for the line-side kitting route from a single timed segment (the 90-second stockroom pick) and the stated demand.
- Calculated the loop takt time (720 sec) from shift schedule and one-kit-per-12-minutes demand, but could not state a cycle time — 9 of 10 route segments are untimed.
- Flagged that only 12.5% of the loop is currently measured; no conclusion about whether the route meets takt is possible yet.

**What still needs a human:**
- Time the four walk segments and four drop-off actions — at least 5 cycles each, modal value — before this sheet can be treated as anything but a placeholder.
- Confirm whether the 12-minute-per-station demand figure is itself current, or whether it should be re-checked against the schedule before locking in the loop takt.
- Decide who does the timing — a separate observer is recommended over the handler self-timing, per the note above.

**Suggested next step:** Have the materials supervisor time the full kitting loop for at least 5 cycles this week, using a separate observer rather than the handler self-timing, and send the results back to complete the sheet.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
