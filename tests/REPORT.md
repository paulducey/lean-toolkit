# Independent Validation Report — Lean Toolkit Skills

Reviewer: adversarial, independent. Method: `tests/VALIDATION-PROMPT.md` phases 1-4, exactly. All behavioral tests are **role-played** from `SKILL.md` text only (no live Claude Code session with the skills installed) - see Section 5.

## 1. Verdict

**Not yet safe to hand to a practitioner as-is.** The one skill with a real script (`oee-from-csv`) is mostly sound but has two reproducible numeric bugs (unflagged negative/absurd Availability, and a hard failure when `good_count` is missing that contradicts the skill's own stated behavior). Every other skill is text-only: 16 of 17 skills reference example, template, or export files that do not exist anywhere in the repository, and two shared scripts (`scripts/md_to_docx.py`, `skills/vsm-calc/scripts/vsm_calc.py`) that skill text tells the assistant to run are entirely absent. The single biggest gap is that the ten-point contract the conference talk promises **for the whole toolkit** - the data-safety line "every time, every setting," the headcount guardrail sentence, and vocabulary mirroring - is only actually written into 4-6 of the 17 `SKILL.md` files; for the rest, an assistant loading only that file has no instruction to produce the promised behavior, so it becomes a matter of luck rather than design.

## 2. Scorecard

Contract points: 1 when/not-when · 2 data-safety line · 3 never invents facts · 4 source tags · 5 "just draft it" · 6 mirrors vocabulary · 7 headcount framing · 8 no AI jargon · 9 closing block · 10 runs scripts / files exist

P = PASS, ~ = PARTIAL, F = FAIL

| Skill | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | Broken by |
|---|---|---|---|---|---|---|---|---|---|---|---|
| start-here | P | P | P | P | P | P | P | P | P | F | referenced example files missing |
| a3-coach | P | F | ~ | ~ | F | F | F | P | P | F | A2 "just draft it" - no escape hatch, no `[NEEDS GEMBA]` tag anywhere in file; no data-safety line |
| root-cause | P | P | P | P | P | P | F | P | P | F | no headcount-guardrail sentence anywhere |
| gemba-walk | P | F | P | ~ | F | F | F | P | P | F | no data-safety line; no "just draft it" handling |
| problem-statement | P | F | P | ~ | F | F | F | P* | P | F | no data-safety line; no escape hatch; no mirroring; auditor jargon flag is a false positive (see Section 5) |
| oee-from-csv | P | P | P | P | P | P | F | P | P | ~ | script bugs (B1, P4); `export_docx.py`/`md_to_docx.py`/templates missing; no headcount language |
| vsm-calc | P | P | ~ | P | P | P | P | P | P | F | `scripts/vsm_calc.py` does not exist at all; no reconciliation check for V1 (VA time > lead time) in text |
| kaizen-charter | P | P | P | P | P | P | P | P | P | F | `export_docx.py`, templates, examples missing |
| twi-jbs | P | P | P | P | P | P | P | P | P | F | `export_docx.py`, templates, examples missing |
| standard-work | P | F | P | ~ | F | F | F | P | P | F | no data-safety line anywhere; no escape hatch |
| 5s-audit | P | P | P | P | P | F | F | P | P | F | no mirroring language; no headcount guardrail |
| smed-setup | P | P | P | P | P | F | F | P | P | F | no mirroring language; no headcount guardrail |
| control-chart | P | P | P | P | ~ | F | F | P | P | F | no mirroring, no headcount, no explicit escape hatch |
| fmea-builder | P | P | P | P | P | F | F | P | P | F | no mirroring; no headcount guardrail |
| mistake-proofing | P | P | P | P | P | F | F | P | P | F | no mirroring; no headcount guardrail |
| capacity-planner | P | P | P | P | P | F | F* | P | P | F | computes headcount-reduction scenarios directly (its purpose) yet contains no "leadership decision" sentence at all |
| daily-management | P | P | P | P | P | F | F | P | P | F | no mirroring; no headcount guardrail |

\* problem-statement's `no_ai_jargon` FAIL from the static auditor is a false positive - flagged word is "embedding" used in "embedding it in the problem statement," ordinary English, not AI jargon. Manual read: PASS.

\* capacity-planner's headcount column is the most severe of the "F"s: unlike the other headcount-silent skills, this one's entire purpose repeatedly triggers a headcount-reduction computation (see "what-if scenario modeling" and the mix-shift example), so the missing guardrail sentence is exercised on nearly every real use, not a hypothetical edge case.

## 3. Findings by severity

### Blockers

**B1 - `oee-from-csv` silently produces a fabricated OEE from an empty file.**
`skills/oee-from-csv/scripts/oee.py`, run on a header-only CSV (scenario P3), prints a full report headed `**OEE = A x P x Q** = 0.000 x 0.000 = **0.0%**` with no rows, no error, and no "no data" message. Scenario P3 in `tests/scenarios.md` expects "Clear message, no crash." The script gives neither a crash nor a clear message - it gives a plausible-looking wrong number. On a real floor, a `0.0%` OEE reported this way (rather than "no data found") could be read as a factual result. Fix: if zero groups have complete required data, exit with a clear message instead of computing with zeroed accumulators.

**B2 - `oee.py` never flags Availability outside 0-100%, unlike Performance.**
Fed a negative `downtime_min` value (a plausible data-entry error - someone types `-18` instead of `18`), the script computes `Availability = (480 - -18) / 480 = 103.8%` and shows it as a bare, unflagged bold result; the Six Big Losses table shows `Breakdowns | -18 | 100%`. My 10,000-row stress file (a grouping artifact of my own test data, but it exercises the same code path) produced groups with **Availability = -346.2%** and **Performance = -21.7%**, again with zero flag. Compare `skills/oee-from-csv/scripts/oee.py` line 123: `if P > 1: flags.append(...)` - there is no equivalent check for `A`. The skill's own quality bar (`SKILL.md`, "Performance or OEE above 100% is flagged... Never treat a number over 100% as a usable result") never mentions Availability, and the code matches that omission exactly. Fix: add the same out-of-range flag for Availability (and ideally reject negative downtime outright).

**B3 - `oee.py` cannot actually perform the "Quality omitted with an explicit note" behavior its own SKILL.md and scenario P4 promise, because `good_count` is a hard-required column.**
Running P4 (planned/ideal/total/downtime present, `good_count` and `reject_count` both absent) exits with code 2 and the message "Still needed: good_count" - it never reaches the calculation at all. But `skills/oee-from-csv/SKILL.md` states as a quality-bar rule: "A blank good_count or reject_count cell is excluded from the Quality calculation and named in the report - never treated as 100% good," and the code even contains the dead logic to do exactly that (the `if good is None:` branch and the "Quality: no usable good_count..." print). Scenario P4 explicitly expects "A×P reported... exit code 0 or 2 as designed." The script's REQUIRED dict (`skills/oee-from-csv/scripts/oee.py`, lines 6-11) lists `good_count` alongside `planned_min`/`ideal_cycle_time`/`total_count` as REQUIRED, so the graceful-degradation branch is unreachable dead code. This is a direct contradiction between the shipped script and the shipped skill instructions. Fix: move `good_count` to OPTIONAL, matching the SKILL.md's stated behavior, or change the SKILL.md's claim.

**B4 - `capacity-planner` computes headcount-reduction impact with no leadership-decision guardrail anywhere in the file.**
The skill's own description says it is used for "headcount reduction impact"; its "How this skill works" section runs a full recalculation for a "Headcount reduction" what-if scenario (`skills/capacity-planner/SKILL.md`, "Headcount reduction:" block) and its example row references "one-operator headcount reduction" as a worked scenario. Nowhere in the file - not in the quality bar, not in the how-it-works steps, not in the closing block - does it say anything resembling the sentence the conference talk promises for the whole toolkit ("these tools free capacity; what the organization does with freed capacity is a leadership decision"). `grep -n "leadership decision" skills/capacity-planner/SKILL.md` returns nothing. Contrast `vsm-calc` and `kaizen-charter`, which both carry this sentence almost verbatim. Scenario C5 ("how many people can we cut") is this skill's single most likely real-world use, and the file gives no instruction for the one line the whole toolkit is supposed to say once. Fix: add the guardrail sentence explicitly to capacity-planner's quality bar and how-it-works section.

**B5 - `a3-coach` has no instructed behavior for "just draft it," directly contradicting its own listed scenario A2.**
`tests/scenarios.md` lists "A2: User says 'just draft it' with only a title -> Draft with `[NEEDS GEMBA]` in most boxes; no invented background numbers" as a required scenario for this exact skill. `skills/a3-coach/SKILL.md` contains no escape-hatch language (`grep -il "just draft\|escape hatch" skills/a3-coach/SKILL.md` - no match), no mention of `[NEEDS GEMBA]` or `[ASSUMED]` tagging anywhere in the file, and no data-safety line. Role-played: an assistant with only this file loaded, told "just draft it" with a bare title, has nothing telling it to mark unknowns rather than invent a background, a goal number, or a root cause. It would very plausibly fabricate a plausible-sounding A3 with invented numbers - the single worst failure mode this toolkit exists to prevent. Fix: add an explicit escape hatch and `[NEEDS GEMBA]` placeholder rule, matching every other coaching skill in the toolkit.

### Major

**M1 - Four skills have no data-safety line at all: `a3-coach`, `gemba-walk`, `standard-work`, `problem-statement`.**
Confirmed by `python3 tests/audit_skills.py` (`data_safety_line: false` for all four) and by direct read - none of the four files contains the phrase "leave out names" or any equivalent. Contract point 2 requires this "before anyone pastes a document," and the talk promises it "every time, every setting." Scenario C3 ("I'll paste our procedure/export/notes") would get no safety line at all from these four skills as currently written.

**M2 - Twelve of 17 skills carry no headcount-guardrail sentence, though the talk promises it "the same thing a good sensei would say" for the whole toolkit.**
Only `start-here`, `kaizen-charter`, `twi-jbs`, and `vsm-calc` actually contain guardrail-style language (`root-cause` fails the automated check too - `headcount_guardrail: false` - and manual read confirms no "headcount" text anywhere in `skills/root-cause/SKILL.md`, so scenario C5 posed directly to root-cause has no instructed response at all). `5s-audit`, `smed-setup`, `control-chart`, `fmea-builder`, `mistake-proofing`, `daily-management`, `capacity-planner` (see B4), and `oee-from-csv` are all silent on this. An assistant loading any of these alone, asked "how many people can we cut if we do this," has nothing in the file directing it to answer the process question and add the one leadership-decision sentence - it would improvise, and improvisation is exactly what contract point 7 exists to prevent.

**M3 - Eleven of 17 skills have no vocabulary-mirroring instruction.**
Only `kaizen-charter`, `root-cause`, `twi-jbs`, `vsm-calc`, `oee-from-csv`, and `start-here` instruct the assistant to adopt the user's own words (PDSA vs. PDCA, unit/clinician vs. line/operator). `5s-audit`, `a3-coach`, `capacity-planner`, `control-chart`, `daily-management`, `fmea-builder`, `gemba-walk`, `mistake-proofing`, `problem-statement`, `smed-setup`, `standard-work` say nothing about it. Scenario C4 (healthcare vocabulary) run against, say, `fmea-builder` or `control-chart` has no textual pressure to keep saying "clinician" instead of drifting back to "operator," and no PHI-sentence instruction either (data-safety lines in these files are generic, not healthcare-aware - e.g. `control-chart`'s line only mentions "proprietary product names," nothing about patients).

**M4 - Every non-oee skill (16 of 17) references files that do not exist anywhere in the repository.**
`python3 tests/audit_skills.py` reports 61 failing checks, the overwhelming majority `referenced_files_exist: false`, listing 45 distinct missing paths: every skill's `resources/examples/*.md`, most skills' `resources/templates/*.md`, the shared `resources/closing-block.md` referenced by 6 skills, `skills/{kaizen-charter,oee-from-csv,twi-jbs,vsm-calc}/scripts/export_docx.py`, a shared `scripts/md_to_docx.py` at repo root, and `skills/vsm-calc/scripts/vsm_calc.py`. `find skills -type f` confirms the only files that actually exist under `skills/` are the 17 `SKILL.md` files plus `oee-from-csv/scripts/oee.py` and its one sample CSV. Any behavior the skill text promises by pointing at an example ("see `resources/examples/...`") or by instructing the assistant to run a named script is unverifiable and, for the scripts, non-functional - `vsm-calc`'s core deliverable ("Run the calculator... `python3 skills/vsm-calc/scripts/vsm_calc.py`") cannot be executed at all; this is contract point 10 failing outright for the toolkit's second most-used numeric skill.

**M5 - `vsm-calc` has no textual instruction to catch VA-time > lead-time (scenario V1), and its calculator script doesn't exist to catch it programmatically either.**
`grep -n "reconcile\|VA ratio\|PCE.*100" skills/vsm-calc/SKILL.md` returns nothing. The file's quality bar lists sensible rules (sourced cycle times, takt formula shown, bottleneck via effective cycle time) but no rule resembling "if total value-added time exceeds total lead time, flag it - do not report PCE > 100%." Role-played against V1 (cycle times and lead times that don't reconcile): nothing in the file tells the assistant to notice or refuse a >100% PCE; the closest general safeguard is the analogous rule in `oee-from-csv` (Performance > 100% flag), which vsm-calc's own text does not carry over. Combined with M4 (no script exists), this scenario is untested and unguarded twice over.

### Minor

**N1 - The static auditor's `no_ai_jargon` check has a false-positive regex.** `python3 tests/audit_skills.py`'s jargon pattern `\b(...|embedding)\w*` matches ordinary English "embedding" in `skills/problem-statement/SKILL.md`: "The solution (poka-yoke) may be correct, but embedding it in the problem statement closes off analysis." Verified with a standalone regex test - the only match in the file is this one. The skill is clean of actual AI jargon; the auditor's floor over-reports by one here. Worth narrowing the pattern so the floor doesn't cry wolf and get ignored on a real hit elsewhere.

**N2 - `oee.py` shows the flagged over-100% number as the bold headline before the reader ever sees the flag.** In P6/B2/B6, `**Performance = ... = 155.8%**` (etc.) prints under "## Availability x Performance x Quality" first, and the caveat only appears several sections later under "## Flags." A reader who stops at the top-line numbers - plausible on a busy floor - sees an unflagged-looking bold percentage. Not incorrect, but the sequencing works against the skill's own stated goal.

**N3 - Duplicate header rows mid-file are tolerated by `oee.py` only by accident, with no warning message.** Feeding a CSV with the header row repeated in the middle of the data (my own break-it case) produced the numerically correct total (two real rows summed correctly), but only because the literal text "date," "shift," etc. failed to parse as numbers and the resulting phantom group was silently dropped. There is no message telling the user a duplicate header was found and ignored.

**N4 - `standard-work`, `gemba-walk`, `a3-coach`, `problem-statement` have no explicit "How this skill works" numbered procedure**, unlike every other skill (confirmed by the auditor's `section:how this skill works: false` and manual read - these four go straight from "when to use" into content sections). This correlates exactly with the four skills missing the data-safety line (M1) and the escape hatch (B5) - the skills without a structured "how it works" checklist are the ones where the behaviors that checklist would enforce also went missing.

## 4. Script results (`skills/oee-from-csv/scripts/oee.py`)

| # | Input | Expected | Actual | Pass/Fail |
|---|---|---|---|---|
| P1 | `resources/examples/line1_downtime.csv` | A 85.0%, P 88.2%, Q 96.0%, OEE 72.0%; losses 31/24/9/8; Unmapped "elec"/"waiting mat'l"; planned/unplanned flag present | A 85.0%, P 88.2%, Q 96.0%, OEE 72.0%; Breakdowns 31, Setup&adj 24, Idling 9, Unmapped 8 ("elec" 5, "waiting mat'l" 3); flag present | PASS |
| P2 | Same file, `--cycle-time-unit s`, ideal cycle 30s | Same results as P1 | Identical output to P1 | PASS |
| P3 | Header only, no rows | Clear message, no crash | Prints a full report with fabricated 0.0% OEE, no "no data" message, exit 0 | FAIL (B1) |
| P4 | Missing `good_count` and `reject_count` | Quality omitted with note; A×P reported; exit 0 or 2, no traceback | Hard-fails at column-resolution stage: "Still needed: good_count," exit 2; A×P never computed | FAIL (B3) |
| P5 | Semicolon delimiter | Parsed | Parsed correctly, identical numeric result to P1 | PASS |
| P6 | Ideal cycle time 1.0 (Performance > 100%) | Flag printed; number still shown but marked unusable | Flag printed correctly; OEE 144.0% shown as bold headline above the flag | PASS (see N2 for sequencing) |
| P7 | `planned_downtime` = yes on the changeover row | Changeover excluded from unplanned; missing-split flag absent | Changeover (24 min) correctly excluded; missing-split flag correctly absent | PASS |
| P8 | Two shifts, two dates | Per-group table appears; totals consistent with sum | Per-group table present, 4 rows; totals (planned 1920, downtime 63, total 2820, good 2721) match the sum exactly | PASS |
| B1 | Negative `downtime_min` (-18) | (my case) - expect either rejection or a flag | Availability computed as 103.8% with no flag; Pareto shows "-18 min, 100%" | FAIL (B2) |
| B2 | Thousands-separator quantities ("7,200", "6,910") | Parsed correctly | Parsed correctly via comma-strip; resulting 779.2% Performance correctly flagged | PASS |
| B3 | Duplicate header row mid-file | (my case) - expect rejection, warning, or silently-correct handling | Silently and correctly dropped (both real rows summed correctly) - no message that a duplicate header was found | PASS functionally (see N3) |
| B4 | Tab-delimited file | (my case) - expect correct delimiter sniffing | Parsed correctly, identical result to P1 | PASS |
| B5 | 10,000-row synthetic file | (my case) - expect no crash, reasonable performance | Ran in 0.12s, no crash; incidentally reproduced the unflagged-Availability bug with extreme values (-346.2%, -21.7%, no flag) | PASS (perf), reinforces FAIL (B2) |
| B6 | Seconds-valued ideal cycle time run without `--cycle-time-unit s` | (my case) - expect the resulting absurd Performance to be caught | Performance 5294.1%, correctly flagged as over 100%, though the flag doesn't suggest a unit mismatch as the likely cause | PASS functionally |

## 5. What I could not test, and what that leaves unverified

- All behavioral scenarios (Phase 2, all 17 skills x common set + skill-specific additions) were role-played by reading each `SKILL.md` and reasoning about what an assistant with only that file loaded would do - not run inside an actual Claude Code session with the skill installed. This means: I cannot verify how a real model actually resolves ambiguity the text leaves open (e.g., whether it would spontaneously add a data-safety line even when the file doesn't instruct one, out of its own training, or whether it would silently drift vocabulary back to manufacturing terms as the conversation gets longer). Everywhere I wrote "no instruction for X," that is a fact about the file, not a guarantee about model behavior - a capable model might compensate; a literal-minded one would not. This leaves the actual severity of M1-M3 and B5 genuinely unverified in practice, only verified as a gap in the written contract.
- I could not test the six paid orchestration skills mentioned in `README.md` ("Six paid orchestration skills... available at paulducey.com/skills") - they are not in this repository.
- I could not run `vsm-calc`'s calculator, `export_docx.py`, or `md_to_docx.py` at all - none exist (M4). All statements about their behavior are therefore about what the skill text claims they do, not what they actually do.
- I did not attempt to install any skill into an actual `.claude/skills/` directory and interact with it live; the prompt's method section describes exactly this limitation and asks it be stated plainly, which I have done here.
- I did not review the two HTML files under `docs/` (`nelean2026-ai-at-the-gemba.html`, `nelean2026-script.html`) exhaustively - only spot-checked them for the specific promises cited in this report (headcount, closing block, jargon, data safety, vocabulary, "all seventeen").

## 6. Counts

- Skills fully passing (all 10 contract points, manual read, no missing referenced files): 0 of 17. (Even the strongest skills - `kaizen-charter`, `twi-jbs`, `start-here` - fail point 10 because referenced example/template files don't exist.)
- Skills partially passing (7-9 of 10 points, or PASS with caveats noted): 6 of 17 - `start-here`, `root-cause`, `oee-from-csv`, `vsm-calc`, `kaizen-charter`, `twi-jbs`.
- Skills failing (4 or more contract points weak/absent): 11 of 17 - `a3-coach`, `gemba-walk`, `problem-statement`, `standard-work`, `5s-audit`, `smed-setup`, `control-chart`, `fmea-builder`, `mistake-proofing`, `capacity-planner`, `daily-management`.
- Findings by severity: 5 Blocker (B1-B5) · 5 Major (M1-M5) · 4 Minor (N1-N4).
