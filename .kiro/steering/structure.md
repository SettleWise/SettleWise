---
inclusion: always
---

# Repository structure

- `frontend/` contains the Next.js application. App Router source is in `frontend/src/app/`.
- `backend/app/` contains the FastAPI application; routes are organized under
  `backend/app/api/routes/`.
- `backend/tests/` contains backend tests.
- `.kiro/specs/` contains versioned feature requirements, designs, and task plans.
- `.kiro/steering/` contains the Kiro workspace context shared by the team.
- `docs/adr/` contains durable architecture decision records.

Keep a feature's changes focused. Update tests and relevant documentation in the same change.
