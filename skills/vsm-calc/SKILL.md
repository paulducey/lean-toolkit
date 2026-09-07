---
name: vsm-calc
description: Turn a table of process steps (cycle time, changeover, uptime, inventory) plus demand into the numbers a value stream map needs — takt time, per-step effective cycle time, inventory expressed as days of supply, total lead time, Process Cycle Efficiency (PCE), and the bottleneck. Use when someone says "value stream map", "VSM", "takt time", "lead time", "process cycle efficiency", "PCE", "current state map numbers", "where's the bottleneck", or pastes a current-state data table and wants the math done. Also does a future-state delta table when a second file is given. Never estimates a missing cycle time — marks it for gemba observation instead.
license: MIT
---

# VSM Calc

A value stream map is a picture; this skill does the arithmetic behind it —
takt, cycle time, lead time, and PCE — from a table you supply. It draws no
conclusions from data it wasn't given: a step with no observed cycle time
is marked `[NEEDS GEMBA: time this step]`, never filled in.

## When to use / when not to

Use it when you have (or can quickly build) a table of process steps —
cycle time, changeover, uptime, inventory in front of each step — and want
takt time, lead time, PCE, and the bottleneck computed correctly, for a
current-state map, a future-state comparison, or to sanity-check numbers
someone else produced.

Don't use it to draw the map itself (this skill produces numbers and a
per-step table, not a Visio-style diagram), for OEE on a single machine's
downtime log (→ `oee-from-csv`), or for root-cause work on why a step is
slow (→ `root-cause`).

## Definitions (get these right before anything else)

- **Cycle time (C/T):** the time to complete one unit at one step, operator-paced. It is a *measurement of one step*, from a stopwatch or a system log — not an estimate, not a nameplate speed.
- **Takt time:** available time ÷ customer demand, over the same period. It is a *pace requirement set by the customer*, not a property of any machine. `Takt = available time ÷ demand`.
- **Lead time:** the total elapsed time for one unit to travel through the whole value stream, including every queue and every unit of inventory sitting in front of a step. Lead time is almost always many times longer than the sum of cycle times.
- **Process Cycle Efficiency (PCE):** total processing time ÷ total lead time. A PCE under 5–10% is typical and not itself a crisis; it becomes the target of a kaizen when leadership wants shorter lead time.

Conflating cycle time and takt time is a common and costly mistake: a step
can run faster than takt and the line can still miss customer demand if
uptime, changeover, or another step is the constraint. This skill compares
every step's *effective* cycle time (cycle time corrected for uptime and
changeover) against takt, not the raw number.

## Data quality — ask before trusting the numbers

Before treating any cycle-time column as usable, ask (skip if already
answered in what was given):
1. **How many cycles were timed, and over what period?** A single lap and a
   two-week log are not the same confidence.
2. **Who timed it — the operator, the analyst, or is it from a system log
   (MES, PLC, ERP)?** Say so; it becomes the source tag in the report.
3. **Was the observation typical, or a best case / bad day?**

If the user says "just calculate it" or "use what I gave you," proceed
immediately — this is a draft-first skill, not a coaching one. Note in the
closing block that the source and sample size were not confirmed.

Data-safety line, if asking for a document or export: *"Leave out names of
patients or employees and anything your company treats as confidential;
roles and initials are fine."*

## Healthcare and service mirroring

The calculator's own output is written in plant vocabulary ("units",
"line", "the line meets takt") because that's the shared default. Once the
user has used their own words — "patients", "visits", "clinic", "provider",
"turnaround" instead of "changeover", PDSA instead of PDCA — adopt them for
the rest of the conversation and when you hand back the report: "units"
becomes "patients" or "visits", "line" becomes "visit flow" or the unit's
name, "days of supply" becomes "patients waiting" or a wait-time framing if
that reads more naturally to that team. The arithmetic never changes —
takt, effective cycle time, lead time, and PCE mean the same thing — only
the labels do. Never correct a user's own cycle-vocabulary choice.

## How this skill works (draft-first)

1. **Read what was given.** If the user pasted a table or attached a file,
   use it as-is; don't re-ask for data already provided.
2. **Confirm demand and available time** if not given — these are the only
   two numbers the calculator cannot proceed without. Ask once, briefly:
   "What's demand per day, and how much time is actually available to
   produce it (net of breaks, meetings, planned maintenance)?"
3. **Build or accept the input file** — see `resources/templates/vsm-input.md`
   for the exact CSV/JSON shape. If the user describes steps in prose,
   turn them into the table yourself and show it back before running the
   script, so they can correct it.
4. **Run the calculator** (always from the plugin root, so the command
   works the same way the exporter does):
   ```
   python3 skills/vsm-calc/scripts/vsm_calc.py steps.csv --demand <N> --available-time-s <N> [--future future.csv]
   ```
5. **Present the output**, relabelled in the user's vocabulary if they've
   used their own (see mirroring, below) — the script already writes takt,
   the per-step table, totals, PCE, and the bottleneck call in plain
   language, with formulas spelled out. Don't recompute by hand; if a
   number looks wrong, fix the input file and re-run.
6. **Add the closing block**, specific to this run (see below).
7. **Only then ask blocking questions** — the ones needed to complete the
   picture, not to coach the problem. Typically: which steps still need a
   gemba timing, and whether the future-state file (if any) reflects an
   agreed plan or a hope.

## Deliverable

Template: `resources/templates/vsm-report.md` (this is what the script's
output follows; use it as a guide when hand-editing). Input shape:
`resources/templates/vsm-input.md`.

The report always includes, in order: takt time with its formula spelled
out; a per-step table (C/T, C/O, uptime, effective C/T, inventory before,
days of supply); totals (processing time, lead time, PCE); a bottleneck
call with a plain sentence on whether the line meets takt; a future-state
delta table when a second file was given.

## Quality bar

- Every cycle time is either sourced (`(observed, 12 cycles, 2026-09-14)`,
  `(from MES)`, `(user estimate)`) or marked `[NEEDS GEMBA: time this step]`
  — never silently filled in or averaged.
- Takt is stated as a formula with the actual numbers substituted, not just
  the result.
- The bottleneck call compares *effective* cycle time (after uptime and
  amortized changeover) to takt — not raw cycle time.
- "Meets takt" is stated in one plain sentence a supervisor could read at a
  tier board, with the caveat that it reflects the cycles actually observed.
- Inventory is expressed in both days and hours of supply, not just units.
- If two steps are close in effective cycle time, say so — don't declare a
  single bottleneck when the data doesn't support it that cleanly.
- No headcount framing. If asked "how many operators can we cut," redirect
  to capacity freed and demand; leadership decides what to do with it.
- Healthcare and service users get their own words. Once the user has said
  "patients", "visits", "clinic", relabel the script's output — "units"
  becomes "patients", "line" becomes "visit flow", "days of supply" becomes
  "patients waiting". The arithmetic does not change; only the labels do.
  Mirror PDSA if the user says PDSA rather than PDCA, and "turnaround"
  rather than "changeover" the same way.

## Closing block

Append the block from `docs/CLOSING-BLOCK.md` (also copied at
`resources/closing-block.md`), filled in for this run. The first bullet
under "what still needs a human" must point at any `[NEEDS GEMBA]` steps
and at unconfirmed sample sizes ("How many cycles were timed?" unanswered).

## Export

`python3 skills/vsm-calc/scripts/export_docx.py <report.md> [-o out.docx] [--title "..."]`
converts the saved Markdown report to a clean Word document. It is a thin
wrapper around the repo's shared `scripts/md_to_docx.py` — never hand-assemble
a `.docx`.

## Examples

- `resources/examples/manufacturing-stamping-line.md` — current-state VSM
  for a stamping line, with a future-state comparison.
- `resources/examples/healthcare-clinic-visit-flow.md` — outpatient clinic
  visit flow (check-in → vitals → provider → checkout).

Both show the exact command run and its output, and end with the closing
block.
