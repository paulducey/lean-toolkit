---
name: smed-setup
description: Analyze and reduce equipment changeover time using the Single-Minute Exchange of Die (SMED) method — separating internal from external elements, converting internal to external, and streamlining what remains — then calculate the production capacity gained. Use when someone says "changeover", "setup time", "SMED", "die change", "product changeover", "flavor changeover", "size changeover", "we lose too much time switching products", "setup reduction", or describes a process where transitions between runs consume significant time that could be producing output.
license: MIT
---

# SMED Setup Reduction

Every minute of changeover time is a minute the machine is not making what the customer wants. SMED (Single-Minute Exchange of Die) is the systematic method for reducing that time — not by working faster, but by redesigning what happens and when. The core insight is that most changeover time is spent doing things inside the changeover window that could be done before or after it, or eliminated entirely.

## When to use / when not to

Use it when changeover time is a meaningful constraint — when it limits run frequency, forces large batches, reduces available production time, or appears as a significant OEE loss. Use it with filmed observation data when available; use it with interview data when it's not.

Don't use it to model the broader capacity picture without changeover (→ `capacity-planner`), to calculate current OEE losses from changeover (→ `oee-from-csv`), or to document the resulting standard changeover process after improvements are made (→ `standard-work`). If the changeover is a VSM activity, connect the results to `vsm-calc`.

## The three-phase SMED method

**Phase 1 — Separate internal from external elements**

This is the single highest-leverage step. It routinely yields 30–50% reduction before anything else is changed.

- **Internal elements** can only be done while the machine is stopped. The machine must be down.
- **External elements** can be done before shutdown or after restart — while the machine is still running.

Most operations have never made this distinction. Elements that appear internal (finding tools, staging materials, confirming specs) are often external — they only happen during downtime because no one has moved them.

**Phase 2 — Convert internal elements to external**

For every element that is currently internal, ask: *What would have to be true for this to happen before the machine stops?* Common conversions:

- Pre-staging materials, tooling, and fixtures before shutdown begins
- Pre-heating, pre-setting, or pre-measuring offline
- Completing paperwork, work orders, and quality documentation before or after — not during
- Performing equipment inspections on the outgoing run rather than after shutdown

**Phase 3 — Streamline all elements**

Once the internal/external separation is clean, reduce the time of each remaining element:

- Eliminate adjustments by using pre-set tooling, gauges, and fixtures (adjustments are the most common source of extended changeover)
- Replace fasteners that require multiple turns with quarter-turn or snap fasteners
- Use functional clamps in place of threaded bolts wherever possible
- Build standardized carts or kits so everything needed is in one place at changeover time
- Create visual standards so anyone can verify correct setup without guessing or measuring repeatedly

## How this skill works

**Open with one sentence the first time:** "Tell me about the changeover — what machine or process, what you switch between, roughly how long it takes now, and how you know what's happening (video, observation notes, or memory) — and I'll help you find the time."

1. **Read everything given.** Identify the machine or process, the changeover type (product, size, flavor, material, tooling, etc.), current changeover time, and the data source.
2. **Clarify the data source.** Filmed observation is the most reliable — elements are timed to the second. Interview or memory data introduces gaps and optimism; mark these `[ESTIMATED — verify with observation]`.
3. **Escape hatch:** on "just draft it" → build the element list from what's given, mark unknowns, and still estimate a reduction range from available data.
4. **Build the element list** — every discrete step in the current changeover, with current time (actual or estimated) and initial classification (Internal / External / Unknown).
5. **Challenge every internal classification.** For each element, ask: *Could this happen while the machine is still running — with the right preparation?* Never accept "that's how we've always done it" without testing whether the element is truly constrained to downtime. Apply the rule: an element is only truly internal if the machine must be stopped for physical or safety reasons. Convenience, habit, and sequence assumptions are not physical constraints.
6. **Calculate Phase 1 savings** — sum of all converted elements.
7. **Build Phase 2 and 3 improvements** — for each remaining internal element, recommend the streamlining approach.
8. **Run the capacity math** — calculate production time gained per changeover event and per week/shift.
9. **Close** with the shared closing block, specific to this analysis.

Data-safety line: *"Leave out proprietary product names or formulations; machine type, process step, and time data are fine."*

## Element classification table format

```
Machine/Line: [identifier]
Changeover type: [e.g., product A → product B]
Current total changeover time: [minutes]
Data source: [filmed observation / interview / estimate]

| # | Element Description | Current Time | Classification | Phase 2 Action | Target Time |
|---|---------------------|-------------|----------------|----------------|-------------|
| 1 | [step]              | [min:sec]   | Internal / External | [if converting] | [min:sec] |
```

Mark any estimated time with `[EST]`. Mark any classification requiring verification with `[VERIFY]`.

## Capacity math

After building the improvement plan, calculate what the reduction is worth in production time:

```
Current changeover time:          [A] minutes
Target changeover time:           [B] minutes
Time saved per changeover:        [A − B] minutes
Changeovers per shift/week:       [C]
Production time recovered:        [(A − B) × C] minutes per shift/week
At [takt time or cycle time]:     [recovered minutes ÷ cycle time] additional units possible
```

If the user has OEE data, connect this to `oee-from-csv` to model the effect on availability.
If this is part of a value stream, connect to `vsm-calc` to show the batch-size and lead-time implications of shorter changeover.

## The adjustment elimination principle

If a single improvement should be prioritized above all others, it is this: **eliminate adjustments**. Adjustments — trial runs, tweaks, re-checks, fine-tuning — account for the majority of extended changeover time in most processes. They exist because:

- Tooling or fixtures are not pre-set to a known position
- Setup dimensions are not documented to a usable tolerance
- Worn tooling or equipment variation makes the same setup produce different results each time

An adjustment is a signal that the process is not robust enough to set up without feedback. Every adjustment should be treated as a defect to be designed out, not a step to be optimized.

## The internal-only rule

An element is only genuinely internal if:

1. The machine must be physically stopped for safety reasons (lockout/tagout, guarding, access), OR
2. The machine must be stopped because the part or material being changed is in motion during operation, OR
3. The machine must be stopped because measurement or verification requires zero-speed conditions.

Everything else — including "we need the machine stopped to concentrate," "it's easier when it's not running," or "we do it that way because we always have" — is a candidate for conversion to external. Flag these explicitly and recommend testing the conversion before writing it off as impossible.

## Quality bar

- Every element in the current changeover is listed — not grouped into vague categories like "setup."
- Internal vs. external classification is applied to every element, not just the obvious ones.
- No element is classified as internal solely due to habit, convenience, or tradition — each internal classification states the physical or safety reason.
- Phase 1 savings are calculated from actual converted elements, not estimated as a percentage.
- At least one adjustment-elimination recommendation is included if any adjustments appear in the current element list.
- The capacity math shows time recovered per changeover event and per planning period (shift or week).
- Any time data from interview or memory is marked `[EST]` — the analysis does not treat estimates as precise measurements.
- The recommended next step is specific: which elements to observe, convert, or trial first — not "run SMED on the process."

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

Append the block from `docs/CLOSING-BLOCK.md`, filled in for this analysis. The first bullet under "what still needs a human" should name the most significant unverified internal-to-external conversion — the one that, if it turns out to be truly internal, would materially change the projected savings.

## Examples

- `resources/examples/smed-setup-packaging-line.md` — 47-minute changeover on a packaging line reduced to 19 minutes using filmed observation, Phase 1 conversion of pre-staging elements, and adjustment elimination through pre-set tooling.
- `resources/examples/smed-setup-interview-data.md` — analysis built from supervisor interview, estimates marked throughout, priority verification list produced, capacity math run on best-case and conservative scenarios.
