# Revenue Intelligence

Sales intelligence system that transforms call recordings, deal data, and content performance into actionable insights. Combines win/loss pattern recognition, auto-generated competitive battlecards, champion tracking across job changes, and pricing sensitivity analysis.

## Key Capabilities

- **Win/Loss Pattern Recognition** -- analyzes closed-won vs closed-lost deals to identify statistically significant patterns. Surfaces: which industries convert best, which objections kill deals, optimal deal sizes, critical stakeholder roles, and timing patterns (day of week, quarter effects)
- **Competitive Battlecard Auto-Generation** -- monitors competitor mentions in sales calls, reviews, and public content. Auto-generates and updates battlecards with: competitor positioning, pricing intel, feature gaps, win-against talking points, trap-setting questions, and customer proof points
- **Champion Tracking** -- monitors your top advocates (power users, references, internal champions) across LinkedIn. When a champion moves to a new company: alerts sales with new role context, generates personalized re-engagement sequence, adds new company to pipeline as warm lead
- **Pricing Sensitivity Analysis** -- analyzes deal outcomes by price point. Maps: discount frequency by deal stage, win rate vs discount depth, optimal price anchoring ranges, expansion revenue by initial price tier. Identifies the "pricing cliff" (discount level where win rate stops improving)
- **Content Attribution** -- connects content touches to deal outcomes. Maps the buyer journey: which blog posts, case studies, and webinars appear in winning deals? Calculates Content Influence Score per asset: how often it appears in the journey of deals that close
- **Deal Risk Scoring** -- real-time risk assessment for open deals based on: engagement velocity (declining = risk), stakeholder breadth (single-threaded = risk), competitive mention frequency, sales cycle vs benchmark, missing next steps
- **Conversation Intelligence** -- extracts structured data from sales calls: objections raised, buying signals, competitor mentions, pricing discussions, next steps, decision timeline, budget confirmation

## Workflow

1. **Data Ingestion** -- pull call recordings (Gong/Chorus), deal data (CRM), content analytics (GA4)
2. **Call Analysis** -- extract objections, signals, competitors, pricing from transcripts
3. **Win/Loss Classification** -- tag deals with outcome + contributing factors
4. **Pattern Analysis** -- run statistical analysis on win/loss factors (chi-square, logistic regression)
5. **Battlecard Generation** -- compile competitor intel from calls + public sources into structured cards
6. **Champion Monitoring** -- weekly LinkedIn scan for job changes among tracked contacts
7. **Content Mapping** -- link content touches to deal journeys, calculate influence scores
8. **Pricing Analysis** -- map discount patterns to outcomes, identify sensitivity ranges
9. **Risk Scoring** -- score all open deals daily, flag at-risk opportunities
10. **Weekly Intelligence Brief** -- synthesize insights for sales leadership

## Activation Triggers

- "Analyze this call transcript"
- "Generate battlecard for [competitor]"
- "Show win/loss patterns"
- "Who changed jobs this week?"
- "Score deal risk for [opportunity]"
- "Which content drives deals?"
- "Pricing sensitivity report"
- "Weekly intelligence brief"

## Configuration

```
CALL_INTELLIGENCE=gong              # gong | chorus | fireflies | local_files
CRM_SOURCE=hubspot                  # hubspot | salesforce | pipedrive
ANALYTICS_SOURCE=ga4                # ga4 | amplitude | mixpanel
CHAMPION_TRACKING_ENABLED=true
CHAMPION_SCAN_CADENCE=weekly
LINKEDIN_API_KEY=xxx
COMPETITOR_LIST=["comp1","comp2","comp3"]
BATTLECARD_UPDATE_CADENCE=weekly
DEAL_RISK_SCAN_CADENCE=daily
PRICING_CLIFF_SENSITIVITY=0.05      # 5% win rate change threshold
WIN_LOSS_MIN_SAMPLE=30              # minimum deals for statistical significance
CONTENT_ATTRIBUTION_MODEL=linear    # first_touch | last_touch | linear | time_decay
```

## Scoring Methodology

### Deal Risk Score (0-100, higher = more risk)
| Signal | Weight | High Risk | Medium Risk | Low Risk |
|--------|--------|-----------|-------------|----------|
| Engagement Velocity | 25% | Declining 2+ weeks | Flat | Increasing |
| Stakeholder Breadth | 20% | Single contact | 2 contacts | 3+ contacts + executive |
| Competitive Pressure | 15% | Active eval, named competitor | Mentioned once | No competitor |
| Sales Cycle vs Benchmark | 15% | >1.5x average | 1-1.5x | Below average |
| Next Steps Clarity | 15% | No defined next step | Vague timeline | Specific date + action |
| Budget Confirmation | 10% | Unknown | Discussed, not confirmed | Confirmed + approved |

### Content Influence Score (0-100)
```
Influence = (appearance_rate_in_won_deals * 0.50) +
            (avg_recency_before_close * 0.25) +
            (engagement_depth * 0.25)

appearance_rate: % of won deals that touched this content
avg_recency: days before close when content was consumed (closer = higher score)
engagement_depth: time on page, scroll depth, return visits
```

### Win/Loss Pattern Significance
- Method: Chi-square test for categorical factors, logistic regression for continuous
- Minimum sample: 30 deals per segment
- Significance threshold: p < 0.05
- Effect size reporting: odds ratio with 95% confidence interval
- Factors tested: industry, company size, deal size, competitor present, champion seniority, number of stakeholders, sales cycle length, discount depth, content touches

### Pricing Sensitivity
```
Win Rate Curve: plot win_rate vs discount_percentage
Pricing Cliff: point where d(win_rate)/d(discount) < threshold (marginal returns stop)
Optimal Anchor: price point with highest (win_rate * deal_value) product
Discount Bands: 0-10% (standard), 10-20% (negotiated), 20-30% (strategic), >30% (requires VP approval)
```

## Output Formats

- **Win/Loss Report** -- statistically significant patterns with sample sizes and confidence intervals
- **Competitive Battlecard** -- structured card per competitor: positioning, pricing, strengths, weaknesses, trap questions, proof points
- **Champion Alert** -- notification with old/new role, company intel, recommended outreach
- **Deal Risk Dashboard** -- all open deals scored with risk factors highlighted
- **Content Influence Matrix** -- content assets ranked by deal influence with journey maps
- **Pricing Sensitivity Chart** -- win rate curve with cliff point and optimal anchor range
- **Weekly Intelligence Brief** -- top 5 insights for sales leadership with recommended actions

## Integration Points

- Gong / Chorus / Fireflies (call intelligence)
- HubSpot / Salesforce (CRM deal data)
- Google Analytics 4 (content engagement)
- LinkedIn Sales Navigator (champion tracking)
- G2 / Capterra (competitor review monitoring)
- Slack (alerts, weekly brief delivery)
- Google Sheets (manual data supplements)

## Example Usage

```
> "Generate a battlecard for Competitor X based on last quarter's calls"
> "Show win/loss patterns for enterprise deals over 50K"
> "Which champions changed jobs this week? Draft re-engagement outreach"
```

## Prerequisites

- Call intelligence platform (Gong, Chorus, or call transcripts)
- CRM with win/loss tagged deals (minimum 30 per segment)
- Competitor list for battlecard generation
