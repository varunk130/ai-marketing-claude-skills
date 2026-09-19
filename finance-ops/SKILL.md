---
name: finance-ops
description: 'Marketing finance and unit economics system that goes beyond basic P&L analysis. Use when: calculate ltv by cohort, show cac by channel, what’s our magic number?, payback period for [channel], optimize marketing budget, run scenario analysis.'
---

# Finance Ops

Marketing finance and unit economics system that goes beyond basic P&L analysis. Builds cohort-based LTV/CAC models, channel-level unit economics, SaaS magic number tracking, payback period calculators, and scenario modeling with sensitivity analysis.

## When to Use
- Calculate LTV by cohort
- Show CAC by channel
- What's our magic number?
- Payback period for [channel]
- Optimize marketing budget
- Run scenario analysis
- How much runway do we have?
- Monthly finance report

## Workflow
1. **Data Ingestion** -- import financials (QuickBooks, Stripe, ChartMogul) and marketing spend (ad platforms, CRM)
2. **Cohort Construction** -- group customers by acquisition month and channel
3. **LTV Calculation** -- plot retention curves, calculate cumulative revenue per cohort over time
4. **CAC Calculation** -- total channel spend / customers acquired per channel per month
5. **Unit Economics Dashboard** -- LTV:CAC ratio, payback period, magic number per channel
6. **Budget Optimization** -- recommend budget reallocation based on channel performance
7. **Scenario Modeling** -- generate base/bull/bear projections with variable sensitivity
8. **Burn Rate Analysis** -- current runway, breakeven projection, self-funding timeline
9. **Monthly Report** -- executive summary with health indicators and recommendations
10. **Quarterly Deep Dive** -- cohort comparisons, channel mix evolution, trend analysis

## Reference
Full methodology lives in [README.md](README.md) in this folder: configuration, scoring formulas, output formats, integration points, and worked examples. Read it before producing scored output.
