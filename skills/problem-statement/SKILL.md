---
name: problem-statement
description: >
  Write a problem statement; define the problem clearly; scope a problem using IS/IS-NOT; apply SMART criteria
  to a problem statement; validate a problem statement; avoid solution-embedded problem statements; identify the
  gap between current condition and target; frame a problem for root cause analysis or A3; write a one-sentence
  problem statement; prevent jumping to solutions.
license: MIT
---

## When to use / when not to use

**Use** before starting any structured problem-solving — root cause analysis, A3, kaizen charter — to ensure the team is solving the right problem at the right scope. A weak problem statement causes wasted effort on the wrong cause or the wrong scope. Spend time here to save time everywhere else.

**Don't use** as a standalone deliverable when what's needed is a full A3 (reference `a3-coach`) or a root cause analysis (reference `root-cause`). The problem statement feeds those tools — it does not replace them.

---

## IS / IS-NOT scoping

IS/IS-NOT is a structured technique to define the boundaries of the problem before analysis begins. It prevents scope creep and focuses data collection. Apply it along four dimensions:

| Dimension | IS (observed) | IS NOT (not observed, but plausible) |
|-----------|--------------|--------------------------------------|
| **Object** | Which specific product, part, machine, or process has the problem? | What similar objects do not have the problem? |
| **Location** | Where does the problem occur — which station, line, plant, shift? | Where does it not occur? |
| **Time** | When did it start? What pattern — shift, day of week, after changeover? | When does it not occur? |
| **Magnitude** | How large is the problem? Rate, frequency, cost? | What portion of output is unaffected? |

The IS/IS-NOT comparison is where the problem statement gets its power. If defects occur on Line 3 but not Lines 1 and 2 (IS NOT), the root cause is almost certainly something specific to Line 3. If defects occur only on the morning shift (IS NOT: afternoon shift), the cause is likely in the setup or handoff. The contrast generates hypotheses before root cause analysis begins.

Rules:
- Fill in the IS NOT column with genuine observations, not guesses. "We haven't checked Line 1" is not the same as "Line 1 does not have the problem."
- If you cannot identify anything in the IS NOT column, the scope is probably too broad. Tighten it.

---

## SMART validation

After drafting the problem statement, validate it against five criteria:

| Criterion | Test |
|-----------|------|
| **Specific** | Does it name the exact object, location, or condition — not "some defects" but "solder bridging on PCB-12 at Station 7"? |
| **Measurable** | Does it include a quantified baseline — a rate, count, cost, or time value? |
| **Actionable** | Is the problem within the team's scope to investigate? If the root cause is entirely outside the team's control, escalate before analyzing. |
| **Relevant** | Is this problem tied to a metric or outcome that matters — safety, quality, delivery, cost? |
| **Time-bound** | Does it state when the problem started, or over what time period the baseline was measured? |

A problem statement that fails any of these criteria is not ready for root cause analysis.

---

## The four traps

**Trap 1: Solution embedded in the problem**
Wrong: "We need to implement a poka-yoke to prevent Part 44 from being installed backwards."
Right: "Part 44 is installed backwards on 3.2% of units on Line B, averaging 14 occurrences per day."
The solution (poka-yoke) may be correct, but embedding it in the problem statement closes off analysis before it begins.

**Trap 2: Cause stated as the problem**
Wrong: "Operators are not following the torque specification."
Right: "Bolted joints on Assembly X are failing final torque verification at a rate of 8%, up from 1% six weeks ago."
"Operators not following spec" is a hypothesis about cause, not an observed problem. State what you observe, not why you think it happens.

**Trap 3: Scope too broad**
Wrong: "Our quality is poor."
Right: "Weld spatter on Product Family C has exceeded the 2% defect rate threshold for 6 of the last 8 weeks, averaging 3.7%."
Broad problem statements produce broad root causes and ineffective countermeasures. Use IS/IS-NOT to narrow the scope until it is actionable.

**Trap 4: No measurable baseline**
Wrong: "Changeover times are too long."
Right: "Changeover time on Press 4 averages 87 minutes over the last 30 changeouts, against a target of 45 minutes."
Without a baseline, there is no way to confirm that countermeasures worked. Reference `control-chart` for baseline data analysis if the measure has significant variation.

---

## Output format

The output is one sentence, structured as:

> **[What]** is occurring at **[magnitude/rate]** at **[location]** since **[when]**, against a target/expectation of **[target]**.

Example:
> Solder bridging defects on PCB-12 are occurring at 4.1% of units on Line 3, morning shift only, over the past three weeks, against a target of ≤0.5%.

This one sentence feeds directly into the Background and Current Condition sections of an A3. Reference `a3-coach` for what comes next.

---

## Quality bar

1. Problem statement contains a measured baseline value, not a range or subjective description.
2. No solution language appears anywhere in the problem statement.
3. No causal language appears — no "because," "due to," or "caused by."
4. IS/IS-NOT is completed with observed data in the IS NOT column, not assumptions.
5. The scope is narrow enough that a single team can investigate it within 2–4 weeks.
6. The statement passes all five SMART criteria.
7. The output is one sentence — if it requires more, the scope needs to be split.

---

## Closing block

Append the block from `docs/CLOSING-BLOCK.md`, filled in for this run.

---

## Examples

- `resources/examples/problem-statement-solder-defects.md` — electronics assembly scoping with IS/IS-NOT
- `resources/examples/problem-statement-late-deliveries.md` — delivery performance problem scoped to shift and route
- `resources/examples/problem-statement-machine-downtime.md` — unplanned downtime scoped from broad complaint to specific failure mode
