# Getting started

You know Lean. You may not know AI assistants. That's fine — this page assumes nothing about the second part.

**What this toolkit is:** seventeen plain-text files. Each one is standard work for an AI assistant — it tells the assistant how to do one job you'd normally do at a keyboard (an A3, an OEE breakdown, a job breakdown sheet), when *not* to do it, and what a good result looks like. The assistant holds the clipboard; you go see.

**What you need:** an AI assistant that can read a file you give it. Claude works with all of these out of the box; the files are plain text, so any assistant that lets you paste instructions can use them.

**Time to first result:** about ten minutes.

---

## Path A — No install: paste a skill into a Claude chat (easiest)

Use this if you have a Claude account (free or paid) at claude.ai and you've never installed anything.

1. Open the skill you want. Start with `skills/start-here/SKILL.md` if you're not sure which — it asks you one question and routes you.
2. Select everything in the file and copy it.
3. In claude.ai, start a **new Project** (left sidebar → Projects → New project). Name it after the skill, e.g. "OEE from CSV."
4. In the project, open **Project instructions** (sometimes "Set custom instructions") and paste the whole file there. Save.
5. Start a chat inside that project. Say what's in front of you: *"I have a downtime export from Line 1 — here it is."* Then paste or attach your file.
6. The assistant will say the data-safety line first (leave out names of employees or patients). Then it works.

If you don't want to use Projects: start any new chat, paste the skill file as your first message, then on the next line write what you need. That works too; you'll just have to re-paste next time.

## Path B — Claude Code (for the ones that run scripts)

Two of the skills — `oee-from-csv` and `vsm-calc` — run a small Python script so the arithmetic is never done in the assistant's head. To use those the way they're designed, you need Claude Code, which runs on your computer. Four skills (`kaizen-charter`, `twi-jbs`, `oee-from-csv`, `vsm-calc`) can also export the finished deliverable to a Word file with a script; that part is optional — in a plain chat, just copy the Markdown into your document. If a skill mentions `export_docx.py` and you're in a chat, ignore it.

1. Install Claude Code — follow the current instructions at https://code.claude.com/docs (it's a single install; you'll sign in with your Claude account).
2. Make a folder for your Lean work, e.g. `lean-work`, and put your data files in it (your downtime export, your step table).
3. Download this toolkit (the green **Code → Download ZIP** button on GitHub, or the zip from paulducey.com/gemba) and unzip it.
4. Copy the skills into your work folder:
   ```
   cp -r lean-toolkit/skills/*/ lean-work/.claude/skills/
   ```
   (On Windows, copy the folders inside `lean-toolkit/skills/` into `lean-work\.claude\skills\`.)
5. Open a terminal in `lean-work` and run `claude`.
6. Type what you need in plain English: *"Run the oee-from-csv skill on line1_downtime.csv."* Claude reads the skill, says the data-safety line, runs the script, and shows you every formula with the numbers substituted.

Try it first on the sample that ships with the toolkit: `skills/oee-from-csv/resources/examples/line1_downtime.csv`. You should get OEE 72.0% and a row called **Unmapped** — that row is the point.

## Path C — Another assistant

The files are plain text with no special syntax. Paste a `SKILL.md` into whatever "custom instructions" or "system prompt" box your assistant offers, then talk to it. The two calculators need Python and Claude Code; the Word export is optional everywhere; the other skills need nothing.

---

## Your first ten minutes

1. **Paste `start-here`.** Say: *"I'm a CI lead at a plant. What can you do?"* You'll get a 120-word answer and one question: "What's in front of you right now?"
2. **Answer it honestly.** "A changeover that takes 47 minutes." It routes you to one skill and hands off.
3. **Paste that skill** (new project or new chat) and say the same thing again. Answer its two or three questions — or say **"just draft it."**
4. **Read the deliverable's tags.** Every number says where it came from: `[observed]`, `[from system: MES]`, `[user estimate]`, or `[NEEDS GEMBA]`.
5. **Go to the floor with the yellow tags.** A first draft that's mostly `[NEEDS GEMBA]` is normal. It's your to-do list.

---

## The five things to know

**"Just draft it."** The coaching skills ask a few questions first, like a sensei would. If you're in a hurry, say *just draft it* and you get the deliverable immediately with placeholders where facts are missing. Neither mode invents facts.

**`[NEEDS GEMBA]`** means "nobody knows this yet — go look, go ask." It is not an error. It's the assistant pulling the andon cord instead of passing a guess downstream. `[ASSUMED — verify]` means "I used this assumption; if it's wrong, the answer changes."

**Source tags.** If a number doesn't have a tag, don't trust it. Ask where it came from. The skills are written so that never happens, but you're the check.

**Data safety.** Before you paste anything, leave out names of employees or patients — roles and initials are fine. In healthcare, no patient identifiers, chart numbers, or dates of birth. The skill will remind you; the reminder is not a control — know your company's policy on what can go into an AI tool at all.

**It speaks your language.** Say PDSA and it says PDSA. Say unit and clinician and it stops saying line and operator. It never corrects you.

---

## When something goes wrong

| What you see | What it means | What to do |
|---|---|---|
| "Still needed: planned_min, ideal_cycle_time" | Your export is missing a column the script needs. It will not guess. | Rename a column in your export to one of the names it lists, or add it. |
| A big **Unmapped** row in the OEE losses | Your downtime reason codes don't fit the six categories. | That's a finding, not a bug: the reason codes need better categories at the source system. |
| "Performance 104% — not a usable result" | Your "ideal" cycle time is probably an average, not the best-demonstrated rate. | Find the best demonstrated rate and re-run. |
| It keeps asking questions | You're in coaching mode. | Say *just draft it.* |
| It won't tell you how many people to cut | By design. | It will tell you capacity freed. What to do with it is a leadership decision. |
| It used a word you don't use | It hasn't heard your vocabulary yet. | Use your word once; it will follow. |

---

## Which skill for what

| You have… | Use |
|---|---|
| No idea where to start | `start-here` |
| A problem to put on one page for a review | `a3-coach` |
| A recurring defect or "why does this keep happening" | `root-cause` |
| A vague complaint that needs to become a problem | `problem-statement` |
| A kaizen event to plan | `kaizen-charter` |
| A walk to plan or debrief | `gemba-walk` |
| A job to document as it's done today | `standard-work` |
| A job to teach someone | `twi-jbs` |
| Cycle times and inventories from a walk | `vsm-calc` |
| A downtime export from the MES | `oee-from-csv` |
| A workplace to score for 5S | `5s-audit` |
| A changeover to shorten | `smed-setup` |
| A measurement that varies and you need to know if it's in control | `control-chart` |
| A process or new machine to risk-assess | `fmea-builder` |
| A mistake that keeps happening and needs designing out | `mistake-proofing` |
| "Can we hit the volume?" | `capacity-planner` |
| Tier boards that nobody looks at | `daily-management` |

Every skill's folder has worked examples in `resources/examples/` — a full exchange, the deliverable, and the closing block. Read one before your first real run; it's the fastest way to see what "good" looks like.
