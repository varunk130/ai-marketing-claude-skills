"""Tests for the Voice Guard checker."""

import unittest

from python_runtime.voice import check_voice

CLEAN = (
    "We cut onboarding from nine steps to three. Most teams finish setup before lunch. "
    "The rest email us, and we answer within the hour. Try it on one workflow first."
)
SLOPPY = (
    "In today's fast-paced world, our revolutionary platform lets you unlock seamless growth. "
    "It's important to note that we empower teams to leverage synergy — arguably the best."
)


class VoiceTests(unittest.TestCase):
    def test_clean_copy_ships(self):
        r = check_voice(CLEAN)
        self.assertEqual(r.band, "ship")
        self.assertEqual(r.findings, [])

    def test_sloppy_copy_is_flagged(self):
        r = check_voice(SLOPPY)
        self.assertLess(r.score, 60)
        kinds = {f["kind"] for f in r.findings}
        self.assertTrue({"filler", "hype", "hedge"} <= kinds)

    def test_findings_quote_the_original_text(self):
        r = check_voice("Our Revolutionary tool.")
        self.assertEqual(r.findings[0]["match"], "Revolutionary")

    def test_uniform_sentence_rhythm_is_flagged(self):
        text = "We make good tools. We help many teams. We ship every week. We fix bugs fast."
        kinds = {f["kind"] for f in check_voice(text).findings}
        self.assertIn("uniform", kinds)

    def test_score_never_negative(self):
        self.assertGreaterEqual(check_voice(SLOPPY * 20).score, 0)


if __name__ == "__main__":
    unittest.main()
