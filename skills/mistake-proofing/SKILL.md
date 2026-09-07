---
name: mistake-proofing
description: Design error-proofing (poka-yoke) solutions for specific error modes — classifying each by the five-level hierarchy from Elimination through Prevention, Detection, Mitigation, to Procedure — and produce implementation-ready solutions for each error mode. Use when someone says "mistake-proof", "poka-yoke", "error-proof", "how do we prevent this from happening again", "idiot-proof", "we keep making this mistake", "operators keep forgetting to", "wrong part installed", "step was skipped", "we need to prevent errors not just catch them", or when a root cause analysis or FMEA points to an error-proofing solution.
license: MIT
---

# Mistake-Proofing (Poka-Yoke)

The goal of mistake-proofing is to make errors impossible or immediately obvious — not to rely on people being careful. Human attention is finite, variable, and degrades under repetition, stress, and time pressure. A process that depends on attention to prevent errors will eventually fail. A well-designed poka-yoke removes attention from the equation entirely: the correct outcome happens automatically, or the incorrect outcome is physically impossible.

## When to use / when not to

Use it when a `root-cause` or `fmea-builder` analysis identifies a specific error mode that needs to be prevented or detected, when an error has recurred after previous corrective action, or when designing a new process step and wanting to build error prevention in from the start.

Don't use it to investigate why an error is occurring (→ `root-cause`), to assess the full risk landscape of a process before deciding where to focus (→ `fmea-builder`), or to document the standard method after mistake-proofing is in place (→ `standard-work`). If the error mode also involves workplace organization or visual management gaps, connect to `5s-audit`.

## The five-level hierarchy

Mistake-proofing solutions are not equal. The hierarchy defines their strength — higher levels are more reliable and do not depend on people remembering to use them. Always work from the top down: can the error be eliminated? If not, can it be prevented? Only descend to lower levels when higher levels are genuinely infeasible.

**Level 1 — Elimination:** Redesign the product, process, or equipment so the error mode cannot exist. No error is possible because the opportunity for the error has been removed.
*Examples: redesign a part so it has only one possible orientation; combine two steps that were being done in the wrong sequence into one automated step; remove a process step that was a source of omission errors.*

**Level 2 — Prevention:** The process is designed so the incorrect action is physically impossible or automatically blocked. The correct outcome happens; the incorrect outcome cannot.
*Examples: asymmetric pins that make incorrect assembly physically impossible; interlocks that prevent the next step until the current step is verified complete; go/no-go gauges that block a non-conforming part from proceeding.*

**Level 3 — Detection:** The error or its conditions are detected immediately — before the work moves to the next step or the next operator. Detection at the point of occurrence is far superior to detection downstream.
*Examples: sensors that detect the presence or absence of a component; vision systems that verify correct assembly; checklists embedded in equipment software that require confirmation before the machine cycles; light curtains that detect missing fasteners before the fixture opens.*

**Level 4 — Mitigation:** The error is not prevented or immediately detected, but its effects are reduced so the consequences are minimized.
*Examples: secondary seals that contain a leak; fuses that protect against downstream circuit damage; overflow containers that catch spills before they reach the floor.*

**Level 5 — Procedure:** A written step, verbal reminder, or manual checklist is added to the process. Relies entirely on human compliance and attention.

**"Add a checklist step" is Procedure level — Level 5, the weakest form.** Never call it mistake-proofing. A procedure depends on attention and compliance; it does not error-proof the process. If a procedure is the current state, the question is: what Level 1–4 solution would make the procedure unnecessary?

## Error taxonomy

Classify each error mode before designing a solution. Knowing the error type narrows the solution space.

| Error type | Definition | Common causes |
|---|---|---|
| Wrong item | Incorrect part, material, ingredient, or information used | Similar-looking items stored together; no differentiation at point of use |
| Omission | A required step, component, or action was skipped | No mechanism to confirm completion; interruptions; no visual indicator of state |
| Sequence error | Steps performed out of order | Steps look independent; no interlocking between steps; untrained operator |
| Timing error | Action performed too early, too late, or for wrong duration | No timer or limit control; operator judgment required; inconsistent feedback |
| Quantity error | Wrong number of units, fasteners, doses, or repetitions | No count verification; no dispenser control; manual counting |
| Extra action | An unnecessary step is added — a component added that shouldn't be, or a step repeated | Unclear standard; incorrect habit; no status indicator showing the step is already done |

## How this skill works

**Open with one sentence the first time:** "Describe the error — what's happening, where in the process, and how it's being caught now (or not) — and I'll design a solution."

1. **Read everything given.** Identify the error mode, the process step, and current detection (or lack of it).
2. **Classify the error type** from the taxonomy. State which type it is and why.
3. **Work down the hierarchy** from Level 1. For each level, ask whether a solution at that level is feasible — and say so explicitly. Do not skip to Procedure without showing why Level 1–4 solutions are infeasible.
4. **Design at least one concrete solution** per feasible level. Solutions should be specific enough to evaluate for implementation — not "use a sensor" but "add a presence sensor at Station 3 that detects the gasket before the lid press cycles."
5. **Note implementation requirements** — tooling, equipment modification, software change, layout change, cost tier (low/medium/high as a rough guide).
6. **For each solution, state what it eliminates from the operator's cognitive load** — what the operator no longer has to remember, count, check, or decide.
7. **Close** with the shared closing block, specific to this analysis.

Data-safety line: *"Describe the error mode and process step in functional terms — leave out proprietary product specifications or supplier names."*

**Escape hatch:** on "just draft it" → propose solutions at the highest feasible levels from the information given, mark assumptions `[ASSUMED]`, and flag where a gemba observation would most improve the solution.

## Solution output format

```
Error mode: [specific description]
Error type: [from taxonomy]
Process step: [where it occurs]
Current detection: [how it's caught now, or "none"]

| Level | Feasibility | Proposed Solution | What Operator No Longer Needs to Do | Implementation Notes |
|-------|-------------|-------------------|--------------------------------------|---------------------|
| 1 — Elimination | [Feasible / Not feasible — reason] | [solution or why not] | | |
| 2 — Prevention | [Feasible / Not feasible — reason] | [solution or why not] | | |
| 3 — Detection | [Feasible / Not feasible — reason] | [solution or why not] | | |
| 4 — Mitigation | [Feasible / Not feasible — reason] | [solution or why not] | | |
| 5 — Procedure | [Fallback only] | [if used, state why higher levels are not feasible] | | |
```

Produce one solution table per error mode. If multiple error modes are provided, produce a table for each.

## Common mistake-proofing patterns by error type

These are starting points, not exhaustive lists. Always adapt to the specific process.

**Wrong item:** color-coding at point of use; shape differentiation (keying); separate storage locations that make picking the wrong item physically difficult; label verification at point of use; kitting upstream so only the correct items arrive at the workstation.

**Omission:** presence sensors that verify completion before allowing advance; sequence-enforcing fixtures that cannot be closed until all components are loaded; visual indicators (andon lights, shadow boards) that show incomplete state; poka-yoke kits where leftover parts signal a missed step.

**Sequence error:** physical interlocks that prevent Step B until Step A is confirmed; single-piece flow that forces sequence; labeled staging locations that make out-of-sequence work visible immediately.

**Timing error:** timers with audible or visual alarms built into the fixture or equipment; cycle time controls on automated equipment that enforce dwell time; process locks that cannot be opened until a timer expires.

**Quantity error:** dispensers pre-loaded with the correct quantity (torque controlled, pre-counted kits, pre-measured doses); counters integrated into the tool or fixture; tray designs with fixed quantity slots.

**Extra action:** status indicators that show "already done" (filled light, turned indicator, locked position); fixtures that physically block a second operation; automated equipment that rejects re-entry.

## The checklist test

Before proposing any Procedure-level solution, apply this test: *"If the operator is distracted, tired, or rushed, does this solution still prevent the error?"* If the answer is no — the solution depends on the operator choosing to consult it — it is a procedure, not mistake-proofing. Label it honestly. Then ask what Level 1–4 solution would make the procedure unnecessary.

## Quality bar

- Every error mode is classified by error type from the taxonomy before solution design begins.
- The hierarchy is worked top-down — each level's feasibility is addressed, not skipped.
- At least one solution at Level 2 or above is proposed for every error mode, or an explicit reason is given for why Levels 1–3 are infeasible.
- No solution is labeled mistake-proofing if it depends on operator attention or compliance — Procedure-level solutions are labeled as such.
- Each proposed solution states what cognitive burden it removes from the operator.
- Implementation notes include at least a rough indicator of effort (low/medium/high) and what type of change is required (equipment, tooling, layout, software).
- Solutions at Level 3–4 that only catch errors downstream (after the next station or after the customer) are noted as inferior to solutions that catch at the point of occurrence.

## Closing block

Append the block from `docs/CLOSING-BLOCK.md`, filled in for this analysis. The first bullet under "what still needs a human" should name the highest-level feasibility judgment that most needs gemba verification — the Level 1 or Level 2 solution that looks feasible from the description but requires seeing the physical process to confirm.

## Examples

- `resources/examples/mistake-proofing-assembly-omission.md` — omission error (gasket skipped during assembly) analyzed top-down, Level 2 prevention solution designed using a presence sensor, Procedure-level fallback documented for the transition period.
- `resources/examples/mistake-proofing-wrong-item-kitting.md` — wrong-item error in a multi-SKU pick process, Level 1 elimination attempted (kit redesign), Level 2 prevention designed using dedicated storage lanes with physical keying, Level 5 procedure noted as insufficient and labeled explicitly.
