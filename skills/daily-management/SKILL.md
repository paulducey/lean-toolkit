---
name: daily-management
description: Design or assess a tiered daily management system — Tier 1 team-level, Tier 2 supervisor-level, Tier 3 value-stream or plant-level — specifying the right metrics for each tier, the cadence and duration of each review, the lead vs. lag metric distinction, and the four-step response-to-abnormality. Use when someone says "daily management", "tiered meetings", "T1 T2 T3", "huddle", "standup", "production board", "daily visual management", "gemba board", "shift review", "how do we know how we're doing in real time", "our metrics are all lagging", or describes a situation where problems aren't surfaced quickly enough for the team to respond.
license: MIT
---

# Daily Management System

A daily management system is the operating cadence that connects what is happening on the floor right now to the people who need to know and act. Without it, problems surface hours or days after they occur — when the shift is over, when the daily report is compiled, when the customer calls. With a well-designed tiered system, abnormalities are detected within the cycle or the hour, contained before they cascade, and escalated only when the problem exceeds the team's authority or capability to resolve.

## When to use / when not to

Use it to design a new tiered daily management system, to assess and improve an existing one, to define what belongs on each tier's board, or to diagnose why a current system isn't surfacing problems in time to act.

Don't use it to design the improvement events triggered by the daily management system (→ `kaizen-charter`), to conduct the broader analysis that a T3 review might initiate (→ `a3-coach`), to calculate the OEE metrics a T2 board should display (→ `oee-from-csv`), or to define the standard work that feeds the T1 board (→ `standard-work`).

## The tier structure

Tier structure is not about hierarchy — it is about resolution time. Each tier reviews the right information at the right frequency to catch and respond to abnormalities before they become irreversible.

**Tier 1 — Team / floor level**
- Who: Front-line team, team lead
- Where: At the point of work — the line, the cell, the workstation
- Frequency: Start of shift, and ideally each hour (or each cycle in high-frequency processes)
- Duration: 15 minutes maximum; 5–10 minutes is the target
- Purpose: Is performance on track right now? Are we running to plan this hour? Did anything go wrong that we need to address or escalate?

**Tier 2 — Supervisor / area level**
- Who: Supervisor, area manager, support functions (maintenance, quality, engineering on rotation)
- Where: Area board or value stream board
- Frequency: Once per shift or once per day
- Duration: 30 minutes maximum
- Purpose: Are all T1 teams on track across the area? Are there patterns across teams that suggest a systemic problem? Are T1 escalations being resolved?

**Tier 3 — Value stream / plant level**
- Who: Value stream manager, plant manager, functional leads
- Where: Plant-level board or value stream board
- Frequency: Daily
- Duration: 60 minutes maximum
- Purpose: Are value streams on track to meet the plan for the day/week? Are T2 escalations and systemic issues getting resources and resolution? Is performance trending toward strategic targets?

## Lead metrics vs. lag metrics — the critical distinction

**Lag metrics** tell you what happened. They are outputs: units shipped, defects found, OEE for the day, customer complaints, end-of-day yield. They are necessary but insufficient for T1 boards — by the time a lag metric appears, the opportunity to intervene has passed.

**Lead metrics** tell you what is happening or what is about to happen. They are inputs or in-process indicators: units produced per hour vs. plan, first-pass yield at each station, changeover time completed vs. target, tasks completed vs. standard, machine running / not running right now.

**The T1 rule: a metric measurable only once per shift is a lag metric — it belongs on T2 or T3, not T1.**

A T1 board showing only daily or shift-end totals is not a daily management system — it is a daily reporting system. The distinction matters: a reporting system tells you what happened; a management system gives you time to act.

Test each metric against this question: *"If this number is off, can the team at this tier do something about it in the next 30–60 minutes?"* If yes, it's a lead metric for that tier. If no, it belongs at a higher tier.

## Tier board content guide

**T1 board — must have:**
- Production plan vs. actual by hour (or by cycle in high-frequency environments)
- Top abnormalities from previous period — what happened, what was done, status
- Safety cross or near-miss tracking (daily or weekly)
- Today's tasks or standard work items and completion status
- One or two key quality indicators measurable at the point of work each cycle or hour

**T1 board — does not belong:**
- End-of-day or end-of-shift totals only (those are lag)
- Department-level or plant-level metrics the team cannot influence
- Financial metrics

**T2 board — must have:**
- T1 summary: which teams are meeting plan, which are not
- Escalations from T1 and resolution status
- Safety and quality trends across teams (daily or weekly patterns)
- Maintenance and downtime tracking with root cause status
- Key lead metrics one level above the team: OEE by area, first-pass yield across the area

**T3 board — must have:**
- T2 summary: value stream performance vs. plan
- Open escalations and A3s with owner and status
- Strategic KPIs: delivery performance, quality metrics, safety rate, cost trends
- Customer issues and commitments

## The four-step response to abnormality

When a T1 metric is off plan, the response is structured — not freestyle problem-solving in the standup. The four steps apply at every tier, with escalation thresholds defined in advance.

**Step 1 — Detect:** The abnormality is visible on the board or is called out by a team member. This requires that the metric is being measured at the right frequency. If the team only finds out at shift end, detection has already failed.

**Step 2 — Contain:** Immediate action to prevent the abnormality from getting worse or affecting the next step in the process or the customer. Containment is not root cause analysis — it is damage limitation. Reroute, quarantine, resource-shift, notify.

**Step 3 — Escalate (if needed):** If the team cannot contain or resolve the abnormality with their own authority and resources, escalate to T2 immediately — not at the next scheduled meeting. Escalation criteria should be defined in advance so the team lead doesn't have to judge each situation from scratch. Define thresholds: if we're more than X units behind by the second hour, escalate.

**Step 4 — Analyze:** After containment, investigate the root cause — using `root-cause` for recurring or significant abnormalities. The daily standup is not the place for root cause analysis; it is the place to assign the analysis and confirm it happens.

The four steps should be visible on the T1 board or in the team's response protocol. If the team is doing freestyle discussion in the standup without a response structure, the standup will fill the allotted time with talk and produce no defined action.

## How this skill works

**Open with one sentence the first time:** "Tell me about the current state — which tiers exist, what's on the boards, how long the meetings run, and where the system isn't working — and I'll help you design or fix it."

1. **Read everything given.** Identify which tiers are in place, current meeting cadence and duration, what metrics are displayed, and the stated problem (problems not surfacing, meetings too long, metrics misaligned, team engagement low).
2. **Clarify the scope.** Is this a design (starting fresh) or a diagnosis (something isn't working)?
3. **Escape hatch:** on "just draft it" → design a standard three-tier system, mark assumptions `[ASSUMED]`, and flag the design choices that most need the user's operational context.
4. **Map current metrics to tiers.** Apply the lead/lag rule — identify every lag metric currently sitting on a T1 board and recommend where it should move.
5. **Identify missing lead metrics** for each tier. For T1, ask: *What could the team measure each hour that would tell them whether they're on track before the shift is over?*
6. **Design or assess the response-to-abnormality protocol** for T1.
7. **Set meeting duration targets** — T1 ≤15 min, T2 ≤30 min, T3 ≤60 min. If current meetings exceed these, identify what is filling the time and recommend how to remove it.
8. **Close** with the shared closing block, specific to this design or assessment.

Data-safety line: *"Process and performance data is fine; leave out personnel names — roles and shift designations are sufficient."*

## Common failure modes of daily management systems

| Failure mode | Root cause | Fix |
|---|---|---|
| T1 board shows only shift-end totals | Metrics are lag metrics; no hourly tracking | Replace with hourly plan vs. actual; break the shift into intervals |
| Standup runs 45 minutes | No agenda; becomes problem-solving forum; no time discipline | Time-box each section; problem-solving happens offline, not in the standup |
| T2 and T3 discuss what T1 already handles | Tier boundaries not defined; same metrics at all tiers | Define which escalations go to T2; remove T1 metrics from T2 board |
| Team doesn't update the board | Board is seen as management reporting, not a team tool | Move board ownership to the team lead; team updates their own data |
| Problems discussed but no action assigned | No response-to-abnormality protocol | Add action/owner/date column; close each problem with an assignment |
| Safety cross is a formality | Never linked to near-miss response | Require a response step for any marked day |

## Quality bar

- Each tier's meeting duration is stated and within the tier maximum (T1 ≤15, T2 ≤30, T3 ≤60).
- Every metric assigned to T1 passes the lead-metric test: measurable more than once per shift, actionable by the team within the hour.
- No lag metric (measurable only once per shift) is placed on a T1 board without explanation.
- The response-to-abnormality protocol is specified for T1 — four steps, with escalation thresholds defined.
- Each tier's board content is distinct — T2 and T3 boards do not duplicate T1 metrics.
- Board ownership is assigned to a role, not to management — the team that generates the data updates the board.
- The assessment identifies at least the top two failure modes if a current system is being evaluated.

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

Append the block from `docs/CLOSING-BLOCK.md`, filled in for this design or assessment. The first bullet under "what still needs a human" should name the lead metric choice that is most context-dependent — the one where the team's knowledge of what actually predicts their performance is irreplaceable.

## Examples

- `resources/examples/daily-management-assembly-area.md` — three-tier design for a mixed-model assembly area, hourly plan vs. actual on T1 board, OEE moved from T1 to T2, response-to-abnormality protocol written with defined escalation thresholds, meeting agendas specified.
- `resources/examples/daily-management-assessment.md` — assessment of an existing system with three failure modes identified (45-minute T1 standup, lag metrics on T1, no escalation protocol), redesign proposed, standard-work reference added for the new T1 standup format.
