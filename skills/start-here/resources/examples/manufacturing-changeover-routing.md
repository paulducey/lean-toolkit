# Example: routing a plant CI lead's changeover complaint to a3-coach

**User:** Hey, not sure what I need here — our changeovers are a mess and my plant manager wants something written up.

**Assistant:** This toolkit has eight working tools: a3-coach structures a problem onto one page for review; root-cause runs a 5-Whys or fishbone on something recurring; kaizen-charter plans a focused improvement event; standard-work and twi-jbs document how a job is done, or build the trainer's version of it; vsm-calc turns walk observations into value-stream numbers; oee-from-csv turns a downtime export into OEE; gemba-walk structures a walk. It's here so the paperwork gets out of the way and you can be at the gemba instead of at a keyboard.

What's in front of you right now?

**User:** Changeovers on our stamping line are running long and missing takt, and my plant manager wants it written up for the next review — something he can read in one page.

**Assistant:** Sounds like you need it structured on one page for a review — that's `a3-coach`. It'll coach you left to right: background, current condition, goal, root cause, then countermeasures — and it won't let you jump to a fix before the cause is nailed down. Before you paste any changeover data or notes there: leave out names of employees and anything confidential; roles and initials are fine.

**User:** Do I need to already know the root cause before I go to it, or can it help me find that too?

**Assistant:** It can help you find it — that's actually the point of the left side of an A3. You don't need the cause figured out yet, just what you already have: the changeover numbers, where it shows up, and what "good" would look like. If it turns out you need a deeper dig than what fits on one page, a3-coach will point you to `root-cause` for that piece and come back with what it finds.

That's a3-coach territory from here — go ahead and tell it what you just told me and it'll take it from there.

---

**What this skill did:**
- Oriented a plant CI lead to the toolkit in one short pass, asked the one routing question, and routed the changeover-review request to `a3-coach` based on the "one page for review" framing.
- Passed along the data-safety line before any paste, since the user is about to hand over changeover notes next.

**What still needs a human:**
- a3-coach will need the actual changeover metric, baseline, and target from the user — not yet captured here.
- Whether root cause has already been investigated for the changeover delay is unknown — a3-coach will ask.

**Suggested next step:** Open a3-coach with this summary — a stamping-line changeover problem needing a one-page write-up for the plant manager's review.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
