---
name: sales-pipeline
description: 'End-to-end pipeline automation from anonymous website visitor to closed deal. Use when: score this lead, enrich [company name], check suppression for [email], show stalled deals, train deal scoring model, who changed jobs this week?.'
---

# Sales Pipeline

End-to-end pipeline automation from anonymous website visitor to closed deal. Combines multi-channel intent scoring across email, LinkedIn, and call signals with AI-powered lead enrichment and predictive deal scoring using logistic regression on your historical win/loss data.

## When to Use
- Score this lead
- Enrich [company name]
- Check suppression for [email]
- Show stalled deals
- Train deal scoring model
- Who changed jobs this week?
- Update ICP weights

## Workflow
1. **Visitor Identification** -- capture anonymous visitors via reverse IP lookup or pixel tracking
2. **Intent Scoring** -- calculate composite score from all available signals
3. **Enrichment** -- pull firmographic + technographic data via API
4. **Suppression Check** -- run through 7-layer cascade
5. **ICP Match** -- score against ideal customer profile (industry, size, tech stack, geography)
6. **Route Decision** -- high intent (>70) to sales, medium (40-70) to nurture, low (<40) to marketing
7. **Sequence Enrollment** -- auto-enroll in appropriate outreach sequence
8. **Deal Monitoring** -- track velocity, engagement, champion movement
9. **Predictive Scoring** -- update win probability weekly as deal progresses
10. **ICP Feedback Loop** -- monthly analysis of what converted vs what didn't

## Reference
Full methodology lives in [README.md](README.md) in this folder: configuration, scoring formulas, output formats, integration points, and worked examples. Read it before producing scored output.
