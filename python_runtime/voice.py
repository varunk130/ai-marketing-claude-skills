"""Voice Guard: score marketing copy for machine-sounding writing.

Deterministic, stdlib-only. Each check contributes a penalty; the score is
100 minus penalties, floored at 0. Findings point at the exact phrase so a
writer (or agent) can fix it instead of guessing.
"""

from __future__ import annotations

import re
import statistics
from dataclasses import dataclass, field

FILLER = (
    "in today's fast-paced world", "it's important to note", "it is worth noting",
    "in conclusion", "at the end of the day", "when it comes to", "needless to say",
    "in the ever-evolving", "navigate the complexities", "a testament to",
)
HYPE = (
    "revolutionary", "game-changing", "game changer", "cutting-edge", "seamless",
    "seamlessly", "unleash", "unlock", "supercharge", "elevate", "empower",
    "robust", "leverage", "synergy", "delve", "tapestry", "landscape",
)
HEDGES = ("arguably", "potentially", "somewhat", "perhaps", "it could be said", "in many ways")

PENALTY = {"filler": 8, "hype": 5, "hedge": 3, "dash": 4, "uniform": 10, "triplet": 4}


@dataclass
class VoiceReport:
    score: int
    band: str
    findings: list[dict] = field(default_factory=list)


def _sentences(text: str) -> list[str]:
    return [s for s in re.split(r"(?<=[.!?])\s+", text.strip()) if s]


def _find(text: str, phrases: tuple[str, ...], kind: str) -> list[dict]:
    low = text.lower()
    out = []
    for p in phrases:
        for m in re.finditer(r"\b" + re.escape(p) + r"\b", low):
            out.append({"kind": kind, "match": text[m.start():m.end()]})
    return out


def check_voice(text: str) -> VoiceReport:
    findings: list[dict] = []
    findings += _find(text, FILLER, "filler")
    findings += _find(text, HYPE, "hype")
    findings += _find(text, HEDGES, "hedge")

    words = max(1, len(text.split()))
    dashes = text.count("—")
    if dashes and dashes / words > 1 / 60:
        findings.append({"kind": "dash", "match": f"{dashes} em dashes in {words} words"})

    for m in re.finditer(r"\b(\w+), (\w+),? and (\w+)\b", text):
        findings.append({"kind": "triplet", "match": m.group(0)})

    lengths = [len(s.split()) for s in _sentences(text)]
    if len(lengths) >= 4:
        spread = statistics.pstdev(lengths) / statistics.mean(lengths)
        if spread < 0.15:
            findings.append({"kind": "uniform", "match": f"sentence lengths barely vary ({spread:.0%} spread)"})

    score = max(0, 100 - sum(PENALTY[f["kind"]] for f in findings))
    band = "ship" if score >= 85 else "revise" if score >= 60 else "rewrite"
    return VoiceReport(score=score, band=band, findings=findings)
