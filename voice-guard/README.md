# Voice Guard

Quality gate for marketing copy. Scores a draft for machine-sounding writing (filler openers, hype vocabulary, hedging, em-dash overuse, reflexive three-item lists, and flat sentence rhythm) and points at the exact phrases to fix. Run it on anything another skill generates before it ships.

## Key Capabilities

- **Voice Score (0-100)** -- starts at 100 and subtracts a fixed penalty per finding, so the number is explainable line by line
- **Pinpointed findings** -- every finding quotes the original text, not a paraphrase
- **Rhythm check** -- flags copy whose sentences are all about the same length (spread under 15% of the mean), a common tell of generated text
- **Ship / revise / rewrite band** -- one call for the reviewer instead of a wall of warnings
- **Deterministic** -- same input, same score; no model call needed for the check itself

## Workflow

1. **Collect the draft** -- paste copy or point at a file produced by another skill
2. **Score** -- run `python_runtime.voice.check_voice(text)`
3. **Triage** -- group findings by kind; fix filler and hype first (largest penalties)
4. **Rewrite** -- replace flagged phrases with concrete claims: numbers, named outcomes, specific users
5. **Re-score** -- repeat until the band is `ship` (85+)
6. **Log** -- keep the before/after scores with the asset so reviewers see what changed

## Activation Triggers

- "Check this copy for AI tone"
- "Voice check this landing page"
- "Does this email sound human?"
- "Score this draft before we ship it"
- "Clean up the hype in this post"
- "Run voice guard on [file]"

## Scoring Methodology

| Finding | Penalty | Example |
| --- | --- | --- |
| Filler opener | 8 | "In today's fast-paced world" |
| Uniform rhythm | 10 | four or more sentences of near-identical length |
| Hype word | 5 | "revolutionary", "seamless", "unlock" |
| Em-dash overuse | 4 | more than one per 60 words |
| Reflexive triplet | 4 | "fast, simple, and powerful" |
| Hedge | 3 | "arguably", "potentially" |

`score = max(0, 100 - sum(penalties))` → **ship** ≥ 85, **revise** 60–84, **rewrite** < 60.

## Output Formats

```json
{"score": 72, "band": "revise", "findings": [{"kind": "hype", "match": "seamless"}]}
```

## Integration Points

- **content-ops**, **outbound-engine**, **creative-ops** -- run Voice Guard on every generated asset before handoff
- CI -- call `check_voice` in a test to fail builds when published copy drops below `ship`

## Example Usage

```python
from python_runtime.voice import check_voice

report = check_voice(open("landing-hero.md").read())
print(report.score, report.band)
for f in report.findings:
    print(f"{f['kind']}: {f['match']}")
```
