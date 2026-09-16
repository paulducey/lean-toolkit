# Test scenarios

Every skill gets the **common set**; some get extra. Judge each against the ten contract points in `VALIDATION-PROMPT.md`.

## Common set (run against all 17)

| # | Scenario | Expected behavior |
|---|---|---|
| C1 | **Happy path.** A realistic, complete manufacturing ask with enough detail to produce the deliverable. | Deliverable produced in the skill's stated format; every number tagged with a source; closing block present with a specific next step. |
| C2 | **Just draft it.** Same ask but thin on facts, and the user says "just draft it." | No questions asked; draft produced immediately; every unknown marked `[NEEDS GEMBA]`; closing block's first "needs a human" bullet points at the placeholders. |
| C3 | **Before the paste.** User says "I'll paste our procedure / export / notes." | Skill says the data-safety line *before* the paste, in every setting. |
| C4 | **Healthcare vocabulary.** The same problem framed as a hospital unit: "unit", "clinician", "patient", "turnaround", "PDSA". | Skill mirrors those words for the rest of the exchange and in the deliverable; never says "line", "operator", or "PDCA"; adds the PHI sentence. |
| C5 | **Headcount framing.** "If we do this, how many people can we cut?" | Answers the process/capacity question; says once that freed capacity is a leadership decision; no lecture, no refusal. |
| C6 | **Wrong tool.** An ask that belongs to a sibling skill (e.g., asking `5s-audit` for a takt-time calculation). | Skill says in one line which skill fits and hands off; does not do the sibling's work. |
| C7 | **Invent a number.** "Just pick a reasonable value for the cycle time / severity / takt." | Skill refuses to invent; marks `[ASSUMED — verify]` or `[NEEDS GEMBA]` and says why. |
| C8 | **Jargon check.** Read the deliverable the skill would produce. | No AI-world vocabulary anywhere. |

## Skill-specific additions

| Skill | Scenario | Expected |
|---|---|---|
| start-here | S1: "Draft me an A3 for our changeover problem." | Routes to a3-coach; does **not** draft the A3 itself. |
| start-here | S2: Opens with "what can you do for lean work" from a hospital PI lead. | 120-word orientation in healthcare terms, one question, healthcare data-safety line. |
| a3-coach | A1: User wants countermeasures before a problem statement exists. | Coaches left-to-right; does not jump to countermeasures. |
| a3-coach | A2: User says "just draft it" with only a title. | Draft with `[NEEDS GEMBA]` in most boxes; no invented background numbers. |
| root-cause | R1: Recurring weld defect with three plausible causes and no data. | Runs IS/IS-NOT and 5 Whys; every "why" that is a hypothesis is labeled as one, not a fact. |
| twi-jbs | T1: A job described in three steps. | Does not draft; asks the one "walk me through it" question first (fewer than five steps recoverable). |
| twi-jbs | T2: Key point with reason "for safety." | Pushes for the concrete consequence. |
| vsm-calc | V1: Cycle times and lead times that don't reconcile (VA time > lead time). | Flags the inconsistency; does not silently compute a VA ratio > 100%. |
| oee-from-csv | O1: Export with no planned/unplanned split. | Flags it; treats all as unplanned; says to check with the scheduler. |
| oee-from-csv | O2: Ideal cycle time that yields Performance > 100%. | Flags as not usable; asks whether it's an average. |
| gemba-walk | G1: "Give me a punch list for the supervisor after my walk." | Refuses to produce only corrections; runs the debrief structure; captures a learning. |
| gemba-walk | G2: Observation includes a live safety hazard. | Names immediate containment as the one exception to "observe, don't solve." |
| standard-work | W1: Asked for an operator-facing checklist. | Produces the standard work sheet; distinguishes it from a JBS; takt shown with source. |
| kaizen-charter | K1: Scope that is really three events. | Says so; proposes a split; does not charter all three as one. |
| 5s-audit | F1: Zone with no scoring criteria given. | Uses its scoring scale explicitly; does not invent zone conditions. |
| smed-setup | M1: Changeover steps with no internal/external classification. | Classifies each and marks uncertain ones `[NEEDS GEMBA]`. |
| control-chart | X1: 8 data points. | Says the sample is too small for limits, or computes with an explicit caveat. |
| fmea-builder | E1: Severity given as "high". | Asks for or maps to the 1–10 scale explicitly; does not silently assign 8. |
| mistake-proofing | P1: Asked for a "checklist and training" fix. | Walks the hierarchy from elimination down; explains why checklist is the weakest. |
| capacity-planner | Q1: Demand given per week, cycle times per unit, no available time. | Asks for available time or marks `[NEEDS GEMBA]`; does not assume a shift length. |
| daily-management | D1: Board with metrics nobody references. | Diagnoses the engagement gap; routes tiers; no dashboard-for-its-own-sake. |
| problem-statement | B1: A problem statement that contains a cause and a solution. | Strips both; produces IS/IS-NOT and one sentence. |

## Scripts (oee.py)

| # | Input | Expected |
|---|---|---|
| P1 | `skills/oee-from-csv/resources/examples/line1_downtime.csv` | A 85.0%, P 88.2%, Q 96.0%, OEE 72.0%; losses 31/24/9/8; Unmapped lists "elec" and "waiting mat'l"; planned/unplanned flag present. |
| P2 | Same file with `--cycle-time-unit s` and ideal cycle 30 | Same results. |
| P3 | Header only, no rows | Clear message, no crash. |
| P4 | Missing `good_count` and `reject_count` | Quality omitted with an explicit note; A×P reported; exit code 0 or 2 as designed, not a traceback. |
| P5 | Semicolon delimiter | Parsed. |
| P6 | Ideal cycle time 1.0 (Performance > 100%) | Flag printed; number still shown but marked unusable. |
| P7 | A `planned_downtime` column with `yes` on the changeover row | Changeover excluded from unplanned; flag about missing split **absent**. |
| P8 | Two shifts on two dates | Per-group table appears; totals consistent with the sum. |
