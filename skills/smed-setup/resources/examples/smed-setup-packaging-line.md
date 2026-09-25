Shows a 47-minute changeover on a packaging line reduced to a 19-minute target using filmed observation data, Phase 1 internal/external conversion, and adjustment elimination through pre-set tooling.

**User:** We filmed our packaging line changeover from box style A to box style B. Total time was 47 minutes. Can you help us reduce it?

**Assistant:** Tell me about the changeover — what machine, what you switch between, and how you know what's happening. Sounds like you've got filmed observation, which is the most reliable data source — elements timed to the second rather than estimated. Before you paste the element list — leave out any proprietary product names or formulations; machine type, process step, and time data are fine.

**User:** Machine is the case packer, line 4. Switching from Box Style A to Box Style B. From the film:
1. Machine stopped, last A case cleared — 0:45
2. Operator walks to tool cage to get B-style tooling — 4:10
3. Old A tooling unbolted and removed — 6:30
4. New B tooling installed and bolted — 8:20
5. Trial run, adjust guide rails by feel — 12:40
6. Second trial run, check case squareness, re-adjust — 9:15
7. Paperwork — changeover log and quality sign-off — 3:10
8. Restart and confirm first good case — 2:10

Total: 47:00

**Assistant:** Here's the element list with internal/external classification challenged for every step, not just the obvious ones.

## Element Classification — Case Packer, Line 4 (A → B changeover)

Machine/Line: Case packer, Line 4
Changeover type: Box Style A → Box Style B
Current total changeover time: 47:00 [observed, filmed]
Data source: filmed observation

| # | Element Description | Current Time | Classification | Phase 2 Action | Target Time |
|---|---|---|---|---|---|
| 1 | Last A case cleared, machine stopped | 0:45 | Internal — machine must be stopped for the operator to reach into the case path safely | none — genuinely internal | 0:45 |
| 2 | Walk to tool cage for B tooling | 4:10 | External — this can happen before shutdown with no physical constraint requiring the machine to be stopped | Convert: stage B tooling at the machine before the last A case runs | 0:00 |
| 3 | Unbolt and remove A tooling | 6:30 | Internal — machine must be stopped to safely remove tooling from the case path | Streamline: quarter-turn fasteners in place of bolts | 2:30 [EST] |
| 4 | Install and bolt B tooling | 8:20 | Internal — same physical constraint | Streamline: quarter-turn fasteners, pre-set to correct position | 3:00 [EST] |
| 5 | Trial run, adjust guide rails by feel | 12:40 | Internal, but the *adjustment* itself is the target, not the running | Eliminate: pre-set guide rails to a documented, gauged position offline before changeover begins | 1:00 [EST] |
| 6 | Second trial run, re-adjust for squareness | 9:15 | Same as above — a second adjustment cycle exists because the first setting wasn't trusted | Eliminate: with pre-set rails at a known gauge, no second trial should be needed | 0:00 [EST] |
| 7 | Paperwork — changeover log, QA sign-off | 3:10 | External — no physical reason this can't be completed after restart while the machine is running | Convert: complete paperwork after restart, during the next run | 0:00 |
| 8 | Restart, confirm first good case | 2:10 | Internal — the machine must be running to confirm a good case, but confirmation itself doesn't require the changeover window to still be open | none — genuinely internal, but happens after Phase 1 elements are already converted | 2:10 |

**Classification note on elements 5 and 6:** Neither survives the internal-only rule as currently performed — "adjust by feel" is not a physical or safety constraint, it's a symptom of tooling that isn't pre-set to a known position. This is flagged as the adjustment-elimination priority.

## Phase 1 Savings (external conversion only)

- Element 2 (tool staging): 4:10 saved
- Element 7 (paperwork): 3:10 saved
- **Phase 1 total: 7:20 saved** — before any tooling or fixture change

## Phase 2/3 Streamlining (after Phase 1)

- Elements 3 + 4 (fastener change to quarter-turn): estimated 6:30 + 8:20 (14:50) reduced to 2:30 + 3:00 (5:30) → 9:20 saved [EST — verify with a timed trial of the new fasteners]
- Elements 5 + 6 (pre-set, gauged guide rails eliminating the double trial run): estimated 12:40 + 9:15 (21:55) reduced to 1:00 + 0:00 (1:00) → 20:55 saved [EST — verify with a timed trial]

## Capacity Math

```
Current changeover time:          47:00
Target changeover time:           19:00 [0:45 + 2:30 + 3:00 + 1:00 + 0:00 + 2:10, rounded]
Time saved per changeover:        28:00
Changeovers per shift/week:       [NEEDS GEMBA: how many A↔B changeovers run per week on Line 4]
Production time recovered:        28:00 × changeovers/week [NEEDS GEMBA — cannot total until frequency is known]
```

The per-event savings (28 minutes) is solid — it's built from converted and estimated elements above, not a guessed percentage. The weekly total depends on changeover frequency, which wasn't given.

---

**User:** We run A→B or B→A roughly 6 times a week, does that help?

**Assistant:** Yes — with 6 changeovers per week, 28 minutes saved per event comes to 168 minutes (2 hours 48 minutes) of production time recovered per week, once the fastener and guide-rail improvements are validated. [user estimate: 6 changeovers/week] I'd still hold that number as directional until the Phase 2/3 elements are trialed — it's built on estimated element times, not measured ones, for elements 3 through 6.

**User:** If we're only converting Phase 1 for now and haven't done the fastener/rail work yet, what's the number today?

**Assistant:** With only Phase 1 converted (staging tooling early, moving paperwork after restart), the changeover drops from 47:00 to 39:40 — a 7:20 saving per event, or 44 minutes per week at 6 changeovers. That's the number to use if you're reporting progress before the fastener and guide-rail changes are in place; the fuller 28-minute-per-event figure only applies once those are validated.

---

**What this skill did:**
- Built a full element list from filmed changeover data (47:00 total), classified every element against the internal-only rule rather than accepting the current internal/external split.
- Phase 1 conversion (staging tooling early, moving paperwork after restart) saves 7:20 with no equipment change; pre-set, gauged guide rails and quarter-turn fasteners are projected to save a further 20:55 combined, bringing the target to roughly 19 minutes.
- Flagged that the double trial run (elements 5–6) exists because tooling isn't pre-set to a known position — the adjustment-elimination priority for this line.

**What still needs a human:** The Phase 2/3 estimates (fastener and guide-rail savings) are projections, not measured times — the first thing that would materially change the savings number if it turns out wrong is whether pre-set, gauged guide rails actually eliminate the second trial run in practice.

**Also unverified:** the weekly changeover frequency for Line 4's A↔B switch — the capacity math above stops at per-event savings because that figure wasn't given.

**Suggested next step:** Run one timed trial of the pre-set guide rails and quarter-turn fasteners on Line 4 and compare the actual result against the 19-minute target before rolling the change out to other lines.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
