# Example: fishbone plus barrier analysis on a medication near-miss, drilling past "nurse didn't check"

**User:** We had a medication near-miss on our unit last week — wrong dose almost given, caught before administration. Charge nurse wants a root cause done before the safety committee meets.

**Assistant:** Before you paste any notes or the incident report — leave out names of patients or employees, and anything the organization treats as confidential; roles and initials are fine. Please also don't paste protected health information — no patient identifiers, no chart numbers, no dates of birth tied to a name. Tell me what you've seen — what happened, where, and how often something like this occurs — and I'll help find the real cause, not just the symptom.

**User:** A clinician was about to administer a 10x overdose of a medication on our med-surg unit. It was caught by the second clinician during the double-check, so no harm occurred. This is the third near-miss like this in about 4 months that I know of.

**Assistant:** Three similar near-misses in four months with multiple contributing factors is a fishbone situation rather than a single chain — I'll use fishbone to find where the causes cluster, then drill the top ones with 5 Why. First, let's scope it with IS/IS-NOT. Does this pattern show up on all shifts, or a particular one? And is it always the same medication or class?

**User:** Mostly on high-alert medications — the ones needing a double-check. Seems to happen more on night shift, though I'm not certain that's really true or just what I remember.

**Assistant:** Good — flag that as unconfirmed rather than a fact. Let's build the table.

## IS / IS-NOT

| Dimension | IS | IS NOT |
|---|---|---|
| What | High-alert medication dosing near-misses | Routine (non-high-alert) medication errors — not seeing a pattern |
| Where | Med-surg unit | Other units — `[Unknown]`, not yet checked |
| When | Night shift impression [ASSUMED — verify against incident log] | `[Unknown]` — day shift rate not pulled yet |
| Who | Multiple different clinicians involved across the 3 events | `[Unknown]` |
| How much | 3 near-misses in ~4 months [user estimate] | `[Unknown]` baseline rate before this period |

**Method: Fishbone** (multiple contributing factors, pattern across several events) followed by 5 Why on the top branches, then barrier analysis since a double-check safeguard is directly involved.

**Assistant:** Let's populate the fishbone. What do you know about how the double-check is normally performed for high-alert meds here?

**User:** Two clinicians are supposed to independently verify dose and calculation before administration. In this case, the second clinician caught it, so the double-check "worked" that time — but the near-miss got as far as it did.

**Assistant:** So the barrier caught it this time, but I want to know how close it got and why the first clinician's calculation was wrong in the first place — that's a Method or Measurement branch. What's the workflow for calculating the dose before the double-check?

**User:** The prescribing system shows dose per weight, but on our unit clinicians often have to manually recalculate for a concentration change on the floor, using a paper conversion chart taped near the med room. Some clinicians told me they don't fully trust the chart's formatting and redo it in their head.

**Assistant:** That's a real Method/Measurement factor, not "someone wasn't careful." Let's put it on the fishbone.

## Fishbone

| Category | Candidate causes | Drilled? |
|---|---|---|
| People/Roles | Multiple different clinicians involved — not one individual's pattern | Rules out a single-person training issue |
| Machine | Prescribing system doesn't auto-recalculate for concentration changes on the floor | Yes — drilled below |
| Method | Manual recalculation off a paper conversion chart near the med room | Yes — drilled below |
| Material | `[Unknown]` — no medication supply issue reported | Not drilled |
| Measurement | Some clinicians report not trusting the chart's formatting, redoing math mentally | Related to Method branch |
| Environment/Policy | Double-check performed at bedside, sometimes under time pressure `[NEEDS GEMBA]` | Not drilled — insufficient detail |

**5 Whys on the Method/Machine branch:**

```
Problem: Clinicians manually recalculate high-alert medication doses off a paper chart when floor concentration differs from the prescribing system's assumption.

Why 1: The prescribing system doesn't account for the concentration actually stocked on this unit.
Why 2: The unit uses a different concentration than the system default, requiring a manual conversion step.
Why 3: A permanent system fix (updating the default concentration or building in an alert) hasn't been made.
Why 4: This has been treated as a workaround rather than escalated as a system gap [ASSUMED — verify: confirm whether pharmacy or IT has been asked to fix this].
Why 5: There's no standing process for clinicians to report a workaround like this as a system defect rather than "just how we do it here" — root cause.
```

**Root cause candidate:** No standing process exists for escalating a manual-workaround-around-a-system-gap as a defect to fix, so the concentration mismatch has persisted as normal practice instead of being corrected at the source.

**Barrier analysis:**

| Barrier | Designed to prevent | Why it (nearly) failed |
|---|---|---|
| Independent double-check by second clinician | Catching a dosing error before administration | Worked this time, but relies on the second clinician independently redoing the same manual, error-prone calculation — a shared design flaw, not independent verification |

**Assistant:** Verification question: if we fix the underlying concentration mismatch (or give clinicians a system-calculated dose instead of a manual chart), does this near-miss pattern go away and stay gone?

**User:** I believe so, yes — if the system did the math, there'd be nothing to manually recalculate.

---

## Root Cause Analysis: High-Alert Medication Dosing Near-Misses, Med-Surg Unit

**1. Problem statement:** Three high-alert medication dosing near-misses on the med-surg unit in approximately 4 months [user estimate], each caught by the independent double-check before administration; no harm occurred in any event.

**2. IS/IS-NOT table** — see above.

**3. Method:** Fishbone (multiple contributing factors across repeated events), drilled with 5 Why on the Method/Machine branch, followed by barrier analysis on the double-check.

**4. Verified root cause** `[CANDIDATE — needs gemba verification]`: No standing process exists to escalate the manual concentration-conversion workaround as a system defect; clinicians manually recalculate high-alert doses off a paper chart because the prescribing system's default concentration doesn't match what's stocked on the unit.

**5. Provisional corrective action:** Have pharmacy or IT correct the prescribing system's default concentration for this unit (or add a hard alert requiring pharmacist verification when a concentration mismatch is detected), removing the need for bedside manual recalculation. Scope is limited to this concentration mismatch — not a general redesign of the double-check process.

**6. What still needs gemba**
- `[NEEDS GEMBA]` Confirm whether the night-shift impression is a real pattern or recall bias — pull the incident log by shift.
- `[ASSUMED — verify]` Whether this workaround has ever been formally escalated to pharmacy or IT.
- `[NEEDS GEMBA]` Observe the actual bedside double-check to see whether time pressure independently contributes.

---

**What this skill did:**
- Ran a fishbone across three near-miss events on a med-surg unit, then drilled the Method/Machine branch with 5 Why to a systemic cause.
- Rejected "clinician wasn't careful" implicitly by tracing to the manual-recalculation workaround, and ran barrier analysis on the double-check that caught it.
- Verified the candidate cause against the user's own account before closing, and flagged it as still needing gemba confirmation.

**What still needs a human:**
- Confirm whether the night-shift pattern is real by pulling the incident log by shift — the whole analysis was scoped assuming that impression matters, and it's unconfirmed.
- Confirm with pharmacy or IT whether the concentration mismatch has ever been formally reported.
- Decide who owns getting the system default corrected — this needs authority outside the unit.

**Suggested next step:** Have the charge nurse pull the incident log for all three events by shift and unit before the safety committee meets, to confirm or rule out the night-shift pattern.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
