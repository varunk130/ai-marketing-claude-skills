"""Example: run the lead-scoring skill end-to-end."""

from python_runtime import score_lead, score_account


def main() -> None:
    leads = [
        {"title_match": 90, "company_size": 70, "industry_match": 80,
         "intent_signal": 65, "engagement": 70, "tech_stack_match": 50},
        {"title_match": 50, "company_size": 60, "industry_match": 40,
         "intent_signal": 30, "engagement": 20, "tech_stack_match": 10},
        {"title_match": 70, "company_size": 80, "industry_match": 75,
         "intent_signal": 80, "engagement": 65, "tech_stack_match": 60},
    ]

    for i, features in enumerate(leads, start=1):
        s = score_lead(features)
        print(f"Lead #{i}: {s.total} ({s.band})")

    account = score_account(leads)
    print(f"Account: {account.total} ({account.band})")


if __name__ == "__main__":
    main()
