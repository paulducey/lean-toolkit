Shows: a wrong-item error in a hospital pharmacy med room, the assistant mirroring the user's own words ("med room," "cassette," "tech") throughout, a Level 1 elimination attempt, a Level 2 prevention design using keyed storage lanes, and the existing double-check labeled honestly as Level 5.

**User:** In our med room, techs sometimes put the wrong medication into a patient's cassette bin during restock. A few of our SKUs look alike and sit right next to each other on the shelf. Can you help mistake-proof this? I'll paste some notes on how it's done now.

**Assistant:** Happy to help. Before you paste those notes: leave out names of patients or staff, and anything the hospital treats as confidential — roles and initials are fine. And please don't include any protected health information — no patient identifiers, no chart numbers, no dates of birth tied to a name. Describing the process and the look-alike items is all I need.

**User:** Here's the setup: techs restock the cassette wall from stock bins on a shelf behind the med room counter. Two of our meds — let's call them Med A and Med B — come in nearly identical bottles and sit side by side on that shelf. Right now the only check is a second tech looking over the cassette wall before the cart goes out to the unit.

**Assistant:** This is a **wrong item** error — the tech is picking a similar-looking bottle and placing it into the wrong cassette bin, and the current control is a second person looking it over afterward, not anything that stops the wrong bottle from going in.

**Error mode:** wrong medication placed into a patient's cassette bin during restock
**Error type:** Wrong item — similar-looking items stored together, no differentiation at the point of picking
**Process step:** cassette wall restock, from shelf stock bins
**Current detection:** second-tech visual check of the cassette wall before the cart leaves the med room

Working the hierarchy from the top:

| Level | Feasibility | Proposed Solution | What Tech No Longer Needs to Do | Implementation Notes |
|-------|-------------|-------------------|--------------------------------------|---------------------|
| 1 — Elimination | Feasible if the budget's there | Move restocking to an automated packaging or carousel system that pre-picks the exact medication into each patient's bin, removing manual shelf-picking for look-alike items entirely | Nothing — the tech no longer hand-picks the item at all | Capital cost, likely a multi-month project — `[ASSUMED — verify]` budget and timeline; this is the strongest fix but the slowest |
| 2 — Prevention | Feasible now | Give Med A and Med B physically separated storage lanes with different bin shapes or sizes (keying), so Med B physically doesn't fit into Med A's shelf slot, plus a barcode scan-to-bin match that locks the drawer until the scanned medication matches the assigned patient bin | No longer needs to visually tell two similar bottles apart — the slot and the scan both block the wrong one | Moderate cost: new bin hardware plus barcode logic if scanners already exist in the med room — `[NEEDS GEMBA]` to confirm scanner infrastructure is already there |
| 3 — Detection | Feasible as a stronger interim step than what's in place now | Barcode scan verification at the moment the tech places the medication into the cassette bin — system alerts immediately if the scanned med doesn't match the bin assignment | Doesn't have to catch the mismatch by eye — the scan catches it before the bin closes | Lower cost than full keyed lanes if scan infrastructure exists; still requires the tech to scan every time, so it's weaker than physical keying |
| 4 — Mitigation | Already partly in place, but weak | The second-tech check before the cart leaves catches some errors after the fact, but it's downstream of the actual placement and relies on the second tech noticing the same look-alike difference the first tech missed | Doesn't reduce anything the first tech has to do — only adds a second look | Zero additional cost, already running, but doesn't address the root cause |
| 5 — Procedure | Current state — label it honestly | The existing second-tech visual double-check is a manual verification step, not mistake-proofing | Nothing removed — both techs still have to remember to look carefully | This is what's running today; it depends entirely on two people's attention rather than physically preventing the wrong pick |

**Why the second-tech check is Level 5, not a real fix:** apply the test — if the second tech is distracted, tired, or rushed at the end of a long shift, does the double-check still catch a Med A/Med B mix-up? No — it's the same look-alike judgment call the first tech already got wrong, just made by a second person under the same time pressure. That's a Procedure-level control, and it should be labeled that way rather than called mistake-proofing. Stacking a third manual check on top wouldn't fix that — it would just add a third person's attention to depend on.

**Recommended path:** pursue Level 2 first — keyed storage lanes plus barcode scan-to-bin — since it's feasible now and physically blocks the wrong bottle rather than relying on anyone noticing. Keep the second-tech check running in parallel until the keyed lanes and scan verification are confirmed working, then it becomes a redundant backstop rather than the primary control.

**User:** We only have a few of these look-alike pairs on the shelf — is it worth keying every bin, or just the ones that look alike?

**Assistant:** Just the ones that look alike, at least to start. Keying every bin on the wall for a risk that's concentrated in a couple of pairs adds cost and shelf-reconfiguration work without adding protection where it matters — the wrong-item risk here comes specifically from Med A and Med B sitting close together and looking similar, not from the whole cassette wall. If there's a second pair you're aware of with the same look-alike problem, key that pair too; otherwise I'd pilot the keyed lanes on this one pair, confirm it holds up over a few weeks of restocking, and then decide whether to extend it based on what the pilot shows rather than keying the whole wall up front.

**User:** That's easier to sell to the pharmacy director. What would you tell them the second-tech check is actually catching right now, if not this?

**Assistant:** Worth being honest with the director about this too: the second-tech check is still useful for other things — quantity errors, an obviously wrong bin label, a cassette left open — but for a look-alike wrong-item mix-up specifically, it's checking the same visual difference the first tech already missed, under the same time pressure. It's not that the double-check does nothing; it's that it isn't the right tool for this particular error type. That's a fair distinction to bring to the director alongside the keyed-lane proposal — it explains why you're not just asking for a third check, you're asking for something that removes the need for the first two to catch this specific mistake.

**User:** Should we keep the second-tech check running once the keyed lanes are in, or drop it to save time?

**Assistant:** I'd keep it running for at least a few weeks after the keyed lanes and scan verification go live, and treat it as a pilot period rather than a permanent decision either way. That gives you a way to confirm the new controls are actually catching what they're supposed to before you remove a check that's been your only safety net until now. Once you've seen a stretch of restocks with no Med A/Med B mix-ups and the scan logs show the verification is firing correctly, dropping the redundant visual check for that specific pair is reasonable — but that's a call for the pharmacy manager to make once there's real data behind it, not something to decide up front.

**User:** Anything else we should watch for once this is live?

**Assistant:** One thing worth watching: whether techs start treating the barcode scan as the only check and stop paying attention to the physical bin shape at all — that's not a problem by itself, since the scan is the stronger control, but if the scanner ever goes down or gets skipped for a rush order, you want the keyed lanes to still be doing their job on their own. Confirming the keyed bins are hard to defeat even without the scan running (not just awkward, but actually blocked) would be worth checking during the pilot.

---

**What this skill did:**
- Classified the med-room error as Wrong Item and walked the full hierarchy from Elimination down for the cassette-wall restock step.
- Recommended keyed storage lanes with barcode scan-to-bin verification (Level 2) as the near-term fix, and named automated packaging (Level 1) as the strongest long-term option.
- Labeled the current second-tech visual check honestly as Level 5 Procedure rather than crediting it as mistake-proofing.

**What still needs a human:**
- Whether barcode scanners already exist in the med room to support scan-to-bin verification, or whether that infrastructure needs to be added first — `[NEEDS GEMBA]`.
- Budget and timeline for an automated packaging system, if Level 1 is something the pharmacy wants to pursue — `[ASSUMED — verify]`.
- Whether the keyed-lane bin hardware can be sized to fit the existing cassette wall footprint — worth a look on the floor before ordering anything.

**Suggested next step:** Walk the med room with the pharmacy manager and confirm whether barcode scanners are already available at the restock shelf, since that determines whether Level 2 can start next week or needs new equipment first.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
