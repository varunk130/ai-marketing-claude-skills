"""Lead and account scoring used by multiple marketing skills."""

from dataclasses import dataclass, field


DEFAULT_WEIGHTS: dict[str, float] = {
    "title_match": 0.25,
    "company_size": 0.15,
    "industry_match": 0.15,
    "intent_signal": 0.20,
    "engagement": 0.15,
    "tech_stack_match": 0.10,
}


@dataclass
class LeadScore:
    total: float
    band: str
    breakdown: dict[str, float] = field(default_factory=dict)


def _band(total: float) -> str:
    if total >= 80:
        return "A"
    if total >= 60:
        return "B"
    if total >= 40:
        return "C"
    return "D"


def score_lead(features: dict[str, float], weights: dict[str, float] | None = None) -> LeadScore:
    """Score a lead 0..100 from feature -> raw_score (0..100) inputs."""
    weights = weights or DEFAULT_WEIGHTS
    breakdown: dict[str, float] = {}
    total = 0.0
    for k, w in weights.items():
        raw = float(features.get(k, 0.0))
        contribution = round(raw * w, 3)
        breakdown[k] = contribution
        total += contribution
    total = round(min(100.0, max(0.0, total)), 2)
    return LeadScore(total=total, band=_band(total), breakdown=breakdown)


def score_account(leads: list[dict[str, float]]) -> LeadScore:
    """Aggregate lead scores into an account score (mean of top quartile)."""
    if not leads:
        return LeadScore(total=0.0, band=_band(0.0))
    scored = sorted((score_lead(f).total for f in leads), reverse=True)
    cut = max(1, len(scored) // 4)
    top = scored[:cut]
    total = round(sum(top) / len(top), 2)
    return LeadScore(total=total, band=_band(total))


def blend_scores(*scores: LeadScore, weights: list[float] | None = None) -> LeadScore:
    if not scores:
        return LeadScore(total=0.0, band=_band(0.0))
    weights = weights or [1.0 / len(scores)] * len(scores)
    total = round(sum(s.total * w for s, w in zip(scores, weights)), 2)
    return LeadScore(total=total, band=_band(total))
