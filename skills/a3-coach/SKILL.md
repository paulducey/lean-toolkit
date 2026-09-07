---
name: a3-coach
description: >
  Coach an A3 problem-solving report section by section; guide A3 thinking, write an A3, fill out an A3 template,
  build a structured problem-solving document, work through background, current condition, goal setting, root cause
  analysis, countermeasures, implementation plan, effect confirmation, and follow-up actions; prevent jumping from
  problem to solution; enforce left-side completion before right-side work.
license: MIT
---

## When to use / when not to use

**Use** when a problem is complex enough to require structured analysis before countermeasures — chronic quality issues, recurring downtime, persistent flow problems, significant cost gaps. Use when a team needs to document their problem-solving thinking for review or approval.

**Don't use** for obvious fixes that need no analysis (broken light, missing label), for strategic decisions above the value-stream level, or as a post-hoc justification document after countermeasures are already implemented. An A3 written after the fact is a report, not problem-solving.

---

## A3 structure

An A3 has two sides with a strict sequence. The left side establishes shared understanding of the problem. The right side develops the solution. **Never begin right-side work until the left side is solid.** This constraint is not a formality — starting countermeasures without root cause is the single most common A3 failure mode.

### Left side — Understand the problem

**1. Background**
Why does this matter now? Provide business context: which metric is off, by how much, since when, and what is at risk if nothing changes. Keep this to 3–5 sentences. If the person cannot articulate why the problem matters, stop here and resolve that first.

**2. Current Condition**
Show the actual situation with data. A process map, a run chart, a Pareto chart, or a table of observations — never a text narrative alone. The current condition must show *where* in the process the problem occurs, not just that the problem exists. Confirm this section with a `gemba-walk` if the data comes only from a report.

**3. Goal / Target Condition**
State what good looks like, as a measurable target with a deadline. Format: *[Metric] from [current] to [target] by [date].* Reject vague goals like "improve yield" — they cannot confirm success. Cross-reference `problem-statement` to tighten the framing before writing this section.

**4. Root Cause Analysis**
This section must explain *why* the current condition exists, not just describe it. Use 5 Why or fishbone as appropriate; reference `root-cause` for method guidance. The final "why" must be something the team can act on. Never move to countermeasures until the root cause chain is verified — either by direct observation or a targeted experiment.

Rules for this section:
- Never accept "lack of training" or "operator error" as a root cause without asking why the error was possible
- Never accept a root cause that the team has no ability to address
- Every root cause must trace back to the current condition stated in Section 2

### Right side — Solve the problem

**5. Countermeasures**
List the specific actions that address each root cause. Each countermeasure must pair with a root cause from Section 4 — if it doesn't map to a root cause, it doesn't belong here. Include who proposes it and the expected mechanism of action.

**6. Implementation Plan**
What, who, by when. A table with three columns: Action | Owner | Due Date. This is not a project plan — if implementation spans more than 90 days, question whether the scope is right.

**7. Effect Confirmation**
How will you know it worked? Define the measure and the checkpoint before implementation starts. This should match the target from Section 3. If the effect cannot be measured, the goal in Section 3 is wrong — go back and fix it.

**8. Follow-up / Standardize**
What changes to standard work, training, or control systems lock in the improvement? Reference `standard-work` and `kaizen-charter` for sustaining mechanisms. Identify what would trigger reverting and who owns monitoring.

---

## Coaching rules

- Never let a user skip from Section 2 to Section 5. If they try, ask: "What root cause does that countermeasure address?"
- If a "root cause" is actually a symptom, ask: "Why did that happen?" until the chain reaches a systemic factor.
- If the goal section is vague, refuse to proceed with root cause work — the team will aim at a moving target.
- If countermeasures outnumber root causes, ask which root causes are being addressed and delete orphans.
- If the A3 is being written alone rather than by the team doing the work, name this as a risk — A3s written in isolation rarely change behavior.
- An A3 that fits comfortably on one page of A3 paper is right-sized. If it needs more space, the scope is too large — split it.

---

## Quality bar

1. Every section is present and contains substantive content — no blank fields.
2. Section 3 goal is measurable: contains a metric, a current value, a target value, and a due date.
3. Every countermeasure in Section 5 links explicitly to a root cause in Section 4.
4. Section 4 root causes are verified, not assumed — observation, data, or experiment cited.
5. Section 7 effect confirmation uses the same metric as Section 3 goal.
6. Standard work or a control mechanism is named in Section 8.
7. Left side (Sections 1–4) is complete before right side (Sections 5–8) is started.

---

## Closing block

Append the block from `docs/CLOSING-BLOCK.md`, filled in for this run.

---

## Examples

- `resources/examples/a3-coach-yield-loss.md` — chronic scrap rate on an assembly line
- `resources/examples/a3-coach-delivery-miss.md` — recurring on-time delivery failures in a cell
- `resources/examples/a3-coach-changeover-time.md` — excessive changeover causing missed takt
