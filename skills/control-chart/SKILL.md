---
name: control-chart
description: Build and interpret statistical process control (SPC) charts — distinguishing common cause from special cause variation using Western Electric rules, calculating control limits, and computing Cp and Cpk process capability indices — to determine whether a process is stable and whether it is capable of meeting specifications. Use when someone says "control chart", "SPC", "statistical process control", "is this process in control", "process capability", "Cp", "Cpk", "common cause", "special cause", "are these results normal or is something wrong", "control limits", "we're trying to understand if our variation is random", or shares process measurement data over time.
license: MIT
---

# Control Chart and Process Capability

The most expensive mistake in process management is treating common cause variation as if it were a special cause — adjusting a stable process in response to normal noise, which adds variation instead of reducing it. The second most expensive mistake is the reverse: ignoring a genuine signal because it "seems within range." Statistical process control (SPC) exists to make this distinction objectively. This skill builds control charts, applies the Western Electric detection rules, and calculates process capability.

## When to use / when not to

Use it when you have a series of process measurements over time and want to know whether the process is stable, whether something has changed, and whether the process is capable of meeting specification limits.

Don't use it to investigate why a special cause occurred (→ `root-cause`), to assess what failure modes could generate out-of-control signals (→ `fmea-builder`), or to calculate OEE losses from a process running outside its specification (→ `oee-from-csv`).

## The one concept that everything else depends on

**Common cause variation** is the inherent, random variation of a stable process — noise produced by the many small, consistent sources of variation that are always present. It is predictable in aggregate. You cannot eliminate common cause variation by reacting to individual points; you can only reduce it by changing the process itself.

**Special cause variation** is a signal — a pattern that could not plausibly arise from random noise. Something has changed: a new material lot, a different operator, equipment wear, a process shift. Special causes are investigated and removed. Reacting to common cause variation as if it were a special cause is called **tampering** — it adds variation and degrades the process.

**This distinction is the entire point of a control chart.** Every other feature — the limits, the rules, the capability indices — exists to support it.

## Chart selection

| Data type | Subgroup size | Chart |
|---|---|---|
| Continuous measurement (dimension, weight, time) | n = 1 | Individuals and Moving Range (I-MR) |
| Continuous measurement | n = 2–9 | X-bar and R |
| Continuous measurement | n ≥ 10 | X-bar and S |
| Count of defectives (pass/fail, % defective) | Variable | p-chart or np-chart |
| Count of defects per unit | Variable | c-chart or u-chart |

When in doubt with small datasets or individual measurements, default to I-MR. Say which chart you're using and why in one sentence.

## Control limits — calculation and meaning

Control limits are calculated from the data — they are not specification limits, and they are not set by management preference. Setting control limits equal to or near specification limits is a common and serious error; state this explicitly if the user suggests it.

**For I-MR charts:**

```
Moving Range (MR_i) = |X_i − X_{i−1}|  for i = 2 to n

X̄ = mean of all individual values
MR̄ = mean of all moving ranges

Upper Control Limit (UCL_X) = X̄ + 2.66 × MR̄
Lower Control Limit (LCL_X) = X̄ − 2.66 × MR̄  (floor at 0 if negative and data is non-negative)
UCL_MR = 3.267 × MR̄
LCL_MR = 0
```

**For X-bar and R charts** (use standard d2, A2, D3, D4 factors for the appropriate subgroup size — document the subgroup size used).

State the number of data points used to calculate control limits. Control limits calculated from fewer than 20–25 points are provisional — note this explicitly.

## Western Electric detection rules

These four rules detect special causes. A point or pattern meeting any rule is a signal — investigate it.

**Rule 1 — Point beyond 3σ:** One point falls outside the 3-sigma control limit (above UCL or below LCL). The most fundamental rule. Probability of false alarm from random variation: 0.27%.

**Rule 2 — Nine consecutive on one side:** Nine or more consecutive points on the same side of the centerline (all above or all below X̄). Signals a sustained shift in the process mean.

**Rule 3 — Six consecutive trending:** Six or more consecutive points consistently increasing or consistently decreasing. Signals a drift — gradual wear, temperature change, material depletion, operator fatigue.

**Rule 4 — Fourteen alternating:** Fourteen or more consecutive points alternating up-down-up-down. Often signals over-adjustment (tampering), two alternating process streams (two machines, two shifts, two suppliers), or a measurement system problem.

Apply all four rules to every chart. Flag each violation with the rule number and the point(s) involved. Do not apply rules without stating which points triggered them.

**The tampering rule — never adjust a process showing only common cause variation.** If no Western Electric rule is triggered, the process is in statistical control. Adjusting it in response to an individual high or low point adds variation. State this plainly. If the user wants to reduce common cause variation, that requires a process improvement — not a reaction to individual data points.

## Process capability — Cp and Cpk

Capability indices are only meaningful for a **stable process** (in statistical control). Calculate capability only after confirming control. If the process is not in control, state that capability indices are not valid until special causes are removed.

```
Process sigma (σ) estimated from the control chart:
  For I-MR:  σ = MR̄ / 1.128
  For X-bar/R:  σ = R̄ / d2

Cp = (USL − LSL) / (6σ)
Cpk = min[(USL − X̄) / (3σ),  (X̄ − LSL) / (3σ)]
```

**Cp measures spread only** — whether the process variation fits within the specification window, assuming perfect centering. **Cpk measures centering** — whether the process is actually positioned within the window. Both are required. A process can have excellent Cp and poor Cpk if it is running off-center.

**Cpk thresholds:**

| Cpk | Interpretation |
|---|---|
| < 1.00 | Not capable — producing out-of-specification output |
| 1.00 – 1.33 | Marginal — technically capable but with little margin; vulnerable to shifts |
| > 1.33 | Capable — generally accepted as the minimum for production |
| > 1.67 | Highly capable — sometimes called "Six Sigma capable" at 1.67; used in safety-critical applications |

**When Cp >> Cpk:** the process has the spread to fit within spec but is running off-center. The improvement action is centering (adjust the target), not reducing variation.

**When Cp ≈ Cpk:** the process is centered but the spread is too large. The improvement action is reducing variation — which requires identifying and removing common causes, not reacting to individual points.

## How this skill works

**Open with one sentence the first time:** "Share the measurement data — values and sequence matter — along with the spec limits if you have them, and I'll build the control chart and tell you what it's showing."

1. **Read all data given.** Confirm data type (continuous/attribute), subgroup structure, and sequence.
2. **Calculate control limits** from the data, showing the formula and values used.
3. **Apply all four Western Electric rules.** Name every triggered rule and the specific points involved.
4. **State the stability conclusion explicitly:** in control (only common cause present) or out of control (special cause detected) — no ambiguity.
5. **Calculate Cp and Cpk** if spec limits are provided and the process is stable. If not stable, state capability analysis is deferred.
6. **State the capability conclusion** using the threshold table.
7. **Recommend the improvement path** — tamper warning if appropriate, centering recommendation if Cp >> Cpk, variation-reduction recommendation if Cp is low.
8. **Close** with the shared closing block, specific to this analysis.

Data-safety line: *"Share measurement values and sequence — leave out proprietary product names or customer-specific tolerances if those are sensitive; spec limits expressed as ± values are fine."*

## Quality bar

- Chart type is explicitly named with the rationale stated.
- Control limits are calculated from the data, not set to match spec limits — any suggestion to do otherwise is corrected.
- All four Western Electric rules are applied and each violation is identified by rule number and data point.
- The stability conclusion (in control / out of control) is stated explicitly — never left implicit.
- Cp and Cpk are both calculated when spec limits are available; neither is omitted.
- Cp and Cpk are interpreted together — the centering gap (Cp − Cpk) is called out when it is meaningful.
- Capability analysis is withheld or flagged as provisional if the process is not in statistical control.
- Any control limits calculated from fewer than 20 points are labeled provisional.
- The tamper warning is issued if the user proposes adjusting a process that shows only common cause variation.

## Closing block

Append the block from `docs/CLOSING-BLOCK.md`, filled in for this analysis. The first bullet under "what still needs a human" should name the most important unverified special cause — the signal that, if investigated, would most change the process improvement path.

## Examples

- `resources/examples/control-chart-fill-weight.md` — I-MR chart on fill weight data, Rule 2 triggered (shift in mean after material lot change), Cp and Cpk calculated after removing out-of-control points, centering action recommended.
- `resources/examples/control-chart-cycle-time.md` — X-bar/R chart on cycle time subgroups, Rule 4 triggered (alternating pattern from two-shift process), tamper warning issued after operator had been adjusting machine settings in response to individual readings.
