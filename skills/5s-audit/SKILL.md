---
name: 5s-audit
description: Conduct a structured 5S workplace organization audit — Sort, Set in Order, Shine, Standardize, Sustain — scoring each pillar 0–3 per zone, producing a scored audit table with gaps and prioritized improvement actions. Use when someone says "5S audit", "workplace organization", "we need to clean up the floor", "things are hard to find", "our area is disorganized", "Seiri Seiton Seiso Seiketsu Shitsuke", "5S assessment", "visual management", or describes a cluttered or unsafe workspace where the condition of the environment is affecting performance.
license: MIT
---

# 5S Audit

A 5S audit is not a cleanliness inspection — it is an assessment of whether the workplace is designed to make correct behavior the easiest behavior. A well-run 5S creates a standard condition that makes abnormalities immediately visible. This skill scores each of the five pillars per zone, identifies gaps, and produces a prioritized action list.

## When to use / when not to

Use it when assessing an existing workplace, launching a 5S program in a new area, preparing for a formal audit, or when performance problems have a visual-management or organization component.

Don't use it to design a new layout from scratch (→ `vsm-calc` for flow design), to run a broader floor walk looking for waste (→ `gemba-walk`), or to document the resulting standard condition after improvements are made (→ `standard-work`). A takt-time, capacity or lead-time question is not a 5S question — say so in one line and hand off to `capacity-planner` or `vsm-calc`.

## The five pillars — definitions

These definitions are the scoring anchor. Auditors routinely inflate scores because they use softer definitions. Hold the line.

| Pillar | Japanese | What it actually means |
|---|---|---|
| Sort | Seiri | Only what is needed for current work is present. Everything else is tagged and removed. |
| Set in Order | Seiton | Every needed item has a designated location, labeled so anyone can find it and return it without asking. |
| Shine | Seiso | Equipment and surfaces are clean and inspected — not merely swept. Cleaning is the act of inspecting. |
| Standardize | Seiketsu | The first three pillars are documented as a visual standard, so the "clean and organized" condition can be recognized and restored by anyone. |
| Sustain | Shitsuke | The standard condition is being maintained through habit, scheduled audits, and management engagement — not by heroic pre-audit cleanup. |

## Scoring scale

**0 — Not present:** No evidence of this pillar. Problems are severe and/or no attempt has been made.
**1 — Attempted:** Some effort visible, but incomplete, inconsistent, or limited to part of the zone.
**2 — Implemented:** The pillar is implemented and working, with minor gaps or inconsistencies.
**3 — Sustained:** Fully implemented, consistently maintained, with evidence that it holds over time without intervention.

**Critical scoring rule — Sustain cannot exceed the lowest of the other four pillars.** A Sustain score of 3 requires Sort, Set in Order, Shine, and Standardize all at 3. If Sort scores 1, Sustain cannot score above 1. This rule exists because you cannot sustain what you haven't established.

## How this skill works

**Open with one sentence the first time:** "Describe the area — what's there, how many zones, and what you're seeing — and I'll build the audit."

1. **Read everything given.** Identify the zones to be audited (e.g., assembly cell A, tool crib, warehouse aisle 3).
2. **Ask for data** if zone count or observable conditions haven't been described. One focused question only: "What zones are you auditing, and what's the current condition — can you walk me through what you see or have observed?"
3. **Escape hatch:** on "just draft it" or similar → score from what's been given, mark unknowns `[NEEDS OBSERVATION]`, and still flag which cells most need on-site verification.
4. **Score each pillar for each zone** using the 0–3 scale. Enforce the Sustain cap rule — state it explicitly in the table when it applies.
5. **Calculate the zone total** (max 15 per zone) and the audit total. Do not average across zones — a zone scoring 3/15 is a failure even if other zones score well.
6. **Build the gap table** — for each pillar score below 3, write one specific, observable gap description.
7. **Prioritize actions** — rank by impact on safety first, then on quality and flow, then on general organization.
8. **Close** with the shared closing block, specific to this audit.

Data-safety line, used whenever asking for documents or photos: *"Leave out any personally identifiable information; area names, zone codes, and equipment IDs are fine."*

## Shine is inspection — the most important mindset shift

The most common 5S misconception: Shine means "keep it clean." The correct interpretation: **cleaning is inspection**. When team members physically wipe down a machine, they find oil leaks, loose fasteners, worn seals, frayed wiring, and cracks that would otherwise go unnoticed until failure.

A Shine score of 3 means team members are cleaning equipment with a purpose — they know what normal looks like and flag abnormalities when found. A score of 2 or below means the cleaning is cosmetic only, or inconsistent. When scoring Shine, ask: "Does cleaning here reveal equipment problems before they cause downtime or defects?"

If Shine reveals equipment problems, those problems belong in `root-cause` or `fmea-builder` — this skill documents the condition, not the fix.

## Audit table format

```
Zone: [Zone name]
Date: [date]
Auditor: [role or initials]

| Pillar          | Score (0–3) | Key Observation |
|-----------------|-------------|-----------------|
| Sort            |             |                 |
| Set in Order    |             |                 |
| Shine           |             |                 |
| Standardize     |             |                 |
| Sustain         |             | [cap applied if relevant] |
| ZONE TOTAL      | /15         |                 |
```

Run one table per zone. Do not merge zones into a single table — zone-level scores are the diagnostic unit.

## Gap and action format

For each zone with any pillar below 3, produce a gap table:

```
| Zone | Pillar | Score | Gap Description | Priority Action | Owner (role) | Due |
|------|--------|-------|-----------------|-----------------|--------------|-----|
```

**Priority action rules:**
- Actions addressing safety hazards (tripping, pinch points, blocked exits, chemical exposure) rank first.
- Actions for Sort and Set in Order typically unlock progress on the other pillars — score them second.
- Standardize and Sustain actions should never be written as "make a checklist" without specifying what the checklist must verify. A generic checklist is not a standard.

## Common scoring traps

| Trap | Correction |
|---|---|
| Scoring Sort a 2 because "most" unneeded items are removed | Sort is 2 only if the remaining items are tagged and actively being dispositioned |
| Scoring Shine a 3 after a pre-audit deep clean | Ask: was this cleaned as part of a routine, or for the audit? Evidence of routine is required for a 3 |
| Scoring Sustain higher than the weakest pillar | Apply the cap rule — state it in the table |
| Treating labels as sufficient for Set in Order | Labels on empty locations, or locations that are labeled but frequently empty or doubled-up, are a score of 1 |
| Scoring Standardize a 2 when no visual standard exists | A verbal agreement is not a standard. A posted, dated, visual document is required for a score of 2 or above |

## Connection to other skills

A 5S audit reveals where abnormalities are hiding — but it does not trace causes or design improvements. After scoring:

- Use `gemba-walk` to investigate what's driving the conditions observed.
- Use `standard-work` to document the target condition once Sort, Set in Order, and Shine have been established.
- Use `root-cause` or `fmea-builder` if Shine-as-inspection surfaces equipment defects that are causing quality or safety problems.

## Quality bar

- Every zone has its own scored table — no zone-to-zone averaging or consolidation.
- Every Sustain score has been checked against the four-pillar cap rule; any cap application is noted explicitly.
- Shine observations include whether cleaning is tied to inspection or is cosmetic only.
- Every gap description is observable — specific enough that two auditors on the same day would agree whether the gap exists.
- Priority actions are ordered by safety first, then quality/flow impact.
- No action is written as "maintain 5S" — every action names a specific, verifiable change.
- Standardize gaps are not closed by proposing a generic checklist — the proposed standard must specify what condition it documents.
- The audit total is presented per zone, not as an overall average.

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

Append the block from `docs/CLOSING-BLOCK.md`, filled in for this audit. The first bullet under "what still needs a human" should name the most important unobserved zone or condition — the one that, if scored differently, would change the priority action list.

## Examples

- `resources/examples/5s-audit-assembly-cell.md` — three-zone audit of an assembly cell, Sustain cap applied to two zones, Shine revealing a hydraulic leak, priority actions ordered with safety item first.
- `resources/examples/5s-audit-tool-crib.md` — single-zone tool crib audit from interview data, several cells marked [NEEDS OBSERVATION], gap table driving Set in Order and Standardize actions.
