---
name: creative-ops
description: 'LinkedIn ad creative testing and iteration engine. Use when: test new creative for [audience], generate linkedin ad variants for [campaign], design an a/b test for our [value prop] ads, why did our last linkedin test fail to declare a winner?, refresh ads - we’re seeing creative fatigue, score our linkedin ad performance.'
---

# Creative Ops

LinkedIn ad creative testing and iteration engine. Closes the loop performance marketers burn the most cycles on: generating fresh creative variants across multiple angles, structuring statistically valid A/B tests against realistic audience sizes, and learning from results so the *next* iteration is sharper than the last - not just different. Pairs naturally with **Sales Pipeline** (audience signals from intent scoring) and **Revenue Intelligence** (which messaging wins deals downstream).

## When to Use
- Test new creative for [audience]
- Generate LinkedIn ad variants for [campaign]
- Design an A/B test for our [value prop] ads
- Why did our last LinkedIn test fail to declare a winner?
- Refresh ads - we're seeing creative fatigue
- Score our LinkedIn ad performance

## Workflow
1. **Brief Intake** - target audience description, value prop, optional current best-performing creative, audience size estimate, weekly budget
2. **3-Angle Variant Generation** - produce 6 creatives:
   - 2 × Problem/Solution (lead with pain → product as resolution)
   - 2 × Social Proof (lead with customer outcome → product as the cause)
   - 2 × Contrarian (challenge conventional wisdom → product as the new way)
   Each variant includes: headline, intro line (first 150 chars), CTA, visual brief, and the *single hypothesis* it tests
3. **Test Structure Design**:
   - Map each variant to a budget split (typically equal allocation unless a control needs protection)
   - Compute MDE for the audience size at 80% power, α = 0.05
   - Pick stopping rule (Sequential / Bayesian / Fixed Horizon) based on weekly impressions
4. **Pre-Mortem** - list the top 3 failure modes with mitigations (e.g., "Audience too narrow → MDE > 30% → relax interest filters or extend test 2 weeks")
5. **Live Monitoring Plan** - daily KPIs to watch (CTR, CPL, frequency), early-stop triggers, and which variant gets cut first if budget reallocation is needed
6. **Post-Test Diagnostic**:
   - Winning variant + statistical confidence (posterior probability if Bayesian, p-value if frequentist)
   - Angle-level signal: did one of the 3 strategic angles dominate? If yes, that's a *learning*, not just a win
   - Segment cuts: did the win hold across job titles / company sizes, or was it driven by one segment?
   - Next-iteration recommendation: which winning element to lock in and which dimension to test next
7. **Promote to Playbook** - winning creative + full context archived so future iterations build on prior learnings instead of starting from scratch

## Reference
Full methodology lives in [README.md](README.md) in this folder: configuration, scoring formulas, output formats, integration points, and worked examples. Read it before producing scored output.
