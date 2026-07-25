# SettleWise

SettleWise is an agentic relocation assistant that helps people move to and settle in a new
city with more confidence. It pulls in information from maps, Reddit, YouTube, local news,
housing sources, and city resources to compare neighborhoods based on budget, commute, safety,
lifestyle, and daily needs, then builds a personalized move-in plan (housing research, local
setup tasks, transportation, groceries, healthcare, and social integration).

## Project layout

```
SettleWise/
├── frontend/   # Next.js + React + Tailwind CSS (TypeScript)
├── backend/    # FastAPI + Pydantic (Python)
├── .kiro/
│   ├── specs/      # Kiro feature requirements, designs, and task plans
│   └── steering/   # Shared Kiro product, stack, structure, and workflow context
├── docs/
│   ├── adr/        # Architecture Decision Records (durable technical/process decisions)
│   ├── specs/      # Kiro spec review and approval workflow documentation
│   └── sdd-tool-comparison.md
├── .pre-commit-config.yaml
└── README.md
```

## Prerequisites

- Node.js 20+ and npm
- Python 3.11+
- [pre-commit](https://pre-commit.com/) (installed via the backend's dev dependencies, see below)

## Backend (FastAPI)

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -e ".[dev]"

cp .env.example .env              # optional, defaults already work locally

uvicorn app.main:app --reload --port 8000
```

The API will be available at `http://localhost:8000` (interactive docs at `/docs`,
health check at `/health`).

### Backend tooling

```bash
# from backend/, with the venv activated
pytest              # run tests
ruff check .        # lint
black .             # format
```

## Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

The app will be available at `http://localhost:3000`.

### Frontend tooling

```bash
# from frontend/
npm run lint          # ESLint
npm run format         # Prettier (write)
npm run format:check   # Prettier (check only)
```

## Running both together

Run the backend and frontend commands above in two separate terminals. By default the
backend allows CORS requests from `http://localhost:3000`, so the frontend can call the
API directly once both are running.

## Pre-commit hooks

This repo uses [pre-commit](https://pre-commit.com/) to run Ruff/Black on `backend/` and
ESLint/Prettier on `frontend/` before each commit.

One-time setup (uses the backend venv, which already includes `pre-commit` as a dev
dependency):

```bash
cd backend
python3 -m venv .venv        # if you haven't already
source .venv/bin/activate
pip install -e ".[dev]"

cd ..
./backend/.venv/bin/pre-commit install
```

After that, the hooks run automatically on `git commit`. You can also run them manually
against the whole repo:

```bash
./backend/.venv/bin/pre-commit run --all-files
```

## Spec-driven development

SettleWise uses Kiro for spec-driven development. Kiro feature artifacts are committed under
`.kiro/specs/` and reviewed in GitHub before implementation. See
[`docs/specs/README.md`](docs/specs/README.md) for the team workflow and
[`docs/sdd-tool-comparison.md`](docs/sdd-tool-comparison.md) for the tool decision.

Use a Kiro spec for new capabilities, material behavior changes, API/data changes, integrations,
or security/privacy work. Use a Kiro bug or quick spec when a smaller change needs investigation
or a plan. Do not create a spec for trivial typos, routine chores, or behavior-preserving refactors;
use a normal GitHub issue and PR instead.

## Architecture decision records

`docs/adr/` contains Architecture Decision Records (ADRs): short, permanent notes explaining an
important technical or process decision, why it was made, alternatives considered, and its
consequences. For example, [`0001-adopt-kiro-sdd.md`](docs/adr/0001-adopt-kiro-sdd.md) records
why the team chose Kiro for spec-driven development.

Create an ADR for durable decisions such as authentication architecture, data ownership, API
compatibility, or team tooling. Do not use ADRs for ordinary feature requirements; those belong in
`.kiro/specs/` when planning is needed, or in a normal GitHub issue for routine work. If a feature
implements a durable decision, create both: an ADR for the decision and a Kiro spec for its
requirements, design, and tasks. See [`docs/adr/README.md`](docs/adr/README.md) for the format and
numbering rules.
