# ICP Scoring + Messaging — B2B vs B2C Variants

ICP (Ideal Customer Profile) scoring and the messaging that sits on top of it have different *shapes* in B2B vs B2C motions. Forcing them into a single template produces brittle scoring and bland messaging. This document describes when to use which variant and how the variants differ structurally.

---

## When to Use Which Variant

| Signal | Recommended Variant |
|--------|---------------------|
| Buyer is an organization (≥1 paid seat at company level) | **B2B** |
| Buyer is an individual (B2C, prosumer, freemium-to-paid) | **B2C** |
| Pricing is per-seat or contract-based | **B2B** |
| Pricing is per-individual / subscription / one-time consumer purchase | **B2C** |
| Sales cycle is multi-stakeholder | **B2B** |
| Sales cycle is single-buyer | **B2C** |
| Hybrid (e.g., PLG with paid team upgrade): use both — B2C for individual activation, B2B for team conversion | **Both** |

When in doubt: if the *purchase decision* involves more than one person, use B2B.

---

## ICP Scoring — B2B Variant

B2B scoring works at the **account level**, with persona attributes nested inside.

### Account-Level Dimensions (60% of score weight)

| Dimension | Signals | Weight |
|-----------|---------|-------:|
| **Firmographic Fit** | Industry, size band (employees / revenue / funding), geography, tech stack | 25% |
| **Engagement Signal** | Account-level engagement: web visits, content consumption, intent data | 15% |
| **Buying Group Coverage** | Number of named contacts with mapped role + engagement | 10% |
| **Champion Quality** | Champion seniority, tenure, problem-domain authority | 10% |

### Persona-Level Dimensions (40% of score weight)

| Dimension | Signals | Weight |
|-----------|---------|-------:|
| **Persona-Title Match** | Title fits target persona (Champion, EB, Tech Eval, End User) | 15% |
| **Pain-Signal Match** | Persona has expressed signals of the specific pain we solve | 15% |
| **Decision Authority** | Inferred from title + recent role changes | 10% |

### B2B Scoring Output

A composite **0–100 account score** plus a **buying-group readiness flag**:
- `ALL CLEAR` — Champion + EB + Tech Eval all engaged
- `CHAMPION ONLY` — needs multi-thread before sales engagement
- `COLD` — no engaged contacts; account-level marketing required first

---

## ICP Scoring — B2C Variant

B2C scoring works at the **individual level**. There is no buying group, no firmographic layer. The dimensions that dominate are different:

| Dimension | Signals | Weight |
|-----------|---------|-------:|
| **Behavioral Fit** | Activation events completed, recency / frequency / depth of use | 35% |
| **Demographic Fit** | Age band, geography, life-stage signals (where ethically available) | 15% |
| **Psychographic Fit** | Stated motivations, channel preferences, identity signals from onboarding | 15% |
| **Channel of Acquisition** | Source channel correlates strongly with LTV in B2C — score it explicitly | 10% |
| **Monetization Readiness** | Engagement intensity, paywall exposure, prior conversion attempts | 25% |

### B2C Scoring Output

A composite **0–100 individual score** plus a **monetization-readiness flag**:
- `READY` — high behavioral fit + high monetization readiness → trigger conversion play
- `NURTURE` — high behavioral fit, low monetization readiness → engagement play
- `RE-ENGAGE` — was active, has decayed → re-engagement play
- `DRIFT` — low fit on all dimensions → deprioritize

---

## Messaging — B2B Variant

B2B messaging is **multi-persona** by construction. The same product update produces different messages for different roles in the buying group:

| Role | Message Lead | Proof Type | Length |
|------|--------------|------------|--------|
| **Champion** | Personal career capital ("how this makes you the hero") | Peer testimonials, named champions at peer companies | Medium |
| **Economic Buyer** | Business outcome ($, time, risk) | Case study with named metrics, ROI calculation | Short |
| **Technical Evaluator** | Risk reduction (architecture, security, fit) | Technical brief, security artifact pack, reference architecture | Long |
| **End User** | Day-to-day usability | Demo video, "first 5 minutes" walkthrough | Short |
| **Procurement / Legal** | Compliance + standard terms | Pre-built MSAs, security questionnaire pre-fills, certifications list | Medium |

Each B2B message must name the role it targets explicitly. Generic "B2B messaging" that targets "the buyer" almost always under-engages 4 of the 5 roles.

---

## Messaging — B2C Variant

B2C messaging is **single-persona** but **journey-stage-specific**:

| Journey Stage | Message Lead | Proof Type | Length |
|---------------|--------------|------------|--------|
| **First-touch** | Identity / aspiration ("for people like you") | Social proof at scale (user counts, ratings) | Very short |
| **Onboarding** | Quick wins, low effort | "60-second" demos, immediate value moments | Short |
| **Activation** | Habit formation, streaks, social hooks | Personalized progress, peer comparison | Short |
| **Conversion** | FOMO + value framing (annual vs monthly, founder pricing) | Loss-aversion language, scarcity (legitimate, not manufactured) | Short |
| **Retention** | Identity reinforcement, deeper value, expansion uses | "You've used X for Y; have you tried Z?" | Medium |

B2C messaging that ignores journey stage produces over-engagement (treating Day-1 users like Day-90 users) or under-engagement (treating Day-90 users like Day-1 users).

---

## Output

Two skill output templates ship side-by-side:

- `icp-score-b2b-[account]-[YYYY-MM-DD].md` — account-level scorecard, buying-group map, recommended next play
- `icp-score-b2c-[user-segment]-[YYYY-MM-DD].md` — segment-level scorecard, journey-stage distribution, recommended messaging mix

The skill picks the variant by reading the scoring inputs (presence of `account_id` field → B2B; presence of `user_id` only → B2C). Hybrid PLG motions explicitly run both: B2C scoring for individual activation, B2B scoring for team-conversion accounts.

---

## Process

### Step 1: Variant Selection
I'll ask:
> "Is the buyer an individual or an organization? If hybrid (PLG with team upgrade), are you scoring activation or team conversion right now? What scoring inputs do you have available?"

### Step 2: Score on the Right Dimensions
Apply the variant's dimension weights. Resist the temptation to "blend" — a blended scorecard hides which lever to pull.

### Step 3: Generate Variant-Appropriate Messaging
For B2B: produce per-role messages with explicit role tagging.
For B2C: produce per-journey-stage messages with explicit stage tagging.

### Step 4: Pair Score with Play
The scorecard outputs the *recommended next play* — not just a number. A score without an action recommendation is a vanity metric.

---

## Tips
1. **Don't blend B2B and B2C scoring.** A "universal" ICP score is bland and brittle. Split early; converge only at the report level.
2. **B2B messaging that names a single buyer fails.** Always produce the multi-role variant.
3. **B2C messaging that ignores journey stage churns users.** Onboarding messaging to a Day-90 user is annoying; conversion messaging to a Day-1 user is jarring.
4. **Hybrid PLG motions need both variants running concurrently.** Don't try to collapse them.
5. **Re-validate scoring weights quarterly.** Champion-quality weight in B2B and channel-source weight in B2C drift the most.
