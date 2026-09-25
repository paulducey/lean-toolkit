# Lean Toolkit

**Seventeen free skills that turn an AI assistant into a clipboard-carrier for Lean work.** The assistant does the document — the A3, the OEE breakdown, the job breakdown sheet — so you can be at the gemba instead of at a keyboard.

Every number it produces carries a source tag. Every fact it doesn't have is marked **[NEEDS GEMBA]** instead of invented. Every deliverable ends by sending you back to the floor.

MIT licensed: copy it, change it, put your company's name on it.

**New here?** Read [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md) — ten minutes, assumes you know Lean and nothing about AI tools.

## What's a skill?

A plain-text file. It tells the assistant how to do one job, when *not* to do it, and what a good result looks like — the same way a job breakdown sheet tells a trainer how to teach one job. You don't need to read it to use it, but you can, and you should: there is nothing in these files you couldn't write yourself.

## The seventeen

| You have… | Skill | What you get |
|---|---|---|
| No idea where to start | `start-here` | A 120-word orientation, one question, and a hand-off to the right skill |
| A problem to put on one page | `a3-coach` | An 8-box A3, coached left to right — countermeasures only after the root cause |
| "Why does this keep happening?" | `root-cause` | IS/IS-NOT, 5 Whys or fishbone, a verified root cause, one corrective action |
| A vague complaint | `problem-statement` | IS/IS-NOT scoping and one measurable sentence, with the cause and solution stripped out |
| A kaizen event to plan | `kaizen-charter` | An 11-section charter a sponsor could sign, after asking whether this is the right event |
| A walk to plan or debrief | `gemba-walk` | A pre-walk plan by process order, or a six-step debrief — never a punch list |
| A job to document as done today | `standard-work` | A combination sheet: takt, sequence, standard WIP, every time sourced |
| A job to teach | `twi-jbs` | A job breakdown sheet — important steps, key points, reasons — plus a training timetable |
| Timings and inventories from a walk | `vsm-calc` | Takt, effective cycle time, lead time, PCE, and the bottleneck — computed by a script |
| A downtime export from the MES | `oee-from-csv` | Availability × Performance × Quality with every formula shown, and the Six Big Losses |
| A workplace to score | `5s-audit` | A scored 5S audit by zone with a prioritized action list |
| A changeover to shorten | `smed-setup` | Internal/external separation and a changeover plan |
| A measurement that varies | `control-chart` | Control limits, common vs. special cause, Cp/Cpk — with the sample-size caveat |
| A process or machine to risk-assess | `fmea-builder` | An FMEA table on explicit 1–10 scales, RPN shown |
| A mistake to design out | `mistake-proofing` | The poka-yoke hierarchy, from elimination down, and why a checklist is weakest |
| "Can we hit the volume?" | `capacity-planner` | Takt, station loading, the bottleneck, and what-ifs — as capacity, never headcount |
| Tier boards nobody looks at | `daily-management` | A tiered daily management design with escalation |

Each skill's folder holds a `SKILL.md` and `resources/examples/` — full worked exchanges showing what "good" looks like, at least one of them in a hospital or clinic setting.

## Use it

**No install — paste into a chat.** Copy a `SKILL.md` into a Claude Project's instructions (or any assistant that takes pasted instructions), then say what's in front of you.

**Claude Code — for the skills that run scripts.** Two skills do their arithmetic in a script (`oee-from-csv`, `vsm-calc`), and four can export a deliverable to Word (`kaizen-charter`, `twi-jbs`, `oee-from-csv`, `vsm-calc`). Exporting is optional — in a chat you simply copy the Markdown. The calculators are not optional; use Claude Code for those two.
```bash
cp -r skills/*/ .claude/skills/
```
Then: *"Run the oee-from-csv skill on line1_downtime.csv."* Try it first on the sample in `skills/oee-from-csv/resources/examples/`.

Both paths, step by step, with what to do when something goes wrong: [docs/GETTING-STARTED.md](docs/GETTING-STARTED.md).

## The promises every skill keeps

The ten-point contract is in [docs/TOOLKIT-CONTRACT.md](docs/TOOLKIT-CONTRACT.md). The ones that matter most on a real floor:

- It says the **data-safety line** before you paste anything — leave out names of employees or patients.
- It **never invents a fact**. `[NEEDS GEMBA]` means go look; `[ASSUMED — verify]` means this changes the answer if it's wrong.
- **"Just draft it"** always works — skip the questions, get the deliverable with placeholders.
- It **mirrors your vocabulary** — PDSA, unit, clinician — and never corrects you.
- Ask **"how many people can we cut"** and it answers the capacity question, then says once: these tools free capacity; what the organization does with it is a leadership decision.
- Any result outside its sane range is **flagged, never printed** — a spreadsheet will happily compute 104% OEE; this won't.

## Tested

`tests/audit_skills.py` checks every skill against the contract and that every file it references exists. `tests/VALIDATION-PROMPT.md` and `tests/scenarios.md` let a fresh model session try to break each skill and write a cited report; the two independent reports are in `tests/REPORT.md` (first pass, 5 blockers) and `tests/REPORT-2.md` (after fixes: 0 blockers).

```bash
python3 tests/audit_skills.py
```

## From the talk

These skills were the subject of *"AI at the Gemba"* at the 22nd Northeast Lean Conference (Sept 2026). The deck, the script, and a one-page handout are in `docs/`, and at [paulducey.com/gemba](https://paulducey.com/gemba).

## License

MIT — free to use, copy, modify, and distribute. See [LICENSE](LICENSE).
