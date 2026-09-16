#!/usr/bin/env python3
"""VSM arithmetic from a step table: takt, effective cycle time, inventory as days of supply, lead time, PCE, bottleneck.
Never estimates a missing cycle time — marks it [NEEDS GEMBA]. Flags any result outside its sane range."""
import argparse, csv, io, re, sys

ALIASES = {
    "step": ["step", "process", "process_step", "name", "station"],
    "cycle_time_s": ["cycle_time_s", "ct_s", "cycle_time", "c_t", "ct", "cycle time (s)", "processing_time_s"],
    "changeover_s": ["changeover_s", "co_s", "changeover", "c_o", "setup_s", "turnaround_s"],
    "lot_size": ["lot_size", "units_per_changeover", "batch", "batch_size"],
    "uptime_pct": ["uptime_pct", "uptime", "availability_pct", "availability"],
    "inventory_before": ["inventory_before", "inventory", "wip_before", "queue", "waiting", "patients_waiting"],
    "source": ["source", "ct_source", "cycle_time_source"],
}
def norm(s): return re.sub(r"[^a-z0-9]+", "_", (s or "").strip().lower()).strip("_")
def num(v):
    try: return float(str(v).replace(",", "").replace("%", ""))
    except (ValueError, TypeError): return None
def fmt_s(s):
    if s is None: return "—"
    if s >= 3600: return f"{s/3600:.1f} h"
    if s >= 60: return f"{s/60:.1f} min"
    return f"{s:.0f} s"

def read_table(path):
    text = open(path, encoding="utf-8-sig").read()
    try: dialect = csv.Sniffer().sniff(text.splitlines()[0], delimiters=",;\t|")
    except (csv.Error, IndexError): dialect = csv.excel
    rows = list(csv.reader(io.StringIO(text), dialect))
    if not rows: sys.exit(f"{path}: empty file.")
    header = [norm(h) for h in rows[0]]
    col = {}
    for key, al in ALIASES.items():
        hit = next((h for h in header if h in [norm(x) for x in al]), None)
        if hit: col[key] = header.index(hit)
    if "step" not in col or "cycle_time_s" not in col:
        sys.exit(f"{path}: need at least a step column and a cycle_time_s column. Found: {', '.join(header)}. See resources/templates/vsm-input.md.")
    out = []
    for r in rows[1:]:
        if not any(c.strip() for c in r): continue
        g = lambda k: (r[col[k]].strip() if k in col and col[k] < len(r) else "")
        out.append({"step": g("step"), "ct": num(g("cycle_time_s")), "co": num(g("changeover_s")), "lot": num(g("lot_size")),
                    "uptime": num(g("uptime_pct")), "inv": num(g("inventory_before")), "source": g("source")})
    return out

def compute(steps, demand, available_s):
    takt = available_s / demand
    flags, rows = [], []
    proc_total, lead_total = 0.0, 0.0
    for s in steps:
        r = dict(s)
        if s["ct"] is None:
            r.update(eff=None, inv_days=None, note="[NEEDS GEMBA: time this step]")
            flags.append(f"{s['step']}: no cycle time given — marked [NEEDS GEMBA: time this step]; excluded from totals, so lead time and PCE are understated until it is timed.")
            rows.append(r); continue
        if s["ct"] < 0: flags.append(f"{s['step']}: negative cycle time — not usable.")
        up = (s["uptime"] / 100.0) if s["uptime"] and s["uptime"] > 1 else (s["uptime"] if s["uptime"] else 1.0)
        if up <= 0 or up > 1: flags.append(f"{s['step']}: uptime {s['uptime']} is outside 0–100% — treated as 100%, check the input."); up = 1.0
        co_per_unit = 0.0
        if s["co"]:
            if s["lot"] and s["lot"] > 0: co_per_unit = s["co"] / s["lot"]
            else: flags.append(f"{s['step']}: changeover given without lot_size — cannot amortize per unit; changeover excluded. [NEEDS GEMBA: units between changeovers]")
        eff = (s["ct"] + co_per_unit) / up
        inv_days = (s["inv"] / demand) if s["inv"] is not None else 0.0
        r.update(eff=eff, co_per_unit=co_per_unit, up=up, inv_days=inv_days, note="")
        proc_total += s["ct"]; lead_total += s["ct"] + inv_days * available_s
        rows.append(r)
    pce = (proc_total / lead_total) if lead_total else None
    if pce is not None and (pce > 1 or pce < 0):
        flags.append(f"PCE {pce*100:.1f}% is outside 0–100% — processing time cannot exceed lead time. Usually a unit mix-up (seconds vs minutes) or inventory in the wrong column. Not a usable result.")
    timed = [r for r in rows if r.get("eff") is not None]
    bottleneck = max(timed, key=lambda r: r["eff"]) if timed else None
    near = [r["step"] for r in timed if bottleneck and r is not bottleneck and r["eff"] >= 0.95 * bottleneck["eff"]]
    return {"takt": takt, "rows": rows, "proc": proc_total, "lead": lead_total, "pce": pce, "bottleneck": bottleneck, "near": near, "flags": flags}

def report(res, demand, available_s, label="Current state"):
    print(f"## {label}\n")
    print(f"**Takt time = available time ÷ demand** = {available_s:.0f} s ÷ {demand:g} units = **{res['takt']:.1f} s per unit** ({fmt_s(res['takt'])})\n")
    print("| Step | C/T | C/O per unit | Uptime | Effective C/T | vs takt | Inventory before | Days of supply | Source |")
    print("|---|---:|---:|---:|---:|---:|---:|---:|---|")
    for r in res["rows"]:
        if r["eff"] is None:
            print(f"| {r['step']} | {r['note']} | | | | | {r['inv'] if r['inv'] is not None else ''} | | {r['source']} |"); continue
        ratio = r["eff"] / res["takt"]
        status = "OVER" if ratio > 1 else ("at risk" if ratio > 0.85 else "ok")
        print(f"| {r['step']} | {r['ct']:.0f} s | {r['co_per_unit']:.1f} s | {r['up']*100:.0f}% | {r['eff']:.1f} s | {ratio:.2f} {status} | {r['inv'] if r['inv'] is not None else 0:g} | {r['inv_days']:.2f} d ({fmt_s(r['inv_days']*available_s)}) | {r['source'] or '[NEEDS GEMBA: source]'} |")
    print()
    print(f"- **Processing time** (sum of C/T) = **{fmt_s(res['proc'])}** ({res['proc']:.0f} s)")
    print(f"- **Lead time** (processing + inventory waiting) = **{fmt_s(res['lead'])}** ({res['lead']:.0f} s = {res['lead']/available_s:.2f} days of available time)")
    if res["pce"] is not None:
        bad = res["pce"] > 1 or res["pce"] < 0
        print(f"- **PCE = processing ÷ lead time** = {res['proc']:.0f} ÷ {res['lead']:.0f} = **{res['pce']*100:.1f}%**" + ("  ⚠ NOT USABLE — see flags" if bad else ""))
    b = res["bottleneck"]
    if b:
        meets = b["eff"] <= res["takt"]
        print(f"- **Bottleneck: {b['step']}** at {b['eff']:.1f} s effective vs takt {res['takt']:.1f} s — the line {'meets' if meets else 'does NOT meet'} takt on the cycles observed."
              + (f" {', '.join(res['near'])} is within 5% — treat as a shared constraint, not a single bottleneck." if res["near"] else ""))
    print()

def main():
    ap = argparse.ArgumentParser(description="VSM numbers from a step table.")
    ap.add_argument("steps"); ap.add_argument("--demand", type=float, required=True, help="units per period")
    ap.add_argument("--available-time-s", type=float, required=True, help="available seconds per period, net of breaks")
    ap.add_argument("--future", help="second step table for a future-state delta")
    a = ap.parse_args()
    if a.demand <= 0 or a.available_time_s <= 0: sys.exit("demand and available time must be positive.")
    cur = compute(read_table(a.steps), a.demand, a.available_time_s)
    print(f"# VSM calculation — {a.steps}\n")
    report(cur, a.demand, a.available_time_s)
    if a.future:
        fut = compute(read_table(a.future), a.demand, a.available_time_s)
        report(fut, a.demand, a.available_time_s, "Future state")
        print("## Delta (future − current)\n")
        print("| Measure | Current | Future | Change |\n|---|---:|---:|---:|")
        for name, c, f in (("Processing time", cur["proc"], fut["proc"]), ("Lead time", cur["lead"], fut["lead"])):
            print(f"| {name} | {fmt_s(c)} | {fmt_s(f)} | {fmt_s(f-c) if f>=c else '−'+fmt_s(c-f)} |")
        if cur["pce"] is not None and fut["pce"] is not None:
            print(f"| PCE | {cur['pce']*100:.1f}% | {fut['pce']*100:.1f}% | {(fut['pce']-cur['pce'])*100:+.1f} pts |")
        print()
        cur["flags"] += [f"future: {f}" for f in fut["flags"]]
    print("## Flags\n")
    for f in cur["flags"] or ["None — every step timed and sourced. Confirm sample sizes before treating the bottleneck call as final."]: print(f"- {f}")

if __name__ == "__main__":
    main()
