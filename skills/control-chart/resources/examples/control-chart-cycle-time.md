Shows: an X-bar/R chart on cycle-time subgroups that trips Rule 4 (alternating pattern), traced to a two-shift difference, and a tampering warning after the operator had been nudging the machine off individual readings.

**User:** Just tell me what's going on — don't ask me a bunch of questions, I've got the data right here. Cycle time, subgroups of 3 parts, one subgroup per hour, 16 hours across two shifts (day then night, alternating). Leave out the part number, it's proprietary.

Subgroup values (seconds):
1: 77, 79, 78
2: 94, 96, 95
3: 76, 78, 77
4: 95, 97, 96
5: 78, 80, 79
6: 93, 95, 94
7: 77, 77, 79
8: 96, 94, 95
9: 79, 78, 77
10: 95, 96, 94
11: 78, 77, 79
12: 94, 96, 95
13: 77, 79, 78
14: 96, 95, 94
15: 78, 79, 77
16: 95, 94, 96

**Assistant:** Continuous measurement, subgroup size n=3 — this is an X-bar and R chart, factors A2=1.023, D3=0, D4=2.574, d2=1.693 for n=3.

Subgroup means and ranges [observed]:

| Subgroup | Mean | Range |
|---|---|---|
| 1 | 78.00 | 2 |
| 2 | 95.00 | 2 |
| 3 | 77.00 | 2 |
| 4 | 96.00 | 2 |
| 5 | 79.00 | 2 |
| 6 | 94.00 | 2 |
| 7 | 77.67 | 2 |
| 8 | 95.00 | 2 |
| 9 | 78.00 | 2 |
| 10 | 95.00 | 2 |
| 11 | 78.00 | 2 |
| 12 | 95.00 | 2 |
| 13 | 78.00 | 2 |
| 14 | 95.00 | 2 |
| 15 | 78.00 | 2 |
| 16 | 95.00 | 2 |

X̿ (grand mean) = 1383.67/16 = **86.48**
R̄ = 32/16 = **2.00**

UCL_X = 86.48 + 1.023×2.00 = 86.48 + 2.05 = **88.52**
LCL_X = 86.48 − 2.05 = **84.43**
UCL_R = 2.574×2.00 = **5.15**; LCL_R = 0

With only 16 subgroups, these limits are provisional — fewer than 20–25 points is the general threshold, so treat them as a strong first read, not final.

**Western Electric rules:**
- Rule 4 (14+ alternating): **triggered.** Every subgroup mean alternates — low (77–79.67) on the odd subgroups, high (94–96) on the even ones — for all 16 points, well past the 14-point threshold.
- Rule 1 (beyond 3σ): also technically triggered on nearly every point, since the swing between the two levels is large enough to clear both control limits in both directions. That's expected given how extreme this alternation is — it doesn't change the read, it confirms it.
- Rule 2 (9 consecutive on one side): not applicable — the pattern alternates, it doesn't run to one side.
- Rule 3 (6 consecutive trending): none — there's no drift, just a jump each subgroup.
- Range chart: all 16 ranges are exactly 2, well under the UCL_R of 5.15 — the variation *within* each subgroup is consistent and in control. The problem is entirely in the mean, not the spread.

**Stability conclusion: out of control.** A 14+ alternating pattern usually means two distinct process streams feeding one chart — two machines, two suppliers, or two shifts running differently. Given you said day/night alternates hour to hour here, that fits: this reads as two shifts running at two different cycle-time levels, not one process bouncing around randomly.

**No spec limits were given, so capability isn't calculated here** — that's fine, capability wasn't the question.

**User:** That tracks — the night operator has been nudging the machine's feed speed up a little every time a reading comes in high, trying to keep it near 85. Should he keep doing that?

**Assistant:** No — stop that. Adjusting the machine in response to individual readings is tampering, and here it's adding to a problem that isn't random noise in the first place. The two levels you're seeing (~78 sec days, ~95 sec nights) aren't the machine drifting point to point — they're two different settings or methods running consistently within each shift. Reacting to individual high readings by nudging feed speed treats a systematic difference as if it were common cause variation, which just adds a third source of variation on top of the two-shift gap.

The fix is to find out what's actually different between the two shifts — feed speed setting, material handling, operator method — and standardize it, not to keep adjusting mid-shift. **Exactly what's different between the two shift setups is [NEEDS GEMBA]** — worth watching both shifts run the same step back to back.

---

**What this skill did:**
- Built an X-bar/R chart on 16 subgroups of cycle-time data; range chart is in control, but the mean chart trips Rule 4 — a clean 16-point alternating pattern between two levels.
- Traced the alternation to the day/night shift split you described, and flagged the night operator's manual feed-speed nudging as tampering that's compounding the issue rather than fixing it.
- Limits are provisional given only 16 subgroups — worth confirming with more data once the shift difference is addressed.

**What still needs a human:**
- What's actually different between the day and night shift setups (feed speed, method, material) that produces two distinct cycle-time levels — [NEEDS GEMBA].
- Whether the night operator's manual adjustments should stop immediately or be phased out — that's a call for the line supervisor, not this chart.
- More subgroups once the shift difference is addressed, to confirm the limits with a full 20–25+ point baseline.

**Suggested next step:** Have the line supervisor watch one day-shift cycle and one night-shift cycle back to back on the same station and compare feed speed settings and method before the next production run.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
