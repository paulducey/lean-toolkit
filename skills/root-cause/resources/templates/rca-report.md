# Root Cause Analysis Report Template

## 1. Problem statement
[Specific, scoped, observable — includes what, where, rate/frequency, and since when. Every number carries a source tag: [observed] / [from system: NAME] / [user estimate] / [NEEDS GEMBA].]

## 2. IS / IS-NOT table

| Dimension | IS (the problem exists here) | IS NOT (same thing, no problem) |
|---|---|---|
| What | | |
| Where | | |
| When | | |
| Who | | |
| How much | | |

Mark any cell not actually known as `[Unknown]` — never fill a cell with what seems likely.

## 3. Method selected

State the method (5 Whys, Fishbone, or Fishbone + Barrier Analysis) and why, in one sentence.

### 3a. 5 Whys (if used)

```
Problem: [restate]

Why 1: [answer]
Why 2: [answer]
Why 3: [answer]
Why 4: [answer]
Why 5: [answer — candidate root cause]

Root cause candidate: [restate as a clear, specific cause]
Verification question: If we fix [root cause], does [problem] go away — and stay gone?
```

### 3b. Fishbone (if used)

| Category | Candidate causes | Drilled? |
|---|---|---|
| Man / People | | |
| Machine | | |
| Method | | |
| Material | | |
| Measurement | | |
| Environment | | |

Top 1–2 candidates carried into a 5 Whys chain above.

### 3c. Barrier analysis (if applicable)

| Barrier | What it's designed to prevent | Why it failed here |
|---|---|---|
| | | |

## 4. Verified root cause

State one clear, specific cause. Tag `[VERIFIED]` if the verification question was answered yes with evidence, or `[CANDIDATE — needs gemba verification]` if not.

## 5. Provisional corrective action

One specific action that removes the verified (or candidate) root cause — not a list of everything wrong with the process.

## 6. What still needs gemba

- [List every `[ASSUMED]` or `[NEEDS GEMBA]` item left unresolved.]

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
