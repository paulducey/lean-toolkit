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

## How this skill works

**Open with one sentence the first time:** "Tell me the job, who does it best, and what you timed — and I'll build the combination sheet; say *just draft it* and I'll draft from what you have."

1. **Read everything given** — observations, timings, the current sequence, demand and available time.
2. **Ask up to three questions:** who performs this job best and was that the person observed; how many cycles were timed and by whom; available time and demand for takt.
3. **Escape hatch:** on "just draft it" → draft the combination sheet now. Any step not timed is `[NEEDS GEMBA: time this step]`; takt without demand or available time is `[NEEDS GEMBA: demand / available time]`. Never fill a time from the tool's idea of how the job usually goes.
4. **Every time carries a source** — `[observed, n cycles, date]`, `[from system]`, `[user estimate]` — and the modal time is used, not the average.
5. **Say in one line** if what's really needed is a JBS (→ `twi-jbs`) or a procedure manual, and **close** with the shared closing block.

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
2. Cycle time is observed (modal of 5+ cycles) and documented with observation date and observer role — or marked `[NEEDS GEMBA: time this step]`, never estimated.
3. Work sequence lists steps at the action level, not task level.
4. Standard WIP is explicitly stated, even if it is 1.
5. The combination sheet is posted at the workstation, not stored in a binder.
6. The document has a revision date — it is not undated.
7. Cycle time is ≤ takt time; if not, the gap is explicitly noted and an improvement action is open.

---

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

Append the block from `docs/CLOSING-BLOCK.md`, filled in for this run.

---

## Examples

- `resources/examples/standard-work-welding-cell.md` — combination sheet for a 4-step weld operation
- `resources/examples/standard-work-kitting.md` — material handler kitting route with walk time analysis
- `resources/examples/standard-work-inspection-station.md` — inspection sequence with go/no-go criteria
