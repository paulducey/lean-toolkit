Shows: a five-station assembly line where machine and labor cycle times are tracked separately, a labor-constrained bottleneck at Station 3 that a machine-only view would miss, and two what-if scenarios — a 15% demand increase and a one-operator headcount reduction reported as capacity freed/lost, closing with the leadership-decision sentence exactly once.

**User:** Can you tell if we can hit our volume on the bracket line? Five stations, one operator each. Shift is 480 minutes with 30 minutes of breaks. Demand is 400 units/shift.

Machine cycle time / labor content per station, in seconds:
Station 1: machine 50, labor 40
Station 2: machine 60, labor 55
Station 3: machine 45, labor 78
Station 4: machine 65, labor 50
Station 5: machine 55, labor 45

**Assistant:** Process times, headcount, and demand figures are fine to share — just leave out proprietary product specs or customer-identifying information, which you already have.

**Takt time:**
Available time = 480 − 30 = 450 min/shift = 27,000 sec/shift `[observed]`
Takt = 27,000 ÷ 400 = **67.5 sec/unit**

**Station loading** — station cycle time is the larger of machine and labor time at each station, since whichever is slower sets the pace:

| Station | Machine (sec) | Labor (sec) | Station Cycle (sec) | Takt (sec) | Ratio | Status |
|---|---|---|---|---|---|---|
| 1 | 50 | 40 | 50 | 67.5 | 0.74 | OK |
| 2 | 60 | 55 | 60 | 67.5 | 0.89 | At risk |
| 3 | 45 | 78 | **78** | 67.5 | **1.16** | **CONSTRAINT** |
| 4 | 65 | 50 | 65 | 67.5 | 0.96 | At risk |
| 5 | 55 | 45 | 55 | 67.5 | 0.81 | OK |

**Bottleneck: Station 3, ratio 1.16.** This one's worth flagging specifically — the machine at Station 3 only needs 45 seconds, well under takt, so a machine-only view would call this station fine. The operator's 78 seconds of labor content is what's actually constraining it. This is labor-constrained, not machine-constrained, and faster equipment wouldn't fix it — the fix is reducing labor content or adding help at that station.

**System capacity** = 27,000 ÷ 78 = **346 units/shift** (bottleneck-governed)
**Capacity gap** = 400 − 346 = **54 units/shift short**, or 13.5% of required demand.

**Options to close the gap**, ordered by speed and investment:
1. Reduce labor content at Station 3 — rebalance a work element to a lower-loaded station (Station 1, at 0.74, has the most slack), or look for a `smed-setup`-style reduction if any of that 78 seconds is changeover-related.
2. Add a second operator at Station 3 for the highest-content elements, splitting the 78 seconds of work.
3. Capital option — semi-automate the manual portion of Station 3's work content.

**User:** What if demand goes up 15%? And separately — what happens if we pull one operator off Station 2?

**Assistant:** Running both, one at a time, from scratch.

**Scenario 1 — 15% demand increase:**
New demand = 400 × 1.15 = 460 units/shift
New takt = 27,000 ÷ 460 = **58.70 sec/unit**

| Station | Station Cycle (sec) | New Takt (sec) | New Ratio | Status |
|---|---|---|---|---|
| 1 | 50 | 58.70 | 0.85 | At risk |
| 2 | 60 | 58.70 | 1.02 | CONSTRAINT |
| 3 | 78 | 58.70 | 1.33 | CONSTRAINT |
| 4 | 65 | 58.70 | 1.11 | CONSTRAINT |
| 5 | 55 | 58.70 | 0.94 | At risk |

The bottleneck stays Station 3, but it gets worse (1.16 → 1.33), and Stations 2 and 4 cross over 1.00 as well — a 15% demand bump turns a one-station problem into a three-station problem. **The assumption that matters most here is the 400-unit baseline demand figure — if that's off, the ratios above shift with it.**

**Scenario 2 — remove one operator from Station 2:**
Station 2 currently runs 2 operators sharing 110 seconds of total labor content (55 sec/unit effective, matching the labor figure above). Removing one operator means that same 110 seconds of work has to be done by one person:

New labor content at Station 2 = 110 ÷ 1 = **110 sec/unit**
New station cycle at Station 2 = max(machine 60, labor 110) = **110 sec** (now labor-constrained, was machine-constrained before)
New ratio at Station 2 = 110 ÷ 67.5 = **1.63** — this becomes the new plant bottleneck, well above Station 3's 1.16.

**Capacity freed:** 1 operator headcount at Station 2.
**Capacity lost:** Station 2's own throughput falls from 27,000 ÷ 60 = 450 units/shift to 27,000 ÷ 110 = 245 units/shift — a loss of 205 units/shift at that station. Because Station 2 becomes the new bottleneck, plant-wide system capacity falls from 346 units/shift to 27,000 ÷ 110 = 245 units/shift — a loss of 101 units/shift plant-wide.

These tools free capacity; what the organization does with freed capacity is a leadership decision.

---

**What this skill did:**
- Calculated takt (67.5 sec/unit) and built a station-by-station loading chart, tracking machine and labor cycle times separately at each station.
- Identified Station 3 as the bottleneck (ratio 1.16) — a labor constraint the machine numbers alone would have missed, since Station 3's machine time (45 sec) is well under takt.
- Ran both requested what-ifs from scratch: a 15% demand increase (bottleneck stays at Station 3 but Stations 2 and 4 also cross 1.00), and a one-operator reduction at Station 2 (which becomes the new, worse bottleneck at ratio 1.63, cutting plant capacity by 101 units/shift).

**What still needs a human:**
- The 400-unit/shift baseline demand figure is the assumption that most changes the bottleneck identification if it's wrong — worth confirming against the actual order book.
- Whether the 78 seconds of labor content at Station 3 includes any changeover time that `smed-setup` could reduce — that's the fastest lever before touching headcount.
- Whether removing the Station 2 operator is actually on the table, or whether this was a "what if we could" question — that determines how urgently option 1 above needs pursuing.

**Suggested next step:** Take the Station 3 labor-content breakdown to the line supervisor and confirm which of the 78 seconds could realistically move to Station 1, which has the most slack (ratio 0.74).

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
