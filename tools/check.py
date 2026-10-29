"""Checks a standalone script for shared ecosystem lines and for lines another product's standalone cut already uses.

usage: python tools/check.py scripts/<product>-standalone.json
A script is a JSON list of scenes, each a list of sentences (the format of the story-video pipelines).
Exit code 1 when something repeats.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
norm = lambda s: re.sub(r"[^a-z0-9 ]", "", s.lower()).strip()  # noqa: E731


def sentences(path):
    return [s for scene in json.loads(Path(path).read_text(encoding="utf-8")) for s in scene]


target = Path(sys.argv[1]).resolve()
hits = []
shared = [norm(x) for x in json.loads((ROOT / "shared-lines.json").read_text(encoding="utf-8"))["lines"]]
mine = sentences(target)
for s in mine:
    for x in shared:
        if x and x in norm(s):
            hits.append(f"shared line   | {s}")
for other in sorted((ROOT / "scripts").glob("*-standalone.json")):
    if other.resolve() == target:
        continue
    theirs = {norm(s) for s in sentences(other)}
    hits += [f"{other.stem:<14}| {s}" for s in mine if norm(s) in theirs]
print("\n".join(hits) or "no repeats")
sys.exit(1 if hits else 0)
