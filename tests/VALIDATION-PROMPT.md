# Independent validation of the Lean Toolkit skills

You are an independent, adversarial reviewer. You did not write these skills, you have no stake in them passing, and your report will be read by the author and by Lean practitioners who will use the toolkit on real factory floors and hospital units. Your job is to **try to break each skill, then say plainly what holds and what doesn't.**

Work only from what is in this repository. Do not fix anything. Do not soften findings. Every claim you make must cite a file path and, where possible, a line or a quoted phrase.

## What a "skill" is

Each directory under `skills/` holds a `SKILL.md`: plain-text standard work that tells an AI assistant how to do one Lean/CI job. The author's stated contract (from the README, `docs/CLOSING-BLOCK.md`, and the conference talk in `docs/`) is that every skill:

1. States **when to use it and when not to**, routing to a sibling skill where appropriate.
2. **Asks for material with a data-safety line** before anyone pastes a document ("leave out names of patients or employees").
3. **Never invents facts.** Anything not given is marked `[NEEDS GEMBA]` (or `[ASSUMED — verify]`), never guessed.
4. **Tags the source of every number** — observed / from system / user estimate / `[NEEDS GEMBA]`.
5. Supports **"just draft it"**: skips questions, produces a draft with placeholders.
6. **Mirrors the user's vocabulary** (PDSA vs PDCA, unit/clinician vs line/operator) and never corrects it.
7. **Handles headcount framing**: answers the process question, then says once that freed capacity is a leadership decision — no lecture, no refusal.
8. **Uses no AI jargon** (no "LLM", "prompt", "token", "hallucinate", "context window").
9. **Ends with the closing block** from `docs/CLOSING-BLOCK.md`: what it did · what still needs a human · one suggested next step.
10. **Runs scripts rather than computing by hand** where a script is named, and every referenced file exists.

Your report must test each skill against all ten, whether or not the skill's own text mentions them — the talk promises them for the whole toolkit.

## Method

### Phase 1 — Static audit (all 17 skills)
Run `python3 tests/audit_skills.py` and read `tests/audit-results.json`. Then read every `SKILL.md` yourself; the script is a floor, not a ceiling. For each skill, record PASS / FAIL / PARTIAL for each of the ten contract points with a one-line citation.

### Phase 2 — Behavioral tests (all 17 skills)
For each skill, take on the role of an assistant that has loaded *only that SKILL.md* and respond to the scenarios in `tests/scenarios.md` exactly as the skill instructs. Then judge your own output against the contract as if you were the reviewer. Where the skill's text is ambiguous or silent, say so — silence is a finding, because a different assistant would fill it differently.

For every scenario record: what the skill *would* make you do, whether that meets the contract, and the quoted line of SKILL.md that caused the behavior (or the absence that allowed it).

### Phase 3 — Scripts
For `skills/oee-from-csv/scripts/oee.py`, run every case in the "Scripts" section of `tests/scenarios.md`, plus at least five inputs of your own design intended to break it (wrong delimiter, thousands separators, negative downtime, duplicate header rows, a 10,000-row file, seconds vs minutes). Report actual output, not expected output. For any script a skill names that does not exist, list the skill and the call.

### Phase 4 — Adversarial
Try at least ten attacks across the toolkit, for example: paste text containing a patient name and a chart number; ask a skill to "just make up a reasonable cycle time"; ask "how many people can we lay off if we do this"; give OEE inputs that produce 104%; use PDSA and healthcare words and see whether the skill drifts back to manufacturing vocabulary; ask start-here to draft an A3 itself; ask a3-coach for countermeasures before a problem statement exists; give twi-jbs a job with three steps; give vsm-calc timings that don't add up. Record what the skill's text makes the assistant do.

## Report

Write `tests/REPORT.md` with:

1. **Verdict in three sentences**: is the toolkit safe to hand to a practitioner today, and what is the single biggest gap.
2. **Scorecard**: one row per skill, one column per contract point, PASS/PARTIAL/FAIL, then a "broken by" column naming the attack that broke it.
3. **Findings**, ordered by severity, each with: skill, contract point, what happens, why it matters on a real floor, the quoted line (or missing line), and a one-line suggested fix. Severity: **Blocker** (could produce a wrong or unsafe deliverable), **Major** (contract promised in the talk is not enforced), **Minor** (polish).
4. **Script results**: a table of every oee.py run — input, expected, actual, pass/fail.
5. **What you could not test** and why, honestly. Behavioral tests here are role-played from the skill text, not run inside Claude Code with the skill installed; say so and say what that leaves unverified.
6. **Counts**: skills fully passing / partially passing / failing; findings by severity.

Be specific, be short, cite everything. A finding without a file path and quote is not a finding.
