# Kiro feature-spec workflow

SettleWise uses Kiro for spec-driven development. Kiro keeps each feature's requirements,
technical design, and implementation tasks under `.kiro/specs/<feature-slug>/`. These files are
the canonical record of intended behavior and must be committed with the repository.

## When to use a Kiro spec

Use a Kiro feature spec when work introduces a new user-facing capability or materially changes
existing behavior. Also use one for API or data-model changes, integrations, and changes with
security or privacy impact. The spec records the intended requirements, technical design, and
implementation tasks before code is written.

Use a Kiro bug or quick spec when a bug or smaller change still needs investigation, explicit
acceptance criteria, or a short implementation plan.

Do **not** create a Kiro spec for a trivial typo, routine dependency update, simple chore, or
strictly internal refactor that does not change behavior and needs no design decision. Create a
normal GitHub issue and PR instead. A Kiro spec is not an Architecture Decision Record; use an ADR
only when the work creates or changes a durable technical or process decision.

## Authoring and approval

1. In Kiro, run `/spec new <feature-slug>` and select the appropriate spec type.
2. Work through the requirements, design, and task phases. Review and refine each artifact before
   allowing Kiro to proceed to the next phase.
3. Open a spec-only PR containing `.kiro/specs/<feature-slug>/`. State in the PR's
   **Specification** section that it is a spec review.
4. Product lead approves the problem, scope, user experience, and acceptance criteria. Technical
   lead approves the design, contracts, risk handling, and test strategy.
5. Merge after both approvals. The spec on the default branch is approved and becomes the source
   of truth.
6. Create linked implementation issues when needed. Start a fresh implementation branch, then run
   `/spec run <feature-slug>` to execute the approved task plan. Every issue and implementation PR
   links to the approved Kiro spec.

Do not begin implementation until the feature spec is approved. If implementation changes the
agreed behavior or technical approach, update the Kiro spec in a new PR and obtain re-approval.

## Required Kiro artifacts

Each feature spec directory contains the Kiro-generated artifacts below. Do not rename or move
them; Kiro uses this structure across its IDE, CLI, and web interfaces.

```
.kiro/specs/<feature-slug>/
├── requirements.md
├── design.md
└── tasks.md
```

Kiro's workspace standards are committed under `.kiro/steering/`. They give every Kiro session
the same product, technology, structure, and SDD workflow context.

## GitHub configuration

Repository administrators must configure the default branch to require pull-request reviews and
require approval from both the product lead and technical lead (or their designated teams).
GitHub's review requirement is the enforcement point; this repository documents the workflow but
cannot grant or require reviewer permissions itself. Use protected-branch settings or rulesets,
and add the appropriate people or teams as required reviewers.

Use GitHub Projects only to plan and track delivery. It is not a substitute for the approved
Kiro spec.
