---
name: growth-engine
description: 'Autonomous experimentation framework that goes beyond basic A/B testing. Use when: run experiment on [channel], check for conflicting experiments, score this test, what’s in the playbook for [channel]?, calculate sample size for [metric] with [mde], switch to bandit mode.'
---

# Growth Engine

Autonomous experimentation framework that goes beyond basic A/B testing. Combines Bayesian inference, multi-armed bandits, CUPED variance reduction, and experiment dependency graphs to run statistically rigorous growth experiments across all marketing channels.

## When to Use
- Run experiment on [channel]
- Check for conflicting experiments
- Score this test
- What's in the playbook for [channel]?
- Calculate sample size for [metric] with [MDE]
- Switch to bandit mode

## Workflow
1. **Define Hypothesis** -- state expected lift, primary metric, guardrail metrics
2. **Check Dependency Graph** -- verify no conflicting experiments are running
3. **Calculate Sample Size** -- CUPED-adjusted MDE with channel-specific minimums
4. **Select Testing Mode** -- Bayesian (fixed horizon), Bandit (continuous), or Sequential (early stopping)
5. **Run Experiment** -- log daily variant metrics
6. **Score Results** -- posterior distributions + credible intervals (Bayesian) or confidence intervals (frequentist)
7. **Decision Gate** -- requires >90% posterior probability AND >10% relative lift to declare winner
8. **Archive to Playbook** -- winning variant, context, screenshots, follow-up ideas

## Reference
Full methodology lives in [README.md](README.md) in this folder: configuration, scoring formulas, output formats, integration points, and worked examples. Read it before producing scored output.
