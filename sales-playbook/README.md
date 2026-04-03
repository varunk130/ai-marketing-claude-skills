# Sales Playbook

Sales methodology and deal execution system that combines MEDDPICC + BANT hybrid discovery frameworks, mutual action plans, ROI calculators with industry benchmarks, competitive displacement playbooks, and value-based pricing strategies.

## Key Capabilities

- **MEDDPICC + BANT Hybrid Discovery** -- structured discovery framework that maps every deal against qualification criteria: Metrics (quantified pain), Economic Buyer (budget authority identified), Decision Process (steps mapped), Decision Criteria (evaluation factors known), Paper Process (procurement requirements), Implicate Pain (consequences of inaction), Champion (internal advocate activated), Competition (alternatives mapped). Plus BANT overlay: Budget confirmed, Authority verified, Need validated, Timeline established. Generates a Deal Qualification Score (0-100)
- **Mutual Action Plans** -- auto-generates a shared timeline between you and the prospect. Maps every step from discovery to signed contract: technical evaluation, stakeholder demos, security review, legal review, procurement, implementation planning. Each step has: owner, deadline, dependency, and completion criteria. Exports as shareable document
- **ROI Calculator with Industry Benchmarks** -- builds prospect-specific ROI models using: their current metrics (manual input or enrichment), your product's impact data (from closed-won case studies), and industry benchmarks (by vertical and company size). Outputs: projected savings, revenue impact, payback period, 3-year NPV. Formats as a shareable PDF or interactive calculator
- **Competitive Displacement Playbook** -- structured approach for ripping out an incumbent. Phases: 1) Identify dissatisfaction triggers, 2) Quantify switching cost vs staying cost, 3) Build migration timeline, 4) Address risk objections, 5) Reference similar displacement wins. Includes trap questions to expose competitor weaknesses without badmouthing
- **Objection Handling Library** -- categorized objection responses: Price (too expensive, no budget, cheaper alternative), Timing (not now, next quarter, renewing with current), Authority (need to check with boss, committee decision), Need (we already have something, not a priority), Trust (too small/new, bad reviews, security concerns). Each objection has: acknowledge, reframe, evidence, bridge-to-value
- **Proposal Generator** -- creates tiered proposals with value-based pricing: Tier 1 (Starter), Tier 2 (Growth), Tier 3 (Scale), Tier 4 (Enterprise). Each tier: scope, deliverables, timeline, price, ROI projection. Anchors with highest tier first
- **Post-Call Analyzer** -- scores call transcripts against discovery framework completion. Identifies: qualification gaps (what you didn't ask), buying signals (what to follow up on), next steps (agreed vs implied), risk factors (hesitation, competitor mentions)

## Workflow

1. **Deal Qualification** -- run MEDDPICC + BANT assessment, generate qualification score
2. **Discovery Prep** -- generate question framework based on prospect industry and deal stage
3. **Discovery Call** -- guide conversation through qualification criteria with real-time checklist
4. **Post-Call Analysis** -- score transcript against framework, identify gaps and signals
5. **ROI Model** -- build prospect-specific ROI calculator with industry benchmarks
6. **Mutual Action Plan** -- generate shared timeline with all milestones to close
7. **Competitive Strategy** -- if competitor identified, activate displacement playbook
8. **Proposal Creation** -- tiered proposal with value-based pricing and ROI justification
9. **Objection Prep** -- pre-load likely objections with prepared responses
10. **Deal Review** -- weekly pipeline review with qualification scores and risk flags

## Activation Triggers

- "Qualify this deal"
- "Generate discovery questions for [industry]"
- "Analyze this call"
- "Build ROI model for [prospect]"
- "Create mutual action plan"
- "Displacement playbook for [competitor]"
- "Generate proposal for [prospect]"
- "Prep for objections"
- "Deal review for this week"

## Configuration

```
CRM_SOURCE=hubspot                  # hubspot | salesforce | pipedrive
CALL_INTELLIGENCE=gong              # gong | chorus | fireflies | manual
INDUSTRY_BENCHMARKS_PATH=~/.sales-playbook/benchmarks/
CASE_STUDY_PATH=~/.sales-playbook/case-studies/
COMPETITOR_PLAYBOOKS_PATH=~/.sales-playbook/competitors/
QUALIFICATION_THRESHOLD=60          # minimum score to advance deal
PROPOSAL_TIERS=4
PRICING_ANCHOR_MULTIPLIER=1.50      # top tier = 1.5x base
ROI_PROJECTION_YEARS=3
DISCOUNT_APPROVAL_THRESHOLDS=[10,20,30]  # %, requires manager/VP/C-level
MAP_DEFAULT_STEPS=12                # typical mutual action plan steps
OBJECTION_LIBRARY_PATH=~/.sales-playbook/objections/
```

## Scoring Methodology

### Deal Qualification Score (0-100)
| Criteria | Weight | Complete (10) | Partial (5) | Missing (0) |
|----------|--------|--------------|-------------|-------------|
| Metrics | 15% | Quantified pain with numbers | Pain identified, not quantified | No pain articulated |
| Economic Buyer | 15% | Met and engaged | Identified, not met | Unknown |
| Decision Process | 10% | Steps mapped with timeline | General understanding | Unknown |
| Decision Criteria | 10% | Documented evaluation factors | Some criteria known | Unknown |
| Paper Process | 5% | Procurement steps known | General timeline | Unknown |
| Implicate Pain | 10% | Cost of inaction calculated | Acknowledged | Not discussed |
| Champion | 15% | Active advocate, coaching you | Supportive contact | No internal ally |
| Competition | 10% | Known, strategy in place | Aware of alternatives | Unknown |
| Budget | 5% | Confirmed and allocated | Discussed | Unknown |
| Timeline | 5% | Specific date with driver | General timeframe | No urgency |

### ROI Model Framework
```
Current State Cost = (manual_hours * hourly_rate) + tool_costs + error_cost + opportunity_cost
Future State Cost = your_product_price + implementation_cost + training_time
Annual Savings = Current_State - Future_State
Revenue Impact = (conversion_improvement * deal_value * deal_volume) + (time_saved * revenue_per_hour)

Payback Period = Total_Investment / Monthly_Savings
3-Year NPV = sum(annual_net_benefit / (1 + discount_rate)^year) - initial_investment
ROI = (3_year_net_benefit - total_investment) / total_investment * 100
```

### Post-Call Score (0-100)
```
Framework Coverage = (criteria_discussed / total_criteria) * 50
Signal Strength = (buying_signals - risk_signals) / max_signals * 25
Next Steps Clarity = (specific_actions_agreed / expected_actions) * 25

Rating:
> 80: Strong call, deal advancing
60-80: Decent, but gaps to fill next call
40-60: Needs significant follow-up
< 40: Deal at risk, requires strategy reset
```

### Competitive Displacement Score
```
Displacement Feasibility = (dissatisfaction_level * 0.35) +
                           (switching_cost_ratio * 0.25) +
                           (reference_similarity * 0.20) +
                           (timeline_alignment * 0.20)

dissatisfaction: confirmed frustration (10), implied (6), satisfied (2)
switching_cost_ratio: staying costs > switching (10), equal (5), switching > staying (2)
reference_similarity: exact same displacement win (10), similar (6), none (2)
timeline_alignment: contract ending soon (10), mid-contract (5), recently renewed (2)
```

## Output Formats

- **Deal Qualification Card** -- MEDDPICC + BANT scorecard with gaps highlighted and next actions
- **Discovery Question Framework** -- industry-specific questions mapped to each qualification criterion
- **ROI Calculator** -- shareable PDF/HTML with prospect-specific projections and benchmarks
- **Mutual Action Plan** -- shared document with milestones, owners, dates, and dependencies
- **Competitive Battlecard** -- displacement playbook with trap questions and proof points
- **Tiered Proposal** -- multi-tier proposal with scope, pricing, ROI per tier
- **Post-Call Summary** -- transcript analysis with scores, signals, gaps, and recommended next steps
- **Weekly Deal Review** -- pipeline summary with qualification scores, risk flags, and forecast

## Integration Points

- HubSpot / Salesforce / Pipedrive (deal data, pipeline stages)
- Gong / Chorus / Fireflies (call recordings and transcripts)
- PandaDoc / DocuSign (proposal delivery and tracking)
- LinkedIn Sales Navigator (prospect research)
- G2 / Capterra (competitor review intelligence)
- Slack (deal alerts, weekly review notifications)
- Google Sheets (ROI model sharing, benchmark data)

## Example Usage

```
> "Qualify this deal using MEDDPICC + BANT and show the gaps"
> "Build an ROI model for Acme Corp with 3-year NPV projection"
> "Create a competitive displacement playbook for replacing Competitor X"
```
