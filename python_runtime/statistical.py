"""Statistical helpers for A/B tests, sample sizing, and CIs."""

import math


Z_BY_CONFIDENCE = {
    0.80: 1.282,
    0.90: 1.645,
    0.95: 1.96,
    0.99: 2.576,
}


def confidence_interval(
    successes: int, trials: int, confidence: float = 0.95
) -> tuple[float, float]:
    """Wald confidence interval for a single proportion."""
    if trials <= 0:
        raise ValueError("trials must be > 0")
    z = Z_BY_CONFIDENCE.get(confidence)
    if z is None:
        raise ValueError(f"unsupported confidence: {confidence}")
    p = successes / trials
    margin = z * math.sqrt(p * (1 - p) / trials)
    return max(0.0, p - margin), min(1.0, p + margin)


def sample_size_for_proportion(
    baseline: float, mde: float, confidence: float = 0.95, power: float = 0.8
) -> int:
    """Approximate per-arm sample size for a 2-proportion z-test."""
    if not 0 < baseline < 1:
        raise ValueError("baseline must be in (0,1)")
    if not 0 < mde < 1:
        raise ValueError("mde must be in (0,1)")
    z_alpha = Z_BY_CONFIDENCE.get(confidence, 1.96)
    z_beta = {0.8: 0.842, 0.9: 1.282}.get(power, 0.842)
    p1 = baseline
    p2 = baseline + mde
    p_bar = (p1 + p2) / 2
    numerator = (z_alpha * math.sqrt(2 * p_bar * (1 - p_bar))) + (
        z_beta * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    )
    n = (numerator**2) / (mde**2)
    return int(math.ceil(n))


def welch_t_test(
    mean_a: float, var_a: float, n_a: int,
    mean_b: float, var_b: float, n_b: int,
) -> float:
    """Return the Welch t statistic. Caller looks up p separately."""
    if n_a < 2 or n_b < 2:
        raise ValueError("each sample needs n>=2")
    se = math.sqrt(var_a / n_a + var_b / n_b)
    if se == 0:
        return 0.0
    return (mean_a - mean_b) / se
