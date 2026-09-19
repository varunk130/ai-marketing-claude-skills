---
name: outbound-engine
description: 'Multi-channel outbound campaign system that orchestrates coordinated sequences across email, LinkedIn, and video. Use when: build outbound sequence for [persona], check deliverability for [domain], score this email copy, a/b test these subject lines, show reply classification breakdown, generate warmup schedule for [domain].'
---

# Outbound Engine

Multi-channel outbound campaign system that orchestrates coordinated sequences across email, LinkedIn, and video. Includes deliverability warmup planning, A/B subject line optimization, timezone-aware send scheduling, and expert panel copy scoring.

## When to Use
- Build outbound sequence for [persona]
- Check deliverability for [domain]
- Score this email copy
- A/B test these subject lines
- Show reply classification breakdown
- Generate warmup schedule for [domain]
- Pause outbound to [company]

## Workflow
1. **Infrastructure Audit** -- verify domains, mailboxes, SPF/DKIM/DMARC, warmup status
2. **ICP & List Building** -- define target persona, pull prospects from enrichment tools
3. **Sequence Design** -- map multi-channel touchpoint sequence with timing and personalization tier
4. **Copy Creation** -- draft email templates, LinkedIn messages, video scripts per sequence step
5. **Expert Panel Scoring** -- 10 evaluators score copy. Target: 90/100 or 3 rounds max
6. **Subject Line A/B Setup** -- create 3-5 variants per email step, define test batch size
7. **Warmup Verification** -- confirm all sending domains have completed warmup ramp
8. **Timezone Mapping** -- assign local timezone to each prospect
9. **Launch Sequence** -- activate with human approval gate before first batch
10. **Monitor & Optimize** -- track open/reply/meeting rates, rotate underperforming copy, pause flagged domains

## Reference
Full methodology lives in [README.md](README.md) in this folder: configuration, scoring formulas, output formats, integration points, and worked examples. Read it before producing scored output.
