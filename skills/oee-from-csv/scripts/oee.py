#!/usr/bin/env python3
"""OEE from a downtime/production CSV. Never guesses a missing column — says what it found and what it needs."""
import argparse, csv, io, re, sys
from collections import OrderedDict, defaultdict

REQUIRED = {
    "planned_min": ["planned_min", "planned_time", "planned_production_time", "planned time (min)", "scheduled_min", "scheduled hours"],
    "ideal_cycle_time": ["ideal_cycle_time", "ideal_cycle_time_min", "ideal cycle time", "rated_speed", "cycle_time"],
    "total_count": ["total_count", "total", "units", "count", "produced", "total units"],
    "good_count": ["good_count", "good", "good units", "first_pass"],
}
OPTIONAL = {
    "reject_count": ["reject_count", "rejects", "scrap", "reject"],
    "downtime_min": ["downtime_min", "downtime", "duration_min", "duration", "downtime (min)"],
    "downtime_reason": ["downtime_reason", "reason", "reason_code", "cause", "downtime reason"],
    "planned_downtime": ["planned_downtime", "is_planned", "planned"],
    "date": ["date", "day"], "shift": ["shift"], "line": ["line", "machine", "asset", "cell", "room"],
}
LOSSES = OrderedDict([
    ("Breakdowns", ["breakdown", "failure", "fail", "fault"]),
    ("Setup & adjustments", ["setup", "changeover", "adjust", "c/o"]),
    ("Idling & minor stops", ["jam", "minor stop", "idle", "idling", "blocked", "starved"]),
    ("Reduced speed", ["slow", "reduced speed", "speed loss"]),
    ("Process defects", ["scrap", "defect", "rework"]),
    ("Reduced yield / startup", ["startup", "start-up", "warm-up", "warmup", "yield"]),
])

def norm(s): return re.sub(r"[^a-z0-9]+", "_", (s or "").strip().lower()).strip("_")

def sniff_rows(text):
    lines = [l for l in text.splitlines() if l.strip()]
    if not lines: sys.exit("The file is empty.")
    # tolerate a junk title row: find the first line that looks like a header (2+ delimited fields, mostly non-numeric)
    start = 0
    for i, l in enumerate(lines[:10]):
        parts = re.split(r"[,;\t|]", l)
        if len(parts) >= 3 and sum(1 for p in parts if re.fullmatch(r"\s*-?\d+(\.\d+)?\s*", p)) < len(parts) / 2:
            start = i; break
    body = "\n".join(lines[start:])
    try: dialect = csv.Sniffer().sniff(body.splitlines()[0], delimiters=",;\t|")
    except csv.Error: dialect = csv.excel
    rows = list(csv.reader(io.StringIO(body), dialect))
    header = [norm(h) for h in rows[0]]
    keep = [i for i, h in enumerate(header) if h]  # drop blank columns
    header = [header[i] for i in keep]
    data = [[(r[i] if i < len(r) else "").strip() for i in keep] for r in rows[1:] if any(c.strip() for c in r)]
    return header, data, start

def resolve(header):
    found, missing = {}, []
    for key, aliases in list(REQUIRED.items()) + list(OPTIONAL.items()):
        hit = next((h for h in header if h in [norm(a) for a in aliases]), None)
        if hit: found[key] = header.index(hit)
        elif key in REQUIRED: missing.append(key)
    return found, missing

def num(v):
    try: return float(str(v).replace(",", ""))
    except ValueError: return None

def classify(reason):
    r = (reason or "").lower()
    for name, kws in LOSSES.items():
        if any(k in r for k in kws): return name
    return "Unmapped"

def pct(x): return f"{x*100:.1f}%"

def main():
    ap = argparse.ArgumentParser(description="OEE + Six Big Losses from a CSV export.")
    ap.add_argument("csv"); ap.add_argument("--cycle-time-unit", choices=["min", "s"], default="min")
    a = ap.parse_args()
    text = open(a.csv, encoding="utf-8-sig", errors="replace").read()
    header, data, skipped = sniff_rows(text)
    col, missing = resolve(header)
    print(f"# OEE report — {a.csv}\n")
    print(f"Columns found: {', '.join(header)}" + (f"  (skipped {skipped} title row(s))" if skipped else ""))
    if missing:
        print(f"\n**Still needed:** {', '.join(missing)}")
        print("Rename a column in the export to one of these, or add it — this script will not estimate a substitute value.")
        for m in missing: print(f"- `{m}` accepts: {', '.join(REQUIRED[m])}")
        sys.exit(2)

    def g(row, key):
        return row[col[key]] if key in col and col[key] < len(row) else ""

    # group by date/shift/line; planned + counts come from the first row of the group that carries them
    groups = OrderedDict()
    for row in data:
        key = tuple(g(row, k) for k in ("date", "shift", "line"))
        grp = groups.setdefault(key, {"planned": None, "ideal": None, "total": None, "good": None, "reject": None,
                                      "down": 0.0, "events": [], "planned_down": 0.0, "blank_quality": False})
        for k, src in (("planned", "planned_min"), ("ideal", "ideal_cycle_time"), ("total", "total_count"), ("good", "good_count"), ("reject", "reject_count")):
            v = num(g(row, src))
            if grp[k] is None and v is not None: grp[k] = v
        if g(row, "total_count") and not g(row, "good_count"): grp["blank_quality"] = True
        d = num(g(row, "downtime_min"))
        if d:
            planned_flag = g(row, "planned_downtime").lower() in ("1", "true", "yes", "y", "planned")
            if planned_flag: grp["planned_down"] += d
            else:
                grp["down"] += d; grp["events"].append((g(row, "downtime_reason"), d))

    unit = 1.0 / 60 if a.cycle_time_unit == "s" else 1.0
    flags, losses, totals = [], defaultdict(float), {"planned": 0, "run": 0, "total": 0, "good": 0, "ideal_x_count": 0}
    unmapped_text = defaultdict(float)
    per = []
    for key, grp in groups.items():
        if grp["planned"] is None or grp["ideal"] is None or grp["total"] is None: continue
        good = grp["good"]
        if good is None and grp["reject"] is not None: good = grp["total"] - grp["reject"]
        run = grp["planned"] - grp["down"]
        ideal = grp["ideal"] * unit
        A = run / grp["planned"] if grp["planned"] else 0
        P = (ideal * grp["total"]) / run if run else 0
        Q = (good / grp["total"]) if (good is not None and grp["total"]) else None
        label = " / ".join(k for k in key if k) or "all rows"
        per.append((label, grp["planned"], grp["down"], run, ideal, grp["total"], good, A, P, Q))
        totals["planned"] += grp["planned"]; totals["run"] += run; totals["total"] += grp["total"]
        totals["ideal_x_count"] += ideal * grp["total"]
        if good is not None: totals["good"] += good
        if grp["blank_quality"]: flags.append(f"{label}: good_count blank — excluded from Quality, not treated as 100% good.")
        if P > 1: flags.append(f"{label}: Performance {pct(P)} is over 100% — ideal cycle time is probably an average, not best-demonstrated, or counts include units made outside run time. Not a usable result.")
        for reason, d in grp["events"]:
            cat = classify(reason); losses[cat] += d
            if cat == "Unmapped": unmapped_text[reason or "(blank)"] += d

    A = totals["run"] / totals["planned"] if totals["planned"] else 0
    P = totals["ideal_x_count"] / totals["run"] if totals["run"] else 0
    Q = totals["good"] / totals["total"] if totals["total"] and totals["good"] else None
    OEE = A * P * (Q if Q is not None else 1)
    down = totals["planned"] - totals["run"]

    print("\n## Availability × Performance × Quality\n")
    print(f"- **Availability = run time ÷ planned time** = ({totals['planned']:.0f} − {down:.0f}) ÷ {totals['planned']:.0f} = {totals['run']:.0f} ÷ {totals['planned']:.0f} = **{pct(A)}**")
    print(f"- **Performance = (ideal cycle time × total count) ÷ run time** = {totals['ideal_x_count']:.0f} ÷ {totals['run']:.0f} = **{pct(P)}**")
    if Q is not None:
        print(f"- **Quality = good count ÷ total count** = {totals['good']:.0f} ÷ {totals['total']:.0f} = **{pct(Q)}**")
        print(f"- **OEE = A × P × Q** = {A:.3f} × {P:.3f} × {Q:.3f} = **{pct(OEE)}**")
    else:
        print("- **Quality:** no usable good_count — OEE below is Availability × Performance only.")
        print(f"- **A × P** = {A:.3f} × {P:.3f} = **{pct(OEE)}**")

    print("\n## Six Big Losses (unplanned downtime, minutes)\n")
    print("| Loss | min | share |\n|---|---:|---:|")
    total_loss = sum(losses.values()) or 1
    for name in list(LOSSES) + ["Unmapped"]:
        if losses.get(name): print(f"| {name} | {losses[name]:.0f} | {losses[name]/total_loss*100:.0f}% |")
    if unmapped_text:
        print("\n**Unmapped reason text (needs a category at the source system):** " + ", ".join(f'"{k}" {v:.0f} min' for k, v in sorted(unmapped_text.items(), key=lambda x: -x[1])))

    print("\n## Downtime Pareto\n")
    for name, m in sorted(losses.items(), key=lambda x: -x[1]):
        print(f"{name:<28} {'█' * int(round(m / total_loss * 40)):<40} {m:.0f}")

    if len(per) > 1:
        print("\n## By date / shift / line\n")
        print("| Group | planned | downtime | A | P | Q |\n|---|---:|---:|---:|---:|---:|")
        for label, planned, d, run, ideal, total, good, a_, p_, q_ in per:
            print(f"| {label} | {planned:.0f} | {d:.0f} | {pct(a_)} | {pct(p_)} | {pct(q_) if q_ is not None else '—'} |")

    print("\n## Flags\n")
    if "planned_downtime" not in col:
        flags.append("The export does not separate planned from unplanned downtime; all downtime was treated as unplanned. Check with whoever built the schedule.")
    if "downtime_reason" not in col:
        flags.append("No downtime reason column — the Six Big Losses table above is empty. The export needs reason codes to be actionable.")
    if not any(classify(r) == "Setup & adjustments" for grp in groups.values() for r, _ in grp["events"]):
        flags.append("No changeover rows found. If changeover isn't logged as downtime it shows up as a Performance loss instead of Availability, which misdirects the countermeasure.")
    flags.append("Confirm the ideal cycle time is the best-demonstrated rate, not an average of normal days — an average flatters Performance.")
    for f in flags: print(f"- {f}")

if __name__ == "__main__":
    main()
