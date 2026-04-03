# Podcast Ops

Podcast growth and content multiplication system that goes beyond episode-to-posts conversion. Includes guest outreach scoring, sponsorship valuation, cross-promotion network mapping, audiogram/video clip automation, and performance analytics.

## Key Capabilities

- **Guest Outreach Scoring** -- evaluates potential guests on a 0-100 Guest Fit Score: audience overlap (shared ICP), reach multiplier (their audience size vs yours), content alignment (topic relevance), engagement quality (do they promote appearances?), booking feasibility (how hard to book?). Auto-generates personalized pitch emails ranked by score
- **Sponsorship Valuation Calculator** -- calculates your podcast's ad inventory value using: CPM model (downloads * rate), engagement-adjusted CPM (completion rate * listener quality), and attribution-based pricing (tracked conversions). Generates rate cards for pre-roll, mid-roll, post-roll, and host-read placements
- **Cross-Promotion Network Mapping** -- identifies non-competing podcasts with overlapping audiences. Scores potential partners on: audience similarity, episode frequency compatibility, promotion willingness, and combined reach. Generates mutual promo scripts and scheduling calendar
- **Audiogram & Video Clip Automation** -- extracts the 10 most shareable moments from each episode using: controversy score, quotability, emotional peaks, and insight density. For each moment: generates waveform audiogram specs, vertical video clip timestamps, quote card text, and platform-specific captions
- **Content Atomization** -- breaks one episode into 25+ content pieces: 3-5 LinkedIn posts, 5-8 tweets/X threads, 2-3 short-form video scripts, 1 newsletter section, 1 blog post, 3-5 quote cards, 2-3 carousel slides. Each atom tagged with viral potential score
- **Performance Analytics** -- tracks per-episode: downloads (7-day, 30-day, all-time), completion rate, subscriber conversion, review generation, social amplification. Identifies what topics/guests/formats drive the most growth
- **Episode Planning Calendar** -- 90-day forward calendar with: topic clusters (aligned to content strategy), guest slots, solo episodes, sponsorship placements, and cross-promo windows

## Workflow

1. **Episode Ingestion** -- upload audio/video or provide RSS feed URL. Auto-transcribe via Whisper
2. **Content Atom Extraction** -- identify quotable moments, frameworks, stories, data points, hot takes
3. **Viral Scoring** -- score each atom: (Novelty * 0.30) + (Controversy * 0.25) + (Utility * 0.25) + (Emotion * 0.20)
4. **Multi-Platform Generation** -- create 25+ content pieces with platform-specific formatting
5. **Audiogram/Clip Selection** -- pick top 10 moments with timestamps for audio and video clips
6. **Publishing Calendar** -- schedule content pieces across platforms over 7-14 days
7. **Guest Pipeline Management** -- score prospective guests, generate pitches, track outreach
8. **Sponsorship Pricing** -- calculate rate card based on latest download and engagement data
9. **Cross-Promo Outreach** -- identify partner podcasts, generate mutual promo proposals
10. **Performance Review** -- weekly analytics digest with growth trends and content performance

## Activation Triggers

- "Process this episode"
- "Score guest candidates for [topic]"
- "Calculate sponsorship rates"
- "Find cross-promo partners"
- "Generate content calendar from episode"
- "Show podcast analytics"
- "Plan next 90 days of episodes"
- "Extract clips from [episode]"

## Configuration

```
PODCAST_RSS_URL=https://your-podcast.com/feed.xml
TRANSCRIPTION_ENGINE=whisper        # whisper | deepgram | assembly_ai
CONTENT_PIECES_PER_EPISODE=25
CLIP_COUNT_PER_EPISODE=10
PUBLISHING_SPREAD_DAYS=14           # spread content over N days
VIRAL_SCORE_THRESHOLD=60            # minimum score to publish
DEDUP_OVERLAP_THRESHOLD=0.70        # 70% similarity = duplicate
GUEST_SCORE_WEIGHTS_OVERLAP=0.30
GUEST_SCORE_WEIGHTS_REACH=0.25
GUEST_SCORE_WEIGHTS_ALIGNMENT=0.20
GUEST_SCORE_WEIGHTS_ENGAGEMENT=0.15
GUEST_SCORE_WEIGHTS_FEASIBILITY=0.10
SPONSORSHIP_BASE_CPM=25.00
SPONSORSHIP_HOST_READ_MULTIPLIER=2.5
CROSS_PROMO_MIN_AUDIENCE_OVERLAP=0.20
```

## Scoring Methodology

### Guest Fit Score (0-100)
| Factor | Weight | Scoring |
|--------|--------|---------|
| Audience Overlap | 30% | >50% ICP match = 30, 30-50% = 20, <30% = 10 |
| Reach Multiplier | 25% | >5x your audience = 25, 2-5x = 18, 1-2x = 12, <1x = 6 |
| Content Alignment | 20% | Core topic expert = 20, adjacent = 14, tangential = 7 |
| Promo Engagement | 15% | Actively promotes appearances = 15, sometimes = 10, rarely = 5 |
| Booking Feasibility | 10% | Open to podcasts = 10, selective = 6, very hard to book = 2 |

### Viral Potential Score (0-100)
```
Viral = (Novelty * 0.30) + (Controversy * 0.25) + (Utility * 0.25) + (Emotion * 0.20)

Novelty: never-heard-before insight (10), fresh angle (7), known-but-well-said (4), common knowledge (1)
Controversy: challenges conventional wisdom (10), strong opinion (7), nuanced take (4), consensus view (1)
Utility: immediately actionable framework (10), useful advice (7), interesting but abstract (4), purely theoretical (1)
Emotion: evokes strong reaction (10), relatable story (7), mildly engaging (4), neutral (1)
```

### Sponsorship CPM Model
```
Base CPM = $25 (industry average)
Adjusted CPM = Base * completion_multiplier * niche_multiplier * engagement_multiplier

completion_multiplier: >80% completion = 1.5, 60-80% = 1.2, <60% = 0.8
niche_multiplier: B2B SaaS = 2.0, finance = 1.8, tech = 1.5, general = 1.0
engagement_multiplier: high social shares + reviews = 1.3, moderate = 1.0, low = 0.7

Rate Card:
Pre-roll (15s): CPM * 0.7
Mid-roll (60s): CPM * 1.0
Post-roll (30s): CPM * 0.5
Host-read mid-roll: CPM * 2.5
```

## Output Formats

- **Episode Content Pack** -- 25+ platform-ready content pieces with publish dates and captions
- **Clip Sheet** -- top 10 moments with timestamps, transcripts, and audiogram specs
- **Guest Pipeline** -- ranked prospects with fit scores, pitch drafts, and outreach status
- **Sponsorship Rate Card** -- tiered pricing with audience demographics and engagement data
- **Cross-Promo Proposals** -- partner podcast list with overlap scores and mutual promo scripts
- **Performance Dashboard** -- per-episode metrics with growth trends and content attribution
- **90-Day Calendar** -- planned episodes with topics, guests, sponsors, and cross-promo slots

## Integration Points

- Spotify for Podcasters / Apple Podcasts Connect (download analytics)
- OpenAI Whisper / Deepgram (transcription)
- Riverside.fm / Descript (recording + editing)
- Buffer / Hootsuite (social scheduling)
- Canva API (audiogram and quote card generation)
- Slack (episode processing alerts, guest pipeline updates)
- Google Sheets (guest tracking, sponsorship CRM)

## Example Usage

```
> "Score these 10 guest candidates for our AI marketing series"
> "Calculate our sponsorship rate card based on current download numbers"
> "Extract the top 10 shareable clips from this week's episode"
```

## Prerequisites

- Podcast RSS feed URL or audio/video files
- Download analytics access (Spotify for Podcasters or Apple Podcasts)
- Social media scheduling tool for content distribution
