"""Tests for the skill installer."""

import tempfile
import unittest
from pathlib import Path

from scripts.install import install
from scripts.validate_skills import skill_dirs


class InstallTests(unittest.TestCase):
    def test_installs_every_skill_with_skill_md(self):
        with tempfile.TemporaryDirectory() as tmp:
            names = install(Path(tmp))
            self.assertEqual(sorted(names), sorted(d.name for d in skill_dirs()))
            for n in names:
                self.assertTrue((Path(tmp) / n / "SKILL.md").exists())

    def test_reinstall_replaces_existing_copy(self):
        with tempfile.TemporaryDirectory() as tmp:
            install(Path(tmp))
            stale = Path(tmp) / "seo-ops" / "stale.txt"
            stale.write_text("old")
            install(Path(tmp))
            self.assertFalse(stale.exists())


if __name__ == "__main__":
    unittest.main()
