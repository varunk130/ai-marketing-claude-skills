# Sales Pipeline

End-to-end pipeline automation from anonymous website visitor to closed deal. Combines multi-channel intent scoring across email, LinkedIn, and call signals with AI-powered lead enrichment and predictive deal scoring using logistic regression on your historical win/loss data.

## Key Capabilities

- **Multi-Channel Intent Scoring** -- composite score (0-100) combining website behavior (page depth, pricing page visits, return frequency), email engagement (opens, clicks, replies), LinkedIn activity (profile views, post engagement), and call signals (inbound requests, demo bookings)
- **AI Lead Enrichment Pipeline** -- auto-enriches leads via Clay, Apollo, or Clearbit. Pulls firmographics (revenue, headcount, funding), technographics (tech stack), and contact data (title, seniority, department)
- **Predictive Deal Scoring** -- logistic regression model trained on your closed-won/closed-lost deals. Features: deal size, sales cycle length, number of stakeholders, competitor mentions, engagement velocity. Outputs win probability (0-100%)
- **7-Layer Suppression Cascade** -- prevents wasted outreach: existing customer check, active deal check, recent outreach check, do-not-contact list, competitor employee filter, bounced email filter, unsubscribe check
- **Champion Tracking** -- monitors key contacts via LinkedIn. When a champion leaves their company, alerts you with their new role and company for re-engagement
- **Deal Velocity Alerts** -- flags deals that stall beyond stage-specific thresholds (e.g., Discovery > 14 days, Proposal > 7 days)
- **ICP Auto-Learning** -- analyzes patterns in approved vs rejected leads monthly. Adjusts ICP weights based on actual conversion data

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

## Activation Triggers

- "Score this lead"
- "Enrich [company name]"
- "Check suppression for [email]"
- "Show stalled deals"
- "Train deal scoring model"
- "Who changed jobs this week?"
- "Update ICP weights"

## Configuration

```
ENRICHMENT_PROVIDER=clay            # clay | apollo | clearbit
CRM_PROVIDER=hubspot               # hubspot | salesforce | pipedrive
INTENT_WEIGHTS_WEBSITE=0.35
INTENT_WEIGHTS_EMAIL=0.25
INTENT_WEIGHTS_LINKEDIN=0.25
INTENT_WEIGHTS_CALLS=0.15
HIGH_INTENT_THRESHOLD=70
MEDIUM_INTENT_THRESHOLD=40
DEAL_VELOCITY_DISCOVERY_DAYS=14
DEAL_VELOCITY_PROPOSAL_DAYS=7
DEAL_VELOCITY_NEGOTIATION_DAYS=10
CHAMPION_TRACKING_ENABLED=true
ICP_LEARNING_CADENCE=monthly
```

## Scoring Methodology

### Intent Score (0-100)
```
Intent = (Website * 0.35) + (Email * 0.25) + (LinkedIn * 0.25) + (Calls * 0.15)

Website signals: pricing page (30pts), case studies (15pts), docs (10pts), return visit (15pts), 3+ pages (10pts)
Email signals: opened 3+ (20pts), clicked CTA (30pts), replied (40pts), forwarded (10pts)
LinkedIn signals: viewed profile (15pts), liked post (10pts), commented (25pts), connected (20pts), messaged (30pts)
Call signals: inbound call (40pts), demo booked (50pts), referred by customer (10pts)
```

### Predictive Deal Score
- Model: L2-regularized logistic regression
- Features: deal_size, cycle_days, stakeholder_count, competitor_mentioned, engagement_velocity, industry_match, champion_seniority
- Training: retrained monthly on last 12 months of closed deals
- Output: win probability 0-100% with feature importance breakdown

## Output Formats

- **Lead Scorecard** -- enriched profile with intent score, ICP match, recommended action
- **Pipeline Dashboard** -- deals by stage with velocity indicators (green/yellow/red)
- **Champion Alert** -- markdown notification with old role, new role, recommended outreach
- **ICP Drift Report** -- monthly comparison of ICP vs actual conversions with weight adjustments
- **Deal Forecast** -- probability-weighted pipeline value by close date

## Integration Points

- HubSpot / Salesforce / Pipedrive (CRM)
- Clay / Apollo / Clearbit (enrichment)
- Instantly / Smartlead / Lemlist (sequences)
- LinkedIn Sales Navigator (champion tracking)
- Slack (alerts and digests)
- PostgreSQL (historical deal data)

## Example Usage

```
> "Score this lead from Acme Corp and check ICP match"
> "Show all stalled deals past discovery stage"
> "Enrich the Q2 lead list with firmographic data via Clay"
```

## Prerequisites

- CRM with deal data (HubSpot, Salesforce, or Pipedrive)
- Lead enrichment API key (Clay, Apollo, or Clearbit)
- Minimum 30 closed deals for predictive model training
