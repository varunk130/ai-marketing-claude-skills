# ROI Worked Example - `revenue-intelligence`

> Synthetic data. Numbers are illustrative.

**Before** (manual quarterly pipeline review)

| Stage | Deals | Cycle days | Won |
|---|---|---|---|
| Discovery | 120 | 14 | - |
| Eval | 60 | 28 | - |
| Negotiation | 24 | 21 | 6 |

**Skill run:** `revenue-intelligence/next-best-action` on the pipeline export.

**After** (priorities + warnings surfaced)

- 9 of the 24 Negotiation deals had no exec sponsor identified → flagged.
- 3 Eval deals were idle >21 days → recommended re-engagement script from `sales-playbook`.
- Forecast variance narrowed from ±32% to ±18%.

**Estimated impact:** ~$420k pulled-forward revenue per quarter at the same close rate, plus 1 SDR-week saved per rep on pipeline hygiene.
