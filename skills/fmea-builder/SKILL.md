---
name: fmea-builder
description: Build a Failure Mode and Effects Analysis (FMEA) table — identifying failure modes, their effects and causes, scoring Severity, Occurrence, and Detection on 1–10 scales to calculate Risk Priority Numbers (RPN), and producing a ranked action list with owners and target dates. Use when someone says "FMEA", "failure mode", "risk analysis", "what could go wrong", "failure analysis", "RPN", "process risk", "design risk", "we need to identify failure modes", "proactive risk assessment", or is preparing a new product, process, or equipment for launch and wants to identify risks before they occur.
license: MIT
---

# FMEA Builder

A Failure Mode and Effects Analysis is a structured, proactive risk tool: it asks *what could go wrong, how bad would it be, how often might it happen, and how likely are we to catch it before it reaches the customer.* The output is a ranked table of risks with recommended actions — built before failures occur, not after. This skill builds the FMEA table, enforces the severity priority rule, and produces an actionable output ready for review with the team.

## When to use / when not to

Use it for process FMEAs (P-FMEA) on production and service processes, design FMEAs (D-FMEA) for new products or equipment, and equipment/maintenance FMEAs for critical assets.

Don't use it to investigate a failure that has already occurred (→ `root-cause`), to design controls for a specific failure mode after the FMEA identifies it (→ `mistake-proofing`), or to monitor process stability after controls are put in place (→ `control-chart`). If an FMEA produces priority actions that require a formal improvement event, use `kaizen-charter` to scope it.

## The three scoring dimensions

**Severity (S) — 1 to 10**

Severity scores the worst-case consequence of the failure effect on the customer (internal or external) or on safety and regulatory compliance. Severity is a property of the *effect*, not the failure mode — the same failure mode can have different severity scores if it produces different effects in different contexts.

| Score | Anchor description |
|---|---|
| 10 | Safety hazard or regulatory violation — potential for injury, death, or product recall without warning |
| 9 | Safety hazard with warning, or serious regulatory exposure |
| 8 | Loss of primary function — product or process fails to perform its intended purpose |
| 7 | Significant performance degradation; customer very dissatisfied |
| 6 | Partial loss of function; customer dissatisfied; rework required |
| 5 | Moderate effect; customer experiences discomfort; some rework |
| 4 | Minor effect noticed by most customers; minor rework |
| 3 | Minor effect noticed by some customers; minor process disruption |
| 2 | Very minor effect; noticed only by discerning customers; no rework |
| 1 | No discernible effect |

**Occurrence (O) — 1 to 10**

Occurrence scores the likelihood that the specific cause will occur and produce the failure mode over the product or process lifetime.

| Score | Approximate frequency |
|---|---|
| 10 | Almost certain — failure is expected to occur repeatedly |
| 9 | Very high — repeated failures likely |
| 8 | High — failures occur frequently |
| 7 | Moderately high — occasional failures |
| 6 | Moderate — occasional failures |
| 5 | Low-moderate — relatively few failures |
| 4 | Low — isolated failures |
| 3 | Very low — only rare isolated failures |
| 2 | Remote — failure is unlikely |
| 1 | Essentially impossible — failure is not expected |

**Detection (D) — 1 to 10**

Detection scores the likelihood that current controls *fail* to detect the failure mode or its cause before it reaches the next customer (internal or external). **Lower detection scores mean better detection** — a score of 1 means the control will almost certainly catch the failure; a score of 10 means there is no detection mechanism at all.

| Score | Detection likelihood |
|---|---|
| 10 | No current control — failure will not be detected |
| 9 | Control is unreliable; detection is uncertain |
| 8 | Control detects only when failure is already severe |
| 7 | Control may detect; effectiveness is inconsistent |
| 6 | Moderate chance of detection with current controls |
| 5 | Controls have moderate effectiveness |
| 4 | Controls are likely to detect |
| 3 | Controls have high probability of detection |
| 2 | Controls almost certain to detect |
| 1 | Controls are certain to detect before reaching customer |

## RPN calculation and its limits

```
RPN = Severity × Occurrence × Detection
```

RPN ranges from 1 to 1,000. Higher RPN = higher risk priority.

**The severity priority rule — the most important rule in this skill:**

**High severity items ALWAYS receive action regardless of RPN.** A failure mode with Severity 9 and RPN 72 (e.g., S=9, O=2, D=4) outranks a failure mode with Severity 4 and RPN 120 (S=4, O=6, D=5) for action priority — regardless of RPN arithmetic. This rule exists because an infrequent, detectable safety hazard is still a safety hazard.

**Threshold for mandatory review regardless of RPN:** Severity ≥ 8 always requires a recommended action and team review. Never leave a high-severity row with "none — RPN is acceptable."

**RPN is a ranking tool, not an absolute threshold.** "Our RPN is below 100 so no action needed" is not a valid conclusion if severity is high. Flag this reasoning explicitly if it appears.

## How this skill works

**Open with one sentence the first time:** "Describe the process, design, or equipment — what it does, where it operates, and what concerns you — and I'll help build the FMEA."

1. **Read everything given.** Identify scope (process, design, equipment), the function or step being analyzed, and any known failure history or risk concerns.
2. **Define the scope and function** — one sentence per process step or component being analyzed. A function statement is required: *"The function of [step/component] is to [action] so that [outcome]."*
3. **Identify failure modes** for each function — the specific ways the function could fail to perform. Failure modes are not effects; they are failure mechanisms. "Weld fails" is a failure mode; "customer receives defective part" is an effect.
4. **For each failure mode:** identify effects (downstream), causes (upstream), and current controls (both prevention and detection).
5. **Score S, O, and D** using the anchor tables. Show the rationale for any score of 7 or above.
6. **Calculate RPN** and rank the table by: (a) Severity ≥ 8 first regardless of RPN, then (b) remaining rows by RPN descending.
7. **Recommend actions** — one action per row where Severity ≥ 8 or RPN is above threshold. Each action targets a specific S, O, or D driver.
8. **Assign owner and target date** — propose a role and a realistic timeframe; the user fills in the actual names.
9. **Close** with the shared closing block, specific to this FMEA.

Data-safety line: *"Leave out proprietary process parameters or supplier names; describe failure modes and effects in functional terms — that's sufficient for the analysis."*

**Escape hatch:** on "just draft it" → build from the information given, use `[ESTIMATED]` scores where data is missing, and flag which scores most need team validation.

## FMEA table format

```
Process/Design/Equipment: [name]
Scope: [step range or component list]
Date: [date]
Revision: [1]

| # | Function / Step | Failure Mode | Effect(s) | S | Cause(s) | O | Current Controls | D | RPN | Priority | Recommended Action | Owner (role) | Target Date | Notes |
|---|----------------|-------------|-----------|---|----------|---|-----------------|---|-----|----------|-------------------|-------------|------------|-------|
```

- Sort: Severity ≥ 8 rows first (regardless of RPN), then remaining rows by RPN descending.
- Flag every Severity 9–10 row with `[SAFETY/REGULATORY]`.
- Leave the "Notes" column for assumptions, data gaps, and verification needs.

## Recommended action guidelines

Actions should target the highest-leverage driver:

- **To reduce Severity:** redesign or eliminate the failure mode at the source — process or design change. Detection and occurrence actions do not reduce severity.
- **To reduce Occurrence:** add prevention controls, address the root cause of the failure, improve incoming material, reduce variation (→ `control-chart`), apply mistake-proofing (→ `mistake-proofing`).
- **To reduce Detection:** add or improve inspection controls, move detection earlier in the process, add automated detection, apply mistake-proofing at the detection point.

A recommended action of "train operators" addresses none of these dimensions reliably — it does not reduce severity, cannot reliably reduce occurrence, and does not reduce detection score. Flag this and recommend a structural alternative.

## Quality bar

- Every function statement is written in the form "[step/component] performs [action] so that [outcome]" — not just a label.
- Failure modes are mechanisms, not effects — each failure mode is reviewable by two people and would produce the same classification.
- Severity ≥ 8 rows have a recommended action — no exceptions.
- The severity priority rule is enforced in the sort order — no high-severity row is buried below a low-severity high-RPN row.
- Detection scores reflect current controls actually in place — not wishful controls, not planned controls.
- Any estimated score is marked `[ESTIMATED]`.
- "Train operators" is not accepted as a recommended action that changes any of S, O, or D without a structural complement.
- The FMEA table includes owner (role) and target date for every recommended action.

## Closing block

Append the block from `docs/CLOSING-BLOCK.md`, filled in for this FMEA. The first bullet under "what still needs a human" should name the failure mode with the highest severity score that has the most uncertain occurrence or detection estimate — the one where the team's real-world knowledge would most change the RPN and action priority.

## Examples

- `resources/examples/fmea-builder-assembly-process.md` — P-FMEA for a five-step assembly process, two Severity 9 rows surfaced with mandatory actions, RPN ranking applied to remaining rows, mistake-proofing and control-chart referenced for specific action rows.
- `resources/examples/fmea-builder-new-equipment.md` — equipment FMEA for a filling machine during commissioning, estimated scores marked throughout, team review items identified, safety failure modes isolated at the top of the table.
