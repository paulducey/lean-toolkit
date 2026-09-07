---
name: oee-from-csv
description: Calculate OEE (Overall Equipment Effectiveness) — Availability x Performance x Quality — and a Six Big Losses breakdown with Pareto from a downtime/production CSV export. Use when someone says "OEE", "overall equipment effectiveness", "downtime analysis", "six big losses", "here's our downtime export", "availability performance quality", or pastes a CSV from an MES, historian, or manual downtime log. Auto-detects delimiter, tolerates a messy header row and blank columns, and never guesses a missing column — it lists what it found and what's still needed.
license: MIT
---

# OEE from CSV

OEE is three factors multiplied together, each one a different kind of
loss. A single OEE number tells you almost nothing about what to fix; the
breakdown by loss category does. This skill computes both from a CSV
export and explains every formula it used.

## When to use / when not to

Use it when you have a downtime and production export — from an MES,
PLC/SCADA historian, or a manual downtime log — and want Availability,
Performance, Quality, overall OEE, and a Six Big Losses Pareto, with the
formulas shown so the numbers can be checked.

Don't use it for value-stream-level cycle time and lead time (→
`vsm-calc`), or to investigate *why* a specific loss category is high (→
`root-cause`). If leadership wants a single trend number for a scorecard,
this skill can produce it, but say plainly that a bare OEE percentage
without the loss table isn't actionable.

## The three factors, in plain language

- **Availability** — the fraction of planned production time the line
  actually ran. `Availability = run time ÷ planned production time`, where
  `run time = planned time − downtime`. Planned downtime (breaks, changeover
  the schedule already accounts for, PM windows) should not be counted as a
  loss here — only *unplanned* downtime against the schedule.
- **Performance** — how fast the line ran while it *was* running, against
  the best rate it's capable of. `Performance = (ideal cycle time × total
  count) ÷ run time`. "Ideal cycle time" means the best demonstrated rate,
  not an average of normal days — using an average flatters the number and
  hides speed loss.
- **Quality** — the fraction of output that was good the first time.
  `Quality = good count ÷ total count`.
- **OEE = Availability × Performance × Quality.**

## Classic traps this skill won't let you fall into silently

- **Planned downtime counted as loss.** If your export doesn't separate
  planned from unplanned downtime, say so in the report rather than
  treating all downtime as loss — check with the person who built the
  schedule.
- **Ideal cycle time set to "average" instead of best-demonstrated.** If
  the ideal cycle time you're using came from an average of normal
  production, the Performance number is inflated. Ask where the value in
  the `ideal_cycle_time` (or `rated_speed`) column came from before
  trusting it.
- **Changeover hidden inside run time.** If changeover isn't logged as
  downtime, it shows up as a Performance loss instead of an Availability
  loss, which misdirects the countermeasure. Check whether changeover has
  its own downtime rows.
- **A bare OEE number.** Reporting "OEE is 61%" without the Six Big Losses
  table tells a team nothing to act on. Always hand over both.

## How this skill works (draft-first)

1. **Ask for the export**, with the data-safety line: *"Paste or attach
   your downtime export (the CSV your MES, historian, or maintenance log
   produces). Leave out names of employees; roles, shifts, or line IDs are
   fine."*
2. **Run the calculator** on the file as given, always from the plugin root
   (so the command works the same way the exporter does):
   ```
   python3 skills/oee-from-csv/scripts/oee.py downtime_export.csv
   ```
   If the ideal-cycle-time column is in seconds rather than minutes, add
   `--cycle-time-unit s`.
3. **If it reports missing columns**, show the user exactly what the
   script printed (columns found vs. still needed) and ask them to check
   the export or rename a column — never estimate a substitute value
   yourself.
4. **Present the output**, relabelled in the user's vocabulary if they've
   used their own (see the healthcare/service bullet in Quality bar) —
   Availability, Performance, Quality, OEE with formulas spelled out, the
   Six Big Losses table, the Pareto, and the per-day/shift/line table if
   those columns exist. Never recompute by hand.
5. **Flag the classic traps above** if the data suggests one (e.g., no
   distinction between planned and unplanned downtime, or a downtime-reason
   column with a large "Unmapped" bucket).
6. **Add the closing block**, specific to this run.
7. **Only then ask blocking questions** — e.g., whether the ideal cycle
   time is best-demonstrated or an average, or what the biggest "Unmapped"
   reason codes actually mean on the floor.

## Six Big Losses keyword map

Downtime reasons are matched by keyword, case-insensitively, into:
breakdowns (breakdown, failure, fail); setup & adjustments (setup,
changeover, adjust); idling & minor stops (jam, minor stop, idle);
reduced speed (slow, reduced speed); process defects (scrap, defect,
rework); reduced yield / startup rejects (startup, warm-up, yield). A
reason that matches nothing is listed as **Unmapped**, not hidden or
force-fit — a large Unmapped bucket is itself a finding: the reason codes
need better categories at the source system.

## Deliverable

Template: `resources/templates/oee-report.md`. Input shape:
`resources/templates/oee-input.md`. The report always includes, in order:
Availability/Performance/Quality/OEE with formulas; the Six Big Losses
table with an explicit Unmapped row when applicable; a downtime Pareto;
a per-day/shift/line breakdown when those columns are present.

## Quality bar

- Every formula is shown with the actual numbers substituted, not just the
  result.
- Planned vs. unplanned downtime is called out explicitly if the export
  doesn't distinguish them.
- The source of "ideal cycle time" (best-demonstrated vs. average) is
  questioned, not assumed correct.
- Six Big Losses categories never absorb an unmapped reason silently — it
  goes in "Unmapped" with the raw reason text shown.
- Never a bare OEE number without the loss breakdown alongside it.
- Missing required columns produce a clear message naming what was found
  and what's needed — never a guess, never a crash.
- Performance or OEE above 100% is flagged, not printed as a plain result —
  it almost always means the ideal cycle time is an average rather than the
  best-demonstrated rate, or that counts include units made outside the run
  time. Never treat a number over 100% as a usable result.
- A blank good_count or reject_count cell is excluded from the Quality
  calculation and named in the report — never treated as 100% good.
- Healthcare/service data uses the user's vocabulary once they've used it
  (e.g., "scheduled hours" instead of "planned time," "scan" instead of
  "unit") while the underlying formulas stay the same, with a note that OEE
  terms map imperfectly onto healthcare — see the MRI example.

## Closing block

Append the block from `docs/CLOSING-BLOCK.md` (also copied at
`resources/closing-block.md`), filled in for this run. If any columns were
missing or a keyword-mapped category leans heavily on "Unmapped," the first
bullet should point at that.

## Export

`python3 skills/oee-from-csv/scripts/export_docx.py <report.md> [-o out.docx] [--title "..."]`
converts the saved Markdown report to a clean Word document. It is a thin
wrapper around the repo's shared `scripts/md_to_docx.py` — never hand-assemble
a `.docx`.

## Examples

- `resources/examples/manufacturing-stamping-line.md` — Line 1 downtime
  export, including a messy raw CSV with a bad header row and a blank
  column.
- `resources/examples/healthcare-mri-utilization.md` — MRI scanner
  scheduled-hours/downtime/scan export, with the honest caveat that OEE
  terms map imperfectly onto healthcare.

Both show the exact command run and its output, and end with the closing
block.
