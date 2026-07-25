---
inclusion: always
---

# Spec-driven development rules

For a material feature or behavior change, start with `/spec new <feature-slug>` and complete the
requirements, design, and tasks phases before implementation. Requirements must be testable;
design must cover affected frontend/backend contracts, data changes, risks, and alternatives; and
tasks must include verification.

Do not run `/spec run <feature-slug>` until the feature spec has been committed, approved by the
product and technical leads in GitHub, and merged to the default branch. If implementation changes
an approved requirement or design decision, update the spec and obtain another approval first.

Use Kiro-generated files at `.kiro/specs/<feature-slug>/requirements.md`, `design.md`, and
`tasks.md` as the feature source of truth. Link each implementation issue and PR to that directory.
