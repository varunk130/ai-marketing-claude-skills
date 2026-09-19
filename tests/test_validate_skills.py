"""Tests for the SKILL.md validator."""

import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import parse_frontmatter, validate

GOOD = "---\nname: demo-skill\ndescription: 'Does a thing. Use when: you need the thing.'\n---\n\n# Demo\n"


def make_skill(root: Path, folder: str, skill_md: str | None) -> None:
    d = root / folder
    d.mkdir()
    (d / "README.md").write_text("# Demo\n")
    if skill_md is not None:
        (d / "SKILL.md").write_text(skill_md)


class ParseFrontmatterTests(unittest.TestCase):
    def test_parses_quoted_values(self):
        fm = parse_frontmatter(GOOD)
        self.assertEqual(fm["name"], "demo-skill")
        self.assertTrue(fm["description"].startswith("Does a thing."))

    def test_rejects_missing_frontmatter(self):
        with self.assertRaises(ValueError):
            parse_frontmatter("# No frontmatter\n")


class ValidateTests(unittest.TestCase):
    def test_repository_skills_are_valid(self):
        self.assertEqual(validate(), [])

    def test_flags_missing_skill_md(self):
        with tempfile.TemporaryDirectory() as tmp:
            make_skill(Path(tmp), "demo-skill", None)
            self.assertIn("demo-skill: missing SKILL.md", validate(Path(tmp)))

    def test_flags_name_mismatch(self):
        with tempfile.TemporaryDirectory() as tmp:
            make_skill(Path(tmp), "other-skill", GOOD)
            errors = validate(Path(tmp))
            self.assertTrue(any("must match folder name" in e for e in errors))

    def test_flags_description_without_trigger(self):
        with tempfile.TemporaryDirectory() as tmp:
            make_skill(Path(tmp), "demo-skill", "---\nname: demo-skill\ndescription: Does a thing.\n---\n")
            errors = validate(Path(tmp))
            self.assertTrue(any("Use when" in e for e in errors))

    def test_accepts_valid_skill(self):
        with tempfile.TemporaryDirectory() as tmp:
            make_skill(Path(tmp), "demo-skill", GOOD)
            self.assertEqual(validate(Path(tmp)), [])


if __name__ == "__main__":
    unittest.main()
