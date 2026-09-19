---
name: content-ops
description: 'Content quality assurance system that combines expert panel evaluation with automated readability analysis, originality detection, content decay monitoring, and auto-refresh scheduling. Use when: score this content, run readability check on [url/text], check for content decay, generate refresh calendar, extract atoms from [content], run expert panel on [draft].'
---

# Content Ops

Content quality assurance system that combines expert panel evaluation with automated readability analysis, originality detection, content decay monitoring, and auto-refresh scheduling. Ensures every piece of content meets publishing standards before going live and stays fresh after publishing.

## When to Use
- Score this content
- Run readability check on [URL/text]
- Check for content decay
- Generate refresh calendar
- Extract atoms from [content]
- Run expert panel on [draft]
- Check brand voice consistency

## Workflow
1. **Ingest Content** -- accept draft from any format (Google Doc, markdown, Notion, raw text)
2. **Readability Scan** -- calculate Flesch-Kincaid + Dale-Chall scores, flag structural issues
3. **Originality Check** -- compare against published content library for overlap
4. **AI Detection Pass** -- scan for AI-generated content patterns, flag for humanization
5. **Brand Voice Check** -- score against voice fingerprint, highlight deviations
6. **Expert Panel Review** -- route to relevant evaluators based on content type and channel
7. **Iterative Scoring** -- panel scores, identifies top 3 weaknesses, content is revised, re-scored
8. **Publishing Gate** -- requires readability pass + originality pass + voice pass + panel score >= 90
9. **Post-Publish Monitoring** -- track performance weekly, flag decay signals monthly
10. **Refresh Queue** -- prioritized backlog of content needing updates, sorted by traffic impact

## Reference
Full methodology lives in [README.md](README.md) in this folder: configuration, scoring formulas, output formats, integration points, and worked examples. Read it before producing scored output.
