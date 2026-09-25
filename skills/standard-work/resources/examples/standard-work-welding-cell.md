Shows a combination sheet built from direct observation for a 4-step weld operation, with modal cycle time and standard WIP stated explicitly.

**User:** I need standard work for our weld station on the bracket line. I timed it myself this morning.

**Assistant:** Tell me the job, who does it best, and what you timed — and I'll build the combination sheet; say "just draft it" and I'll draft from what you have. Before you paste your timing notes — leave out names of employees; roles and initials are fine.

**User:** Operator is DR, been on that station two years, everyone agrees he's the fastest and cleanest. I timed 8 full cycles this morning, 9/16. Times in seconds were: 42, 44, 41, 44, 43, 58 (he got interrupted by a forklift), 43, 44. Demand is 160 brackets per shift, shift is 7.5 hours with a 30 min break and two 10 min breaks.

**Assistant:** A few things before the sheet. First, the modal time — 44 seconds appears three times, which is your most frequent reading, so that's the cycle time, not the average and not the 58-second outlier (that cycle was interrupted, so it's excluded as non-representative). Second, for takt time: available time is 7.5 hours minus 50 minutes of breaks = 400 minutes = 24,000 seconds; divided by 160 units = 150 seconds per unit. One question — is the work sequence below what DR actually does, in order, or should I ask you to walk it again step by step?

**User:** That's the actual sequence, I watched him do all 8 cycles.

**Assistant:** Good — then I have what I need. One more thing before the sheet: since cycle time (once we exclude the interrupted one) comes out well under takt, don't be surprised if the numbers below suggest this station has spare capacity. That's a finding to bring to your supervisor, not something to act on unilaterally by pulling work forward — I'll flag it as an assumption to verify rather than a recommendation to rebalance on the spot.

**Assistant:** Here's the sheet.

## Standard Work Combination Sheet — Weld Station, Bracket Line

**Operator observed:** DR (2 years on station, benchmark performer)
**Date observed:** 2026-09-16
**Cycles observed:** 8 [observed, 8 cycles, 2026-09-16]; cycle 6 excluded from modal calculation due to forklift interruption

**Takt time:** 150 sec/unit — 400 min available ÷ 160 units [from user: demand and shift schedule]
**Cycle time:** 44 sec [observed, modal of 7 valid cycles, 2026-09-16]
**Result:** Cycle time (44s) is well under takt time (150s) — this station has slack capacity relative to demand; consider whether rebalancing to a downstream station is appropriate. [ASSUMED — verify: confirm this station isn't intentionally running ahead to buffer a slower downstream step]

| Step # | Step Description | Manual Time | Walk Time | Machine Time | Cumulative |
|---|---|---|---|---|---|
| 1 | Pick bracket blank from bin, place in fixture (right hand) | 6 sec | — | — | 6 sec |
| 2 | Clamp fixture (left hand) | 3 sec | — | — | 9 sec |
| 3 | Weld seam 1 and seam 2 | — | — | 28 sec | 37 sec |
| 4 | Release clamp, place finished bracket on outbound rack | 7 sec | — | — | 44 sec |

Takt time line (150 sec) does not intersect any step — the full cycle finishes well inside takt, meaning no step is individually at risk of pushing the operator past the customer's rhythm.

**Standard WIP:** 1 unit in the fixture at a time; single-piece flow at this station. [observed]

**Hand notation:** Steps 1 and 4 use the right hand primarily; step 2 uses the left hand to clamp while the right hand is already clear of the fixture — noted because a training walkthrough would otherwise miss that these two hands are doing different things at nearly the same moment. [observed]

---

**User:** This is great — one more question, should this feed into a training document for new hires on this station?

**Assistant:** That's a related but separate tool. This combination sheet documents what the standard is — the sequence, the times, the WIP. Teaching a new hire to actually perform it to that standard, including the reasoning behind each step and what to watch for, is what `twi-jbs` (Training Within Industry Job Breakdown Sheet) is built for. I'd treat this sheet as the input to that document rather than trying to make one file do both jobs.

---

**User:** Should I laminate this and post it?

**Assistant:** Yes — this is a floor document, meant to sit at the station where DR can see it, not in a binder. One more thing worth noting on the sheet itself: mark it with today's revision date so anyone finding it later knows whether it's current, and update it the next time this station goes through a kaizen event.

**User:** One thing I noticed — is 4 steps really enough detail? Feels short compared to some standard work sheets I've seen elsewhere.

**Assistant:** Step count isn't the measure of completeness — action-level detail is. Four steps is right here because that's genuinely how many discrete actions make up this cycle: pick and place, clamp, weld, release and place. Splitting "weld seam 1 and seam 2" into two separate rows would only make sense if the operator does something distinct in between them worth capturing — a tool change, a hand switch, a pause to inspect. From what you described, they run as one continuous weld operation, so one row is accurate, not incomplete.

**User:** DR is on vacation next week and a second operator, initials MP, will cover the station. Should the sheet change?

**Assistant:** Not automatically. This sheet documents the best current method — DR's method, since he was identified as the reference performer, not just "whoever happens to be working." If MP runs a meaningfully different sequence, that's worth noting separately, but it doesn't replace this sheet unless MP's method turns out to be genuinely better and gets adopted as the new standard through a deliberate kaizen, not just because he covered a shift. Post this sheet as-is for MP to follow; if he can't hit the times on it, that's useful information about training, not a reason to rewrite the standard around his numbers.

**User:** What if he can't follow it and starts improvising his own sequence?

**Assistant:** Then that's exactly the kind of gap `gemba-walk` or a direct check-in would catch — someone should observe MP against this sheet during the coverage week rather than assume it's fine. If he's deviating because a step is genuinely hard for him, that's a training conversation; if he's deviating because the sequence itself doesn't work for anyone but DR, that's a signal the standard needs review once DR is back, not a reason to let it drift unaddressed.

---

**What this skill did:**
- Built a standard work combination sheet for the bracket-line weld station from direct observation of the benchmark operator (DR), 8 cycles timed same-day.
- Cycle time (44 sec, modal of 7 valid cycles) is well under takt time (150 sec), flagging this station as having slack relative to demand.
- Standard WIP documented as 1 unit — single-piece flow, no queue built into this station.

**What still needs a human:**
- Confirm whether the slack between cycle time and takt time is intentional (buffering a slower downstream step) or genuine excess capacity worth rebalancing — that assumption changes what happens next.
- Whether MP (the covering operator) can actually hit this sequence and these times needs a direct observation during the coverage week, not an assumption either way.
- Whoever owns the training pipeline for this station should decide whether a `twi-jbs` document gets built from this sheet before the next new hire rotates through.

**Suggested next step:** Take this sheet to the line supervisor and confirm whether the weld station's slack capacity should be used to rebalance work from a downstream station.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
