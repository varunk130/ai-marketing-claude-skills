"""Tests for the scoring module."""

import math
import unittest

from python_runtime.scoring import (
    DEFAULT_WEIGHTS,
    blend_scores,
    score_account,
    score_lead,
)


PERFECT = {k: 100 for k in DEFAULT_WEIGHTS}
ZERO = {k: 0 for k in DEFAULT_WEIGHTS}


class ScoringTests(unittest.TestCase):
    def test_perfect_lead_is_band_a(self):
        s = score_lead(PERFECT)
        self.assertGreaterEqual(s.total, 80)
        self.assertEqual(s.band, "A")

    def test_zero_lead_is_band_d(self):
        s = score_lead(ZERO)
        self.assertEqual(s.total, 0.0)
        self.assertEqual(s.band, "D")

    def test_breakdown_sums_to_total(self):
        s = score_lead(PERFECT)
        self.assertTrue(math.isclose(sum(s.breakdown.values()), s.total, rel_tol=1e-3))

    def test_account_aggregates_top_quartile(self):
        leads = [PERFECT, PERFECT, ZERO, ZERO]
        s = score_account(leads)
        self.assertGreaterEqual(s.total, 80)

    def test_blend_respects_weights(self):
        a = score_lead(PERFECT)
        b = score_lead(ZERO)
        blended = blend_scores(a, b, weights=[0.75, 0.25])
        self.assertGreater(blended.total, 50)


if __name__ == "__main__":
    unittest.main()
