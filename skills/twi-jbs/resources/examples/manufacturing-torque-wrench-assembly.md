# Example: building a Job Breakdown Sheet for torquing a fastener assembly, from a trainer's walkthrough

**User:** I need to train a new operator on torquing the bracket assembly bolts. Can you help build a job breakdown sheet? Here's how I do it: I grab the bracket from the bin, seat it on the fixture, hand-start all four bolts, then torque them in a cross pattern to 35 ft-lbs using the calibrated wrench, then I stamp the traveler and set it on the outbound rack.

**Assistant:** Leave out names of employees and anything confidential in what you share; roles and initials are fine. That's a good walkthrough — I can already see five natural steps. One question: is there a step where new people commonly get it wrong, or where you do something not obvious just from watching?

**User:** Yeah — if you don't torque in the cross pattern, the bracket can rock and end up not seated flush, and you won't necessarily see it right away. Also the wrench has to be within its calibration date or the reading isn't trustworthy.

**Assistant:** Good, those are real Key Points. Anything where getting it wrong could hurt the person doing it?

**User:** Not really injury-risk, this one's low-risk physically.

**Assistant:** Then I won't invent a safety Key Point. Who needs to be trained on this, and by when, and who's the trainer this breakdown should capture?

**User:** New hire starting Monday, I'm training them myself — I'm the second-shift lead, R.

**Assistant:** That's enough — I'll draft the full sheet now.

---

## Job Breakdown Sheet: Bracket Assembly Bolt Torquing

*This is a trainer's aid, prepared before teaching the job — not a checklist handed to the learner.*

## Header
| Field | Value |
|---|---|
| Job | Torque bracket assembly fastener bolts (4-bolt pattern) |
| Trainer | Second-shift lead, R. |
| Prepared by | R. |
| Date | [NEEDS GEMBA: confirm exact prep date] |
| Where performed | Bracket assembly station |

## Breakdown table

| # | Important Steps (WHAT) | Key Points (HOW) | Reasons (WHY) |
|---|---|---|---|
| 1 | Retrieve bracket from bin and inspect | Check for visible damage or debris before seating | Damaged bracket won't seat flush regardless of torque technique |
| 2 | Seat bracket on fixture | Bracket sits fully flat with no gap at any corner | Confirms nothing is caught underneath before bolting |
| 3 | Hand-start all four bolts | All four started before any is tightened | Prevents cross-threading and lets the bracket self-align before torque |
| 4 | Torque bolts in cross (star) pattern to 35 ft-lbs [from system: torque spec] | Follow the cross sequence, not a round-the-clock sequence; use only a calibrated wrench, checked against the calibration due date on the tag | Cross pattern prevents the bracket from rocking and seating unevenly; an out-of-calibration wrench gives a torque reading that can't be trusted |
| 5 | Stamp traveler and place on outbound rack | Stamp only after all four bolts are confirmed torqued | Traveler stamp is the record that this unit passed the torque step — stamping early would falsely certify an unfinished unit |

## JI 4-step training plan

1. **Prepare the worker** — put the new hire at ease, state the job (torquing the bracket assembly), ask what they already know about torque wrenches, explain why this step matters to final assembly.
2. **Present the operation** — demonstrate each of the 5 steps in order, stressing Key Points 3 and 4 (hand-start all four first; cross pattern; calibration check) slowly and clearly.
3. **Try out performance** — have the new hire perform the job while stating the cross pattern and the calibration check out loud; correct any deviation immediately; repeat until consistent.
4. **Follow up** — designate R. as who to check with for the first week; check in at end of each shift for the first three shifts, then taper.

## Training timetable

| Who needs training | Trainer | Target date | Status |
|---|---|---|---|
| New hire (second shift) | R. | Monday [NEEDS GEMBA: confirm exact date] | Scheduled |

## Validation

| Check | Confirmed? |
|---|---|
| Trainee performed the job independently and correctly | `[NEEDS GEMBA: confirm after try-out]` |
| Trainee can state Key Points and Reasons in their own words | `[NEEDS GEMBA: confirm after try-out]` |
| Follow-up check completed | `[NEEDS GEMBA: confirm after first week]` |

---

**What this skill did:**
- Built a 5-step Job Breakdown Sheet for bracket bolt torquing directly from the trainer's own walkthrough, adding two real Key Points (cross pattern, wrench calibration) the trainer flagged.
- Did not invent a safety Key Point since the trainer said the job carries no real injury risk.
- Included the JI 4-step training plan and a timetable for the Monday new hire.

**What still needs a human:**
- Confirm the exact training date and prep date — both left as placeholders.
- Complete the try-out and follow-up checks in the Validation table once training actually happens.

**Suggested next step:** Have R. walk the new hire through steps 3 and 4 first on Monday, since that's where the rocking/mis-seating risk lives, before running the full sequence.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
