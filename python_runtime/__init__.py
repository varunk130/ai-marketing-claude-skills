"""Python runtime for the AI Marketing Claude Skills library.

Each skill ships as a Markdown contract; this runtime provides shared
scoring, statistical, and IO helpers that the skills call into when
executed via Claude Code or another agent harness.
"""

from .scoring import (
    LeadScore,
    score_lead,
    score_account,
    blend_scores,
)
from .statistical import (
    confidence_interval,
    sample_size_for_proportion,
    welch_t_test,
)
from .io_helpers import (
    read_csv,
    write_csv,
    read_jsonl,
    write_jsonl,
)

__all__ = [
    "LeadScore",
    "score_lead",
    "score_account",
    "blend_scores",
    "read_csv",
    "write_csv",
    "read_jsonl",
    "write_jsonl",
    "confidence_interval",
    "sample_size_for_proportion",
    "welch_t_test",
]
