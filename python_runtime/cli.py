"""Minimal CLI to exercise the marketing skills runtime locally."""

import argparse
import json
import sys

from python_runtime import (
    confidence_interval,
    sample_size_for_proportion,
    score_lead,
)


def _score(args: argparse.Namespace) -> dict:
    features = json.loads(args.features)
    return {
        "score": score_lead(features).total,
        "band": score_lead(features).band,
    }


def _ci(args: argparse.Namespace) -> dict:
    lo, hi = confidence_interval(args.successes, args.trials, args.confidence)
    return {"lower": lo, "upper": hi}


def _samplesize(args: argparse.Namespace) -> dict:
    n = sample_size_for_proportion(args.baseline, args.mde, args.confidence, args.power)
    return {"per_arm": n}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="marketing-skills")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("score-lead")
    p.add_argument("--features", required=True, help="JSON dict of feature->0..100")
    p.set_defaults(fn=_score)

    p = sub.add_parser("ci")
    p.add_argument("--successes", type=int, required=True)
    p.add_argument("--trials", type=int, required=True)
    p.add_argument("--confidence", type=float, default=0.95)
    p.set_defaults(fn=_ci)

    p = sub.add_parser("sample-size")
    p.add_argument("--baseline", type=float, required=True)
    p.add_argument("--mde", type=float, required=True)
    p.add_argument("--confidence", type=float, default=0.95)
    p.add_argument("--power", type=float, default=0.8)
    p.set_defaults(fn=_samplesize)

    args = parser.parse_args(argv)
    json.dump(args.fn(args), sys.stdout, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
