# Story video phrases: shared vs. Lumen only

The Lumen, MIRA and Greenforest videos each come in two cuts. The **ecosystem** cuts share a narrator (the NPU) and a
set of lines on purpose, so the three videos read as one series. The **standalone** cuts must not use any of them.
Collected on 2026-10-29 from the subtitles of `lumen-story-ecosystem.mp4`, `MIRA_Storyvideo_templte.mp4` and
`greenforest-npu-story.mp4`.

## Shared lines (ecosystem cuts only)

| Line | Lumen | MIRA | Greenforest |
|--|:-:|:-:|:-:|
| Every new industrial PC has three processors. You know two of them. | ✓ | ✓ | ✓ |
| The CPU runs the machine. The GPU draws the screen. | ✓ | ✓ | ✓ |
| … That's me. The NPU. | ✓ | ✓ | ✓ |
| Chapter title "01 The third processor" | ✓ | ✓ | ✓ |
| But don't take my word for it. | ✓ | ✓ | ✓ |
| (Every model is) compiled for me explicitly. No (automatic) fallback. | ✓ | ✓ | ✓ |
| OpenVINO says / Lumen asks OpenVINO where it really ran: NPU. Checked against the CPU. | ✓ | | ✓ |
| The CPU stays free for the machine. | ✓ | ✓ | ✓ |
| So we pushed it / asked … All on me. | ✓ | ✓ | ✓ |
| Then the result / the health goes to the machine. OPC UA … MQTT and REST … | ✓ | | ✓ |
| No cloud. No telemetry. The images / manuals / health data never leave the factory. | ✓ | ✓ | ✓ |
| Every new industrial PC already has me. | ✓ | ✓ | ✓ |
| With Lumen, I see. With MIRA, I explain. With Greenforest, I look after the machine I live in. | ✓ | ✓ | ✓ |

## Lumen standalone cut (`script-solo.json`)

Different voice (`af_bella`), third-person narrator, own chapters ("One bent pin", "Lumen", "Where it runs",
"At the line"). It opens with "Sixty parts a minute. Eight hours a shift." and ends with "Lumen. See every part."
None of the shared lines above appear in it; check new standalone scripts of MIRA and Greenforest against this table
and against `script-solo.json` so the three standalone cuts do not borrow from each other either.

## Greenforest standalone cut (`scripts/greenforest-standalone.json`)

Neutral third-person narrator that speaks to the maintenance engineer ("you"), no NPU narrator and no "I am …"/"… was
born" pattern. Own chapters: "A quiet fault", "Greenforest", "Reading the PC", "The proof", "On the plant network",
"Next". It opens with "Line three, Tuesday night." and ends with "Greenforest. An industrial PC that tells you how it
is doing. Before the line stops. Stay green." `tools/check.py` prints "no repeats" for it.

The Greenforest ecosystem cut (`scripts/greenforest-ecosystem.json`) uses every shared line word for word, including
"OpenVINO says where it really ran: NPU."

## MIRA standalone cut (`MIRA/video/script-solo.json`, here `scripts/mira-standalone.json`)

Different voice (`bf_emma`, British), third-person narrator, own chapters ("Two forty-seven", "MIRA", "Under the hood",
"On site"). It opens with "Two forty-seven in the morning. Line three goes quiet." and ends with "MIRA. Answers from your
own manuals." Kept from the ecosystem cut because they are MIRA's own: the 2:47 stop, E-417, the manual with hundreds of
pages, "Every statement points to its source", "I don't know" when the documents have nothing. Measured numbers stay as
`{placeholders}` here (they change with every run); conditional lines are listed with both branches.
