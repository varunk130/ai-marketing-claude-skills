# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- The documented IO helpers (`read_csv`, `write_csv`, `read_jsonl`, `write_jsonl`) are now exported from `python_runtime`, so the runtime surface described in the README actually resolves.
- Table of Contents in the README for faster navigation.
- `SKILL.md` for all 12 skills so Claude Code, Copilot, and other agents can load them directly.
- `scripts/validate_skills.py` frontmatter validator, wired into CI.
- `scripts/install.py` to install skills into `~/.claude/skills` or a repo's `.github/skills`.
- Voice Guard quality gate (`voice-guard/`, `python_runtime/voice.py`) for scoring generated copy.

### Changed
- Corrected the skill count to 13 in the badge, hero image, and intro.
- Corrected the ai-ux-skill-library reference in Related Work to 13 frameworks.
- Reworded the footer to list Claude Code, OpenAI Codex, and GitHub Copilot.
- Normalized Python file line endings to LF and restored the missing final newline in `CODE_OF_CONDUCT.md`.
- Corrected the AI-Eval-Skills reference in Related Work to 7 skills (the upstream repo added the tool-use-eval skill).
- Added the three Next.js multi-agent demos (Compound, Beacon, Atlas) to the Related Work section.
- Documentation polish across skill READMEs.
- Updated the ai-customer-discovery-skills status in Related Work (5 of 12 skills shipped).

## [1.0.0] - 2026-04-03

### Added
- Initial release with 11 AI marketing skills
- Growth Engine: Bayesian A/B testing, multi-armed bandits, CUPED variance reduction
- Sales Pipeline: Multi-channel intent scoring, AI enrichment, predictive deal scoring
- Content: Expert panel scoring, readability analysis, content decay monitoring
- Conversion: Heatmap-aware CRO audits, Cialdini scoring, micro-conversion funnels
- Outbound Engine: Multi-channel sequences, deliverability warmup, timezone scheduling
- SEO: GEO/AEO optimization, topical authority mapping, SERP feature scoring
- Finance: Cohort LTV/CAC modeling, SaaS magic number, budget allocation
- Revenue Intelligence: Win/loss pattern recognition, auto-generated battlecards
- Podcast: Guest fit scoring, sponsorship CPM calculator, cross-promo mapping
- Team: Skills gap matrix, capacity planning, 1:1 prep generator
- Sales Playbook: MEDDPICC+BANT hybrid, mutual action plans, ROI calculator
- Example usage sections for all 11 skills
- Branch protection with required PR reviews
