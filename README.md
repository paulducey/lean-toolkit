# Lean Toolkit — Claude Code Skills

17 free, MIT-licensed skills for Lean and continuous-improvement practitioners using Claude Code.

Drop any skill into your project's `.claude/skills/` directory and Claude will use it automatically.

## Skills

### Unit Tools (free)

| Skill | What it does |
|-------|-------------|
| `start-here` | Lean diagnostic — identify which skill fits your problem |
| `oee-from-csv` | OEE calculation from raw log data; Six Big Losses breakdown |
| `vsm-calc` | Value Stream Map metrics — lead time, VA ratio, takt vs. cycle |
| `kaizen-charter` | Kaizen event charter with scope, targets, and team structure |
| `twi-jbs` | TWI Job Breakdown Sheet — important steps, key points, reasons |
| `root-cause` | IS/IS-NOT scoping, 5 Whys, fishbone, barrier analysis |
| `a3-coach` | 8-section A3 report, coached left-to-right |
| `gemba-walk` | 5-lens observation guide with structured debrief |
| `standard-work` | Standard work combination sheet — takt, sequence, WIP |
| `problem-statement` | IS/IS-NOT + SMART validation → one tight sentence |
| `5s-audit` | Scored 5S audit by zone with priority action list |
| `smed-setup` | SMED changeover analysis — internal/external separation |
| `control-chart` | SPC control chart — common vs. special cause, Cp/Cpk |
| `fmea-builder` | FMEA table — Severity × Occurrence × Detection = RPN |
| `mistake-proofing` | Poka-yoke hierarchy — elimination through procedure |
| `capacity-planner` | Takt time, bottleneck ID, what-if scenarios |
| `daily-management` | Tiered daily management — T1/T2/T3 boards and escalation |

## Installation

```bash
# Copy a single skill
cp -r skills/oee-from-csv/.claude/skills/

# Copy all skills
cp -r skills/*/ .claude/skills/
```

Then tell Claude: *"Use the oee-from-csv skill to analyze this data."* — or just describe your problem and it will select the right skill.

## Orchestration Skills

Six paid orchestration skills that chain these unit tools into full improvement programs are available at [paulducey.com/skills](https://paulducey.com/skills).

## License

MIT — free to use, copy, modify, and distribute. See [LICENSE](LICENSE).
