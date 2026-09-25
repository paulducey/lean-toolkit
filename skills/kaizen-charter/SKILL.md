---
name: kaizen-charter
description: Coach a practitioner through chartering a kaizen event — business case, scope and boundaries, team roles, baseline and target metrics, pre-work, a day-by-day agenda (3-day or 5-day), deliverables, report-out, and 30/60/90-day follow-up — then draft the complete charter. Use when someone says "kaizen event", "rapid improvement event", "RIE", "charter", "kaizen blitz", "improvement workshop plan", or is planning a week where a team pulls off the floor to fix a process. Coaches on whether this is even the right event before drafting it. Not for a single root-cause analysis (use root-cause) or a full A3 (use a3-coach).
license: MIT
---

# Kaizen Charter

A kaizen event that fails usually fails before day 1 — a problem nobody's watched yet, a team that can't actually get freed from their day job, a process too unstable to improve this week. This skill coaches those questions first, then drafts a complete charter a sponsor could sign.

## When to use / when not to

Use it to plan a focused, time-boxed improvement event (typically 3–5 days) where a cross-functional team is pulled from normal duties to redesign a specific process. Use it whether the request is "help me write a charter" or "we're planning an RIE for X."

Don't use it for open-ended root-cause work with no event planned (→ `root-cause`), for a one-page problem-solving story that isn't an event (→ `a3-coach`), or to plan a single day of gemba observation (→ `gemba-walk`). If the user's actual need is one of those, say so in one line and offer to switch.

## How this skill works

**Open with one sentence the first time:** "I'll ask a few questions a coach would ask — including whether this is the right event to run at all — then draft the charter. Say *just draft it* at any point and I'll work from what you've given me."

1. **Read everything given.** Pull out the process, the pain, any metrics already mentioned, and the timeframe.
2. **Ask up to five coaching questions** from the list below — the readiness questions first if nothing yet suggests they've been considered.
3. **Escape hatch:** on "just draft it," "skip the questions," or similar → go straight to step 4 with `[NEEDS GEMBA: …]` placeholders, but still name any readiness risk you can see from what's given (e.g., no baseline data mentioned) in the charter's `## 3a. Readiness assumptions and risks` section, not silently.
3a. **If two or more readiness answers are negative** (nobody's watched it, process unstable, backfill commitment shaky, problem not understood well enough to scope), say so in one line before drafting, name what would have to be true to run this well, and offer either a short pre-work plan or a `root-cause` pass first. Still draft the charter if the user wants it anyway.
4. **Pick 3-day or 5-day.** Default to 5-day for a process not yet mapped or with no baseline data; 3-day when the team already has a current-state map and data in hand and the week is mainly design-and-test.
5. **Draft using `resources/templates/kaizen-charter.md`**, filling in every section — roles by role, not name; every baseline metric with a source tag.
6. **Critique your own draft** in two or three bullets: the readiness risk most likely to derail the week, the boundary most likely to get tested and broken, and what the report-out will need that isn't nailed down yet.
7. **Close** with the shared closing block, specific to this charter.
8. If asked to export: run `python3 skills/kaizen-charter/scripts/export_docx.py <saved.md>`.

Data-safety line, used whenever asking for documents or data: *"Leave out names of patients or employees and anything your company treats as confidential; roles and initials are fine."*

**Mirroring.** Once the user has used their own vocabulary — unit/clinician/patient, PDSA rather than PDCA, "turnaround" rather than "changeover" — adopt it for the rest of the conversation and in the charter. Never correct a user's own cycle vocabulary.

## Questions to ask (choose ≤ 5 per turn; use the answers)

**Is this the right event? (ask these first if nothing suggests they've been considered)**
- Has anyone watched this process recently, or is the pain described from reports and complaints? A week of redesign on a process nobody's observed is a week of guessing.
- Is the process stable enough to improve — running its normal way most days — or is it currently in crisis (short-staffed, mid-changeover to a new system, a one-off spike)? A kaizen event on an unstable process usually just standardizes the chaos.
- Will the sponsor actually free the team for the full week — no pulling members back for their regular job "just for an hour"? What's happened the last time this was tried?
- Is the problem understood well enough to scope a week around it, or does it need a root-cause pass first?

**Scoping**
- Where does the process start and end for this event — the exact trigger and the exact handoff — and what's explicitly out of scope?
- What's the one metric leadership will judge this event by, and what's the current baseline, with a source?

## Deliverable

Template: `resources/templates/kaizen-charter.md`, eleven sections in order: business case, scope, boundaries/constraints, team (roles), baseline metrics, targets, pre-work checklist, agenda (3-day and 5-day variants — keep the one that fits, or both if undecided), deliverables, report-out plan, 30/60/90-day follow-up.

## Quality bar

A good charter from this skill:
- **Business case** has a number tied to a real consequence (cost, safety, delivery, quality, capacity) and names the decision it supports — not "we've always wanted to fix this."
- **Scope** names the exact start and end points of the process, and what's explicitly out — a charter with no "out of scope" line is an invitation to scope creep on day 2.
- **Boundaries and constraints** are specific enough to test against a real proposal ("can't take the press offline during first shift" beats "minimal disruption").
- **Team** is roles, not names — a sponsor, a facilitator, a team lead who owns the process afterward, members, and named subject-matter experts by function.
- **Baseline metrics** carry a source tag; a charter with an unsourced baseline gets its target argued with on day 1.
- **Pre-work checklist** is complete enough that day 1 starts on the process, not on finding a stopwatch or waiting for a data pull.
- **Agenda** matches the readiness answers — 5-day if the process isn't mapped yet, 3-day if it is.
- **Follow-up** has dates and an owner for 30/60/90 days — a charter that ends at the report-out has no way to know if the gain held.
- **No headcount framing.** If the stated goal is "free up X people," the charter frames the target as capacity freed and leaves the redeployment decision to leadership.

Common failures to catch in the critique step: a business case that's really a complaint; scope with no "out of scope" line; a team of "TBD"; a baseline that's a guess with no source tag; a 3-day agenda for a process nobody's mapped; a follow-up section that's a single vague "check back later."

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

Append the block from `docs/CLOSING-BLOCK.md`, filled in for this charter. The first bullet under "what still needs a human" should name the readiness risk most likely to matter — usually whether the process has actually been observed, and whether the sponsor's freed-team commitment is real.

## Export

`python3 skills/kaizen-charter/scripts/export_docx.py <charter.md> [-o out.docx]` produces a clean Word document ready to circulate for sign-off. Never assemble a .docx by hand.

## Examples

- `resources/examples/manufacturing-changeover-event.md` — 5-day kaizen event to cut changeover time on a stamping line.
- `resources/examples/healthcare-discharge-event.md` — 5-day kaizen event to move inpatient discharges earlier in the day.
Both include the coaching exchange that produced them, including the readiness questions.
