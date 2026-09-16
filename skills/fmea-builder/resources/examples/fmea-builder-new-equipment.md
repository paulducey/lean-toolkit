Shows: an equipment FMEA built with "just draft it" during commissioning, every score marked [ESTIMATED] since the machine hasn't run production yet, and safety/regulatory failure modes sorted to the top of the table.

**User:** We're commissioning a new filling machine next month. Just draft an FMEA for it — we don't have real run data yet, just the station list.

**Assistant:** That's enough to start. One note before you paste anything: leave out proprietary process parameters or supplier names; functional descriptions of what each station does are sufficient. Go ahead with the station list.

**User:** Five stations: bowl/hopper feed, fill nozzle dispense, capping head, cap torque check, label applicator. It's a liquid product with a declared net-contents tolerance, so underfill is a regulatory issue, not just a customer complaint.

**Assistant:** Since this is commissioning and you asked me to just draft it, I'm building the table from the station list alone, marking every score `[ESTIMATED]` — none of this reflects a qualification run yet, so treat these as a starting point for the team to correct once real data exists.

Function statements:
- Bowl/hopper feed performs product staging so that the fill nozzle always has product available to dispense.
- Fill nozzle dispense performs metered fill so that each container receives the declared net contents.
- Capping head performs cap application so that the container is sealed against leakage and contamination.
- Cap torque check performs torque verification so that under- or over-torqued caps don't proceed.
- Label applicator performs label placement so that the correct product identity and declared contents travel with the container.

| # | Function / Step | Failure Mode | Effect(s) | S | Cause(s) | O | Current Controls | D | RPN | Priority | Recommended Action | Owner (role) | Target Date | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Bowl/hopper feed | Foreign material introduced during refill | Contamination reaches product, possible recall | 10 `[ESTIMATED]` | Open refill process, no barrier | 2 `[ESTIMATED]` | None planned yet | 9 `[ESTIMATED]` | 180 | 1 [SAFETY/REGULATORY] | Install foreign-object/metal detection at bowl feed before commissioning sign-off | Equipment Engineer | [ASSUMED — verify] before qualification run | Highest severity in the table — mandatory review regardless of RPN |
| 2 | Fill nozzle dispense | Nozzle clogs or under-fills | Underfilled container ships — net-contents regulatory exposure | 9 `[ESTIMATED]` | Nozzle wear, viscosity variation | 5 `[ESTIMATED]` | Checkweigher specified but not yet validated | 8 `[ESTIMATED]` | 360 | 2 [SAFETY/REGULATORY] | Complete checkweigher validation with automatic reject before production release | Automation Engineer | [ASSUMED — verify] before qualification run | Highest RPN in the table |
| 5 | Label applicator | Wrong label applied (SKU mix-up) | Mislabeled product ships, allergen/regulatory risk | 9 `[ESTIMATED]` | Multiple SKUs run on shared line | 3 `[ESTIMATED]` | Barcode verification specified but not yet validated | 6 `[ESTIMATED]` | 162 | 3 [SAFETY/REGULATORY] | Validate barcode scan-verification before first SKU changeover trial | Quality Engineer | [ASSUMED — verify] before first changeover | |
| 3 | Capping head | Cap not fully seated (cross-threaded) | Leak or contamination path in transit | 8 `[ESTIMATED]` | Cap feed misalignment, cap variation | 4 `[ESTIMATED]` | Vision system specified but not yet validated | 7 `[ESTIMATED]` | 224 | 4 [SAFETY/REGULATORY] | Validate cap-seating vision system during commissioning trials | Automation Engineer | [ASSUMED — verify] before qualification run | |
| 4 | Cap torque check | Torque station miscalibrated, passes bad caps | Under/over-torqued cap ships undetected | 7 `[ESTIMATED]` | Station not yet calibrated to a known standard | 3 `[ESTIMATED]` | None — no audit sampling plan yet | 8 `[ESTIMATED]` | 168 | 5 | Add an independent torque audit sampling plan alongside inline check | Quality Technician | [ASSUMED — verify] before qualification run | Only row under Severity 8, placed last |

Sort order: the four Severity ≥8 rows are grouped at the top (ordered by severity, then RPN within that group) regardless of their RPN — Row 1 (severity 10, RPN 180) sits above Row 2 (severity 9, RPN 360) because severity leads the sort, not RPN. Row 4 is the only row under the severity threshold and sits last even though its RPN (168) is close to Row 1's.

Every occurrence and detection number above is a placeholder built from the station list, not from a run — **the entire Occurrence and Detection column needs a qualification trial to replace it with real counts, which is [NEEDS GEMBA]**. Severity is the one dimension that doesn't depend on run data — it's about the worst-case effect, which you already described.

**User:** Why does Row 1 outrank Row 2 when Row 2's RPN is twice as high?

**Assistant:** Because the severity priority rule sorts on severity first, then RPN within that group — RPN isn't the tiebreaker across severity levels, only within them. Row 1 (foreign material at the bowl feed) is severity 10, the worst possible outcome on the scale: a potential recall with no control in place at all. Row 2 (underfill at the nozzle) is severity 9 with a much higher RPN (360 vs. 180), because its occurrence and detection estimates are both worse. Both are safety/regulatory rows and both get mandatory action regardless — the ordering just reflects that a severity-10 failure mode gets first look even though, on the current guesses, it's arithmetically less likely to slip through than the severity-9 one. If your team's actual risk appetite works differently, that's a judgment call for whoever reviews this table, not something the RPN math should override quietly.

**User:** Got it. One more — should we hold commissioning until all three planned controls (checkweigher, vision system, barcode scan) are validated?

**Assistant:** That's a release decision, not something this table can make for you — it depends on what your commissioning gate requires and what risk your team is willing to accept for a limited early run. What the table does tell you is that three of the four Severity ≥8 rows are currently relying on a control that's "specified but not yet validated," which means right now those rows are effectively running at their worst-case Detection score until proven otherwise. If commissioning starts before validation is done, I'd treat those three rows as still open risks, not closed ones.

**User:** If we had to pick just one of the three controls to validate first, which would you flag?

**Assistant:** The checkweigher on Row 2, since that row has the highest RPN in the table (360) and the underfill failure it's meant to catch is a declared net-contents issue — a regulatory exposure that doesn't require anything else to go wrong at the same time. The cap-seating vision system and barcode label scan both matter, but Row 2's combination of severity, occurrence, and a control that isn't proven yet is the largest single gap on the table right now. That's a suggestion based on the numbers here, not a substitute for your team's own commissioning priorities — if there's a reason Row 1's contamination control matters more operationally (say, a customer audit scheduled before the checkweigher can be validated), that would reasonably move it up.

**User:** Once the qualification trial runs, what should change about this table versus what we have now?

**Assistant:** Every `[ESTIMATED]` Occurrence and Detection score should get replaced with a number tied to what actually happened during the trial — real defect counts per station, and whether the planned controls (checkweigher, vision system, barcode scan) actually caught what they were built to catch or missed things. Severity generally won't move, since it's about the worst-case effect and that doesn't change with a trial run. Once the real numbers are in, re-run the RPN math and re-check the sort order — it's possible a row that looks scary today (like Row 1's contamination risk) turns out to be well-controlled once the detection equipment is proven, while something that looked fine on paper turns up a gap nobody estimated correctly. Treat this draft as the starting hypothesis, not the final answer.

---

**What this skill did:**
- Built a 5-row equipment FMEA for the new filling machine from the station list alone, since you asked for a draft with no run data yet.
- Every Occurrence and Detection score is marked `[ESTIMATED]` and needs replacing once the machine runs; Severity is stable since it doesn't depend on the run.
- All four Severity ≥8 rows are safety/regulatory and sit ahead of the one Severity-7 row, regardless of RPN.

**What still needs a human:**
- The entire Occurrence and Detection column is a placeholder — run a qualification trial and pull actual failure counts before treating any RPN here as real. [NEEDS GEMBA]
- Whether the checkweigher, vision system, and barcode verification actually get validated before production release — right now they're planned controls, not proven ones.
- Row 1 (contamination at bowl feed) has the highest severity in the table and no control at all specified yet — that gap needs engineering attention before commissioning sign-off, not after.

**Suggested next step:** Take this table to the commissioning team before the qualification run and confirm which of the three "specified but not yet validated" controls (checkweigher, cap vision system, barcode verification) will actually be live for that run.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
