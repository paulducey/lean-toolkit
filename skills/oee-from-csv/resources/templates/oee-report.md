# OEE report — [filename]

Columns found: [list]  (skipped [N] title row(s) if any)

## Availability × Performance × Quality

- **Availability = run time ÷ planned time** = ([planned] − [downtime]) ÷ [planned] = [run] ÷ [planned] = **[A%]**
- **Performance = (ideal cycle time × total count) ÷ run time** = [ideal × count] ÷ [run] = **[P%]**
- **Quality = good count ÷ total count** = [good] ÷ [total] = **[Q%]** (omitted, with a note, if no good_count/reject_count column exists — then this section reports A × P and is never called OEE)
- **OEE = A × P × Q** = [A] × [P] × [Q] = **[OEE%]**

Any of A, P, Q, or OEE outside 0–100% is flagged in Flags below, not
printed as a plain result.

## Six Big Losses (unplanned downtime, minutes)

| Loss | min | share |
|---|---:|---:|
| Breakdowns | [min] | [%] |
| Setup & adjustments | [min] | [%] |
| Idling & minor stops | [min] | [%] |
| Reduced speed | [min] | [%] |
| Process defects | [min] | [%] |
| Reduced yield / startup | [min] | [%] |
| Unmapped | [min] | [%] |

**Unmapped reason text (needs a category at the source system):** "[reason]" [min] min, ...

## Downtime Pareto

[Loss name]                   [bar of █]                                [min]

## By date / shift / line

(only when `date`/`shift`/`line` columns are present)

| Group | planned | downtime | A | P | Q |
|---|---:|---:|---:|---:|---:|
| [label] | [min] | [min] | [%] | [%] | [%] |

## Flags

- [Planned vs. unplanned downtime not distinguished, if applicable.]
- [No downtime reason column, if applicable.]
- [No changeover rows found, if applicable — changeover may be hiding inside Performance loss.]
- [Confirm ideal cycle time is best-demonstrated, not an average.]
- [Any A/P/Q/OEE outside 0–100%, named as not usable, with the likely cause.]

---

[Closing block from docs/CLOSING-BLOCK.md, filled in for this run.]
