# Example: chartering a 5-day kaizen event to move inpatient discharges earlier in the day

**User:** We want to run a kaizen event to get our inpatient discharges happening earlier in the day. Right now most happen late afternoon and it backs up the whole unit.

**Assistant:** Leave out names of patients or clinicians, and anything the organization treats as confidential; roles and initials are fine, and please don't paste any protected health information. I'll ask a few readiness questions first, then draft the charter — say *just draft it* anytime.

Has anyone actually watched the discharge process recently — walked a few discharges start to finish — or is this mostly known from complaints and end-of-day backups?

**User:** The unit's process improvement lead, M., has watched a handful informally, not systematically.

**Assistant:** Is the discharge process stable right now — running its normal way most days — or is the unit currently in some kind of crisis (short-staffed, mid-rollout of a new system, etc.)?

**User:** Stable. We rolled out a new charting system four months ago but it's settled in now.

**Assistant:** Will the sponsor free the clinical and case management team for the full week, without pulling them back to cover the unit "just for an hour"? Has that been tried before here?

**User:** This would be our first kaizen event on this unit. Sponsor is the chief nursing officer, who's requested it.

**Assistant:** Good — no negative history to flag, but no track record either, so I'll still name it as a risk to watch. Last readiness question: is the problem understood well enough to scope a week around it, or does discharge timing need a root-cause pass first?

**User:** We know discharges cluster late afternoon. We don't fully know why — could be physician rounding order, could be pharmacy turnaround, could be transport.

**Assistant:** That's a genuine "don't know where to start" situation with several plausible factors — that alone is a reason to map current-state on day 1 rather than skip to redesign, and 5-day is the right length. Since only one readiness answer is genuinely negative (cause not understood) and the others are neutral-to-positive, I don't think this needs a separate root-cause pass first — the week's day 1 can serve that purpose, as long as the agenda is honest that day 1 is discovery, not design.

**User:** Agreed, let's draft it.

---

## Kaizen Charter: Inpatient Discharge Timing

**1. Business case**
Discharges on the unit currently cluster in late afternoon [user estimate], creating a bed-availability backlog that delays admissions and boarding `[NEEDS GEMBA: quantify average discharge time and downstream boarding delay]`. This charter supports the chief nursing officer's request to dedicate a focused week to this before the next capacity review.

**2. Scope**
Starts at the attending physician's discharge decision documented in the chart; ends at the patient physically leaving the unit (bed available for next patient). Out of scope: ED boarding process itself, though it is a downstream effect.

**3. Boundaries and constraints**
- Cannot change physician rounding schedules unilaterally — any proposed change to rounding order needs medical staff sign-off, not just unit-level agreement `[ASSUMED — verify]`.
- No new charting system changes during the event — the new system rolled out four months ago and is still settling in.

**3a. Readiness assumptions and risks**
- The discharge process has only been watched informally, not systematically — day 1 of the event will need to include real observation of several discharges, not rely on the informal impressions gathered so far.
- This is the unit's first kaizen event — there's no track record of the team actually being freed for the week; treat the CNO's commitment as stated, not yet tested, and confirm coverage arrangements in writing.
- The cause of late-afternoon clustering (physician rounding order vs. pharmacy turnaround vs. transport) is not yet known — the agenda below treats day 1 as discovery, not redesign, so the team doesn't jump to a countermeasure for the wrong cause.

**4. Team**
| Role | Who |
|---|---|
| Sponsor | Chief nursing officer |
| Facilitator | `[NEEDS GEMBA: assign]` |
| Team lead | Unit process improvement lead, M. |
| Members | Staff clinician, case manager, unit clerk |
| Subject-matter experts | Pharmacy representative, transport/facilities representative (by function) |

**5. Baseline metrics**
| Metric | Baseline | Source |
|---|---|---|
| Median discharge time of day | `[NEEDS GEMBA: pull from scheduling/EHR discharge timestamps]` | Not yet pulled |
| Share of discharges after 2pm | Majority [user estimate] | User impression, unconfirmed |

**6. Targets**
| Metric | Baseline | Target | By when |
|---|---|---|---|
| Median discharge time | `[NEEDS GEMBA]` | Before noon for majority of planned discharges | End of event week + 90-day confirmation |

**7. Pre-work checklist**
- [ ] Pull discharge timestamp data from the EHR for the last 4–6 weeks `[NEEDS GEMBA]`
- [ ] Confirm coverage/backfill plan for the week in writing with unit leadership `[NEEDS GEMBA]`
- [ ] Invite pharmacy and transport representatives and confirm their availability for the week

**8. Agenda — 5-day**
| Day | Focus |
|---|---|
| 1 | Observe and map current discharge process start to finish; confirm baseline timing data |
| 2 | Identify where delay accumulates (rounding order, pharmacy turnaround, transport, paperwork) |
| 3 | Design future-state discharge sequence and test with 1–2 real discharges |
| 4 | Refine and test on a full day's discharges |
| 5 | Stabilize, document new process, report-out |

**9. Deliverables**
A mapped and timed discharge process, an updated discharge workflow, before/after timing data, and a named owner for sustaining it.

**10. Report-out plan**
Team lead M. presents before/after discharge timing to the chief nursing officer and unit medical director on day 5.

**11. 30/60/90-day follow-up**
| Checkpoint | Date | Owner | What's checked |
|---|---|---|---|
| 30-day | `[NEEDS GEMBA: set date]` | M. | Median discharge time holding earlier than baseline |
| 60-day | `[NEEDS GEMBA: set date]` | M. | New workflow still being followed |
| 90-day | `[NEEDS GEMBA: set date]` | CNO | Sign-off that gain is sustained |

---

**Self-critique:** The readiness risk most likely to derail the week is that day 1 is genuinely discovery, not design — if the team pushes to skip ahead because "we already know it's pharmacy," the week will design a fix for the wrong cause. The boundary most likely to get tested is the no-rounding-schedule-change rule once physician timing turns out to matter. The report-out will need real timing data from test discharges on days 3–4, which don't exist yet.

**What this skill did:**
- Ran the readiness questions and found the process cause is genuinely unknown among several plausible factors — set the agenda so day 1 is discovery, not redesign.
- Drafted a full 5-day discharge-timing charter using the CNO's business case and the team's stated scope and constraints.
- Flagged the untested backfill commitment as a risk even though there's no prior failure on this specific unit.

**What still needs a human:**
- Pull actual discharge timestamp data from the EHR — the "late afternoon clustering" claim is currently just an impression.
- Confirm the coverage/backfill plan in writing before the week starts.
- Get medical staff sign-off in principle on the possibility of a rounding-order change, before the team designs around it.

**Suggested next step:** Have the unit process improvement lead, M., pull four to six weeks of discharge timestamps from the EHR before the event is scheduled.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
