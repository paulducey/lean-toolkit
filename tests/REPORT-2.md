# Independent Validation Report 2 — Lean Toolkit Skills

Reviewer: adversarial, independent, re-testing from scratch (not trusting the authors' "fixed" claim). Method: `tests/VALIDATION-PROMPT.md` phases 1-4. Behavioral tests are **role-played** from `SKILL.md` text only — no live Claude Code session with the skill installed. Static audit run fresh; scripts executed for real with adversarial inputs.

## 1. Verdict

The toolkit is materially improved and is now reasonably safe to hand to a practitioner: the static audit is clean (0/12 checks failing across all 17 skills, vs. 61 failures previously), `oee.py`'s three numeric bugs are fixed, `vsm_calc.py` and all four `export_docx.py` wrappers now exist and work correctly on real and adversarial inputs, and every numeric result I recomputed by hand (control-chart, capacity-planner, vsm-calc) is arithmetically correct. The single biggest remaining gap is documentation drift, not code: README.md and GETTING-STARTED.md both say only "two of the skills... run a small Python script" (`oee-from-csv` and `vsm-calc`), but `kaizen-charter` and `twi-jbs` also instruct the assistant to run `scripts/export_docx.py` — a Path-A (paste-only, no Claude Code) user following the guide as written will hit an unrunnable script instruction mid-session with no warning that Claude Code was ever needed.

## 2. Static audit

```
python3 tests/audit_skills.py
17 skills · 0 failing checks
```
All 17 skills PASS all 12 automated checks (frontmatter, four required sections, when-not-to-use, data-safety line, `[NEEDS GEMBA]` tag, headcount guardrail, vocabulary mirroring, no AI jargon, referenced files exist). Manual read confirms `docs/CLOSING-BLOCK.md`, all `resources/templates/*.md`, all `resources/examples/*.md`, `scripts/md_to_docx.py`, `skills/vsm-calc/scripts/vsm_calc.py`, and all four `scripts/export_docx.py` wrappers physically exist and are non-empty.

## 3. Previous findings — closure status

| ID | Finding | Status | Evidence |
|---|---|---|---|
| B1 | `oee.py` fabricates 0.0% OEE on header-only CSV | **CLOSED** | Re-run on header-only CSV: prints `**No usable rows.** The header was recognized but no row carried planned_min, ideal_cycle_time and total_count together — nothing to compute.` and exits 2. No fabricated number. |
| B2 | `oee.py` never flags Availability outside 0-100% | **CLOSED** | `oee.py` line 123: `if A > 1 or A < 0: flags.append(...)`. Fed `downtime_min = -18`: Availability 103.8% now flagged: "Availability 103.8% is outside 0-100% — downtime is negative or exceeds planned time... not a usable result." A second flag also fires for the negative event itself. |
| B3 | `good_count` hard-required, contradicting stated graceful-degradation | **CLOSED** | `oee.py`'s `REQUIRED` dict now lists only `planned_min`, `ideal_cycle_time`, `total_count`; `good_count`/`reject_count` moved to `OPTIONAL`. Re-ran P4 (missing both): exit 0, prints "No good_count or reject_count column — Quality cannot be computed and is omitted below; this is A x P only, not OEE," then A×P = 75.0%. |
| B4 | `capacity-planner` computes headcount scenarios with no leadership-decision guardrail | **CLOSED** | `skills/capacity-planner/SKILL.md:123`: "Then say once, plainly: *'These tools free capacity; what the organization does with freed capacity is a leadership decision.'*" Also line 162 and the worked example ends with the sentence verbatim, exactly once, after both what-ifs. |
| B5 | `a3-coach` has no "just draft it" / `[NEEDS GEMBA]` instruction | **CLOSED** | `skills/a3-coach/SKILL.md:25`: "**Escape hatch:** on 'just draft it' → fill all eight boxes now. Every box that can't be filled... carries `[NEEDS GEMBA: …]`, never an invented number, cause, or countermeasure." Data-safety line also present at line 96. |
| M1 | 4 skills (`a3-coach`, `gemba-walk`, `standard-work`, `problem-statement`) have no data-safety line | **CLOSED** | All four now contain, verbatim: "Before any paste, in any setting, say: 'Leave out names of patients or employees...'" (e.g. `skills/gemba-walk/SKILL.md:114`, `skills/standard-work/SKILL.md:108`, `skills/problem-statement/SKILL.md:117`). |
| M2 | 12 of 17 skills have no headcount guardrail | **CLOSED** | Grepped all 17; every skill (including `root-cause`, line 164, and `capacity-planner`, B4 above) now carries the "leadership decision" sentence or an equivalent instruction to answer-then-say-once. |
| M3 | 11 of 17 skills have no vocabulary-mirroring instruction | **CLOSED** | Every skill file now contains the line "Mirror the user's vocabulary once they have used it — unit / clinician / patient / turnaround, PDSA rather than PDCA — and never correct it" (verified in all 17 via grep; `gemba-walk` additionally has an inline version at line 38). |
| M4 | 16 of 17 skills reference files that don't exist; `vsm_calc.py`/`md_to_docx.py`/`export_docx.py` absent | **CLOSED** | `find skills -type f` and the audit's `referenced_files_exist` check confirm every referenced example, template, and script now exists. `scripts/md_to_docx.py` (124 lines) and `skills/vsm-calc/scripts/vsm_calc.py` (126 lines) both run correctly (see Script results). |
| M5 | `vsm-calc` has no reconciliation check for PCE > 100% (VA time > lead time), and no script to catch it | **CLOSED** | `skills/vsm-calc/SKILL.md:123`: "Processing time can never exceed lead time. If the inputs make PCE come out above 100%... the calculator flags it as not usable... it is never printed as a plain result." Code matches: `vsm_calc.py` line 69-70, `if pce is not None and (pce > 1 or pce < 0): flags.append(...)`. |
| N1 | Auditor's jargon regex false-positives on "embedding" in `problem-statement` | **CLOSED** | Re-ran the exact regex from `tests/audit_skills.py` against the file: `JARGON.findall(...)` returns `[]`. The word "embedding" no longer trips it and the skill passes `no_ai_jargon` cleanly. |
| N2 | Over-100% number shown as bold headline before the flag appears | **OPEN** | Re-ran P6 (ideal cycle time 1.0): `**Performance = ... = 155.8%**` still prints under "## Availability x Performance x Quality" first; the caveat appears later under "## Flags". Sequencing is unchanged from the previous report. |
| N3 | Duplicate header rows tolerated with no warning message | **OPEN** | Fed a CSV with the header repeated mid-file: both real data rows summed correctly (Availability 97.1%, etc.), but no message anywhere states a duplicate header was found — same silent behavior as before. |
| N4 | 4 skills missing "How this skill works" section | **CLOSED** | `standard-work` (line 19), `gemba-walk` (line 27), `a3-coach` (line 19, titled "How this skill works (coach-first, draft on demand)"), and `problem-statement` (line 19) all now have the section. |

## 4. New findings (this pass)

**Major — README.md and GETTING-STARTED.md understate which skills need Claude Code / a script.** `README.md`: "Claude Code — for the two skills that run scripts" and `docs/GETTING-STARTED.md`: "Two of the skills — `oee-from-csv` and `vsm-calc` — run a small Python script." In fact `skills/kaizen-charter/SKILL.md:29` ("If asked to export: run `python3 skills/kaizen-charter/scripts/export_docx.py <saved.md>`") and `skills/twi-jbs/SKILL.md:26` give the same instruction, and both `scripts/export_docx.py` files exist and work. A Path-A user (paste-only, per the guide) using `kaizen-charter` or `twi-jbs` and asking to export to Word gets an instruction to run a script they were never told requires Claude Code. Fix: change "two" to "four" and list all four skills, or state the export-script skills separately from the calculation-script skills.

**Minor — `fmea-builder` has no explicit instruction against silently mapping a qualitative severity word to a number.** Scenario E1 ("Severity given as 'high'") expects the skill to "ask for or map to the 1-10 scale explicitly; does not silently assign 8." `skills/fmea-builder/SKILL.md` step 5 only says "Score S, O, and D using the anchor tables" (line 89) — since the Occurrence anchor table literally contains the word "High" at score 8 (line 39), a literal-minded assistant given "severity is high" has no anchor row containing that exact word for Severity, and no instruction telling it to show its mapping work or ask rather than silently pick a number.

**Minor — `5s-audit`'s "when not to use" list doesn't cover a takt-time ask (scenario C6).** `skills/5s-audit/SKILL.md`'s "Don't use it..." list names `vsm-calc`, `gemba-walk`, and `standard-work` for other overlaps, but nothing routes a direct "what's our takt time" question, which more naturally belongs to `capacity-planner` or `vsm-calc`. Role-played: an assistant with only this file loaded has no explicit instruction to decline and hand off that specific ask.

**Minor — `oee.py`/duplicate-header silence (N3, reconfirmed) and result-before-flag sequencing (N2, reconfirmed) remain open**, see table above.

**Minor — ragged Markdown tables in `md_to_docx.py` are not validated for column-count consistency.** Feeding a table where row lengths differ (`| a | b`/`|---`/`| 1 | 2 | 3 |`/`| x`) produces a well-formed .docx (verified by parsing `word/document.xml` with `xml.dom.minidom`) but with mismatched cell counts per row — no error, no warning, visually ragged in Word. Not a crash, but a silent malformed-table pass-through.

## 5. Script results

### `oee.py`

| # | Input | Expected | Actual | Pass/Fail |
|---|---|---|---|---|
| P1 | `line1_downtime.csv` | A 85.0%, P 88.2%, Q 96.0%, OEE 72.0%; Unmapped "elec"/"waiting mat'l" | Exact match | PASS |
| P2 | Same file, `--cycle-time-unit s`, ideal 30s | Same as P1 | Identical | PASS |
| P3 | Header only, no rows | Clear message, no crash | "**No usable rows**...", exit 2 | PASS |
| P4 | Missing `good_count`/`reject_count` | A×P reported, no traceback | A×P = 75.0%, explicit note, exit 0 | PASS |
| P6 | Ideal cycle time 1.0 (Perf>100%) | Flag printed | Performance 155.8% flagged correctly | PASS (sequencing still N2) |
| Negative downtime (-18 min) | (own case) | Reject or flag | Availability 103.8% now explicitly flagged; second flag for the negative event | PASS |
| Duplicate header mid-file | (own case) | Rejection/warning/silent-correct | Silently and correctly summed (97.1%/76.2%/96.5%), no duplicate-header message | PASS functionally, FAIL on message (N3) |
| 10,000-row file | (own case) | No crash, reasonable perf | 0.125s, no crash, correctly flagged several >100% Performance groups | PASS |
| Truly empty file (0 bytes) | (own case) | Clear message | "The file is empty." exit 1 | PASS |
| Malformed/short rows | (own case) | No crash | Computed on available data, empty losses table when no reason text present, no crash | PASS |

### `vsm_calc.py` and control-chart/capacity-planner examples (hand-recomputed)

| Example | Values recomputed | Result |
|---|---|---|
| `vsm-calc` `stamping-current.csv` (--demand 400 --available-time-s 27000) | Takt 67.5s, effective C/T for Blank/Form/Weld/Pack (52.8/73.6/78.9/40.0s), inventory days (3.00/2.00/0.88/0.15), processing 220s, lead 162,895s, PCE 0.1%, bottleneck Weld | All match script output exactly |
| `control-chart-cycle-time.md` (X-bar/R, n=3, 16 subgroups) | X-double-bar=86.48, R-bar=2.00, UCL_X=88.52, LCL_X=84.43, UCL_R=5.15 | All match to the printed precision |
| `capacity-planner-assembly-line.md` | Takt 67.5s; Station 3 ratio 1.16; system capacity 346/shift; gap 54 (13.5%); 15%-demand takt 58.70s and all five new ratios; Scenario 2 new ratio 1.63, capacity lost 205 units at Station 2 / 101 units plant-wide | All match by hand recalculation |

### `md_to_docx.py` and the four `export_docx.py` wrappers

All five ran without error and produced well-formed `word/document.xml` (validated with `xml.dom.minidom`) for: a real `oee.py` report, an empty (0-byte) Markdown file, a Markdown file with an unclosed code fence and a ragged table, a 100,000-line Markdown file (1.29s, 371KB output), and a file containing `<script>`, `&`, quotes, and non-ASCII text (all correctly XML-escaped, no injection). `skills/oee-from-csv/scripts/export_docx.py` correctly delegates to the shared `scripts/md_to_docx.py` via `runpy`.

## 6. Guides — practitioner usability findings

- **README.md / GETTING-STARTED.md understate script-dependent skills** — see New Findings above; this is the clearest way a first-time, Lean-literate/AI-naive user gets stuck mid-task on `kaizen-charter` or `twi-jbs`.
- **GETTING-STARTED.md Path A step 6** promises "The assistant will say the data-safety line first" — true for the skill files as currently written, but this is a promise about assistant behavior the guide cannot actually enforce from outside; a practitioner who never reads the SKILL.md has no way to verify it beyond trusting the chat.
- **The "paid orchestration skills" claim from the previous report's unverifiable-claims list is gone from README.md** — this repository now makes no promise it cannot fulfill within itself; a real improvement in scope honesty.
- **The five-things-to-know / troubleshooting table in GETTING-STARTED.md is genuinely good** for a Lean-literate, AI-naive reader — it anticipates the exact confusions (`[NEEDS GEMBA]` isn't an error, "it won't tell you how many to cut" is by design) without using AI jargon itself.
- **Minor friction:** GETTING-STARTED.md's Path B copy command (`cp -r lean-toolkit/skills/*/ lean-work/.claude/skills/`) differs in wording from README.md's (`cp -r skills/*/ .claude/skills/`) — both work if followed literally, but a user cross-referencing the two could be confused about which directory to run each from since the two commands assume different starting working directories and neither says so explicitly.

## 7. What could not be tested

All Phase 2 behavioral scenarios (all 17 skills, common set + skill-specific) were role-played by reading each `SKILL.md` and reasoning about what an assistant with only that file loaded would do — not run inside a live Claude Code or claude.ai session. This means: whether a real model would compensate for the two still-open gaps (fmea-builder's qualitative-severity ambiguity, 5s-audit's missing takt-time handoff) with its own judgment, or drift the way a literal-minded implementation would, is unverified in practice — only verified as present or absent in the written contract. I did not install any skill into a live `.claude/skills/` directory. I did not exhaustively review the two conference HTML files in `docs/` beyond spot-checking claims already covered above.

## 8. Counts

- Static audit: 17/17 skills pass all 12 checks, 0 failing checks (was 61 failing checks previously).
- Script results: 10/10 of my own oee.py test cases pass functionally (1 has an unfixed cosmetic gap, N3); vsm_calc.py and all recomputed example numbers check out exactly; all 5 md_to_docx.py/export_docx.py runs produce well-formed output.
- Findings this pass: 0 Blocker, 1 Major (script-count documentation drift), 4 Minor (fmea qualitative severity, 5s-audit takt handoff, N2/N3 reconfirmed open, ragged-table pass-through).
