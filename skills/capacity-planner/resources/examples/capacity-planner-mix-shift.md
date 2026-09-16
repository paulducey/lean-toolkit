Shows: a three-product mixed-model line where a product mix shift moves the bottleneck from Station 2 to Station 4 with total volume unchanged, built with "just build it" from the data given, and referring out to smed-setup and oee-from-csv for the levers this skill doesn't calculate itself.

**User:** Just build it from what I've got, I don't have time for a bunch of back-and-forth right now. Four-station line, three products A, B, C. Demand is 500 units/shift total, shift available time is 450 minutes. Cycle times by station and product, in seconds:

Station 1: A 40, B 42, C 45
Station 2: A 58, B 60, C 58
Station 3: A 35, B 38, C 44
Station 4: A 30, B 50, C 95

Current mix: 60% A, 30% B, 10% C. We're considering shifting to 30% A, 30% B, 40% C next quarter — same total 500 units/shift, just a different split.

**Assistant:** Working from what you've given me — process times, headcount, and demand are fine to share; just leave out anything product-specific that's sensitive.

**Takt time:** 450 min × 60 = 27,000 sec/shift available `[observed]`, 500 units/shift demand `[observed]`
Takt = 27,000 ÷ 500 = **54.00 sec/unit** — same for both mixes, since total volume is unchanged.

**Current mix (60% A / 30% B / 10% C) — blended cycle time per station:**

Station 1: 0.60×40 + 0.30×42 + 0.10×45 = 24.0 + 12.6 + 4.5 = **41.1 sec**
Station 2: 0.60×58 + 0.30×60 + 0.10×58 = 34.8 + 18.0 + 5.8 = **58.6 sec**
Station 3: 0.60×35 + 0.30×38 + 0.10×44 = 21.0 + 11.4 + 4.4 = **36.8 sec**
Station 4: 0.60×30 + 0.30×50 + 0.10×95 = 18.0 + 15.0 + 9.5 = **42.5 sec**

| Station | Blended Cycle (sec) | Takt (sec) | Ratio | Status |
|---|---|---|---|---|
| 1 | 41.1 | 54.00 | 0.76 | OK |
| 2 | 58.6 | 54.00 | **1.09** | **CONSTRAINT** |
| 3 | 36.8 | 54.00 | 0.68 | OK |
| 4 | 42.5 | 54.00 | 0.79 | OK |

**Bottleneck today: Station 2** (ratio 1.09).
System capacity = 27,000 ÷ 58.6 = **460 units/shift**. Gap to the 500-unit demand = 40 units/shift, 8% short.

**Planned mix (30% A / 30% B / 40% C) — blended cycle time per station:**

Station 1: 0.30×40 + 0.30×42 + 0.40×45 = 12.0 + 12.6 + 18.0 = **42.6 sec**
Station 2: 0.30×58 + 0.30×60 + 0.40×58 = 17.4 + 18.0 + 23.2 = **58.6 sec**
Station 3: 0.30×35 + 0.30×38 + 0.40×44 = 10.5 + 11.4 + 17.6 = **39.5 sec**
Station 4: 0.30×30 + 0.30×50 + 0.40×95 = 9.0 + 15.0 + 38.0 = **62.0 sec**

| Station | Blended Cycle (sec) | Takt (sec) | Ratio | Status |
|---|---|---|---|---|
| 1 | 42.6 | 54.00 | 0.79 | OK |
| 2 | 58.6 | 54.00 | 1.09 | CONSTRAINT (unchanged) |
| 3 | 39.5 | 54.00 | 0.73 | OK |
| 4 | 62.0 | 54.00 | **1.15** | **CONSTRAINT (new leader)** |

**The bottleneck moves from Station 2 to Station 4** even though total volume is unchanged — Station 2's blended time happens to stay exactly the same (product C runs at 58 sec there, same as A), but product C is much slower at Station 4 (95 sec vs. 30–50 for A/B), and raising C's share from 10% to 40% pushes Station 4 past Station 2.

New system capacity = 27,000 ÷ 62.0 = **435 units/shift**. Gap to 500-unit demand widens to 65 units/shift, 13% short — worse than today, purely from the mix shift.

**Two things worth running before deciding how to close this gap, not something this analysis calculates itself:**
- Station 4's 95-second time for product C may include changeover-related time if C requires a tooling change other products don't — run `smed-setup` on that station's C-changeover before assuming 95 seconds is all cycle time.
- Whether Station 4's cycle times above reflect real availability (including minor stops) or a theoretical rate — pull `oee-from-csv` on Station 4 to confirm the 95-second figure holds up under actual run conditions, not just a rate card.

**The assumption that matters most:** if product C's 95-second time at Station 4 is overstated — say it's really closer to A and B's range — the bottleneck might not move at all. **Confirming that number against an actual timed run is [NEEDS GEMBA]** before committing to a fix aimed at Station 4.

---

**What this skill did:**
- Calculated takt (54.00 sec/unit, unchanged by the mix shift) and blended station cycle times for both the current and planned product mix.
- Found the bottleneck moves from Station 2 (ratio 1.09) to Station 4 (ratio 1.15) purely from the mix shift, with total volume held constant — system capacity drops from 460 to 435 units/shift.
- Flagged that Station 4's 95-second product-C time should be checked against `smed-setup` (changeover content) and `oee-from-csv` (real vs. theoretical availability) before planning a fix there.

**What still needs a human:**
- Whether Station 4's 95-second cycle time for product C is a timed, current-state number or a theoretical rate — this is the single assumption that would most change which station gets the improvement effort. [NEEDS GEMBA]
- Whether any of that 95 seconds is changeover time that `smed-setup` could recover.
- Confirming the 30/30/40 planned mix is final before committing capital or labor to Station 4.

**Suggested next step:** Have someone time an actual product-C run at Station 4 with a stopwatch and compare it against the 95-second figure before deciding where to invest ahead of the mix shift.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
