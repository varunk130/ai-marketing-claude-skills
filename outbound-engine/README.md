# Outbound Engine

Multi-channel outbound campaign system that orchestrates coordinated sequences across email, LinkedIn, and video. Includes deliverability warmup planning, A/B subject line optimization, timezone-aware send scheduling, and expert panel copy scoring.

## Key Capabilities

- **Multi-Channel Sequencing** -- design coordinated touchpoint sequences across email (cold + follow-ups), LinkedIn (connection request + messages + post engagement), and personalized video (Loom/Vidyard). Each channel reinforces the others with consistent messaging
- **Deliverability Warmup Planner** -- domain and mailbox warmup schedules. New domains: 14-day ramp (5/day -> 10 -> 20 -> 50 -> 100). Calculates total warmup time based on target daily volume. Monitors sender reputation via Google Postmaster Tools
- **A/B Subject Line Optimizer** -- tests subject lines in small batches (10% of list per variant) before rolling winner to remaining 80%. Scores on: open rate, reply rate (not just opens), and positive sentiment of replies
- **Timezone-Aware Scheduling** -- maps each prospect to their local timezone via IP geolocation or company HQ location. Sends at optimal windows: B2B email (Tue-Thu 8-10am local), LinkedIn (Tue-Wed 7-8am local), follow-ups (same day of week, +3 days)
- **Personalization Engine** -- three tiers: Tier 1 (mail merge: name, company, title), Tier 2 (researched: recent news, job change, funding), Tier 3 (custom: recorded video, hand-written insight). Auto-assigns tier based on deal size and ICP match
- **Reply Classification** -- auto-categorizes responses: Interested, Meeting Booked, Not Now (nurture), Not Interested, Out of Office, Bounced, Unsubscribe. Routes each category to appropriate next action
- **Burnout Prevention** -- caps per-prospect touchpoints at 12 across all channels over 30 days. Respects platform-specific daily limits (email: 50/inbox/day, LinkedIn: 25 connection requests/week)

## Workflow

1. **Infrastructure Audit** -- verify domains, mailboxes, SPF/DKIM/DMARC, warmup status
2. **ICP & List Building** -- define target persona, pull prospects from enrichment tools
3. **Sequence Design** -- map multi-channel touchpoint sequence with timing and personalization tier
4. **Copy Creation** -- draft email templates, LinkedIn messages, video scripts per sequence step
5. **Expert Panel Scoring** -- 10 evaluators score copy. Target: 90/100 or 3 rounds max
6. **Subject Line A/B Setup** -- create 3-5 variants per email step, define test batch size
7. **Warmup Verification** -- confirm all sending domains have completed warmup ramp
8. **Timezone Mapping** -- assign local timezone to each prospect
9. **Launch Sequence** -- activate with human approval gate before first batch
10. **Monitor & Optimize** -- track open/reply/meeting rates, rotate underperforming copy, pause flagged domains

## Activation Triggers

- "Build outbound sequence for [persona]"
- "Check deliverability for [domain]"
- "Score this email copy"
- "A/B test these subject lines"
- "Show reply classification breakdown"
- "Generate warmup schedule for [domain]"
- "Pause outbound to [company]"

## Configuration

```
EMAIL_PROVIDER=instantly            # instantly | smartlead | lemlist | woodpecker
LINKEDIN_AUTOMATION=phantombuster   # phantombuster | dripify | expandi | manual
VIDEO_TOOL=loom                     # loom | vidyard | sendspark
WARMUP_DAILY_START=5
WARMUP_DAILY_MAX=100
WARMUP_RAMP_DAYS=14
EMAIL_DAILY_LIMIT_PER_INBOX=50
LINKEDIN_WEEKLY_CONNECTION_LIMIT=25
MAX_TOUCHPOINTS_PER_PROSPECT=12
TOUCHPOINT_WINDOW_DAYS=30
AB_TEST_BATCH_PCT=0.10
AB_WINNER_METRIC=reply_rate         # open_rate | reply_rate | meeting_rate
OPTIMAL_SEND_WINDOW_START=08:00
OPTIMAL_SEND_WINDOW_END=10:00
PERSONALIZATION_TIER_1_MAX_DEAL=5000
PERSONALIZATION_TIER_2_MAX_DEAL=25000
PERSONALIZATION_TIER_3_MIN_DEAL=25000
```

## Scoring Methodology

### Expert Panel Copy Score (100 points)
- Subject Line Impact: 20 pts (curiosity, specificity, length 4-7 words, no spam triggers)
- Personalization Depth: 20 pts (research quality, relevance, non-generic opener)
- Value Proposition: 20 pts (clear benefit, quantified outcome, relevant to persona)
- Call-to-Action: 20 pts (low friction, specific, single ask, easy to say yes)
- Tone & Voice: 20 pts (conversational, peer-level, no corporate jargon, appropriate length)

### Deliverability Health Score (0-100)
```
Score = SPF_valid(15) + DKIM_valid(15) + DMARC_valid(15) + warmup_complete(15) +
        bounce_rate_under_2pct(10) + spam_complaint_under_0.1pct(10) +
        reply_rate_above_2pct(10) + domain_age_over_30d(10)
```

### Sequence Performance Score
```
Health = (open_rate / industry_avg_open) * 0.25 +
         (reply_rate / industry_avg_reply) * 0.35 +
         (meeting_rate / industry_avg_meeting) * 0.40
Green: > 1.2x | Yellow: 0.8-1.2x | Red: < 0.8x
```

## Output Formats

- **Sequence Blueprint** -- visual timeline of all touchpoints across channels with copy and timing
- **Warmup Schedule** -- day-by-day ramp plan with volume targets per inbox
- **A/B Test Report** -- variant performance comparison with statistical confidence
- **Reply Dashboard** -- classified responses with recommended next actions
- **Domain Health Report** -- SPF/DKIM/DMARC status, reputation score, blacklist checks
- **Weekly Performance Digest** -- open/reply/meeting rates by sequence, persona, and channel

## Integration Points

- Instantly / Smartlead / Lemlist (email sequences)
- PhantomBuster / Dripify / Expandi (LinkedIn automation)
- Loom / Vidyard (video personalization)
- Clay / Apollo (prospect enrichment)
- Google Postmaster Tools (domain reputation)
- HubSpot / Salesforce (CRM sync)
- Slack (reply alerts, performance digests)

## Example Usage

```
> "Build a 5-step outbound sequence for VP Marketing at mid-market SaaS"
> "Generate a 14-day warmup schedule for our new sending domain"
> "A/B test these 3 subject lines on 10% of the list first"
```

## Prerequisites

- Sending domain with SPF, DKIM, and DMARC configured
- Email sequencing tool (Instantly, Smartlead, or Lemlist)
- Prospect list with verified email addresses

## Frequently Asked Questions

**How long does domain warmup take?**
14 days minimum for new domains, ramping from 5 emails/day to your target volume. Rushing warmup risks domain reputation damage.

**What's the maximum safe daily email volume?**
50 per inbox per day for cold outreach. Use multiple inboxes to scale while maintaining deliverability.

**How does reply classification work?**
Responses are auto-categorized as: Interested, Meeting Booked, Not Now, Not Interested, Out of Office, Bounced, or Unsubscribe.
