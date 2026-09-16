Shows: an I-MR chart built from a small first batch (limits marked provisional), then rebuilt once more data arrives, a Rule 2 signal traced to a material lot change, and Cp/Cpk showing a centering problem after the out-of-control points are set aside.

**User:** Our fill weights have felt off this week. Can you build a control chart? I've got 8 readings from this morning so far.

**Assistant:** Sure — share the measurement values and sequence (order matters more than the values alone), and the spec limits if you have them, and I'll build the chart and tell you what it's showing. One note before you paste anything: leave out proprietary product names or customer-specific tolerances if those are sensitive — the raw numbers and a ± spec are all I need.

**User:** Fill weight in grams, in order: 494.2, 496.1, 493.5, 497.0, 495.3, 494.8, 496.5, 495.0

**Assistant:** With continuous measurements and one reading per time point (no subgroups), this is an Individuals and Moving Range (I-MR) chart.

Mean X̄ = (494.2+496.1+493.5+497.0+495.3+494.8+496.5+495.0)/8 = 3962.4/8 = **495.30** [observed]

Moving ranges (|difference from prior point|): 1.9, 2.6, 3.5, 1.7, 0.5, 1.7, 1.5
MR̄ = (1.9+2.6+3.5+1.7+0.5+1.7+1.5)/7 = 13.4/7 = **1.91** [observed]

UCL_X = 495.30 + 2.66×1.91 = 495.30 + 5.08 = **500.38**
LCL_X = 495.30 − 5.08 = **490.22**

I can compute these, but with only 8 points I'm not going to call them settled — control limits from fewer than 20–25 points are provisional. Treat them as a rough read, not a chart to act on yet. None of these 8 points fall outside 490.22–500.38, so nothing looks unusual yet, but that's a small sample. Keep logging and send me the rest of the shift when you have it.

**User:** Here's the rest of the shift, values 9 through 24: 493.2, 497.3, 494.6, 496.2, 495.1, 493.8, 496.4, 499.5, 500.2, 501.0, 499.8, 500.5, 501.5, 500.9, 499.6, 501.3. Also — we switched to a new resin lot around reading 16, in case that matters. Spec on the container is 491–505 g [from system: packaging spec sheet], target 498 g.

**Assistant:** Good, that changes the picture — 24 points is enough to call these limits real rather than provisional. Full run, in order:

494.2, 496.1, 493.5, 497.0, 495.3, 494.8, 496.5, 495.0, 493.2, 497.3, 494.6, 496.2, 495.1, 493.8, 496.4, 499.5, 500.2, 501.0, 499.8, 500.5, 501.5, 500.9, 499.6, 501.3 [observed]

X̄ (all 24) = 11933.3/24 = **497.22** [observed]
MR̄ (all 24, 23 ranges) = 39.7/23 = **1.73** [observed]

UCL_X = 497.22 + 2.66×1.73 = 497.22 + 4.59 = **501.81**
LCL_X = 497.22 − 4.59 = **492.63**
UCL_MR = 3.267×1.73 = **5.65**; LCL_MR = 0

**Western Electric rules:**
- Rule 1 (beyond 3σ): none. All 24 values fall between 493.2 and 501.5, inside 492.63–501.81.
- Rule 2 (9 consecutive on one side): **triggered.** Points 16–24 (499.5, 500.2, 501.0, 499.8, 500.5, 501.5, 500.9, 499.6, 501.3) are all above the centerline of 497.22 — nine in a row.
- Rule 3 (6 consecutive trending): none.
- Rule 4 (14 alternating): none.
- Moving ranges: largest is 4.1 (point 10), well under UCL_MR of 5.65 — no signal in the range chart.

**Stability conclusion: this process is out of control.** The sustained run above the centerline starting at point 16 lines up with the resin lot change you mentioned — that's a special cause, not noise, and it should be investigated rather than averaged into the baseline.

**Whether the lot change is actually the cause, versus something else that happened around the same time, is [NEEDS GEMBA]** — worth confirming with whoever ran the line that shift.

**Capability:** capability indices are only meaningful for a stable process, so I'm calculating them from points 1–15 only (before the shift), not the full 24.

X̄(1–15) = 7429.0/15 = **495.27**
MR̄(1–15) = 28.6/14 = **2.04**
σ = MR̄/1.128 = 2.04/1.128 = **1.81**

Cp = (USL−LSL)/(6σ) = (505−491)/(6×1.81) = 14/10.87 = **1.29** (capable spread)
Cpk = min[(505−495.27)/(3×1.81), (495.27−491)/(3×1.81)] = min[9.73/5.43, 4.27/5.43] = min[1.79, 0.79] = **0.79**

Cp (1.29) is well above Cpk (0.79) — the process has enough spread to fit the 491–505 window, but it's running low relative to the 498 g target, and Cpk under 1.00 means it's **not capable** as centered. The fix here is centering — nudging the fill target up toward 498 g — not chasing variation.

| Metric | Value | Interpretation |
|---|---|---|
| Cp | 1.29 | Spread fits the spec window |
| Cpk | 0.79 | Not capable — running off-center, low side |

**What still needs verification:** whether shifting the fill target upward by roughly 2.7 g is something you're authorized to do on this line without a change request — **[NEEDS GEMBA]**.

**User:** Should we throw out points 16–24 completely, or keep tracking them?

**Assistant:** Keep tracking them — don't throw them away. Excluding points 16–24 from the capability calculation was the right move, because they represent a special cause that hadn't stabilized yet, and folding them into a "normal" baseline would understate how far off the new lot has pushed things. But once you confirm the lot change is really the cause, the next step is to collect a fresh run of points under the new lot on its own, recompute a new baseline from those, and see whether the new lot settles into its own stable center — which might not be 495.27, and might need its own centering correction if it's different again.

**User:** That makes sense. One more thing — is it fair to say the process got worse after the lot change, or just different?

**Assistant:** Based on what's here, different, not worse in variation — the moving ranges in the second half of the data aren't larger than the first half, so the spread hasn't degraded. What changed is the center: the process shifted up by roughly 2 grams. Whether "different" is actually "worse" depends on which side of the 498 g target it's now running relative to spec, and that's the centering question the Cp/Cpk numbers above already answer — right now it's less far off-target than before the shift, but it's still not fixed by accident, and it shouldn't be left as an unexplained shift either.

---

**What this skill did:**
- Built an I-MR chart on 24 fill-weight readings; the first 8 were flagged as provisional, and the full 24-point chart confirmed Rule 2 (points 16–24 all above centerline).
- Found the process is out of control, coinciding with the resin lot change you mentioned; capability run on the pre-shift points shows Cp 1.29 vs Cpk 0.79 — a centering problem, not a spread problem.
- The out-of-control points (16–24) were set aside for the capability calculation rather than folded into the baseline — worth a second look once the lot question is settled.

**What still needs a human:**
- Whether the resin lot change on shift is actually what moved the mean, versus some other change that happened at the same time — [NEEDS GEMBA].
- Whether nudging the fill target up ~2.7 g toward 498 g is authorized without a formal change request — [NEEDS GEMBA].
- Confirming the 491–505 g spec and 498 g target are still current before acting on the Cpk number.

**Suggested next step:** Take this chart to the line lead who was running the shift when the resin lot changed, and confirm whether the fill target was adjusted at the same time.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
