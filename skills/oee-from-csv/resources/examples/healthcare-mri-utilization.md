# Example: MRI scanner utilization (healthcare)

**User:** Can you run OEE-style numbers on our MRI scanner for yesterday?
We track scheduled hours, scans done, and delay reasons.

**Assistant:** Paste or attach your scheduled-hours/scans/delay export.
Leave out names of patients or employees, and anything your facility
treats as confidential; roles and room or scanner IDs are fine. And
please don't paste protected health information — no patient identifiers,
no chart numbers, no dates of birth tied to a name.

**User:** Here's the export for scanner MRI-2, day shift. One note — "sw"
in the reason column is a scheduling shorthand nobody's translated, I
don't know what it stands for either.

```
date,shift,line,planned_min,ideal_cycle_time_min,total_count,good_count,reject_count,downtime_reason,downtime_min
2026-09-10,day,MRI-2,600,25,18,17,1,,
2026-09-10,day,MRI-2,,,,,,Coil fault - reboot,25
2026-09-10,day,MRI-2,,,,,,Patient no-show,30
2026-09-10,day,MRI-2,,,,,,Contrast prep delay,15
2026-09-10,day,MRI-2,,,,,,sw,10
```

**Assistant:** One thing worth saying up front: this calculator is built
around OEE, a manufacturing measure, and its terms map imperfectly onto a
scanner and a schedule — "planned time" isn't quite the same idea as
patient flow, and "quality" here just means "images usable" (as opposed to
a machine defect). I'll use the numbers as-is and put them in your terms
below. Running it now — I'm not adjusting or recomputing anything the
script prints.

```
python3 skills/oee-from-csv/scripts/oee.py skills/oee-from-csv/resources/examples/mri_scheduled_hours.csv
```

```
# OEE report — skills/oee-from-csv/resources/examples/mri_scheduled_hours.csv

Columns found: date, shift, line, planned_min, ideal_cycle_time_min, total_count, good_count, reject_count, downtime_reason, downtime_min

## Availability × Performance × Quality

- **Availability = run time ÷ planned time** = (600 − 80) ÷ 600 = 520 ÷ 600 = **86.7%**
- **Performance = (ideal cycle time × total count) ÷ run time** = 450 ÷ 520 = **86.5%**
- **Quality = good count ÷ total count** = 17 ÷ 18 = **94.4%**
- **OEE = A × P × Q** = 0.867 × 0.865 × 0.944 = **70.8%**

## Six Big Losses (unplanned downtime, minutes)

| Loss | min | share |
|---|---:|---:|
| Breakdowns | 25 | 31% |
| Unmapped | 55 | 69% |

**Unmapped reason text (needs a category at the source system):** "Patient no-show" 30 min, "Contrast prep delay" 15 min, "sw" 10 min

## Downtime Pareto

Unmapped                     ████████████████████████████             55
Breakdowns                   ████████████                             25

## Flags

- The export does not separate planned from unplanned downtime; all downtime was treated as unplanned. Check with whoever built the schedule.
- No changeover rows found. If changeover isn't logged as downtime it shows up as a Performance loss instead of Availability, which misdirects the countermeasure.
- Confirm the ideal cycle time is the best-demonstrated rate, not an average of normal days — an average flatters Performance.
```

**Assistant:** In your terms: MRI-2 used **86.7%** of its scheduled hours
[from system: scheduling export] to actually scan (520 of 600 scheduled
minutes), ran at **86.5%** of its best-demonstrated pace per scan, and
**94.4%** of scans (17 of 18) came back usable. Put together the way the
scanner OEE formula does, that's **70.8%**.

The bigger finding is in the delay breakdown:

- **69% of lost minutes (55 of 80) are Unmapped** — a coil fault (25 min)
  is the only delay that matched a known category. "Patient no-show" (30
  min), "Contrast prep delay" (15 min), and "sw" (10 min) don't match
  anything the calculator recognizes as a mechanical loss category,
  because they aren't mechanical — they're scheduling and prep, and
  "sw" is unmapped because nobody knows what it means. That's the
  real finding here, not the scanner's own reliability.
- The export doesn't separate scheduled maintenance from unplanned
  downtime, so all 80 minutes were counted as lost time. If the coil
  fault reboot is logged the same way every time, that's fine; if any of
  this is actually scheduled service, the "scheduled hours used" number
  is understated.
- No changeover-equivalent rows (e.g., room turnover between patients) —
  if turnover time isn't logged as its own delay, it would be hiding
  inside the pace number instead of showing up as its own category.

As the flag above says, I can't verify from this export alone whether the
25-minute ideal scan time is a best-demonstrated pace or an average day —
that would change the pace number.

---

**What this skill did:**
- Ran the utilization calculator on scanner MRI-2's day-shift export (scheduled minutes, scans, delay reasons) and computed the scanner-OEE-style breakdown: 86.7% of scheduled hours used, 86.5% pace, 94.4% scans usable, 70.8% combined.
- Found that 69% of lost minutes (55 of 80) are scheduling and prep delays — patient no-show, contrast prep, and an untranslated "sw" code — not mechanical faults, which is the opposite of what the combined number alone would suggest.
- Noted once that OEE terms (availability/performance/quality) map imperfectly onto a scanner and a patient schedule; the arithmetic is shown as-is, relabeled into scheduled hours, scans, and usable scans.

**What still needs a human:** [NEEDS GEMBA — see below]
- Find out what "sw" means in the scheduling system (10 min) — nobody on this thread could say.
- Confirm whether the coil fault reboot (25 min) is logged as unplanned every time, and whether room/patient turnover time is captured anywhere, since no turnover-type delay row showed up.
- Confirm the 25-minute ideal scan time is the best-demonstrated pace, not an average day — this changes the pace number and the combined score.

**Suggested next step:** Take the delay breakdown to whoever runs the MRI schedule and ask what "sw" stands for and whether the two no-show/prep delays are being tracked anywhere upstream to reduce them.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
