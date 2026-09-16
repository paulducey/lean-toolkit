Shows: a P-FMEA on a five-step assembly process, explicit mapping of a user's "high" occurrence rating onto the 1–10 scale, two Severity 9 rows enforced to the top regardless of RPN, a "train operators" action flagged and replaced, and references out to mistake-proofing and control-chart.

**User:** We need an FMEA on our bracket assembly line. Five steps: insert bracket, apply adhesive, torque the fasteners, install the wiring harness, final visual inspection.

**Assistant:** Got it — describe what each step is supposed to do, what's gone wrong before (if anything), and how it's caught today, and I'll build the table. One note before you share anything: leave out proprietary process parameters or supplier names; describing failure modes and effects in functional terms is enough for the analysis.

**User:** Step 1, insert bracket: the bracket is symmetric so it can go in flipped, and that only gets caught at final inspection — happens sometimes. Step 2, apply adhesive: sometimes the bead is too thin, and if it's thin the panel can come loose in the field and cause a cut — this happens a lot, I'd call it high. We don't have a good check on the bead until the inspection at the end, and by then it's already cured so you can't fix it. Step 3, torque fasteners: if it's under-torqued, the fastener can back out later and the joint separates — that's a safety issue. We've had 3 field returns this quarter tied to it [from system: warranty log], and there's no torque check logged today, just the wrench's click which nobody verifies. Step 4, wiring harness: two connectors are nearly the same size and can get cross-mated, causing an intermittent fault — moderate occurrence, caught by the end-of-line function test most of the time. Step 5, final visual inspection: when we're behind schedule this step gets rushed and defects slip through — nothing catches it after that, it's the last step.

**Assistant:** Function statements first:
- Step 1 performs bracket insertion so that the bracket is correctly oriented before adhesive is applied.
- Step 2 performs adhesive bead application so that the panel bonds securely to the housing.
- Step 3 performs fastener torquing so that the joint stays clamped under service load.
- Step 4 performs wiring harness connector mating so that the correct circuit is completed.
- Step 5 performs final visual inspection so that non-conforming units don't ship.

You said Step 2's occurrence is "high" — on the 1–10 occurrence scale, "high" (score 8) means failures occur frequently, distinct from 9–10 which is near-certain, repeated failure. "Happens a lot" fits 8, not 9 or 10, since you're not describing it as happening on effectively every unit. I'll use **O=8** for Step 2 and flag it as based on your description rather than a counted rate — **[user estimate]**.

| # | Function / Step | Failure Mode | Effect(s) | S | Cause(s) | O | Current Controls | D | RPN | Priority | Recommended Action | Owner (role) | Target Date | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2 | Apply adhesive | Insufficient bead applied | Panel detaches in service, laceration risk | 9 | Manual bead application, no volume check | 8 | Final visual inspection only, post-cure | 8 | 576 | 1 [SAFETY/REGULATORY] | Add metered adhesive dispenser with volume verification, inline before cure — see `mistake-proofing` for the sensor design | Process Engineer | [ASSUMED — verify] 60 days | Bond can't be corrected after cure; detection must move before that point |
| 3 | Torque fasteners | Fastener under-torqued | Joint separates in service, safety hazard | 9 | Manual torque, no verification logged | 4 | Click wrench only, unverified | 9 | 324 | 2 [SAFETY/REGULATORY] | Add electronic torque wrench with pass/fail logging; monitor logged torque values with `control-chart` to catch drift early | Manufacturing Engineer | [ASSUMED — verify] 45 days | 3 field returns this quarter [from system: warranty log] is the only occurrence data point so far |
| 1 | Insert bracket | Bracket installed in wrong orientation | Alignment failure caught downstream, rework | 7 | Bracket is symmetric, can be inserted either way | 5 | Final visual inspection only | 7 | 245 | 3 | Redesign bracket with an asymmetric feature (keying) so wrong orientation is physically impossible — see `mistake-proofing` Level 1 | Design Engineer | [NEEDS GEMBA] | Exact rate of misorientation not tracked; occurrence is a rough estimate |
| 5 | Final visual inspection | Inspection skipped or rushed under schedule pressure | Defective unit ships to customer | 7 | Time pressure, no enforced check point | 3 | None downstream — this is the last step | 10 | 210 | 4 | Add a poka-yoke check (e.g. sensor-based verification) rather than relying on a visual step under time pressure — see `mistake-proofing` | Quality Engineer | [ASSUMED — verify] 90 days | Last-step failures have no downstream catch by definition |
| 2b | Apply adhesive | Cure time not met before next station | Bond weaker than spec, may fail under stress | 5 | Station cycle time doesn't enforce dwell | 4 | Operator judgment on timing | 6 | 120 | 5 | Add a cure timer/interlock that blocks advance until minimum dwell has passed | Process Engineer | [ASSUMED — verify] 30 days | |
| 4 | Install wiring harness | Wrong connector mated | Intermittent electrical fault, rework | 6 | Similar connector sizes, no keying | 6 | End-of-line function test | 3 | 108 | 6 | Add keyed connectors so mismatched mating is physically blocked | Design Engineer | [ASSUMED — verify] 60 days | |

Table is sorted with both Severity-9 rows first regardless of RPN, per the severity priority rule — Row 3 (RPN 324) outranks Row 1 (RPN 245) even though its RPN is lower, because a safety hazard doesn't wait for RPN to clear a threshold. Note that Row 3's RPN (324) is also lower than Row 5's would be if Row 5 were severity 9 — it isn't, so Row 5 stays in the ranked-by-RPN group below both safety rows, at position 4 with RPN 210.

A word on the two Detection scores of 8–9 in Rows 2 and 3: both reflect controls that either only catch the failure after it's already severe (Row 2 — the bond has already cured, so a post-cure inspection can't be corrected, only rejected) or don't exist in any verified form (Row 3 — the wrench clicks, but nothing logs or checks that click actually happened at the right torque). Those are genuinely weak controls, not a conservative guess — which is part of why both rows carry such high RPNs even with moderate occurrence.

**User:** For Row 1, can we just retrain people to check orientation before gluing?

**Assistant:** That won't move any of the three scores reliably. "Train operators" doesn't change Severity (the effect is the same regardless of training), doesn't reliably reduce Occurrence (the bracket is still symmetric — a tired or rushed operator will still get it wrong sometimes), and doesn't touch Detection (nothing added catches it earlier). The structural fix — keying the bracket so it only fits one way — is what actually removes the failure mode. Training can be a bridge while that's designed, but I wouldn't count it as the action that resolves the row.

**User:** Fair enough. Can you also tell us what to do about the target dates — we don't have a project system for this yet.

**Assistant:** I put a placeholder timeframe on each action row so the table isn't blank, but every one of those is marked `[ASSUMED — verify]` for exactly that reason — I don't know your team's real capacity or queue, so I picked round numbers (30/45/60/90 days) that roughly track the severity and complexity of the fix. Row 3 (torque verification) got the shortest window because it's the safety row with the simplest fix — an off-the-shelf electronic torque wrench — while Row 1 (bracket redesign) has no date at all, just `[NEEDS GEMBA]`, because a design change depends on your engineering queue in a way I can't estimate from here. Whoever owns this FMEA in your team should replace all five dates with real ones once it's reviewed.

---

**What this skill did:**
- Built a 6-row P-FMEA across the five assembly steps, scoring Severity, Occurrence, and Detection on the 1–10 scales and calculating RPN = S×O×D for each.
- Surfaced two Severity 9 rows (insufficient adhesive, under-torqued fastener) and forced them to the top of the priority order regardless of RPN, per the severity rule; both get mandatory actions.
- Flagged "retrain people" as an insufficient action for the bracket-orientation row and pointed to a structural fix instead.

**What still needs a human:**
- Row 3's occurrence (O=4) rests on 3 field returns this quarter — whether that reflects the true failure rate on the floor is worth checking; if it's higher, the RPN and urgency both go up. [from system: warranty log], otherwise unverified.
- Row 1's occurrence and Row 5's detection are estimates, not measured — [NEEDS GEMBA] and [ASSUMED — verify] respectively.
- Target dates are proposed placeholders — a real owner needs to confirm timelines against current workload.

**Suggested next step:** Take Row 3 (the under-torqued fastener) to the line supervisor and confirm whether any of the 3 field returns had a torque reading captured — that would tighten the occurrence estimate immediately.

**User:** Last thing — do we need to do anything about Row 2b, the cure-time row? It's near the bottom.

**Assistant:** It's low on the list (RPN 120, severity 5), but I wouldn't drop it just because it's not a safety row. It shares a root cause path with Row 2 above it — both are about the adhesive station — so if you're already sending someone to install the metered dispenser for Row 2, it's worth having them add the cure timer/interlock in the same visit rather than treating it as a separate project later. That's a sequencing suggestion, not a scoring change; Row 2b still ranks where the numbers put it.

**User:** Should we revisit this whole table once the actions land, or just leave it as-is?

**Assistant:** Revisit it — an FMEA that never gets updated stops reflecting reality. Once the adhesive dispenser, torque wrench logging, and bracket keying are actually in place, the Detection (and in the bracket's case, Occurrence) scores on those rows should drop, and the RPNs and priority order should be recalculated from the new numbers, not carried forward from today's estimates. I'd treat this as a living document tied to the next revision, not a one-time exercise — a good trigger is any time one of these actions is completed, or if a new failure shows up on the floor that isn't on this list yet.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
