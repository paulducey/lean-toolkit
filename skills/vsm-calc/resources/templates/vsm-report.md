# VSM calculation — [filename]

This is the structure `vsm_calc.py` writes to stdout. Every cycle time
carries a source tag (`observed, N cycles, date`, `from MES`, `user
estimate`) or is marked `[NEEDS GEMBA: time this step]` — never filled in
silently. Relabel "units"/"line"/"days of supply" into the user's own
words (patients, visits, patients waiting) once they've used them; the
numbers underneath never change.

## Current state

**Takt time = available time ÷ demand** = [available_s] s ÷ [demand] units = **[takt] s per unit** ([takt in min])

| Step | C/T | C/O per unit | Uptime | Effective C/T | vs takt | Inventory before | Days of supply | Source |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [step] | [ct] s | [co/unit] s | [uptime%] | [eff ct] s | [ratio] ok/at risk/OVER | [inventory] | [days] d ([hours] h) | [source or [NEEDS GEMBA: source]] |
| [step with no timing] | [NEEDS GEMBA: time this step] | | | | | [inventory] | | |

- **Processing time** (sum of C/T) = **[total]**
- **Lead time** (processing + inventory waiting) = **[total]** ([seconds] s = [days] days of available time)
- **PCE = processing ÷ lead time** = [proc] ÷ [lead] = **[PCE%]** (flagged, not printed as a plain result, if outside 0–100%)
- **Bottleneck: [step]** at [eff] s effective vs takt [takt] s — the line [meets/does NOT meet] takt on the cycles observed. [If a second step is within 5%, name it as a shared constraint rather than a single bottleneck.]

## Future state

(only when a `--future` file was given — same table shape as above, for the future-state file)

## Delta (future − current)

| Measure | Current | Future | Change |
|---|---:|---:|---:|
| Processing time | [value] | [value] | [+/− value] |
| Lead time | [value] | [value] | [+/− value] |
| PCE | [%] | [%] | [+/− pts] |

## Flags

- [Each step with no cycle time, marked NEEDS GEMBA, excluded from totals.]
- [Changeover given without lot_size, so it could not be amortized — NEEDS GEMBA: units between changeovers.]
- [Any uptime outside 0–100%, treated as 100%, check the input.]
- [PCE or an effective cycle time outside its sane range — not a usable result, with the likely cause (unit mix-up, inventory in the wrong column).]
- [None, if every step is timed and sourced — still note that sample sizes should be confirmed before treating the bottleneck call as final.]

---

[Closing block from docs/CLOSING-BLOCK.md, filled in for this run.]
