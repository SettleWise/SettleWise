# Architecture decision records

## When to use an ADR

Use an ADR for a durable technical or process decision whose reasoning needs to outlive a single
feature. Examples include a chosen integration pattern, data ownership boundary, authentication
approach, API compatibility policy, or team-wide tooling decision.

Do **not** create an ADR for ordinary feature requirements, implementation tasks, bug fixes,
chores, or refactors. Those belong in a Kiro feature, bug, or quick spec when they need planning;
otherwise use a normal GitHub issue and PR. An ADR explains a lasting decision and its trade-offs;
it does not replace the requirements, design, and tasks required to implement that decision.

When a feature implements a lasting decision, create both artifacts: an ADR for the decision and a
Kiro spec for the feature work. For example, record a move from session cookies to JWTs in an ADR,
then use a Kiro spec to define and plan the authentication migration.

Create files as `docs/adr/NNNN-short-title.md`, using consecutive four-digit numbers. Link each
ADR from the relevant feature specs and implementation PRs. ADRs are reviewed through pull
requests and are immutable once accepted; supersede an old record with a newer ADR instead of
rewriting its decision.

Copy [`TEMPLATE.md`](TEMPLATE.md) for each new record.
