# Spec-driven development tool decision

**Decision:** Adopt **Kiro** as SettleWise's spec-driven development tool. Commit Kiro artifacts
under `.kiro/` and use GitHub pull requests for approval and traceability.

## Side-by-side comparison

| Tool | Workflow and artifacts | Agent experience | Strength | Limitation | Decision |
| --- | --- | --- | --- | --- | --- |
| **Kiro** | Requirements → design → tasks → verified execution in `.kiro/specs/` | Native IDE, CLI, and web spec agent; `/spec new` and `/spec run` | Most complete and polished end-to-end SDD experience | Adopts the Kiro ecosystem | **Selected** |
| **OpenSpec** | Iterative proposals and capability spec deltas in `openspec/` | Native integrations with Codex, Claude Code, Cursor, Copilot, and others | Best open-source, agent-neutral option; strong for existing codebases | Team collaboration features are still developing | Runner-up |
| **GitHub Spec Kit** | Spec → plan → tasks → implement, with Markdown artifacts | Agent-specific `/speckit.*` commands or skills | Most configurable workflow; extensive integrations, extensions, and governance options | More of a toolkit to configure than a cohesive SDD product | Not selected |
| **BMAD Method** | Full agile lifecycle with multi-agent planning, architecture, development, and QA artifacts | Specialized AI personas and 34+ workflows | Most comprehensive option for large, process-heavy organizations | Excessive ceremony for SettleWise's current product development | Not selected |
| **IntentSpec** | A validated `intent.md` with objectives, outcomes, constraints, and edge cases | Agent-neutral context file | Minimal, portable, and easy to understand | Insufficient structure for complex feature design and task execution | Not selected |
| **Tessl SDD** | Previously spec, approval, implementation, and verification with test links | Registry/agent-skill approach | Strong spec-to-test concept | No longer positioned as an SDD-first product | Not selected |

## Why Kiro

Kiro gives the team one coherent workflow rather than a set of templates or commands to assemble.
It gathers requirements, produces a technical design, decomposes work into tasks, and runs the
approved plan with verification. The same spec files work in Kiro's IDE, CLI, and web surfaces,
while Git preserves review history and GitHub supplies the human approval gate.

This decision is about the development workflow, not code hosting: GitHub remains the system for
pull requests, implementation issues, and branch protection.

## References

- [Kiro specs](https://kiro.dev/docs/cli/v3/specs/)
- [OpenSpec](https://openspec.dev/)
- [GitHub Spec Kit](https://github.github.com/spec-kit/)
- [BMAD Method](https://github.com/bmadcode/BMAD-METHOD)
- [Spec-driven tool landscape](https://specdriven.com/landscape/)
