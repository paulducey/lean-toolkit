Shows flow and engagement observations in a shipping dock walk, with the assistant refusing to hand back a punch list alone and running the full six-step debrief instead.

**User:** Just got back from walking the shipping dock. Want to just log what I saw and get a list of what to fix.

**Assistant:** Before you paste your notes — leave out names of employees; roles and initials are fine. And once you give me the notes, I'll run the full debrief rather than just handing back a list of fixes — a walk that only produces corrections is an inspection, not a gemba walk. Go ahead.

**Assistant:** Also — what's the reason for the walk this time? Just routine, or is something specific driving it?

**User:** Routine, it's my monthly walk of the dock.

**Assistant:** Good to know — a routine walk without a specific trigger means I won't assume any of what you find is tied to a known problem; it's a general-condition check across all five lenses, in dock process order. Go ahead with the notes.

**User:** Fine. Dock has 4 bays. Bay 1 and 2 had trucks loading, Bay 3 empty, Bay 4 had a truck backed in but nobody loading it — driver was in the break room. Pallets staged for Bay 4 were sitting about 15 feet from the bay door, not in a marked lane. Asked the lead (RM) why — he said "we stage wherever there's room, no assigned lanes." Saw two people manually re-counting boxes against the packing slip at Bay 2 — RM said "we don't trust the WMS count so we always recheck." No one at the dock could tell me the day's on-time-ship percentage — RM said that report comes from the office at end of day.

**Assistant:** Here's the debrief — not a punch list.

## Gemba Walk Debrief — Shipping Dock

**1. What did you observe? (facts only)**
- Bays 1 and 2 loading in progress; Bay 3 empty; Bay 4 had a truck present with no loading activity and the driver in the break room [observed]
- Pallets staged for Bay 4 were approximately 15 feet from the bay door, in an unmarked area [observed]
- Dock lead (RM) stated there are no assigned staging lanes [observed]
- Two dock workers manually recounted box quantities against the packing slip at Bay 2; lead stated this recheck happens routinely because the warehouse management system (WMS) count is not trusted [observed]
- No one at the dock could state the day's on-time-ship percentage; lead stated this comes from an end-of-day office report [observed]

**2. What surprised you?**
The manual recount at Bay 2 — that's a double-check on a system that's supposed to already be accurate, and it's treated as routine rather than as a flag that something's wrong with the WMS count. [ASSUMED — verify: confirm with the walker whether this was in fact unexpected, or already known]

**3. What did you learn that you didn't know before the walk?**
- Staging has no designated lanes — pallets go wherever there's open floor. That's a Set-in-Order gap that would show up on a `5s-audit` of this dock. [ASSUMED — verify]
- On-time-ship is a lag metric on this dock — nobody at the point of work can see it in time to act on it during the shift.

**4. What questions does this raise that need more data or investigation?**
- How long has the WMS recount practice been standard, and has anyone traced why the system count isn't trusted? [NEEDS GEMBA: ask IT/WMS owner and the dock lead separately]
- Why was Bay 4's truck idle — was this a one-off (driver break, no coverage gap) or a recurring pattern? [NEEDS GEMBA: observe Bay 4 across a few more shifts]
- What is the actual on-time-ship rate today, and how far back does "end of day" reporting push the visibility gap? [NEEDS GEMBA]

**5. What, if anything, requires immediate action? (Safety first)**
- Nothing observed on this walk met the bar for a live safety hazard requiring action during the walk. [observed]

**6. What goes to the T1/T2 board as an open item?**
- Unmarked staging lanes at the dock — route to T1 as a flow/organization item; consider a `5s-audit` of the dock before assigning fixes. Owner: dock lead (RM). Due: [NEEDS GEMBA: set with RM].
- WMS recount practice — route to T2; this crosses into a system trust issue that a shift lead can't resolve alone. Owner: [NEEDS GEMBA: identify WMS system owner].
- On-time-ship visibility — recommend to `daily-management`: this is a lag metric sitting where a lead metric should be; the dock needs an hourly or per-truck indicator instead of an end-of-day number.

---

**User:** Okay but seriously — can I just get the punch list too?

**Assistant:** The three open items above are the action list — each has an owner placeholder and a next step. What I won't do is hand you those three lines without the "what did you learn" and "what surprised you" sections above them; that's what keeps this a gemba walk instead of an inspection report the dock starts performing for.

**User:** Fair. What should I actually say to the dock lead when I follow up — I don't want it to sound like I'm about to write him up.

**Assistant:** Lead with what you learned, not with the list. Something like: "I noticed the recount at Bay 2 — has that always been part of the process, or did something change with the WMS count that made people stop trusting it?" That's an open question, not an accusation, and it might surface something you don't know yet — maybe the WMS was miscounting for a specific product a few months back and nobody ever revisited the recount habit once the root cause was fixed. Save the staging-lane and metric-visibility items for later in the conversation, framed as "here's what I'm thinking about routing to the board" rather than "here's what you're doing wrong."

**User:** And if he gets defensive about the recount thing?

**Assistant:** That's a sign to slow down, not push harder. Thank him for whatever he tells you, even if it's incomplete, and come back to it another day if needed. The interrogation trap — a string of rapid questions, especially aimed at one person — is exactly what turns a walk into an audit in the moment, even after the fact during follow-up.

---

**What this skill did:**
- Ran the full six-step debrief on shipping dock notes rather than returning a bare list of corrections, per the rule against handing back a punch list alone.
- Surfaced three open items — unmarked staging lanes, a WMS recount practice nobody has questioned, and an end-of-day-only ship metric — and one flagged surprise (the recount) for the walker to confirm.
- No live safety hazard was present on this walk, so no on-the-spot action was needed.

**What still needs a human:**
- Confirm whether the WMS recount practice was actually surprising to the walker, or already a known workaround (debrief item 2 is an assumption).
- Investigate whether the Bay 4 idle-truck situation was one-off or recurring — needs more than one walk to know.
- Assign real owners and due dates to the three open items — none are set yet.
- How the follow-up conversation with the dock lead about the recount practice actually goes will shape whether this becomes a T2 escalation about the WMS or stays a local process question.

**Suggested next step:** Take the on-time-ship visibility gap to whoever owns the dock's daily management design and ask whether an hourly or per-truck indicator could replace the end-of-day report.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
