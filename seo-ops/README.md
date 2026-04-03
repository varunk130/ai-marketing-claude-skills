# SEO Ops

SEO strategy and execution system built for the AI search era. Combines traditional keyword research and competitor gap analysis with Generative Engine Optimization (GEO/AEO), topical authority mapping, content cluster visualization, and SERP feature opportunity scoring.

## Key Capabilities

- **GEO/AEO Optimization** -- optimize content for AI Overviews, ChatGPT, Perplexity, and other generative search engines. Scores content on: citation likelihood (structured claims with sources), entity density (named entities per paragraph), question-answer format coverage, and factual specificity
- **Topical Authority Mapping** -- builds a graph of your site's topical coverage vs the ideal coverage for your niche. Identifies authority gaps (topics competitors cover that you don't) and authority clusters (where you have depth). Calculates Authority Score per topic cluster (0-100)
- **Content Cluster Visualization** -- generates pillar-and-spoke content maps. Each cluster has: 1 pillar page, 5-15 supporting articles, internal linking blueprint. Visualizes as a mermaid diagram with link relationships
- **SERP Feature Opportunity Scoring** -- for each target keyword, identifies which SERP features are available (Featured Snippet, People Also Ask, Knowledge Panel, Image Pack, Video Carousel, Local Pack) and scores your likelihood of winning each based on content format, domain authority, and current rankings
- **Impact x Confidence Matrix** -- 2D keyword scoring. Impact = (volume * CPC * funnel_weight * trend_direction). Confidence = (1 - difficulty/100) * current_rank_proximity * topical_authority. Generates prioritized action list
- **Keyword Cannibalization Detection** -- finds pages competing for the same keywords. Recommends: merge (combine thin pages), redirect (point weaker to stronger), differentiate (adjust targeting)
- **Programmatic SEO Scanner** -- identifies opportunities for templatized page creation at scale. Analyzes: data availability, search demand patterns, competitor programmatic pages, estimated pages needed, template structure

## Workflow

1. **Seed Keywords** -- input core keywords or let the system extract from GSC top queries
2. **Keyword Universe Expansion** -- expand seeds into full keyword map with intent labels (BOFU/MOFU/TOFU)
3. **Impact x Confidence Scoring** -- score and rank all keywords in the universe
4. **SERP Feature Analysis** -- for top 50 keywords, identify winnable SERP features
5. **Topical Authority Audit** -- map current coverage against ideal topical graph
6. **Content Cluster Planning** -- group keywords into pillar-spoke clusters with internal linking maps
7. **GEO/AEO Gap Analysis** -- evaluate existing content for AI search readiness
8. **Cannibalization Check** -- identify keyword overlaps across existing pages
9. **Programmatic SEO Scan** -- detect templatizable page opportunities
10. **Weekly Brief** -- prioritized keyword targets, content assignments, and quick wins

## Activation Triggers

- "Run SEO audit for [domain]"
- "Build content clusters for [topic]"
- "Score keywords for [niche]"
- "Check SERP features for [keyword]"
- "Find cannibalization issues"
- "GEO optimize [URL]"
- "Generate topical authority map"
- "Find programmatic SEO opportunities"

## Configuration

```
GSC_CREDENTIALS_PATH=~/.seo-ops/gsc-creds.json
AHREFS_API_KEY=xxx
SEMRUSH_API_KEY=xxx
DOMAIN=yourdomain.com
COMPETITOR_DOMAINS=["comp1.com","comp2.com","comp3.com"]
FUNNEL_WEIGHTS_BOFU=3.0
FUNNEL_WEIGHTS_MOFU=1.5
FUNNEL_WEIGHTS_TOFU=1.0
TREND_LOOKBACK_DAYS=90
TREND_DECAY_THRESHOLD=0.30          # 30% decline flags as decaying
AUTHORITY_SCORE_MIN=40              # minimum to recommend targeting
CANNIBALIZATION_OVERLAP_PCT=0.60    # 60% keyword overlap flags cannibalization
PROGRAMMATIC_MIN_PAGES=50           # minimum pages to justify programmatic approach
GEO_ENTITY_DENSITY_TARGET=3        # named entities per paragraph
GEO_CITATION_TARGET=2              # cited sources per major claim
```

## Scoring Methodology

### Impact Score (0-10)
```
Impact = normalize(
  log(volume) * 0.30 +
  CPC * 0.25 +
  funnel_weight * 0.25 +
  trend_score * 0.20
)
trend_score: >30% growth = 10, stable = 5, >30% decline = 2
funnel_weight: BOFU = 3.0, MOFU = 1.5, TOFU = 1.0
```

### Confidence Score (0-10)
```
Confidence = normalize(
  (1 - difficulty/100) * 0.30 +
  rank_proximity * 0.30 +
  topical_authority * 0.25 +
  existing_content * 0.15
)
rank_proximity: positions 1-10 = 8, 11-20 = 6, 21-50 = 4, 50+ = 2, unranked = 1
existing_content: has relevant page = 8, related page = 4, nothing = 0
```

### GEO Readiness Score (0-100)
| Factor | Weight | Scoring |
|--------|--------|---------|
| Entity Density | 20% | 3+ named entities/paragraph = 20, 2 = 14, 1 = 7, 0 = 0 |
| Citation Presence | 20% | Sources cited per claim: 2+ = 20, 1 = 12, 0 = 0 |
| Q&A Coverage | 20% | PAA questions answered: 5+ = 20, 3 = 14, 1 = 7 |
| Structured Data | 15% | FAQ/HowTo schema present = 15, partial = 8, none = 0 |
| Content Freshness | 15% | Updated <3mo = 15, <6mo = 10, <12mo = 5, older = 0 |
| Topical Depth | 10% | Word count in top quartile for SERP = 10, median = 6, bottom = 2 |

### SERP Feature Win Probability
```
P(feature) = base_probability * authority_modifier * format_modifier
base_probability: current page in top 10 = 0.4, top 20 = 0.2, unranked = 0.05
authority_modifier: DA > competitor avg = 1.5, equal = 1.0, below = 0.6
format_modifier: content matches feature format = 2.0, partial = 1.0, mismatch = 0.3
```

## Output Formats

- **Keyword Universe** -- full keyword map with Impact, Confidence, funnel stage, SERP features
- **Content Cluster Map** -- mermaid diagram of pillar-spoke relationships with linking blueprint
- **Topical Authority Dashboard** -- coverage graph showing gaps and strengths vs competitors
- **GEO Readiness Report** -- per-page scoring with specific optimization recommendations
- **SERP Feature Matrix** -- keyword x feature grid with win probabilities
- **Cannibalization Report** -- conflicting pages with merge/redirect/differentiate recommendations
- **Weekly SEO Brief** -- top 10 priority actions with estimated impact and effort

## Integration Points

- Google Search Console (query data, position tracking, indexing)
- Ahrefs / Semrush (keyword data, competitor analysis, backlinks)
- Google Trends (trend direction signals)
- Screaming Frog (technical crawl data)
- Clearscope / Surfer SEO (content optimization)
- Google PageSpeed Insights (Core Web Vitals)
- Slack (weekly brief delivery, alert notifications)

## Example Usage

```
> "Run an SEO audit for acme.com and score keyword opportunities"
> "Build content clusters for 'marketing automation' with a pillar page plan"
> "Check for keyword cannibalization across our blog"
```

## Prerequisites

- Google Search Console access for target domain
- Keyword research tool API (Ahrefs or Semrush)
- List of 3-5 competitor domains for gap analysis
