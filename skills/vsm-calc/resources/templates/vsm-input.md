# VSM input shape

One row per process step, in flow order. CSV; comma, semicolon or tab all work. Column names are matched loosely (`cycle_time_s`, `CT (s)`, `cycle time` all resolve).

| Column | Required | Meaning |
|---|---|---|
| `step` | yes | Step name in flow order |
| `cycle_time_s` | yes | Time to complete one unit at this step, in **seconds**, operator-paced. Leave blank if not timed — the calculator marks it `[NEEDS GEMBA: time this step]`; never type a guess |
| `changeover_s` | no | Changeover / turnaround time in seconds |
| `lot_size` | if `changeover_s` given | Units produced between changeovers, so changeover can be amortized per unit |
| `uptime_pct` | no | Uptime as a percentage (`92`) or fraction (`0.92`); default 100 |
| `inventory_before` | no | Units (or patients) waiting in front of this step |
| `source` | no, strongly recommended | Where the cycle time came from: `observed, 12 cycles, 2026-09-14` · `from MES` · `user estimate` |

Demand and available time are passed on the command line, over the same period (usually one day):

```
python3 skills/vsm-calc/scripts/vsm_calc.py steps.csv --demand 575 --available-time-s 55200
```

Example `steps.csv`:

```
step,cycle_time_s,changeover_s,lot_size,uptime_pct,inventory_before,source
Blank,45,1800,500,92,1200,"from MES"
Form,60,2400,500,88,800,"observed, 10 cycles, 2026-09-12"
Weld,75,,,95,350,"observed, 8 cycles, 2026-09-12"
Inspect,,,,100,120,
Pack,40,,,100,60,"user estimate"
```

For a future state, give a second file in the same shape with `--future future.csv`; the report adds a delta table.
