# Finance Ops

Marketing finance and unit economics system that goes beyond basic P&L analysis. Builds cohort-based LTV/CAC models, channel-level unit economics, SaaS magic number tracking, payback period calculators, and scenario modeling with sensitivity analysis.

## Key Capabilities

- **Cohort LTV/CAC Modeling** -- tracks customer lifetime value by acquisition cohort (month, channel, campaign). Plots retention curves, calculates cumulative LTV at 3/6/12/24 months, and compares against acquisition cost per cohort. Identifies which cohorts are profitable and when
- **Channel Unit Economics** -- breaks down CAC, LTV, and payback period per acquisition channel (paid search, paid social, organic, referral, outbound, partnerships). Shows which channels produce the highest-quality customers, not just the cheapest leads
- **SaaS Magic Number Tracking** -- calculates: Magic Number = (QoQ ARR growth) / (prior quarter S&M spend). Benchmarks: >0.75 = efficient, invest more. 0.5-0.75 = moderate, optimize. <0.5 = inefficient, fix unit economics before scaling
- **Payback Period Calculator** -- months to recover CAC per channel: Payback = CAC / (ARPU * Gross Margin). Segments by plan tier, annual vs monthly billing, and expansion revenue. Target: <12 months for venture-backed, <18 months for bootstrapped
- **Marketing Budget Allocator** -- given a total budget, allocates across channels using historical CAC and LTV data. Optimizes for: maximum new customers (volume), maximum LTV (quality), or minimum payback (efficiency)
- **Burn Rate & Runway** -- calculates monthly burn rate, months of runway, and breakeven timeline. Projects when marketing spend becomes self-funding based on revenue growth rate
- **Scenario Modeling** -- base/bull/bear projections for revenue, CAC, and LTV. Sensitivity analysis: what happens to payback if CAC increases 20%? If churn drops 2%? If ARPU grows 15%?

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

## Activation Triggers

- "Calculate LTV by cohort"
- "Show CAC by channel"
- "What's our magic number?"
- "Payback period for [channel]"
- "Optimize marketing budget"
- "Run scenario analysis"
- "How much runway do we have?"
- "Monthly finance report"

## Configuration

```
REVENUE_SOURCE=stripe               # stripe | chartmogul | quickbooks | csv
AD_SPEND_SOURCES=["google_ads","meta_ads","linkedin_ads"]
CRM_SOURCE=hubspot                  # hubspot | salesforce | csv
CURRENCY=USD
GROSS_MARGIN=0.80                   # 80% typical for SaaS
COHORT_LOOKBACK_MONTHS=24
LTV_PROJECTION_MONTHS=36
PAYBACK_TARGET_MONTHS=12
MAGIC_NUMBER_TARGET=0.75
LTV_CAC_RATIO_TARGET=3.0
BUDGET_OPTIMIZATION_MODE=quality    # volume | quality | efficiency
SCENARIO_BULL_MULTIPLIER=1.30
SCENARIO_BEAR_MULTIPLIER=0.70
```

## Scoring Methodology

### Channel Health Score (0-100)
| Metric | Weight | Green | Yellow | Red |
|--------|--------|-------|--------|-----|
| LTV:CAC Ratio | 30% | >3.0 | 1.5-3.0 | <1.5 |
| Payback Period | 25% | <12mo | 12-18mo | >18mo |
| CAC Trend (3mo) | 15% | Decreasing | Stable | Increasing |
| Retention Rate | 15% | >90% | 80-90% | <80% |
| Expansion Revenue | 15% | >20% of LTV | 10-20% | <10% |

### SaaS Magic Number
```
Magic Number = (Current Quarter ARR - Previous Quarter ARR) / Previous Quarter S&M Spend

Interpretation:
> 1.0  = Exceptional -- scale aggressively
0.75-1.0 = Strong -- increase spend
0.50-0.75 = Moderate -- optimize channels, then scale
0.25-0.50 = Weak -- fix unit economics before spending more
< 0.25 = Critical -- investigate churn, product-market fit
```

### LTV Calculation
```
Simple LTV = ARPU * Gross_Margin * (1 / Monthly_Churn_Rate)
Cohort LTV = sum(monthly_revenue_per_surviving_customer) over observation window
Projected LTV = Cohort LTV + (remaining_customers * projected_monthly_ARPU * months_remaining)
```

### Budget Allocation Model
```
Per-channel allocation = total_budget * channel_weight
channel_weight = normalize(channel_score)
channel_score = (LTV_CAC_ratio * 0.40) + (1/payback_months * 0.30) + (volume_capacity * 0.30)
Constraint: no single channel > 40% of total budget (diversification)
```

## Output Formats

- **Unit Economics Dashboard** -- per-channel LTV, CAC, payback, magic number with traffic light indicators
- **Cohort Analysis** -- retention curves, cumulative LTV heatmap by acquisition month
- **Budget Recommendation** -- current vs recommended allocation with projected impact
- **Scenario Report** -- base/bull/bear projections with sensitivity tornado chart
- **Burn Rate Summary** -- monthly burn, runway months, breakeven date, self-funding date
- **Executive Finance Brief** -- 1-page summary with 3 key takeaways and recommended actions

## Integration Points

- Stripe / ChartMogul / Baremetrics (revenue and subscription data)
- QuickBooks / Xero (expense data, P&L)
- Google Ads / Meta Ads / LinkedIn Ads (spend data)
- HubSpot / Salesforce (deal and customer acquisition data)
- Google Sheets (manual data import/export)
- Slack (monthly digest, burn rate alerts)

## Example Usage

```
> "Calculate LTV by cohort for the last 12 months"
> "Show CAC and payback period by acquisition channel"
> "Run a scenario analysis — what if churn drops 2% and ARPU grows 15%?"
```
