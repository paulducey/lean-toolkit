# Example: outpatient clinic visit flow (healthcare)

**User:** Can you map our visit flow — check-in, rooming/vitals, provider,
checkout? We're doing a PDSA on wait times and I want the real numbers
first.

**Assistant:** What's demand per day — patients seen — and how much time
is actually available in the clinic day to see them (net of breaks and
meetings)?

**User:** We see about 32 patients a day, clinic is open 7.5 hours, call it
27,000 seconds available.

**Assistant:** If you're pasting a table or notes, leave out patient names
— roles and visit-type labels are fine. And please don't paste protected
health information — no patient identifiers, no chart numbers, no dates of
birth tied to a name. Here's the table built from what you gave me; the
clinic manager timed check-in and rooming herself, checkout comes from the
scheduling system, and nobody's timed the provider visit itself yet — tell
me if anything needs correcting.

```
step,cycle_time_s,changeover_s,uptime_pct,inventory_before,source
Check-in,180,,98,6,"observed, 15 visits, 2026-09-14"
Rooming/vitals,300,,95,4,"observed, 12 visits, 2026-09-14"
Provider visit,,,90,9,
Checkout,150,,100,3,"from scheduling system"
```

**User:** That's right, go ahead.

**Assistant:** Running the calculator now — I won't recompute any of this
by hand; if a number looks wrong the fix is to correct the input file and
re-run.

```
python3 skills/vsm-calc/scripts/vsm_calc.py skills/vsm-calc/resources/examples/clinic-visit.csv --demand 32 --available-time-s 27000
```

```
# VSM calculation — skills/vsm-calc/resources/examples/clinic-visit.csv

## Current state

**Takt time = available time ÷ demand** = 27000 s ÷ 32 units = **843.8 s per unit** (14.1 min)

| Step | C/T | C/O per unit | Uptime | Effective C/T | vs takt | Inventory before | Days of supply | Source |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Check-in | 180 s | 0.0 s | 98% | 183.7 s | 0.22 ok | 6 | 0.19 d (1.4 h) | observed, 15 visits, 2026-09-14 |
| Rooming/vitals | 300 s | 0.0 s | 95% | 315.8 s | 0.37 ok | 4 | 0.12 d (56.2 min) | observed, 12 visits, 2026-09-14 |
| Provider visit | [NEEDS GEMBA: time this step] | | | | | 9.0 | |  |
| Checkout | 150 s | 0.0 s | 100% | 150.0 s | 0.18 ok | 3 | 0.09 d (42.2 min) | from scheduling system |

- **Processing time** (sum of C/T) = **10.5 min** (630 s)
- **Lead time** (processing + inventory waiting) = **3.2 h** (11599 s = 0.43 days of available time)
- **PCE = processing ÷ lead time** = 630 ÷ 11599 = **5.4%**
- **Bottleneck: Rooming/vitals** at 315.8 s effective vs takt 843.8 s — the line meets takt on the cycles observed.

## Flags

- Provider visit: no cycle time given — marked [NEEDS GEMBA: time this step]; excluded from totals, so lead time and PCE are understated until it is timed.
```

**Assistant:** In your terms: takt — the pace the clinic needs to hit to
see 32 patients in the day — is **14.1 minutes per patient**. Rooming and
vitals is the slowest step observed, at **5.3 minutes effective** (300 s
timed, adjusted for 95% uptime), well inside takt, so on the visits that
were actually timed the flow is keeping pace with demand.

The number that matters more here is **patients waiting**: right now
there are 9 patients queued ahead of the provider step — more than double
any other step's queue (6 at check-in, 4 at rooming, 3 at checkout).
That's where a PDSA cycle would have the most to work with, not at
check-in or rooming.

Turnaround from processing to lead time (PCE) comes out to **5.4%** — total
hands-on time is 10.5 minutes but a patient's whole visit, including
waiting, spans about 3.2 hours. A PCE that low is typical for a visit
flow like this, not itself a crisis — it's the number a PDSA cycle would
aim to move once the team decides shorter turnaround is the goal.

The gap worth naming plainly: **the provider visit itself has never been
timed.** It's the step everyone suspects is the constraint, and it's the
one piece of data missing — the 9 patients waiting in front of it are
real, but the effective cycle time, and therefore the true bottleneck call
and the true lead time, can't be confirmed until someone clocks it.

---

**What this skill did:**
- Ran the visit-flow calculator on check-in, rooming/vitals, provider visit, and checkout and computed takt (14.1 min/patient), effective time per step, turnaround (lead time, 3.2 hours), and PCE (5.4%).
- Found rooming/vitals is the slowest timed step (5.3 min effective) but still well inside takt, while patients waiting in front of the provider step (9) is more than double any other step's queue.
- The provider visit has no timing at all, so the turnaround and PCE numbers above are understated until it's clocked, and no single bottleneck can be named with confidence yet.

**What still needs a human:** [NEEDS GEMBA]
- The provider visit needs to be timed — [NEEDS GEMBA: time this step] — before turnaround, PCE, or a bottleneck call can be trusted.
- Confirm how many visits the check-in (15) and rooming (12) timings were based on, and whether those were typical days or unusually light/heavy ones.
- If the PDSA is meant to shorten turnaround, that's a decision for the clinic team on where to start — the data above says the queue in front of the provider step is the visible pressure point, but freeing that capacity is the team's call, not this calculation's.

**Suggested next step:** Have the clinic manager or a colleague time the provider visit for 8–10 patients this week, then re-run this file with that number filled in before the PDSA team picks its first test of change.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
