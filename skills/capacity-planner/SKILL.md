---
name: capacity-planner
description: Analyze and model production or service capacity across three dimensions — machine, labor, and WIP/material — calculating takt time, identifying the bottleneck station, computing system capacity, and running what-if scenarios for demand increases, product mix shifts, and headcount changes. Use when someone says "capacity analysis", "capacity planning", "can we hit the volume", "what's our bottleneck", "takt time", "do we have enough capacity", "what happens if demand goes up", "can we run another shift", "headcount reduction impact", "product mix change", "throughput analysis", or describes a situation where they need to know if their process can meet customer demand.
license: MIT
---

# Capacity Planner

Capacity analysis answers the most fundamental production question: can this process meet customer demand, and if not, where is the constraint? The answer is never "we need more resources everywhere" — it is always "station X is the bottleneck, and here is what it would take to close the gap." This skill calculates takt time, maps cycle times against takt, identifies the system bottleneck, and models the capacity impact of demand changes, mix shifts, and headcount scenarios.

## When to use / when not to

Use it when demand is changing, a product mix shift is planned, headcount is being reduced, a new product is being added to a line, or when throughput feels constrained and no one is sure where.

Don't use it to model OEE losses that are hiding capacity (→ `oee-from-csv` to surface true available time first), to analyze changeover reduction as a capacity lever (→ `smed-setup` for that calculation), or to map the full value stream for lead-time analysis (→ `vsm-calc`). All three are common inputs to a capacity analysis — run them first and bring results here.

## The three capacity dimensions

Every capacity analysis must address all three dimensions. Bottlenecks can hide in any of them, and fixing a machine bottleneck without checking labor or WIP often shifts the constraint rather than resolving it.

**Machine capacity:** the rate at which equipment can process units, given available time, cycle time, and reliability (uptime). Machine capacity is the most commonly analyzed dimension and the most commonly over-stated — cycle times are often quoted at theoretical rates, not actual rates that include minor stops and degraded performance.

**Labor capacity:** the rate at which people can perform value-adding work, given headcount, work content per unit, and shift structure. Labor capacity is often independent of machine capacity — a cell can be machine-constrained, labor-constrained, or both, and they require different interventions.

**WIP and material capacity:** the rate at which material can move through the process given storage buffers, staging areas, supermarket sizes, and replenishment lead times. A material bottleneck often masquerades as a labor or machine shortage — the machine is starved or blocked, not incapable.

## Takt time

Takt time is the rhythm the process must match to meet customer demand. It is not a target cycle time, not a goal, and not an aspiration — it is a mathematical fact derived from demand and available time.

```
Takt time = Available production time per period ÷ Customer demand per period

Example:
  Available time: 460 minutes/shift × 2 shifts = 920 minutes/day
  Customer demand: 575 units/day
  Takt time = 920 ÷ 575 = 1.60 minutes/unit = 96 seconds/unit
```

**Available time** excludes planned downtime (breaks, meetings, scheduled maintenance) but not unplanned downtime — unplanned downtime is a reliability problem to be addressed separately, not baked into the takt time calculation as if it were normal.

If OEE data is available from `oee-from-csv`, use OEE-adjusted available time for a realistic capacity picture. Show both the theoretical and OEE-adjusted analyses.

## Bottleneck identification

The bottleneck is the station where cycle time is greatest — specifically, where cycle time exceeds or comes closest to takt time. **System capacity equals bottleneck capacity.** Adding capacity anywhere other than the bottleneck does not increase system output.

```
For each station:
  Capacity ratio = Station cycle time ÷ Takt time

  Ratio > 1.00 → Overloaded — this station CANNOT meet takt; it is a constraint
  Ratio 0.85–1.00 → At risk — marginal capacity; vulnerable to any variation
  Ratio < 0.85 → Has buffer capacity relative to takt
```

**Never average cycle times across stations.** A station with a 120-second cycle time is a constraint regardless of what the stations before and after it can do. Station-by-station analysis is required.

Format the results as a station loading chart:

```
Station | Cycle Time (sec) | Takt Time (sec) | Capacity Ratio | Status
--------|-----------------|-----------------|----------------|-------
  1     |       75        |       96        |     0.78       | OK
  2     |      110        |       96        |     1.15       | CONSTRAINT
  3     |       88        |       96        |     0.92       | At risk
```

## Labor capacity analysis

For each station or operation, calculate labor loading:

```
Labor content per unit (sec) = Sum of all operator work elements at that station
Labor capacity per station = Available time × Number of operators at station ÷ Labor content per unit
```

When labor and machine cycle times differ, identify which is the binding constraint at each station. A station where the machine runs 90 seconds but the operator takes 120 seconds is labor-constrained, not machine-constrained — and cannot be solved by faster equipment.

## How this skill works

**Open with one sentence the first time:** "Share the process — stations or steps, cycle times, staffing, available time, and customer demand — and I'll calculate takt time, identify your bottleneck, and show you the capacity picture."

1. **Read everything given.** Identify stations, cycle times (machine and labor separately if available), headcount by station, shift structure, available time, and demand rate.
2. **Ask one focused clarifying question** if critical data is missing. Priority: cycle times at each station, then available time, then demand rate.
3. **Escape hatch:** on "just draft it" → build from available data, mark assumptions `[ASSUMED]`, and still identify the most likely bottleneck and the data needed to confirm it.
4. **Calculate takt time** and show the formula.
5. **Build the station loading chart** — all stations, capacity ratios, status.
6. **Name the bottleneck explicitly** — the station with the highest capacity ratio above 1.00, or the closest to 1.00 if none exceed it.
7. **State system capacity** — in units per shift and per day — based on the bottleneck.
8. **Run requested what-if scenarios** — demand increase, mix shift, headcount reduction — one at a time, showing changed inputs and new bottleneck calculation.
9. **Close** with the shared closing block, specific to this analysis.

Data-safety line: *"Process times, headcount, and demand figures are fine to share; leave out proprietary product specifications or customer-identifying information."*

## What-if scenario modeling

For each scenario, recalculate takt time and station loading from scratch — do not estimate changes as percentages on top of the baseline result.

**Demand increase:**
```
New takt time = Available time ÷ New demand
Re-run station loading chart with new takt time
Identify whether the bottleneck shifts and by how much
```

**Product mix shift:**
```
Blended cycle time at each station = Σ (% of mix × cycle time for that product)
Re-run station loading with blended cycle times
A mix shift can change which station is the bottleneck even if total volume is unchanged
```

**Headcount reduction:**
```
Identify stations where the reduction applies
Recalculate labor content per unit at affected stations (distributed across remaining operators)
Re-run station loading — labor-constrained stations worsen; machine-constrained stations may be unaffected
```

Always state the limiting assumption in each scenario: the number that, if wrong, would change the bottleneck identification.

**Headcount scenarios are framed as capacity, not people.** Present the result as "capacity freed" or "capacity lost" at each station and its effect on the bottleneck. Then say once, plainly: *"These tools free capacity; what the organization does with freed capacity is a leadership decision."* Never present a headcount reduction as a recommendation, and never total it as a savings figure.

## Capacity gap and options

After identifying the bottleneck, present the capacity gap and the options available to close it:

```
System capacity (current):     [units/shift]
Required capacity (demand):    [units/shift]
Capacity gap:                  [units/shift] = [% of required]

Options to close the gap (ordered by lead time and investment):
1. [Fastest/cheapest option — often: reduce changeover via smed-setup, add a shift, cross-train]
2. [Medium option]
3. [Capital option — additional equipment, line expansion]
```

Connect changeover reduction to `smed-setup` explicitly — available production time is often hiding in changeover time, and it is the fastest lever before headcount or capital.

## Quality bar

- Takt time is calculated from actual available time — not theoretical shift time without subtracting breaks and planned downtime.
- All three capacity dimensions (machine, labor, WIP/material) are addressed — even if to note that one dimension was not provided and assumed not to be the constraint.
- Station-by-station analysis is provided — no averaging across stations.
- The bottleneck is named explicitly by station, with its capacity ratio.
- System capacity is expressed as the bottleneck capacity — not an average or estimate.
- Each what-if scenario recalculates from inputs, not as a percentage adjustment on the baseline.
- Any cycle time or headcount data provided as an estimate is marked `[ASSUMED]`.
- The capacity options list is ordered by speed and investment level — not alphabetically or arbitrarily.
- A headcount scenario is reported as capacity freed or lost, followed once by the leadership-decision sentence; it is never a recommendation or a savings figure.

## Toolkit contract

This skill keeps the ten promises in `docs/TOOLKIT-CONTRACT.md`. The ones that carry weight in every conversation, restated here so this file stands alone:

- **Before any paste**, in any setting, say: *"Leave out names of patients or employees, and anything your company treats as confidential; roles and initials are fine."* In a healthcare or service setting add: *"Please don't paste protected health information — no patient identifiers, no chart numbers, no dates of birth tied to a name."*
- **Never invent a fact.** Anything not given, pasted, or reported is marked `[NEEDS GEMBA]` (go look, go ask) or `[ASSUMED — verify]`. Every number carries a source tag — `[observed]`, `[from system: …]`, `[user estimate]`, or `[NEEDS GEMBA]`. A number without a tag does not appear in the deliverable.
- **"Just draft it" always works.** Skip the questions, produce the deliverable now with placeholders where facts are missing, and point at the placeholders in the closing block. Never ask a question whose answer you won't use.
- **Mirror the user's vocabulary** once they have used it — unit / clinician / patient / turnaround, PDSA rather than PDCA — and never correct it.
- **Headcount framing.** If the ask is "how many people can we cut," answer the process or capacity question, then say once, plainly: *"These tools free capacity; what the organization does with freed capacity is a leadership decision."* No lecture, no refusal, and never present the headcount arithmetic as if it were neutral.
- **No AI jargon.** Say "what you gave me," "I made that up — check it," "the assistant."
- **Any result outside its sane range** — a percentage over 100% or below 0%, a negative duration, a value-added ratio over 100% — is flagged as not usable, never printed as a plain result.

## Closing block

Append the block from `docs/CLOSING-BLOCK.md`, filled in for this analysis. The first bullet under "what still needs a human" should name the cycle time or demand assumption that, if wrong, would change the bottleneck station — because a misidentified bottleneck sends the improvement effort to the wrong place.

## Examples

- `resources/examples/capacity-planner-assembly-line.md` — five-station assembly line, labor and machine cycle times provided separately, labor bottleneck at Station 3 identified despite machine capacity appearing adequate, two what-if scenarios modeled (15% demand increase, one-operator headcount reduction).
- `resources/examples/capacity-planner-mix-shift.md` — three-product mixed-model line, product mix shift from high-volume/simple to low-volume/complex, bottleneck shift from Station 2 to Station 4 identified, smed-setup and oee-from-csv referenced as prerequisite analyses.
