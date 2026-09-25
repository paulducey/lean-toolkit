#!/usr/bin/env python3
"""Thin wrapper: convert this skill's saved Markdown deliverable to .docx via the shared scripts/md_to_docx.py."""
import pathlib, runpy, sys
shared = pathlib.Path(__file__).resolve().parents[3] / "scripts" / "md_to_docx.py"
sys.argv = [str(shared)] + sys.argv[1:]
runpy.run_path(str(shared), run_name="__main__")
