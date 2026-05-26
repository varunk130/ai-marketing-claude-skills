# Security Policy

These skills are Markdown contracts plus a small zero-dependency Python runtime. If you find a security issue - in the runtime code, the example data, or any guidance that could lead a user to leak credentials or PII - please report it privately rather than opening a public issue.

## Reporting a vulnerability

Use one of these private channels:

1. **GitHub private vulnerability reporting** - open a private advisory on this repository's Security tab. This is the preferred channel.
2. **Direct message** - reach the maintainer through the contact information on their GitHub profile.

When reporting, please include:

- A clear description of the issue and its potential impact
- Steps to reproduce (a minimal proof-of-concept if possible)
- The affected file, commit SHA, or skill name
- Any suggested remediation
- Whether you would like public credit when the fix is released

## What to expect

- **Acknowledgement** within 7 days
- A **triage decision** (accepted, needs more info, out of scope) within 14 days
- A **coordinated disclosure timeline** once the issue is confirmed
- **Public credit** in the release notes, with your consent

## Scope

In scope:

- The `python_runtime/` package
- Skill instructions or examples that could cause credential leakage, PII exposure, or unsafe automation if followed verbatim
- Sample configuration that uses real (rather than placeholder) secrets

Out of scope:

- Findings that depend on the user supplying genuine production credentials or live customer data to these examples
- Issues in third-party services (Apollo, Clay, Ahrefs, etc.) referenced in the skill examples - please report those to the relevant vendor
- Stylistic or wording concerns - open a regular issue or pull request for those

## Supported versions

Only the latest commit on `main` is actively supported. Older snapshots are not patched. If you are running an older fork, please pull the latest before reporting.
