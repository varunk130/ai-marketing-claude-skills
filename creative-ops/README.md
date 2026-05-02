# Creative Ops

LinkedIn ad creative testing and iteration engine. Closes the loop performance marketers burn the most cycles on: generating fresh creative variants across multiple angles, structuring statistically valid A/B tests against realistic audience sizes, and learning from results so the *next* iteration is sharper than the last — not just different.

Pairs naturally with **Sales Pipeline** (audience signals from intent scoring) and **Revenue Intelligence** (which messaging wins deals downstream).

## Key Capabilities

- **3-Angle Variant Generation** — every brief produces 6 creative variants across 3 distinct strategic angles (Problem/Solution, Social Proof, Contrarian). No "10 variations of the same headline" trap.
- **Audience-Aware Sample Sizing** — minimum detectable effect (MDE) is computed against the *actual* LinkedIn audience size you provide, with realistic CTR baselines per industry. Flags tests that need a wider audience or a larger MDE before launch.
- **Multi-Layer A/B Structure** — separates *creative* tests (visual + copy) from *targeting* tests (audience + placement). Prevents the most common LinkedIn mistake: changing both at once and learning nothing.
- **Significance Threshold Calculator** — picks the right alpha and stopping rule for the audience size. Smaller audiences (<5k impressions/wk) get sequential testing with O'Brien-Fleming boundaries; larger audiences get fixed-horizon Bayesian.
- **Post-Test Diagnostic** — not just "winner / loser" but *why*: which angle won, which segment drove the lift, and which insight should propagate to the next test.
- **Creative Decay Watcher** — tracks CTR / CPL drift on running ads and flags when creative fatigue starts (typically 3–4× frequency on LinkedIn) so refresh cycles aren't reactive.
- **Pre-Mortem on the Brief** — surfaces the 3 most likely reasons the test will fail to declare a winner, *before* spend starts.

## Workflow

1. **Brief Intake** — target audience description, value prop, optional current best-performing creative, audience size estimate, weekly budget
2. **3-Angle Variant Generation** — produce 6 creatives:
   - 2 × Problem/Solution (lead with pain → product as resolution)
   - 2 × Social Proof (lead with customer outcome → product as the cause)
   - 2 × Contrarian (challenge conventional wisdom → product as the new way)
   Each variant includes: headline, intro line (first 150 chars), CTA, visual brief, and the *single hypothesis* it tests
3. **Test Structure Design**:
   - Map each variant to a budget split (typically equal allocation unless a control needs protection)
   - Compute MDE for the audience size at 80% power, α = 0.05
   - Pick stopping rule (Sequential / Bayesian / Fixed Horizon) based on weekly impressions
4. **Pre-Mortem** — list the top 3 failure modes with mitigations (e.g., "Audience too narrow → MDE > 30% → relax interest filters or extend test 2 weeks")
5. **Live Monitoring Plan** — daily KPIs to watch (CTR, CPL, frequency), early-stop triggers, and which variant gets cut first if budget reallocation is needed
6. **Post-Test Diagnostic**:
   - Winning variant + statistical confidence (posterior probability if Bayesian, p-value if frequentist)
   - Angle-level signal: did one of the 3 strategic angles dominate? If yes, that's a *learning*, not just a win
   - Segment cuts: did the win hold across job titles / company sizes, or was it driven by one segment?
   - Next-iteration recommendation: which winning element to lock in and which dimension to test next
7. **Promote to Playbook** — winning creative + full context archived so future iterations build on prior learnings instead of starting from scratch

## Activation Triggers

- "Test new creative for [audience]"
- "Generate LinkedIn ad variants for [campaign]"
- "Design an A/B test for our [value prop] ads"
- "Why did our last LinkedIn test fail to declare a winner?"
- "Refresh ads — we're seeing creative fatigue"
- "Score our LinkedIn ad performance"

## Default Frameworks

| Framework | Used When |
|-----------|-----------|
| **3-Angle Variant Generation** | Every brief — guarantees strategic diversity, not just copy variation |
| **Sequential Testing (O'Brien-Fleming)** | Audience < 5k weekly impressions; allows early stopping without inflating false positives |
| **Bayesian (Beta-Binomial)** | Audience ≥ 5k weekly impressions; reports posterior probability of winner |
| **Fixed-Horizon Frequentist** | Pre-committed test windows for stakeholder reporting |
| **CUPED Variance Reduction** | When historical CTR data is available for the audience |

## Sample Size Heuristics (LinkedIn-Specific)

These are the defaults the skill applies before any audience-specific adjustment:

| Audience Size (weekly impressions) | Min MDE Detectable | Test Duration |
|-----------------------------------:|-------------------:|---------------|
| < 2,000 | 50% (very large lifts only) | 4+ weeks, Sequential |
| 2,000–5,000 | 30% | 3 weeks, Sequential |
| 5,000–20,000 | 15–20% | 2 weeks, Bayesian |
| 20,000–100,000 | 8–12% | 1–2 weeks, Bayesian |
| > 100,000 | 5% | 1 week, Fixed Horizon |

The skill always produces an *audience-specific* MDE based on actual baseline CTR — these defaults are the floor.

## Output Structure

Each brief produces:

1. **Test Card** (one-page summary): hypothesis, audience, variants, budget split, stopping rule, MDE, pre-mortem
2. **Creative Briefs** (one per variant): headline, intro line, CTA, visual brief, hypothesis, kill criteria
3. **Monitoring Dashboard Spec**: KPIs, daily check-in cadence, early-stop triggers
4. **Post-Test Report Template**: pre-filled with the winners-and-learnings structure so post-mortems aren't ad-hoc

## Pairs With

- **Sales Pipeline** — feed intent-scored audiences into LinkedIn Matched Audiences for higher-precision targeting
- **Conversion** — landing-page CRO audit ensures the post-click experience matches the ad promise
- **Revenue Intelligence** — closed-won data feeds back into "which messaging actually moved deals" so creative learning loops connect to revenue, not just CTR
