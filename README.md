# syncpool

Shared ground for the story videos of **Lumen**, **MIRA** and **Greenforest** (Siemens industrial AI PoCs on the Intel NPU).

Every product has two cuts:

| Cut | Narrator | Rule |
|--|--|--|
| Ecosystem | the NPU, first person | Uses the shared lines in `shared-lines.json` on purpose, so the three videos read as one series, and ends with "With Lumen, I see. With MIRA, I explain. With Greenforest, I look after the machine I live in." |
| Standalone | product-specific voice | Must not contain any shared line, and must not reuse a sentence from another product's standalone cut. |

## Layout

| Path | What it is |
|--|--|
| `shared-lines.json` | The lines the ecosystem cuts share. Change them here first, then in every product. |
| `PHRASES.md` | The same as a table, with which product uses which line. |
| `scripts/<product>-ecosystem.json`, `scripts/<product>-standalone.json` | The current narration of every cut (one list of sentences per scene). |
| `tools/check.py` | `python tools/check.py scripts/<product>-standalone.json` reports shared lines and sentences another standalone cut already uses. |

## Workflow

1. Before writing or changing a script, pull this repo.
2. After changing a script, copy it to `scripts/`, run `tools/check.py` on every standalone script, and push.

Lumen's scripts live in `etJ-sad/Lumen` under `video/` (`script.json` = ecosystem, `script-solo.json` = standalone).
MIRA and Greenforest: please add theirs under `scripts/`.
