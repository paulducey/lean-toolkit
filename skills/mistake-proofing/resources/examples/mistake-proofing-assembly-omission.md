Shows: an omission error (gasket skipped) walked top-down through all five hierarchy levels using "just draft it," a Level 2 prevention solution built around a presence sensor, and a Level 5 procedure explicitly labeled as an interim fallback rather than a fix.

**User:** We keep having gaskets skipped in the seal assembly step, station 4. Just draft solutions, don't ask me a bunch of questions.

**Assistant:** One note before you share more: describe the error and step in functional terms — leave out proprietary product specs or supplier names, roles and initials are fine. Since you said just draft it, I'll build this from what you've given me and flag anywhere a gemba look would sharpen it.

**Error mode:** gasket not installed before housing closure at Station 4
**Error type:** Omission — a required component was skipped, and nothing currently confirms it before the housing closes over it.
**Process step:** Station 4, seal assembly, gasket placement immediately before the closure fixture clamps
**Current detection:** end-of-line leak test — far downstream of where the gasket goes missing

Working the hierarchy from the top:

| Level | Feasibility | Proposed Solution | What Operator No Longer Needs to Do | Implementation Notes |
|-------|-------------|-------------------|--------------------------------------|---------------------|
| 1 — Elimination | Feasible, but only on the next design revision | Redesign the housing with an integrated, over-molded seal so there's no separate gasket to place at all | Nothing — the failure mode no longer exists | Requires a tooling and design change; long lead time — `[ASSUMED — verify]` cost and timeline, this needs the design team, not a floor fix |
| 2 — Prevention | Feasible now | Add a presence sensor (through-beam or weight check) on the closure fixture that mechanically won't allow the clamp to close unless the gasket is detected in place | No longer needs to remember or visually confirm the gasket is there — the fixture won't move without it | Medium cost: sensor, fixture modification, PLC logic change. Timeline for install is `[NEEDS GEMBA]` — needs an estimate from whoever owns that fixture |
| 3 — Detection | Feasible as a bridge until Level 2 is installed | Vision system at the closure station confirms gasket presence and flags before the next station, rather than waiting for end-of-line leak test | Still has to react to an alert, but doesn't have to remember to check on their own | Lower cost than the fixture interlock, but still catches the error after placement rather than preventing it |
| 4 — Mitigation | Feasible but weak here | None recommended — a missed gasket has no good "contain the consequence" option short of the existing leak test | N/A | The leak test already functions as mitigation; it's just far downstream |
| 5 — Procedure | Fallback only, for the transition period | Add a checklist line item: "confirm gasket present before closing fixture" | Nothing removed — the operator still has to remember, check, and mark it every cycle | Zero cost, immediate, but this is the weakest layer in the hierarchy and should come out once Level 2 is live |

**Why the checklist is the weakest control here:** apply the test — if the operator is distracted, tired, or rushed, does the checklist still catch the missed gasket? No. It depends entirely on the operator choosing to look and choosing to mark it, and it's exactly the same kind of attention lapse that causes the omission in the first place. A checklist doesn't remove the opportunity for the error or block the incorrect outcome; it just asks someone to remember to check for it. That's why Level 5 is labeled Procedure, not mistake-proofing — use it only as a bridge while the presence sensor (Level 2) gets installed, and take it out once that's live rather than stacking it on top permanently.

**Recommended path:** install the Level 2 presence sensor as the real fix. Use the Level 5 checklist only for the weeks between now and when the sensor is installed, and remove it once the sensor is confirmed working — leaving it in place after that just adds a redundant manual step that nobody needs.

**User:** What about the vision system idea — could we do both the sensor and the vision check?

**Assistant:** You could, but I'd think about it as sequencing rather than stacking. The Level 2 presence sensor physically blocks the fixture from closing without a gasket — once that's live and confirmed reliable, a Level 3 vision check at the same station is mostly redundant, since the failure it would catch (missing gasket) is the same one the sensor already prevents. Where a vision system earns its own place is if it's also verifying something the sensor can't — gasket seated correctly and not just present, for instance. If that's a real concern, say so and I'll add a second error mode (gasket present but misaligned) with its own hierarchy walk, since that's a different failure than the omission you described.

**User:** It's mostly just "present or not" for now — misalignment hasn't been a problem.

**Assistant:** Then I wouldn't add the vision system on top. The presence sensor at Level 2 already covers what you're describing, and adding a second detection layer for the same failure mode doesn't reduce risk further — it just adds cost and another thing to maintain. Keep detection in reserve for a failure mode the sensor doesn't already catch.

**User:** How do we know the sensor itself won't just get bypassed or unplugged if it's slowing the line down?

**Assistant:** That's a fair concern, and it's really a question about the specific interlock design, not the general approach — a presence sensor that's wired as a simple stop/alarm can sometimes get overridden under production pressure the same way a checklist gets skipped. The stronger version is a hard interlock: the closure fixture's clamp is mechanically or electrically gated so it physically cannot cycle without the sensor signal, not just alarmed while still able to run. Whether that hard-gate wiring is feasible on this specific fixture without a larger controls change is worth a look with whoever maintains it — `[NEEDS GEMBA]` — but the design intent should be "cannot bypass," not "will complain if bypassed."

**User:** That's the piece I was worried about. Who typically owns getting that specced out on our side?

**Assistant:** Usually whoever maintains the Station 4 fixture and its controls — the same person or team who'd know whether the clamp's actuator can be gated off the sensor signal directly, or whether it needs a PLC logic change to enforce the interlock rather than just sound an alarm. I don't have a name for that role from what you've shared, so I've left it as a fixture-maintenance contact in the closing block below rather than guessing a job title that might not match how your plant is organized.

---

**What this skill did:**
- Classified the gasket-skip issue as an Omission error and worked all five hierarchy levels from Elimination down for Station 4.
- Recommended a Level 2 presence-sensor interlock as the durable fix, with a Level 5 checklist labeled explicitly as a temporary bridge, not a solution.
- Flagged that a full redesign (Level 1, integrated seal) is feasible but belongs on the next design cycle, not this fix.

**What still needs a human:**
- Whether the presence-sensor fixture modification is actually feasible on this specific fixture, and how long it would take to install — `[NEEDS GEMBA]`.
- Cost and lead time for the Level 1 integrated-seal redesign — `[ASSUMED — verify]`.
- A decision on exactly when the Level 5 checklist gets removed once the sensor is confirmed working — don't let it become permanent by default.

**Suggested next step:** Take the presence-sensor concept to whoever maintains the Station 4 fixture and confirm whether a through-beam sensor can be mounted without interfering with the clamp cycle.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
