"""Validate SKILL.md frontmatter for every skill folder.

Stdlib only, so it runs anywhere the tests run. Exits non-zero on any error.

    python -m scripts.validate_skills
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MAX_DESCRIPTION = 1024


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse the simple `key: value` frontmatter block at the top of a SKILL.md."""
    if not text.startswith("---\n"):
        raise ValueError("missing opening '---'")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValueError("missing closing '---'")
    fields: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"malformed line: {line!r}")
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
            value = value[1:-1]
        fields[key.strip()] = value
    return fields


def skill_dirs(root: Path = ROOT) -> list[Path]:
    """Folders that ship a README.md skill definition are expected to ship a SKILL.md."""
    return sorted(p.parent for p in root.glob("*/README.md") if not p.parent.name.startswith("."))


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for d in skill_dirs(root):
        skill = d / "SKILL.md"
        if not skill.exists():
            errors.append(f"{d.name}: missing SKILL.md")
            continue
        try:
            fm = parse_frontmatter(skill.read_text(encoding="utf-8"))
        except ValueError as e:
            errors.append(f"{d.name}: {e}")
            continue
        name, desc = fm.get("name", ""), fm.get("description", "")
        if name != d.name:
            errors.append(f"{d.name}: name {name!r} must match folder name")
        if not NAME_RE.match(name):
            errors.append(f"{d.name}: name must be lowercase kebab-case")
        if not desc:
            errors.append(f"{d.name}: description is required")
        elif len(desc) > MAX_DESCRIPTION:
            errors.append(f"{d.name}: description is {len(desc)} chars (max {MAX_DESCRIPTION})")
        elif "use when" not in desc.lower():
            errors.append(f"{d.name}: description should say when to use the skill ('Use when: ...')")
    return errors


def main() -> int:
    errors = validate()
    for e in errors:
        print(f"ERROR: {e}")
    if errors:
        return 1
    print(f"OK: {len(skill_dirs())} skills valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
