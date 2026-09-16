# Example: 5 Whys drilling a recurring weld defect on second shift to a fixable systemic cause

**User:** We keep getting weld porosity on the frame welds on second shift. It's been going on for weeks and we fixed it once already but it came back.

**Assistant:** Before you share any data or notes — leave out names of employees and anything your company treats as confidential; roles, shifts, and initials are fine. Tell me what you've seen — what's happening, where, and how often — and I'll help you find the real cause, not just the symptom.

**User:** Frame weld porosity on the underbody joint, second shift only, roughly 4-5 out of every 50 frames on that shift, going back about 4 weeks. First shift is basically clean.

**Assistant:** That contrast — second shift affected, first shift clean — is exactly where the cause is likely hiding. Let's scope it with an IS/IS-NOT table first, then I'll pick a method. Since this is one clear defect with a plausible single chain (shift-specific), I'll use 5 Whys rather than fishbone — say if that changes once we scope it.

Two questions to fill the table: does the porosity show up on a particular frame model or all of them, and does it cluster at the start of second shift or throughout?

**User:** All models, and it's actually worse in the first two hours of second shift than later.

**Assistant:** That's useful — points toward something that happens at the second-shift transition, not the welding skill itself.

## IS / IS-NOT

| Dimension | IS | IS NOT |
|---|---|---|
| What | Porosity on underbody frame weld joint | Other joints on the same frame — clean |
| Where | Underbody joint, all frame models | Other weld stations on the line |
| When | Second shift, worse in first 2 hours | First shift — clean; second shift after hour 2 — lower rate |
| Who | Second-shift weld crew | First-shift weld crew — same equipment, no issue |
| How much | 4–5 of 50 frames (8–10%) [user estimate] | First shift: near 0% [user estimate] |

**Method: 5 Whys** — one clear defect, one plausible chain (shift-transition related), fishbone not needed unless this doesn't resolve.

**Assistant:** Let's drill it. Why is porosity worse in the first two hours of second shift?

**User:** The shift supervisor's theory is the second-shift welders are just less careful early in the shift.

**Assistant:** I can't accept "less careful" as a root cause — it doesn't explain why porosity clusters in the first two hours specifically, and it isn't something the team can fix directly. Ask instead: what's physically different about the weld process in those first two hours versus later in the shift, or versus first shift at any point?

**User:** ...Actually, gas shielding. First shift comes in and the argon has been flowing and warming up for a while. Second shift starts cold right at shift change because the gas gets shut off between shifts to save cost.

**Assistant:** That's a real physical mechanism, not a person failing. Let's keep drilling — why does shutting off the gas between shifts cause porosity in the first two hours specifically?

**User:** I think the shielding gas needs a warm-up/purge period to fully displace air in the lines, and if welders start immediately at shift change, the first frames get incomplete shielding.

**Assistant:** Good — that's specific and physical. One more Why: why is welding allowed to start before the purge period is confirmed complete?

**User:** There's no timer or indicator — welders just start when the light comes on that gas is flowing, not when it's actually purged.

**Assistant:** That's a fixable systemic cause. Verification question: if we fix the missing purge-confirmation step, does the porosity go away and stay gone — including on first shift where the gas has already been running?

**User:** Yes, I think so — first shift never sees it because the gas has been flowing continuously since the shift before.

---

## Root Cause Analysis: Second-Shift Frame Weld Porosity

**1. Problem statement**
Underbody frame weld porosity occurs at a rate of approximately 8–10% (4–5 of 50 frames) [user estimate] on second shift only, concentrated in the first two hours after shift start, over the last 4 weeks [user estimate]. First shift shows near-zero occurrence [user estimate].

**2. IS/IS-NOT table** — see above, fully populated across four dimensions.

**3. Method: 5 Whys** (chosen because this is one clear defect with a plausible single causal chain)

```
Problem: Frame weld porosity, second shift, first two hours of shift, ~8-10% rate.

Why 1: Porosity is worse in the first two hours of second shift than later or on first shift.
Why 2: Shielding gas is shut off between shifts to save cost, so second shift starts with gas that has just resumed flowing.
Why 3: The gas lines need a purge period to fully displace air before shielding is complete.
Why 4: Welders start as soon as the "gas flowing" indicator light is on, not when purge is confirmed complete [ASSUMED — verify exact purge duration at gemba].
Why 5: There is no purge-confirmation step or timer built into the shift-start procedure — root cause.

Root cause candidate: The shift-start procedure has no step confirming shielding gas purge is complete before welding begins, so the first frames of second shift weld with incomplete shielding.
Verification question: If we fix the missing purge-confirmation step, does the porosity go away and stay gone? User's answer: yes — consistent with first shift never seeing the defect because its gas has been flowing continuously.
```

**4. Verified root cause** `[VERIFIED]` — No purge-confirmation step exists in the second-shift weld start-up procedure; welding begins on the "gas flowing" indicator rather than a confirmed purge, causing incomplete shielding on the first frames welded each shift.

**5. Provisional corrective action**
Add a timed purge-confirmation step (or indicator) to the second-shift weld station start-up procedure — welding may not begin until the confirmed purge duration has elapsed. Scope is limited to this step; it does not address gas cost policy or general shift-start training.

**6. What still needs gemba**
- `[NEEDS GEMBA]` Confirm the actual required purge duration for this gas line length and diameter — not assumed.
- `[ASSUMED — verify]` That welders are in fact starting before purge completes, rather than some other shift-start variable — confirm by timing the indicator light versus actual purge completion.

---

**What this skill did:**
- Ran 5 Whys on second-shift frame weld porosity, using the IS/IS-NOT contrast (second shift only, worse early) to steer the drill.
- Rejected "welders are less careful" as a root cause and drilled to a fixable systemic cause: no purge-confirmation step at shift start.
- Verified the cause against first shift's clean record before closing.

**What still needs a human:**
- Confirm the actual required purge duration for this specific gas line at gemba — the corrective action's timing depends on this.
- Verify at the station that welders are in fact starting on the indicator light rather than a confirmed purge, before rolling out the new step.
- Decide whether the gas shut-off-between-shifts cost policy should also be revisited, separate from this fix.

**Suggested next step:** Have the second-shift lead, R., time the gas line from cold start to full purge at the underbody weld station and confirm the indicator light comes on before or after that point.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
