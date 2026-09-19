---
name: voice-guard
description: 'Quality gate for marketing copy. Use when: check this copy for ai tone, voice check this landing page, does this email sound human?, score this draft before we ship it, clean up the hype in this post, run voice guard on [file].'
---

# Voice Guard

Quality gate for marketing copy. Scores a draft for machine-sounding writing (filler openers, hype vocabulary, hedging, em-dash overuse, reflexive three-item lists, and flat sentence rhythm) and points at the exact phrases to fix. Run it on anything another skill generates before it ships.

## When to Use
- Check this copy for AI tone
- Voice check this landing page
- Does this email sound human?
- Score this draft before we ship it
- Clean up the hype in this post
- Run voice guard on [file]

## Workflow
1. **Collect the draft** -- paste copy or point at a file produced by another skill
2. **Score** -- run `python_runtime.voice.check_voice(text)`
3. **Triage** -- group findings by kind; fix filler and hype first (largest penalties)
4. **Rewrite** -- replace flagged phrases with concrete claims: numbers, named outcomes, specific users
5. **Re-score** -- repeat until the band is `ship` (85+)
6. **Log** -- keep the before/after scores with the asset so reviewers see what changed

## Reference
Full methodology lives in [README.md](README.md) in this folder: configuration, scoring formulas, output formats, integration points, and worked examples. Read it before producing scored output.
