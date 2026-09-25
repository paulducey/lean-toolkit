# Example: coaching an A3 on excessive changeover time, refusing to skip from current condition to countermeasures

**User:** I want to write an A3 on our press changeover time — we're missing takt every time we changeover. My boss wants me to just put in "add a second setup tech" as the fix and move on.

**Assistant:** Before you paste any data — leave out names of employees and anything confidential; roles and initials are fine. Tell me the problem and who this A3 is for, and I'll coach it left to right.

Also — "add a second setup tech" is a countermeasure, not a starting point. If we put that in Section 5 before we know the root cause, we might be solving the wrong problem. Let's build the left side first: what's the changeover metric, by how much is it off, and where does it show up?

**User:** It's for the plant manager. Press 4 changeover averages 74 minutes against a target of 40 minutes, based on the last 20 changeovers logged by the setup crew.

**Assistant:** That's a solid baseline. Where in the changeover does the time actually go — has anyone timed the individual steps, or is 74 minutes just a start-to-finish total?

**User:** Just start-to-finish so far. Nobody's broken down the steps.

**Assistant:** Then Current Condition needs that breakdown before we can claim we understand the problem — I'll tag it `[NEEDS GEMBA]`. What's the target date for hitting 40 minutes?

**User:** End of next month.

**Assistant:** Good, that's Section 3 done. Now — before your boss's "add a second setup tech" goes anywhere in this document: what root cause does that address? If most of the 74 minutes is looking for tooling or waiting on a crane, a second tech might just mean two people looking for tooling.

**User:** Fair point. We honestly don't know yet why it's 74 minutes.

**Assistant:** Then Section 4 isn't ready either, and I won't put "add a second setup tech" in Section 5 without a cause it addresses. I'll draft the left side solid, mark Section 4 and beyond as needing a timed observation, and note the proposed countermeasure as unverified so it doesn't get treated as decided.

**User:** My boss is going to push back — he wants something in writing that says we're adding headcount to setup.

**Assistant:** That's worth naming directly rather than working around: if the actual need turns out to be tooling organization rather than more hands, adding a person locks in a headcount cost that doesn't fix the problem and is hard to walk back later. I'll draft the A3 honestly — the proposed countermeasure appears as a flagged, unverified idea in the record, not as a decision, so your boss can see exactly what it is and isn't yet.

---

## A3: Press 4 Changeover Time

**1. Background**
Press 4 changeover averages 74 minutes [from system: setup crew changeover log, last 20 changeovers] against a target of 40 minutes. Changeover time this long is causing missed takt on the shifts following a changeover `[NEEDS GEMBA: confirm how many takt cycles are actually lost per changeover]`.

**2. Current Condition**
Only a start-to-finish total exists; no step-by-step timing has been done. `[NEEDS GEMBA: time each changeover step — die removal, tooling retrieval, alignment, first-piece approval — to see where the 74 minutes actually goes]`. Until this exists, the current condition is known only at the whole-changeover level, not at the step level.

**3. Goal / Target Condition**
Reduce Press 4 changeover time from 74 minutes [from system: setup crew changeover log] to 40 minutes by end of next month.

**4. Root Cause Analysis**
Not yet determined. A step-level time study is required before a root cause can be named — without it, any stated cause would be a guess. `[NEEDS GEMBA: run the time study, then apply 5 Why to the largest single time block]`. Note: adding a second setup technician was proposed by leadership before any cause was identified. This is flagged, not adopted — it does not map to a verified root cause and may address the wrong step (e.g., two people searching for tooling instead of one does not reduce search time if the tooling isn't organized).

### Right side — not started

Sections 5–8 are not drafted. The left side is not solid: Section 2 lacks step-level data and Section 4 has no verified cause. Filling in "add a second setup tech" now would repeat the exact mistake this A3 process exists to catch.

---

**What this skill did:**
- Coached the left side of a changeover-time A3 using a real start-to-finish baseline (74 min vs. 40 min target).
- Refused to place the leadership-proposed countermeasure ("add a second setup tech") in Section 5 without a verified root cause, and flagged it explicitly rather than silently dropping it.
- Identified that a step-level time study is the missing piece blocking both Current Condition and Root Cause.

**What still needs a human:**
- Run a step-level time study on Press 4 changeover — this blocks Sections 2 and 4.
- After the time study, run 5 Why on the largest time block before considering any countermeasure, including the proposed second tech.
- Confirm with the plant manager how many takt cycles are actually lost per changeover, to size the business case precisely.

**Suggested next step:** Have the setup crew lead time the next three Press 4 changeovers step by step, using a stopwatch and the standard changeover step list, before this A3 goes further.

**On the headcount question:** if the time study does show waiting or searching accounts for most of the 74 minutes, the honest framing for leadership is that better tooling organization or a pre-staged kit frees capacity within the existing crew — a second person is one option among several, not the default answer, and which option to pursue (including whether to add headcount) is a decision for leadership once the cause is known, not something this A3 should presuppose.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
