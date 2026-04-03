# Growth Engine

Autonomous experimentation framework that goes beyond basic A/B testing. Combines Bayesian inference, multi-armed bandits, CUPED variance reduction, and experiment dependency graphs to run statistically rigorous growth experiments across all marketing channels.

## Key Capabilities

- **Bayesian A/B Testing** -- posterior probability distributions instead of p-values. Get "Variant B has 94% probability of being better" instead of "p < 0.05"
- **Multi-Armed Bandit Mode** -- Thompson Sampling for continuous traffic allocation. Automatically shifts traffic to winning variants during the test
- **CUPED Variance Reduction** -- uses pre-experiment covariates (prior conversion rate, session count) to reduce noise by 30-50%, requiring fewer samples for significance
- **Experiment Dependency Graphs** -- model upstream/downstream relationships between experiments. Flag conflicts before launch (e.g., pricing test affects checkout test)
- **Sequential Testing** -- optional early stopping with alpha-spending functions (O'Brien-Fleming boundaries). Stop tests early when results are conclusive without inflating false positive rates
- **Channel-Specific Sample Calculators** -- minimum detectable effect varies by channel. Email needs 2,000/variant, paid ads 500/variant, homepage 10,000/variant
- **Living Playbook** -- auto-promotes winners with full context. Searchable by channel, lift magnitude, experiment type

## Workflow

1. **Define Hypothesis** -- state expected lift, primary metric, guardrail metrics
2. **Check Dependency Graph** -- verify no conflicting experiments are running
3. **Calculate Sample Size** -- CUPED-adjusted MDE with channel-specific minimums
4. **Select Testing Mode** -- Bayesian (fixed horizon), Bandit (continuous), or Sequential (early stopping)
5. **Run Experiment** -- log daily variant metrics
6. **Score Results** -- posterior distributions + credible intervals (Bayesian) or confidence intervals (frequentist)
7. **Decision Gate** -- requires >90% posterior probability AND >10% relative lift to declare winner
8. **Archive to Playbook** -- winning variant, context, screenshots, follow-up ideas

## Activation Triggers

- "Run experiment on [channel]"
- "Check for conflicting experiments"
- "Score this test"
- "What's in the playbook for [channel]?"
- "Calculate sample size for [metric] with [MDE]"
- "Switch to bandit mode"

## Configuration

```
EXPERIMENT_DB_PATH=~/.growth-engine/experiments.json
PLAYBOOK_PATH=~/.growth-engine/playbook.json
DEFAULT_MODE=bayesian           # bayesian | bandit | sequential
SIGNIFICANCE_THRESHOLD=0.90     # posterior probability threshold
MIN_RELATIVE_LIFT=0.10          # 10% minimum lift to declare winner
CUPED_ENABLED=true
BANDIT_EXPLORATION_RATE=0.1     # epsilon for Thompson Sampling
```

## Scoring Methodology

### Bayesian Framework
- Prior: Beta(1,1) uninformative prior per variant
- Likelihood: Bernoulli for conversion, Normal for revenue
- Posterior: updated daily via conjugate updates
- Decision: P(B > A) computed via 10,000 Monte Carlo samples

### CUPED Adjustment
- Covariate: 14-day pre-experiment metric per user
- Theta: cov(Y, X) / var(X)
- Adjusted metric: Y_cuped = Y - theta * (X - mean(X))
- Variance reduction: typically 30-50%

### Multi-Armed Bandit
- Algorithm: Thompson Sampling
- Each variant draws from its posterior Beta distribution
- Traffic allocated to variant with highest draw
- Regret minimization vs fixed-split testing

## Output Formats

- **Experiment Report** -- markdown with posterior plots, credible intervals, sample sizes, duration
- **Playbook Entry** -- structured JSON with tags, channel, lift, confidence, screenshots
- **Dependency Graph** -- mermaid diagram of active experiments and conflicts
- **Weekly Scorecard** -- aggregated experiment velocity, win rate, cumulative lift

## Integration Points

- Google Analytics 4 (experiment events)
- Amplitude / Mixpanel (cohort metrics)
- LaunchDarkly / Statsig (feature flags)
- Slack (experiment alerts and weekly digests)
- Any CSV export (manual metric logging)

## Example Usage

```
> "Run a Bayesian A/B test on our pricing page with 90% confidence threshold"
> "Check for conflicting experiments before launching the checkout flow test"
> "Calculate sample size for a 15% MDE on email click-through rate"
```

## Prerequisites

- Access to experiment tracking tool (LaunchDarkly, Statsig, or CSV logs)
- Historical conversion data (minimum 2 weeks)
- Defined success metrics and guardrail metrics
