# ADR 0001: Adopt Kiro for spec-driven development

| Field | Value |
| --- | --- |
| Status | Accepted |
| Date | 2026-07-24 |
| Deciders | SettleWise team |
| Related specs | `.kiro/specs/` |
| Supersedes | None |
| Superseded by | None |

## Context

SettleWise needs a repeatable, AI-assisted process that turns a feature idea into reviewed
requirements, technical design, implementation tasks, and verified code. The team evaluated Kiro,
OpenSpec, GitHub Spec Kit, BMAD Method, IntentSpec, and Tessl SDD.

## Decision

Use Kiro as the canonical SDD tool. Commit workspace steering under `.kiro/steering/` and each
feature's generated requirements, design, and tasks under `.kiro/specs/`. Use GitHub pull requests
for product and technical approval before running an implementation plan.

The detailed comparison is in [`docs/sdd-tool-comparison.md`](../sdd-tool-comparison.md).

## Consequences

The team uses `/spec new <feature-slug>` to author feature specs and `/spec run <feature-slug>`
only after approval. Developers need Kiro installed to author and execute specs, while the Markdown
artifacts remain visible and reviewable to every contributor in GitHub.

## Alternatives considered

OpenSpec is the runner-up for its agent neutrality and strong iterative workflow. GitHub Spec Kit
is capable and highly configurable, but Kiro provides a more cohesive out-of-the-box experience.
BMAD Method, IntentSpec, and Tessl SDD were not selected for the reasons recorded in the comparison.
