---
name: create-team-pr
description: Create consistent, review-ready GitHub pull requests for a team.
---

# Create Team PR

Prepare a truthful PR from the current branch, validate it, and create or update it with `gh`.

## Workflow

1. Read applicable repository instructions and `.github/pull_request_template.md`.
2. Inspect `git status`, the current branch, its upstream, and existing PRs for the branch.
3. Fetch the target branch and review `git diff <base>...HEAD` plus branch-only commits.
4. Identify the linked issue or ticket from the request, branch name, or commit history. Never invent one.
5. Run the narrowest relevant tests, lint, formatting checks, builds, and security checks.
6. Confirm no secrets, generated artifacts, debug code, unrelated changes, or accidental dependency updates are included.
7. Write the title and body using the required template sections.
8. Create or update the PR with `gh`. Preserve the branch unless explicitly asked to delete it.
9. Return the PR URL, checks performed, failures or skipped checks, and reviewer attention areas.

Do not merge, force-push, bypass protection, or approve a PR unless explicitly requested.

## Branch naming

Use `BR-<GitHub-issue-number>-<kebab-case-feature-name>` for feature branches.

Example: `BR-59-add-spec-driven-development-template`

The issue number in the branch name is the linked ticket. Do not invent an issue number; create
the branch only when the corresponding GitHub issue exists or is explicitly provided.

## Title

Use a concise imperative title. Preserve a ticket prefix when the team uses one.

Examples:

- `BR-2: Add CI pipeline`
- `Fix duplicate settlement notifications`

## Body

Use every section. Write `Not applicable` rather than deleting a section.

```markdown
## What
- Describe the user-visible and technical changes.

## Why
- Explain the problem, goal, and linked issue.

## How
- Summarize important implementation decisions and trade-offs.

## Testing
- `command` — passed
- Manual verification — describe result

## Security
- Describe changes to permissions, secrets, authentication, user data, dependencies, or attack surface.
- State `No known security impact` only after checking.

## Screenshots
- Add before/after evidence for UI changes, otherwise `Not applicable`.

## Risks and Follow-ups
- Document rollout concerns, known limitations, migrations, and intentionally deferred work.

## Checklist
- [ ] Scope is focused and linked to an issue when applicable
- [ ] Tests, lint, formatting, and build checks pass
- [ ] Documentation and examples are updated
- [ ] No secrets or sensitive data are committed
- [ ] Security and dependency impacts are reviewed
- [ ] Breaking changes and migrations are documented
```

## Accuracy rules

- Base claims only on the diff, commands, and repository context.
- Never mark a check as passed unless it ran successfully; label skipped checks with the reason.
- Distinguish blocking issues from non-blocking follow-ups.
- Mention migrations, environment variables, API changes, and dependency changes explicitly.
- Keep the description concise enough to review quickly.

## GitHub CLI

Check for an existing PR before creating one:

```bash
gh pr view --json number,url,state,title,body
```

Write the body to a temporary file, then create or update:

```bash
gh pr create --base <base> --head <branch> --title "<title>" --body-file <body-file>
gh pr edit <number> --title "<title>" --body-file <body-file>
```
