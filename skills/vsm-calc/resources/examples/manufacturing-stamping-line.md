# Example: stamping line current + future state (manufacturing)

**User:** We want to VSM the stamping cell — blank, form, weld, inspect,
pack. I want to see what a SMED push on changeover buys us.

**Assistant:** What's demand per day, and how much time is actually
available to produce it (net of breaks, meetings, planned maintenance)?

**User:** Demand is 575 units/day, available time is 55,200 seconds (about
15.3 hours across two shifts).

**Assistant:** Got it. If you're pasting a table or export, leave out names
of employees — roles and station names are fine. Here's the current-state
table built from what you gave me plus the cycle-time source for each step;
tell me if any of this needs correcting before I run it.

```
step,cycle_time_s,changeover_s,lot_size,uptime_pct,inventory_before,source
Blank,45,1800,500,92,1200,"from MES"
Form,60,2400,500,88,800,"observed, 10 cycles, 2026-09-12"
Weld,75,,,95,350,"observed, 8 cycles, 2026-09-12"
Inspect,,,,100,120,
Pack,40,,,100,60,"user estimate"
```

**User:** That's right — nobody's timed Inspect yet, that's a real gap.
Here's the future-state table the improvement team agreed on if the SMED
work goes through.

```
step,cycle_time_s,changeover_s,lot_size,uptime_pct,inventory_before,source
Blank,45,900,1000,95,400,"from MES, post-SMED"
Form,55,1200,1000,92,300,"observed, 10 cycles, 2026-09-14"
Weld,72,,,96,150,"observed, 8 cycles, 2026-09-14"
Inspect,20,,,100,60,"observed, 6 cycles, 2026-09-14"
Pack,38,,,100,60,"user estimate"
```

**Assistant:** Running the calculator on both files now — I won't
recompute any of this by hand; if a number looks off the fix is to correct
the input file and re-run.

```
python3 skills/vsm-calc/scripts/vsm_calc.py skills/vsm-calc/resources/examples/stamping-current.csv --demand 575 --available-time-s 55200 --future skills/vsm-calc/resources/examples/stamping-future.csv
```

```
# VSM calculation — skills/vsm-calc/resources/examples/stamping-current.csv

## Current state

**Takt time = available time ÷ demand** = 55200 s ÷ 575 units = **96.0 s per unit** (1.6 min)

| Step | C/T | C/O per unit | Uptime | Effective C/T | vs takt | Inventory before | Days of supply | Source |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Blank | 45 s | 3.6 s | 92% | 52.8 s | 0.55 ok | 1200 | 2.09 d (32.0 h) | from MES |
| Form | 60 s | 4.8 s | 88% | 73.6 s | 0.77 ok | 800 | 1.39 d (21.3 h) | observed, 10 cycles, 2026-09-12 |
| Weld | 75 s | 0.0 s | 95% | 78.9 s | 0.82 ok | 350 | 0.61 d (9.3 h) | observed, 8 cycles, 2026-09-12 |
| Inspect | [NEEDS GEMBA: time this step] | | | | | 120.0 | |  |
| Pack | 40 s | 0.0 s | 100% | 40.0 s | 0.42 ok | 60 | 0.10 d (1.6 h) | user estimate |

- **Processing time** (sum of C/T) = **3.7 min** (220 s)
- **Lead time** (processing + inventory waiting) = **64.3 h** (231580 s = 4.20 days of available time)
- **PCE = processing ÷ lead time** = 220 ÷ 231580 = **0.1%**
- **Bottleneck: Weld** at 78.9 s effective vs takt 96.0 s — the line meets takt on the cycles observed.

## Future state

**Takt time = available time ÷ demand** = 55200 s ÷ 575 units = **96.0 s per unit** (1.6 min)

| Step | C/T | C/O per unit | Uptime | Effective C/T | vs takt | Inventory before | Days of supply | Source |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Blank | 45 s | 0.9 s | 95% | 48.3 s | 0.50 ok | 400 | 0.70 d (10.7 h) | from MES, post-SMED |
| Form | 55 s | 1.2 s | 92% | 61.1 s | 0.64 ok | 300 | 0.52 d (8.0 h) | observed, 10 cycles, 2026-09-14 |
| Weld | 72 s | 0.0 s | 96% | 75.0 s | 0.78 ok | 150 | 0.26 d (4.0 h) | observed, 8 cycles, 2026-09-14 |
| Inspect | 20 s | 0.0 s | 100% | 20.0 s | 0.21 ok | 60 | 0.10 d (1.6 h) | observed, 6 cycles, 2026-09-14 |
| Pack | 38 s | 0.0 s | 100% | 38.0 s | 0.40 ok | 60 | 0.10 d (1.6 h) | user estimate |

- **Processing time** (sum of C/T) = **3.8 min** (230 s)
- **Lead time** (processing + inventory waiting) = **25.9 h** (93350 s = 1.69 days of available time)
- **PCE = processing ÷ lead time** = 230 ÷ 93350 = **0.2%**
- **Bottleneck: Weld** at 75.0 s effective vs takt 96.0 s — the line meets takt on the cycles observed.

## Delta (future − current)

| Measure | Current | Future | Change |
|---|---:|---:|---:|
| Processing time | 3.7 min | 3.8 min | 10 s |
| Lead time | 64.3 h | 25.9 h | −38.4 h |
| PCE | 0.1% | 0.2% | +0.2 pts |

## Flags

- Inspect: no cycle time given — marked [NEEDS GEMBA: time this step]; excluded from totals, so lead time and PCE are understated until it is timed.
```

**Assistant:** Takt is **96.0 s/unit** on both files (demand and available
time haven't changed). Currently the line meets takt — the bottleneck is
**Weld at 78.9 s effective**, well under takt — but Weld and Form (73.6 s)
are both within striking distance of each other, so it's not a single
sharp constraint yet.

The future-state table (with the SMED changeover work and lot sizes
doubled to 1,000) doesn't move processing time much — 3.7 min to 3.8 min,
because Inspect gets timed for the first time and adds 20 s that wasn't in
the current total at all. What it does move is **lead time, down from
64.3 hours to 25.9 hours**, almost entirely by cutting inventory sitting in
front of each step (Blank's queue alone drops from 1,200 to 400 units).
PCE moves from 0.1% to 0.2% — still far below the 5–10% that's typical for
a line at this stage, which is expected and not itself a red flag; it
becomes the kaizen target once leadership decides lead time is the thing
to chase next.

One thing this doesn't tell you: **Inspect has no current-state timing at
all** — the current-state total, and every ratio built from it, is
understated until someone stands at that station with a stopwatch. The
future-state number for Inspect (20 s, 6 cycles) is a real observation, but
it can't be compared to a "before" that was never measured.

---

**What this skill did:**
- Ran the VSM calculator on the current- and future-state stamping tables and computed takt (96.0 s/unit), the per-step effective cycle time, lead time, PCE, and the bottleneck for each, plus the delta between them.
- Found the current-state line meets takt with Weld as the bottleneck (78.9 s, close behind Form at 73.6 s), and that the future-state plan mainly buys back lead time (64.3 h → 25.9 h) by cutting queued inventory, not by making any single step faster.
- Inspect has never been timed in the current state, so the current-state processing time and PCE are understated until it is.

**What still needs a human:**
- Inspect needs a gemba timing in the current state — [NEEDS GEMBA: time this step] — before the current-vs-future comparison is complete.
- Confirm the future-state file reflects the improvement team's agreed plan (lot sizes at 1,000, changeover cut roughly in half) and not just a hope — the lead-time gain depends on both actually happening together.
- Weld and Form are close enough in effective cycle time that calling Weld "the" bottleneck should be checked against a few more cycles before it drives a countermeasure.

**Suggested next step:** Take a stopwatch to Inspect for at least 8–10 cycles and re-run the current-state file with that number filled in before presenting this to the improvement team.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
