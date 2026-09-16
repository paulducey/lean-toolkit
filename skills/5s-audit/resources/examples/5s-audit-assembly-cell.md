Shows a three-zone scored audit of an assembly cell, with the Sustain cap applied in two zones, a Shine finding that reveals a hydraulic leak, and priority actions ordered with the safety item first.

**User:** Need a 5S audit of Assembly Cell 7. It has three zones — incoming materials, the build area, and outbound staging.

**Assistant:** Describe the area — what's there, how many zones, and what you're seeing — and I'll build the audit. Before you paste anything — leave out any personally identifiable information; area names, zone codes, and equipment IDs are fine.

**User:** Incoming materials: bins are labeled but two of the labeled locations are empty and one has the wrong part sitting in it. Build area: tools are on a shadow board, all present, but I noticed the hydraulic press has a small puddle underneath it that someone wiped up before I got there — found out from the operator it's been reappearing for about two weeks and nobody's logged it. Outbound staging: no labels at all, product just gets stacked wherever there's floor space, and there's a stack of pallets partially blocking the fire exit sign.

**Assistant:** Here are the three zone tables.

## Zone: Incoming Materials
Date: 2026-09-16
Auditor: [role or initials — NEEDS GEMBA: confirm who conducted this]

| Pillar | Score (0–3) | Key Observation |
|---|---|---|
| Sort | 2 | Only current-work items observed; no excess noted [observed] |
| Set in Order | 1 | Labels present but two labeled locations empty, one holds the wrong part [observed] |
| Shine | 2 | Surfaces clean, no inspection findings reported for this zone [observed] |
| Standardize | 1 | No posted visual standard describing correct bin fill state [observed] |
| Sustain | 1 | Capped at 1 — cannot exceed the lowest of the other four pillars (Set in Order and Standardize both at 1) |
| ZONE TOTAL | 7/15 | |

## Zone: Build Area
Date: 2026-09-16
Auditor: [role or initials — NEEDS GEMBA]

| Pillar | Score (0–3) | Key Observation |
|---|---|---|
| Sort | 3 | Shadow board holds only needed tools, all present [observed] |
| Set in Order | 3 | Every tool has a designated, labeled location [observed] |
| Shine | 1 | Hydraulic puddle under the press wiped up before audit rather than addressed as a recurring leak; cleaning here is cosmetic, not inspection-linked [observed] |
| Standardize | 2 | Shadow board is a posted visual standard; no standard exists for equipment leak reporting [observed] |
| Sustain | 1 | Capped at 1 — cannot exceed Shine (1), the lowest of the other four pillars |
| ZONE TOTAL | 10/15 | |

**Flag:** The Shine finding here is a live equipment condition, not a scoring nuance — a hydraulic leak reappearing for two weeks and never logged belongs in `root-cause` or `fmea-builder` once this audit closes; this audit documents the condition, not the fix.

## Zone: Outbound Staging
Date: 2026-09-16
Auditor: [role or initials — NEEDS GEMBA]

| Pillar | Score (0–3) | Key Observation |
|---|---|---|
| Sort | 1 | No indication of excess material; insufficient evidence either way [ASSUMED — verify: zone needs a dedicated look for unneeded items] |
| Set in Order | 0 | No labels; product stacked wherever floor space allows [observed] |
| Shine | 1 | No inspection tie observed; condition not assessed beyond stacking [observed] |
| Standardize | 0 | No visual standard of any kind [observed] |
| Sustain | 0 | Capped at 0 — cannot exceed Set in Order or Standardize (both 0) |
| ZONE TOTAL | 2/15 | |

## Gap and Action Table

| Zone | Pillar | Score | Gap Description | Priority Action | Owner (role) | Due |
|---|---|---|---|---|---|---|
| Outbound Staging | Safety (cross-pillar) | n/a | Pallet stack partially blocks the fire exit sign | Relocate pallets immediately; clear exit sign line of sight | Cell 7 supervisor | Immediate |
| Build Area | Shine | 1 | Hydraulic press leak wiped before audit, reappearing 2 weeks, unlogged | Log the leak, route to maintenance for root-cause investigation | Maintenance lead | This week |
| Outbound Staging | Set in Order / Standardize | 0 | No staging lanes or labels | Define and mark staging lanes by destination | Cell 7 supervisor | 2 weeks |
| Incoming Materials | Set in Order | 1 | Two labeled locations empty, one holds wrong part | Reconcile bin contents against labels; correct or update labels | Materials lead | 1 week |

Priority order: the fire-exit obstruction is a safety item and ranks first regardless of pillar; Sort/Set in Order gaps rank next because they unlock progress elsewhere; Standardize/Sustain actions follow once the first two are addressed.

**Audit total (not averaged):** Incoming Materials 7/15, Build Area 10/15, Outbound Staging 2/15 — each reported separately; the cell is not summarized as a single score.

---

**What this skill did:**
- Scored three zones of Assembly Cell 7 independently; applied the Sustain cap rule in two zones (Incoming Materials and Build Area) because a lower-scoring pillar in each zone capped what Sustain could show.
- The Shine pillar in the Build Area revealed an unaddressed hydraulic leak masked by pre-audit cleanup — flagged for `root-cause` or `fmea-builder`, not resolved here.
- A safety item (blocked fire exit sign in Outbound Staging) was ranked first in the action table ahead of any organizational gap.

**What still needs a human:**
- Outbound Staging's Sort score is marked `[ASSUMED — verify]` — this zone needs a dedicated look for unneeded material before that score can be trusted.
- Confirm who conducted the walk-through so the auditor field isn't left blank on the posted record.
- Decide who owns the hydraulic leak investigation and how urgently, given it's been recurring for two weeks unlogged.

**Suggested next step:** Take the hydraulic leak finding to the maintenance lead today and get it logged before the next shift, ahead of any of the organizational actions.

---

*Skill from [paulducey.com/skills](https://paulducey.com/skills) · MIT License*
