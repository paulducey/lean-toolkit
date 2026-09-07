---
name: standard-work
description: >
  Build a standard work document; create a standard work combination sheet; capture takt time, cycle time, and
  work sequence; define standard WIP; document the best current method at the workstation; standardize a process;
  write a standard operating procedure for the floor; create a job breakdown sheet; establish standard work for
  an operator; capture repeatable work sequence.
license: MIT
---

## When to use / when not to use

**Use** when documenting the current best method for a repeatable manual process — assembly, inspection, material handling, machine tending, or any work where operator-to-operator variation creates quality or flow problems. Use as a precondition for improvement: you cannot improve what is not yet standard.

**Don't use** for knowledge work, creative tasks, or processes with legitimate high variation in every cycle. Standard work requires a repeatable cycle. Don't use for engineering design, sales calls, or any process where every instance is genuinely unique. Don't confuse standard work with a procedure manual — if it's meant to sit in a binder, it's not standard work.

---

## The three elements of standard work

Standard work is not a document type — it is the precise definition of three things. All three must be present. Missing any one of them produces a procedure, not standard work.

### 1. Takt time and cycle time

**Takt time** = available production time ÷ customer demand rate

Takt time is the rhythm of the customer. It does not change when the process changes — it changes when demand changes. Always state takt time in seconds per unit.

**Cycle time** = actual time to complete one cycle of the defined work sequence

Cycle time is measured, not calculated. Observe the operator performing the full cycle at least 5–10 times. Use the *modal* time (most frequently occurring), not the average and not the best time. The modal time reflects the real method; the average blends good cycles with interrupted ones.

The goal: cycle time ≤ takt time. When cycle time > takt time, the station cannot meet demand and is the constraint. When cycle time < takt time significantly, the station has capacity that may be rebalanced.

### 2. Work sequence

The exact sequence of steps the operator performs to complete one unit, in the order performed. Not the order the engineer intended — the order actually performed today, by the operator doing it best.

Rules for capturing work sequence:
- Observe the actual sequence; do not reconstruct it from memory or the process sheet
- Separate manual work time, walk time, and machine/wait time in the combination sheet
- Sequence steps at the action level: "pick part from bin," "insert into fixture," "apply torque" — not at the task level: "load machine"
- Note hand (left/right) for two-handed work if relevant to quality or safety

### 3. Standard WIP (Work in Process)

The minimum number of work pieces in the process at any time to allow the operator to complete the sequence without waiting. Standard WIP is not inventory — it is the minimum required to keep the work flowing through the cycle.

In many single-piece-flow cells, standard WIP = 1 unit in-process. In cells with machine cycle time > operator cycle time, standard WIP may be higher. Document it explicitly — "2 units between stations 3 and 4 during machine cycle."

---

## Standard work combination sheet

The primary output document. One sheet per operator, per process. Contains:

| Column | Content |
|--------|---------|
| Step # | Sequence number |
| Step description | Action-level description |
| Manual time | Bar (solid) — operator touch time |
| Walk time | Bar (dashed) — operator travel time |
| Machine time | Bar (wavy) — auto/wait time |
| Cumulative time | Running total vs. takt time line |

The takt time line runs vertically across the time axis. Steps that cross the line are where the operator is at risk of missing takt.

The combination sheet is a floor document. Print it, laminate it, post it at the station. If it lives in a binder, it is not serving its purpose. If it has not been reviewed since the last kaizen, treat it as a draft until verified.

---

## Key rules

- **Captures the best current method, not the average and not the theoretical.** Ask: "Who does this best?" Observe that person. Document what they do.
- **Floor document, not procedure manual.** If you cannot see it from the workstation, it is not standard work.
- **Standard work is the baseline for improvement, not the ceiling.** Every kaizen event should update the standard work sheet. An unchanged standard work document after a kaizen means either nothing changed or the document was not updated — both are problems.
- Never write standard work from memory. Always observe. Reference `gemba-walk` for observation discipline.
- When standard work is absent or ignored, `twi-jbs` (Training Within Industry Job Breakdown Sheet) is the tool for training to the standard. Standard work documents what to do; TWI documents how to teach it.

---

## Quality bar

1. Takt time is calculated from actual available production time and actual demand — not from theoretical capacity.
2. Cycle time is observed (modal of 5+ cycles) and documented with observation date and observer name.
3. Work sequence lists steps at the action level, not task level.
4. Standard WIP is explicitly stated, even if it is 1.
5. The combination sheet is posted at the workstation, not stored in a binder.
6. The document has a revision date — it is not undated.
7. Cycle time is ≤ takt time; if not, the gap is explicitly noted and an improvement action is open.

---

## Closing block

Append the block from `docs/CLOSING-BLOCK.md`, filled in for this run.

---

## Examples

- `resources/examples/standard-work-welding-cell.md` — combination sheet for a 4-step weld operation
- `resources/examples/standard-work-kitting.md` — material handler kitting route with walk time analysis
- `resources/examples/standard-work-inspection-station.md` — inspection sequence with go/no-go criteria
