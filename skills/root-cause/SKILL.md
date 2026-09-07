---
name: root-cause
description: Guide structured root cause analysis — IS/IS-NOT scoping, 5 Whys, fishbone (Ishikawa) diagram, and barrier analysis — then produce a verified root cause and provisional corrective action. Use when someone says "why does this keep happening", "root cause analysis", "RCA", "5 Whys", "fishbone", "Ishikawa", "we keep having this problem", "recurring defect", "recurring incident", "we fixed it and it came back", or describes a repeating problem they can't seem to solve. Coaches on method selection (5 Whys for focused problems, fishbone for multi-factor). Never accepts "operator error" or "human error" as a root cause — always drills to the systemic cause. Does not close until the root cause is verified.
license: MIT
---

# Root Cause Analysis

A fix that doesn't stick almost always means the root cause was never found — only a symptom was addressed. This skill guides structured RCA from problem scoping through verified root cause and provisional corrective action, using the simplest method that fits the situation.

## When to use / when not to

Use it for any recurring defect, incident, near-miss, or "why does this keep happening" question — in manufacturing, healthcare, or any service process.

Don't use it to plan the improvement event that follows (→ `kaizen-charter`), to structure the whole problem on one page for a steering committee (→ `a3-coach`), or to calculate how much loss the problem is causing (→ `oee-from-csv` or `vsm-calc`). If the user is in the middle of a gemba walk and spots the problem, they can describe what they saw and this skill will work with it.

## Method selection — simplest tool that fits

Default to the simpler method. Upsell only when the user's description makes clear the simpler one won't work.

| Situation | Method |
|---|---|
| One clear problem, plausible single causal chain | 5 Whys |
| Multiple simultaneous failures, interdependent factors, or "we don't know where to start" | Fishbone (Ishikawa) |
| A system failure where barriers or safeguards didn't catch the problem | Barrier analysis, after fishbone or 5 Whys identifies the cause |

Say which method you're using and why, in one sentence. Don't run all three on every problem.

## How this skill works

**Open with one sentence the first time:** "Tell me what you've seen — what's happening, where, and how often — and I'll help you find the real cause, not just the symptom."

1. **Read everything given.** Pull out the problem statement, location, frequency, and any data already provided.
2. **Run IS/IS-NOT scoping first** — always, even briefly. Knowing what the problem is *not* is often where the cause hides. Ask at most two questions to complete the scoping.
3. **Select a method** (5 Whys or fishbone) and say why in one sentence.
4. **Escape hatch:** on "just draft it," "skip the questions," or similar → run the analysis from what's been given, mark unknown branches `[NEEDS GEMBA: …]`, and still call out which branches most need field verification.
5. **Run the analysis:**
   - **5 Whys:** chain each Why from the previous answer. Mark any branch where you had to assume `[ASSUMED — verify]`. Never skip a step; never accept a "Why" whose answer is a person failing.
   - **Fishbone:** populate the six categories (Man, Machine, Method, Material, Measurement, Environment). At least two categories must have entries — if only one category has causes, run 5 Whys instead.
   - **Barrier analysis (if appropriate):** after the fishbone or 5 Whys, ask: what barriers or safeguards *should* have caught this? Why didn't each one work?
6. **Verify the root cause.** Before closing, ask: *"If we fix this specific cause, does the problem go away — and stay gone?"* If the answer is "probably not," say so and continue drilling.
7. **Draft the corrective action** — provisional, scoped only to removing the verified root cause, not to solving everything at once.
8. **Close** with the shared closing block, specific to this analysis.

Data-safety line, used whenever asking for documents or data: *"Leave out names of patients or employees and anything your company treats as confidential; roles, shifts, and initials are fine."*

**Mirroring.** Once the user has used their own vocabulary — unit/clinician/patient, "near-miss" vs. "defect," PDSA rather than PDCA — adopt it for the rest of the conversation. Never correct a user's cycle vocabulary.

## IS/IS-NOT scoping

IS/IS-NOT is a two-column table that tightens the problem definition before analysis begins. A narrow scope saves two hours of fishbone work and often reveals the cause directly.

Fill in what you know, mark unknown cells `[Unknown]`, and ask the user for the cells that matter most.

| Dimension | IS (the problem exists here) | IS NOT (the same thing, but no problem) |
|---|---|---|
| What | Specific defect or failure mode | Similar products/steps where it doesn't appear |
| Where | Machine, line, unit, location | Similar equipment/locations where it doesn't appear |
| When | Shift, time of day, day of week | Times when it doesn't appear |
| Who | Role, crew, team | Other roles or crews where it doesn't appear |
| How much | Rate, frequency, severity | When it's lower or absent |

**Key insight:** the contrast between IS and IS NOT almost always points toward the cause. If the problem only happens on second shift, that's not an observation — that's a hypothesis. Ask what's different about second shift.

## 5 Whys — rules

1. Each Why must follow directly from the previous answer.
2. **"Operator error," "human error," "lack of attention," "didn't follow procedure," and "bad luck" are never root causes.** They are always a symptom. Ask: *Why was the operator in a position to make that error? What made the correct behavior harder than the incorrect one?*
3. Lack of training is not a root cause — it is a corrective action disguised as a cause. If training is the answer, ask: *Why was a trained operator required in the first place? Why wasn't the process mistake-proofed so training wasn't the critical control?*
4. Stop when: (a) the cause is something the organization can actually change, and (b) fixing it would eliminate the problem, not just reduce it.
5. Mark any assumed step `[ASSUMED — verify at gemba]`. A 5 Whys built entirely on assumptions is a hypothesis, not an analysis.

**Format:**
```
Problem: [problem statement]

Why 1: [answer]
Why 2: [answer]
Why 3: [answer]
Why 4: [answer]
Why 5: [answer — candidate root cause]

Root cause candidate: [restate as a clear, specific cause]
Verification question: If we fix [root cause], does [problem] go away — and stay gone?
```

## Fishbone (Ishikawa) — rules

Use the six standard categories. In healthcare or service settings, relabel as appropriate (Environment can become "Environment/Policy"; Man can become "People/Roles").

| Category | Manufacturing focus | Healthcare / Service focus |
|---|---|---|
| Man | Operator, skill, fatigue | Clinician, role clarity, cognitive load |
| Machine | Equipment, tooling, calibration | Equipment, devices, software |
| Method | Procedure, standard work, sequence | Protocol, workflow, documentation |
| Material | Raw material, components, supplier | Supplies, medications, information |
| Measurement | Gauges, specs, sampling | Data accuracy, definitions, reporting lag |
| Environment | Temperature, layout, noise | Physical space, policy, shift structure |

For each category: list candidate causes, then ask at least one "Why" on each to avoid stopping at symptoms. Mark causes that need gemba verification.

**Never run a fishbone and stop there.** The fishbone narrows; the 5 Whys drills. Pick the top one or two candidates from the fishbone and run 5 Whys on them to reach a specific, verifiable root cause.

## Barrier analysis (when to use)

Use barrier analysis after the 5 Whys or fishbone when the problem involves a safety system, a detection step, a check, or a safeguard that should have caught the issue but didn't.

For each barrier: (1) name the barrier, (2) describe what it's designed to prevent, (3) state why it failed in this case.

This is especially common in: healthcare adverse events and near-misses, safety incidents, escaped defects in manufacturing, and compliance failures in service processes.

## Verification rule — the skill does not close without this

Before declaring a root cause verified, ask: *"If we fix [specific root cause], does [problem statement] go away — and stay gone?"*

If the team can't confidently answer yes, the cause hasn't been drilled deep enough. State this plainly: *"We have a candidate cause, but I'm not confident fixing it alone would make the problem stay gone — here's where I'd keep drilling."* Then continue drilling.

The skill is not done when the analysis is built. It is done when the verification question is answered.

## "Never accept these as root causes" — what to ask instead

These phrases end analysis prematurely. Always replace them with a systemic question:

| Surface answer | Drill question |
|---|---|
| Operator error | What made the incorrect action easier than the correct one? What would have had to be true for any trained person to make the same mistake? |
| Human error | What process or system condition set up the human to fail? What would mistake-proofing look like here? |
| Lack of training | Why was training the critical control? Why isn't the process designed so a new person can perform it correctly without special knowledge? |
| Didn't follow procedure | Why didn't the procedure get followed? Was it findable, current, and physically accessible at the point of use? Was deviating from it faster or easier? |
| Bad luck | What condition made the process vulnerable to this outcome? What would make the same "bad luck" not matter next time? |

## Deliverable

Output sections, in order:

1. **Problem statement** — specific, scoped, observable. Not "quality issues" — "Type B defects at Station 4, averaging 3.2 per shift on second shift since week 14."
2. **IS/IS-NOT table** — filled in as completely as possible, with `[Unknown]` for gaps.
3. **Root cause tree** — 5 Whys chain, or fishbone with the drilled branches, formatted in the templates below.
4. **Verified root cause** — one clear, specific statement. Tagged `[VERIFIED]` if the verification question was answered yes, `[CANDIDATE — needs gemba verification]` if not.
5. **Provisional corrective action** — one specific action that removes the verified root cause. Not a list of everything wrong — only the action that removes *this* cause.
6. **What still needs gemba** — explicit list of any `[ASSUMED]` or `[NEEDS GEMBA]` items that couldn't be resolved from the information given.

Template reference: `resources/templates/rca-report.md`

## Quality bar

- The problem statement is specific enough that two people independently reading it would agree on whether the problem is happening on any given day.
- IS/IS-NOT has at least three dimensions filled in — a table with only "What" populated hasn't been scoped.
- The 5 Whys chain has no step that could be answered "yes" or "no" — each Why produces a specific, observable cause.
- No why-chain step accepts operator error, human error, lack of training, or bad luck as a final answer.
- The fishbone, if used, drives to at least one 5 Whys chain — a fishbone with no drilled branches is brainstorming, not RCA.
- The root cause is tagged either `[VERIFIED]` or `[CANDIDATE — needs gemba verification]` — never left ambiguous.
- The corrective action removes the stated root cause, not a list of adjacent problems.
- A root cause that begins "we need to train people to…" is not a root cause — flag it and drill further.

## Closing block

Append the block from `docs/CLOSING-BLOCK.md` (also copied at `resources/closing-block.md`), filled in for this analysis. The first bullet under "what still needs a human" should name the most important unverified assumption — the one that, if wrong, would change the root cause entirely.

## Examples

- `resources/examples/manufacturing-weld-defect.md` — recurring weld defect on second shift, scoped with IS/IS-NOT, drilled with 5 Whys to a fixable systemic cause, verified.
- `resources/examples/healthcare-medication-near-miss.md` — medication near-miss on a medical unit, fishbone used for multi-factor analysis, barrier analysis applied, drilling from "nurse didn't check" to a systemic cause.

Both show the full IS/IS-NOT table, the analysis method and why it was chosen, the drilling through any surface-level human-error answers, and the verification question answered before the skill closes.
