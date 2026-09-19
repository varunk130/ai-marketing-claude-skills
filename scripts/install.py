"""Install the skills into an agent's skill directory.

    python -m scripts.install                    # ~/.claude/skills (Claude Code)
    python -m scripts.install --target .github/skills   # GitHub Copilot, per repo
    python -m scripts.install --list

Copies each skill folder (SKILL.md + README.md). Existing copies are replaced.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from scripts.validate_skills import ROOT, skill_dirs, validate

DEFAULT_TARGET = Path.home() / ".claude" / "skills"


def install(target: Path, root: Path = ROOT) -> list[str]:
    target.mkdir(parents=True, exist_ok=True)
    installed = []
    for d in skill_dirs(root):
        dest = target / d.name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(d, dest, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        installed.append(d.name)
    return installed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--target", type=Path, default=DEFAULT_TARGET, help="destination skills directory")
    parser.add_argument("--list", action="store_true", help="list skills without installing")
    args = parser.parse_args(argv)

    if args.list:
        for d in skill_dirs():
            print(d.name)
        return 0

    errors = validate()
    if errors:
        for e in errors:
            print(f"ERROR: {e}", file=sys.stderr)
        return 1
    names = install(args.target.expanduser())
    print(f"Installed {len(names)} skills into {args.target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
