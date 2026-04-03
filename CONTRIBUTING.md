# Contributing to AI Marketing Claude Skills

Thank you for your interest in contributing! This guide will help you get started.

## How to Contribute

### Reporting Issues

- Use GitHub Issues to report bugs or suggest enhancements
- Include clear, descriptive titles
- Provide as much context as possible

### Submitting Changes

1. **Fork** the repository
2. **Create a branch** from `main` (`git checkout -b feature/your-feature`)
3. **Make your changes** — keep commits focused and descriptive
4. **Test your skill** by running it through an AI agent
5. **Open a Pull Request** against `main`

### Pull Request Guidelines

- All PRs require at least 1 approving review before merge
- Direct pushes to `main` are not allowed
- Keep PRs focused on a single skill or feature
- Include a clear description of what changed and why

## Skill Structure

Each skill must follow this structure:

```
skill-name/
└── README.md
```

Every skill README should include these sections:

| Section | Required | Description |
|---------|----------|-------------|
| Key Capabilities | Yes | Bullet list of what the skill does |
| Workflow | Yes | Numbered step-by-step execution flow |
| Activation Triggers | Yes | Natural language phrases that invoke the skill |
| Configuration | Yes | Environment variables and settings |
| Scoring Methodology | Yes | Algorithms and formulas with clear documentation |
| Output Formats | Yes | What deliverables the skill produces |
| Integration Points | Yes | Tools and platforms the skill connects with |
| Example Usage | Yes | 3 practical natural language command examples |

## Code of Conduct

Be respectful, constructive, and collaborative. We're all here to build better marketing tools.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
