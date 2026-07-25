---
inclusion: always
---

# Technology standards

- Frontend: Next.js 16, React 19, TypeScript, and Tailwind CSS 4 under `frontend/`.
- Backend: Python 3.11+, FastAPI, Pydantic, and Uvicorn under `backend/`.
- Keep frontend and backend contracts explicit. Document request/response, validation, error,
  authentication, persistence, and migration implications in Kiro feature specs.
- Use the repository's existing tools: ESLint and Prettier for frontend changes; Ruff, Black, and
  pytest for backend changes; pre-commit before commits.
- Never add secrets to source control. Use `backend/.env.example` for documented configuration.
