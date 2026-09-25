---
name: twi-jbs
description: Build a TWI Job Instruction Job Breakdown Sheet (JBS) — Important Steps, Key Points, Reasons — for training a new operator or clinician on a specific job, plus a JI 4-step training plan and a training timetable. Use when someone says "job breakdown sheet", "JBS", "TWI", "job instruction", "break down this job for training", "key points and reasons", or "train a new operator on...". Draft-first: produces the deliverable immediately from what's given, with [NEEDS GEMBA] placeholders for unconfirmed key points or times, then asks only the questions that block completeness.
license: MIT
---

# TWI Job Instruction — Job Breakdown Sheet

A Job Breakdown Sheet is how a trainer prepares to teach one specific job well, using the TWI Job Instruction method: break the job into a few Important Steps (what happens, in order), note the Key Points inside each step (what could make or break it, hurt someone, or make the work easier), and state the Reason each key point matters. The JBS is a trainer's tool — not the standard, and not something handed to the learner as a checklist.

## When to use / when not to

Use it when someone needs to train a new person on a specific job and wants the steps, key points, and reasons captured before they teach it — new hire onboarding, cross-training, a job that keeps getting done inconsistently because training was informal.

Don't use it to document the current best-known method with cycle times for run-rate or balancing purposes (→ `standard-work`, which produces the sheet a JBS's Important Steps should already match) or for a one-page problem report (→ `a3-coach`). If the user's real need is a standard work sheet with takt time, say so in one line and point to `standard-work`; the two often get built together — a JBS's steps should trace back to the standard work sheet's steps.

If someone asks for something the learner follows step-by-step at the workstation, that's a work instruction or SOP, not a JBS — say in one line that the JBS is what the trainer prepares from, and offer `standard-work` for the learner-facing document. Both often get built from the same job.

## How this skill works (draft-first)

1. **Read everything given** — notes, a transcript of someone explaining the job, an existing procedure, or gemba observations. Pull out the natural break points in the operation and anything already flagged as tricky, risky, or a "knack." **If fewer than five Important Steps can be recovered from what was given, don't draft** — ask one question first: "Walk me through the job from the first thing they touch to the last, in the order it happens." Draft as soon as you have the sequence.
2. **Draft immediately** using `resources/templates/job-breakdown-sheet.md`. Split the job into **5–9 Important Steps** — segments where something happens to *advance* the work (not every hand motion), built only from what the user described, pasted, or reported — never the tool's general idea of how a job like this usually goes. Add Key Points only where they're real (see the rule below), and a concrete Reason for each. Mark any time or detail not actually confirmed as `[NEEDS GEMBA: watch the job performed]`.
3. **Ask only blocking questions** (≤5, see below) — things needed to finish the sheet, not general coaching.
4. **Always include the training plan and timetable** — the JI 4-step method stub and a timetable table for who needs training on this job, by when. Fill the timetable with what's known; use `[NEEDS GEMBA: confirm with supervisor]` for names/dates not given.
5. **Close** with the shared closing block, specific to this job.
6. If asked to export: `python3 skills/twi-jbs/scripts/export_docx.py <saved.md>`.

Data-safety line, used whenever asking for documents or transcripts: *"Leave out names of patients or employees and anything your company treats as confidential; roles and initials are fine."*

**Mirroring.** Once the user has used their own vocabulary — unit/clinician/patient, PDSA rather than PDCA, "turnaround" rather than "changeover" — adopt it for the rest of the conversation and in the deliverable. Never correct a user's own cycle vocabulary.

## Questions to ask (draft-first: blocking only, ≤5)

Ask only what's needed to finish the sheet, and only if the material doesn't already answer it:

1. Where does this job start and end — the first motion and the last, so the Important Steps don't spill into the next job?
2. Is there a step where new people commonly get it wrong, or where the best performer does something not obvious from watching — even if you can't yet state the reason precisely?
3. Any step where getting it wrong could hurt the person doing it or someone nearby?
4. Who needs to be trained on this job, and by when — for the timetable?
5. Who's the trainer — the person whose method this breakdown should capture?

Never ask a question whose answer you won't use. If the user says "just draft it" or has already given enough to work with, skip straight to the sheet with `[NEEDS GEMBA]` placeholders.

## The three columns, precisely

- **Important Steps — WHAT.** A logical segment of the job where something happens to *advance the work* — a physical or informational change of state. Not a motion-by-motion breakdown. Usually **5–9** for one job; fewer usually means steps are too coarse and are hiding key points, more usually means the job should be split into two JBSs.
- **Key Points — HOW.** Anything within a step that might make or break the job, injure the worker, or make the work easier — safety, quality, or technique/knack. Key points are **few and specific**: most steps have zero, one, or two. Never put method detail in the Important Step column — if a "step" is really describing how something is done, the how belongs in Key Points and the step should be reworded to say what happens.
- **Reasons — WHY.** Concrete enough to act on. "Prevents the connector from cross-threading on reinsertion" is a reason; "for quality" or "for safety" is not — push until it names the actual consequence.

## Deliverable

Template: `resources/templates/job-breakdown-sheet.md`. Keep the header → breakdown table → training plan → timetable → validation order. The training plan (prepare / present / try out / follow up) and the timetable are always included, even for a short job — they are what make this a *training* tool and not just a documentation table.

**The JBS is a trainer's aid, not a checklist for the learner.** Say this explicitly in the deliverable's framing line (the template includes it) and don't let the breakdown drift into an operator-facing work instruction — that's what a standard work sheet or SOP is for.

## Quality bar

A good JBS from this skill:
- **5–9 Important Steps**, each a WHAT, none carrying method detail that belongs in Key Points.
- **Key Points are sparse.** A step with four or five "key points" is a sign the step needs to be split, not that the job is unusually tricky.
- **Every Reason is concrete** — names the actual failure it prevents or the actual benefit, not a generic "for quality" or "for safety."
- **Training plan and timetable are both present**, not left as placeholders when information is available; `[NEEDS GEMBA]` only where genuinely unconfirmed.
- **No invented Important Steps.** Every step must come from something the user described, a document they pasted, or an observation they reported. The tool's general idea of how a job like this usually goes is not a source.
- **No invented key points.** A technique detail the tool wasn't told about is marked `[NEEDS GEMBA: watch the job performed]`, never guessed at.
- **No headcount framing.** If the ask drifts toward "how many people do we need once this job is trained up," redirect to capacity and demand.

Common failures to catch: Important Steps written as long paragraphs of method (that's the how, not the what); a Reason that just repeats the Key Point; a JBS presented as something to hand to the trainee to follow step-by-step, rather than a tool the trainer studies beforehand.

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

Append the block from `docs/CLOSING-BLOCK.md`, filled in for this job. The first bullet under "what still needs a human" must point at any `[NEEDS GEMBA]` placeholders left in the sheet.

## Export

`python3 skills/twi-jbs/scripts/export_docx.py <jbs.md> [-o out.docx]` produces a clean Word document. Never assemble a .docx by hand.

## Examples

- `resources/examples/manufacturing-torque-wrench-assembly.md` — training a new operator to torque a fastener assembly correctly, from a trainer's walkthrough.
- `resources/examples/healthcare-specimen-labeling.md` — training a new medical assistant on specimen labeling at the point of collection.
Both include the exchange that produced them and the closing block filled in specifically.
