#!/usr/bin/env python3
"""Static audit of every skill: contract checks that need no model. Exit 1 if any FAIL."""
import re, sys, pathlib, json

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILLS = sorted(p for p in (ROOT / "skills").iterdir() if (p / "SKILL.md").exists())
REQUIRED_SECTIONS = ["when to use", "how this skill works", "quality bar", "closing block"]
JARGON = re.compile(r"\b(LLM|LLMs|prompt engineering|prompts?|tokens?|hallucinat\w*|context window|language model)\b", re.I)

def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m: return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1); fm[k.strip()] = v.strip()
    return fm

results = []
for sk in SKILLS:
    text = (sk / "SKILL.md").read_text(encoding="utf-8")
    name = sk.name
    checks = {}
    fm = frontmatter(text)
    checks["frontmatter"] = bool(fm and fm.get("name") == name and fm.get("description") and fm.get("license") == "MIT")
    low = text.lower()
    for s in REQUIRED_SECTIONS:
        checks[f"section:{s}"] = s in low
    checks["when_not_to_use"] = ("don't use" in low or "do not use" in low or "when not" in low)
    checks["data_safety_line"] = ("leave out" in low and ("names" in low) ) or "data safety" in low or "data-safety" in low
    checks["needs_gemba_tag"] = "[needs gemba" in low
    checks["headcount_guardrail"] = "headcount" in low or "how many people" in low
    checks["mirrors_vocabulary"] = "vocabulary" in low or "mirror" in low or "pdsa" in low
    checks["no_ai_jargon"] = not JARGON.search(text)
    # referenced files must exist
    refs = set(re.findall(r"`?((?:resources|scripts)/[A-Za-z0-9_./-]+)`?", text))
    refs |= set(re.findall(r"skills/%s/(scripts/[A-Za-z0-9_./-]+)" % re.escape(name), text))
    missing = []
    for r in sorted(refs):
        r = r.rstrip(".,)")
        cands = [sk / r, ROOT / r, ROOT / "skills" / name / r]
        if not any(c.exists() for c in cands): missing.append(r)
    checks["referenced_files_exist"] = not missing
    results.append({"skill": name, "checks": checks, "missing_files": missing})

fails = 0
print(f"{'skill':<20} {'pass':>4} {'fail':>4}  failing checks")
for r in results:
    bad = [k for k, v in r["checks"].items() if not v]
    fails += len(bad)
    print(f"{r['skill']:<20} {len(r['checks'])-len(bad):>4} {len(bad):>4}  {', '.join(bad)}")
    for m in r["missing_files"]: print(f"{'':<30}missing: {m}")
print(f"\n{len(SKILLS)} skills · {fails} failing checks")
(ROOT / "tests" / "audit-results.json").write_text(json.dumps(results, indent=2))
sys.exit(1 if fails else 0)
