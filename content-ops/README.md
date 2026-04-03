# Content Ops

Content quality assurance system that combines expert panel evaluation with automated readability analysis, originality detection, content decay monitoring, and auto-refresh scheduling. Ensures every piece of content meets publishing standards before going live and stays fresh after publishing.

## Key Capabilities

- **Expert Panel Scoring** -- 7-10 domain-specific evaluators (LinkedIn strategist, SEO analyst, brand voice guardian, engagement optimizer, etc.) score content iteratively until it reaches 90/100 or completes 3 rounds
- **AI Readability Analysis** -- dual-score system using Flesch-Kincaid Grade Level (target: 6-8 for B2C, 10-12 for B2B) and Dale-Chall Readability Score. Flags sentences over 25 words, paragraphs over 4 sentences, and passive voice above 10%
- **Originality & AI Detection** -- fingerprints content against your published library to catch self-plagiarism (>30% overlap flagged). Detects AI-generated patterns: repetitive sentence openers, hedging language density, lack of specific examples, over-use of transition words
- **Content Decay Detection** -- monitors published content monthly. Flags pages with >20% traffic decline over 90 days, rising bounce rate, or declining average position in GSC. Prioritizes refreshes by traffic impact
- **Auto-Refresh Scheduling** -- generates refresh calendar based on decay signals. Categorizes: quick fix (meta update, 30 min), moderate refresh (new sections, 2 hrs), full rewrite (outdated topic, 8 hrs)
- **Content Atomization** -- extracts reusable atoms from long-form: quotable statements, statistics, frameworks, stories, controversial takes. Tags each atom with platform fit scores
- **Brand Voice Consistency** -- maintains a voice fingerprint (vocabulary, tone markers, sentence rhythm). Scores new content against the fingerprint (target: >85% consistency)

## Workflow

1. **Ingest Content** -- accept draft from any format (Google Doc, markdown, Notion, raw text)
2. **Readability Scan** -- calculate Flesch-Kincaid + Dale-Chall scores, flag structural issues
3. **Originality Check** -- compare against published content library for overlap
4. **AI Detection Pass** -- scan for AI-generated content patterns, flag for humanization
5. **Brand Voice Check** -- score against voice fingerprint, highlight deviations
6. **Expert Panel Review** -- route to relevant evaluators based on content type and channel
7. **Iterative Scoring** -- panel scores, identifies top 3 weaknesses, content is revised, re-scored
8. **Publishing Gate** -- requires readability pass + originality pass + voice pass + panel score >= 90
9. **Post-Publish Monitoring** -- track performance weekly, flag decay signals monthly
10. **Refresh Queue** -- prioritized backlog of content needing updates, sorted by traffic impact

## Activation Triggers

- "Score this content"
- "Run readability check on [URL/text]"
- "Check for content decay"
- "Generate refresh calendar"
- "Extract atoms from [content]"
- "Run expert panel on [draft]"
- "Check brand voice consistency"

## Configuration

```
CONTENT_LIBRARY_PATH=~/.content-ops/library/
VOICE_FINGERPRINT_PATH=~/.content-ops/voice.json
DECAY_CHECK_CADENCE=monthly
DECAY_TRAFFIC_THRESHOLD=-0.20       # 20% decline triggers flag
DECAY_BOUNCE_THRESHOLD=0.10         # 10% bounce increase triggers flag
READABILITY_TARGET_B2C=8            # Flesch-Kincaid grade level
READABILITY_TARGET_B2B=12
MAX_SENTENCE_LENGTH=25
MAX_PARAGRAPH_SENTENCES=4
PASSIVE_VOICE_MAX_PCT=0.10
ORIGINALITY_OVERLAP_THRESHOLD=0.30
AI_DETECTION_SENSITIVITY=medium     # low | medium | high
PANEL_TARGET_SCORE=90
PANEL_MAX_ROUNDS=3
BRAND_VOICE_MIN_SCORE=85
```

## Scoring Methodology

### Expert Panel (100 points)
- Hook Power: 25 pts (first line impact, curiosity generation, scroll-stop potential)
- Voice Authenticity: 25 pts (brand consistency, human feel, unique perspective)
- Value Density: 25 pts (insight-per-paragraph ratio, actionability, specificity)
- Engagement Design: 25 pts (formatting, CTAs, shareability, comment-bait)

### Readability Score
- Flesch-Kincaid: 0.39 * (words/sentences) + 11.8 * (syllables/words) - 15.59
- Dale-Chall: 0.1579 * (difficult_words/words * 100) + 0.0496 * (words/sentences)
- Combined grade: weighted average with Flesch-Kincaid at 0.6, Dale-Chall at 0.4

### Content Decay Priority Score
```
Priority = (monthly_traffic * traffic_decline_pct) * age_multiplier
age_multiplier: <6mo = 0.5, 6-12mo = 1.0, 12-24mo = 1.5, >24mo = 2.0
```

### AI Detection Signals
- Sentence opener repetition: >3 consecutive "This/That/The" starts
- Hedging density: "might/could/perhaps/arguably" > 2% of words
- Transition overuse: "Furthermore/Moreover/Additionally" > 1.5% of words
- Specificity ratio: named examples / total claims < 0.3

## Output Formats

- **Quality Report** -- per-content scorecard with panel scores, readability metrics, voice score
- **Decay Dashboard** -- ranked list of content needing refresh with priority scores and effort estimates
- **Refresh Calendar** -- monthly schedule with assigned effort levels (quick/moderate/full)
- **Atom Library** -- extracted content atoms tagged by platform and reuse potential
- **Voice Drift Report** -- quarterly analysis of brand voice consistency trends

## Integration Points

- Google Search Console (decay monitoring, position tracking)
- Google Analytics 4 (traffic and engagement metrics)
- Notion / Google Docs (content ingestion)
- WordPress / Webflow (published content scanning)
- Grammarly API (supplementary readability data)
- Slack (decay alerts, panel notifications)

## Example Usage

```
> "Score this blog draft with the expert panel and check readability"
> "Show content decay report — what needs refreshing this month?"
> "Extract reusable atoms from our latest whitepaper"
```

## Prerequisites

- Content library or CMS access (WordPress, Webflow, or Notion)
- Google Search Console credentials for decay monitoring
- Brand voice guidelines document
