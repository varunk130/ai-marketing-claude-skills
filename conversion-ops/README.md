# Conversion Ops

Landing page and funnel optimization system that combines traditional CRO auditing with heatmap analysis, session replay insights, micro-conversion funnel mapping, and psychological trigger scoring based on Cialdini's 6 principles of persuasion.

## Key Capabilities

- **Heatmap-Aware CRO Audit** -- 12-dimension scoring that incorporates scroll depth data, click density maps, and attention heatmaps. Identifies "dead zones" (high-value areas with zero interaction) and "rage clicks" (repeated clicks on non-interactive elements)
- **Session Replay Pattern Analysis** -- categorizes user sessions into behavioral archetypes: Scanner (quick scroll, no clicks), Reader (slow scroll, highlights), Comparer (tabs back and forth), Confused (erratic mouse, back button), Ready Buyer (straight to CTA). Prescribes fixes per archetype
- **Micro-Conversion Funnel Mapping** -- maps the full journey from landing to macro-conversion through every micro-step: page load -> first scroll -> section view -> CTA view -> CTA hover -> CTA click -> form start -> form field 1 -> ... -> form submit. Identifies the exact drop-off point
- **Cialdini Psychological Trigger Scoring** -- evaluates pages against all 6 principles: Reciprocity (free value before ask), Commitment (small yeses before big ask), Social Proof (testimonials, logos, numbers), Authority (credentials, press, certifications), Liking (personality, similarity, aesthetics), Scarcity (urgency, limited availability)
- **Form Friction Calculator** -- scores every form field by necessity vs friction: name (low friction), email (low), phone (high), company size (medium), budget (very high). Recommends progressive profiling strategies
- **Mobile-First Scoring** -- separate audit track for mobile: thumb-zone CTA placement, tap target sizes (min 44x44px), input type optimization, viewport-aware lazy loading
- **Competitive Page Benchmarking** -- crawls competitor landing pages and scores them on the same 12 dimensions. Shows where you over/under-index

## Workflow

1. **Page Ingestion** -- provide URL or HTML. System captures desktop + mobile screenshots
2. **Heatmap Analysis** -- if heatmap data available (Hotjar/MS Clarity export), overlay onto audit
3. **12-Dimension CRO Audit** -- score each dimension 0-10 with specific findings
4. **Cialdini Trigger Scan** -- identify present/missing persuasion principles with fix suggestions
5. **Micro-Funnel Map** -- enumerate every micro-conversion step, flag drop-off points
6. **Form Friction Audit** -- score each form field, recommend removals or progressive profiling
7. **Mobile Audit** -- separate scoring pass for mobile experience
8. **Session Replay Classification** -- if replay data available, classify dominant user archetype
9. **Competitive Benchmark** -- crawl 3-5 competitor pages, generate comparison matrix
10. **Prioritized Fix List** -- rank all findings by (impact * ease) and output implementation plan

## Activation Triggers

- "Audit this landing page"
- "Score [URL] for conversions"
- "Map the micro-funnel for [page]"
- "Check Cialdini triggers on [URL]"
- "Analyze form friction"
- "Compare against [competitor URL]"
- "Mobile CRO audit"

## Configuration

```
HEATMAP_PROVIDER=hotjar             # hotjar | clarity | mouseflow | none
SESSION_REPLAY_PROVIDER=clarity     # clarity | hotjar | fullstory | none
COMPETITOR_URLS=[]                  # list of competitor landing pages
INDUSTRY=saas                       # saas | ecommerce | agency | marketplace
MOBILE_PRIORITY=high                # low | medium | high
FORM_FRICTION_THRESHOLD=35          # max acceptable form friction score
CTA_ABOVE_FOLD_REQUIRED=true
MIN_SOCIAL_PROOF_COUNT=3            # minimum testimonials/logos required
```

## Scoring Methodology

### 12-Dimension CRO Score (0-120, normalized to 0-100)
| Dimension | Max Points | What It Measures |
|-----------|-----------|-----------------|
| Headline Clarity | 10 | Value prop in <8 words, benefit-first |
| CTA Visibility | 10 | Above fold, contrast ratio >4.5:1, action verb |
| Social Proof | 10 | Testimonials, logos, case studies, numbers |
| Trust Signals | 10 | Security badges, guarantees, privacy links |
| Page Speed | 10 | LCP <2.5s, CLS <0.1, FID <100ms |
| Visual Hierarchy | 10 | F-pattern or Z-pattern layout, whitespace |
| Urgency/Scarcity | 10 | Deadlines, limited spots, countdown timers |
| Form Optimization | 10 | Field count, progressive profiling, autofill |
| Mobile Experience | 10 | Thumb zones, tap targets, responsive images |
| Content Scanability | 10 | Bullets, headers, bold key phrases, short paragraphs |
| Objection Handling | 10 | FAQ, comparison tables, risk reversal |
| Exit Intent Strategy | 10 | Exit popups, scroll-triggered offers, sticky CTAs |

### Cialdini Score (0-60, normalized to 0-100)
Each principle scored 0-10:
- **Reciprocity**: free tool/calculator (10), free guide (7), free trial (5), nothing (0)
- **Commitment**: micro-yes sequence (10), quiz/assessment (7), email-first (5), cold ask (0)
- **Social Proof**: named case studies (10), logos + numbers (7), testimonials only (5), none (0)
- **Authority**: industry awards + press (10), certifications (7), "trusted by" (5), none (0)
- **Liking**: founder story + team photos (10), brand personality (7), stock photos (3), none (0)
- **Scarcity**: real limited availability (10), time-limited offer (7), implied urgency (3), none (0)

### Form Friction Score
```
Friction = sum(field_friction_weight * field_position_multiplier)
field_friction_weights: name=1, email=1, company=2, phone=4, budget=5, address=4
position_multiplier: first_3_fields=1.0, fields_4-6=1.3, fields_7+=1.8
Target: total friction < 35
```

## Output Formats

- **CRO Audit Report** -- 12-dimension scorecard with screenshots, annotations, fix priorities
- **Cialdini Gap Analysis** -- present vs missing triggers with implementation suggestions
- **Micro-Funnel Diagram** -- visual funnel with drop-off percentages at each step
- **Form Optimization Brief** -- field-by-field friction analysis with removal/reorder recommendations
- **Competitive Benchmark Matrix** -- side-by-side scoring vs 3-5 competitors
- **Implementation Plan** -- prioritized fixes sorted by (impact score * ease score)

## Integration Points

- Hotjar / Microsoft Clarity / Mouseflow (heatmaps + replays)
- Google PageSpeed Insights (Core Web Vitals)
- Google Analytics 4 (micro-conversion events)
- Screaming Frog / Playwright (competitor crawling)
- Figma (annotated screenshot exports)
- Slack (audit result notifications)

## Example Usage

```
> "Audit acme.com/pricing for conversion optimization"
> "Map the micro-conversion funnel and find the biggest drop-off"
> "Score our landing page against Cialdini's 6 persuasion principles"
```

## Prerequisites

- Landing page URL or HTML source
- Heatmap tool access (Hotjar or Microsoft Clarity) recommended
- Google Analytics 4 with conversion events configured
