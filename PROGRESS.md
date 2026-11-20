# Progress

## Current state
- Project root: `bicing/`; git repo with `main` on GitHub, `origin/main` at `25397a5`.
- `origin/feature/feed-notes` at `aed7190` ("Add feed exploration notes"); PR into `main` opened, merge pending.
- Python 3.14.4 venv at `../venv`.
- Phase 1 (Git and data collection) in progress.
- Feed exploration completed: CityBikes v2 `bicing` endpoint selected as first source (no key, 545 stations); GBFS and official Open Data BCN retained as later alternatives.

## Done
- [x] Scaffold directories and empty `src/` placeholders
- [x] Local-only `AGENTS.md`; tracked docs, ignores, Phase 1 requirements
- [x] `git init -b main`; commits `a0d69d6`, `25397a5`
- [x] SSH auth configured; `main` pushed to GitHub
- [x] First feature branch created and pushed; PR opened
- [x] Bicing feed inspected; fields, station keys and cadence options identified

## To do
- Confirm/merge the open PR, delete `feature/feed-notes`, pull `main`
- Choose polling cadence (10 or 15 min) and record the decision
- Add CityBikes v2 feed/cadence decision entry to `docs/decisions.md`
- Implement `src/collect.py`: fetch JSON, validate key relationships, parse timestamps, write observations via SQLAlchemy using `DATABASE_URL` from the environment
- Configure free Postgres instance; store connection details only as GitHub Secrets or local env vars
- Add scheduled GitHub Actions workflow and verify first rows in Postgres
- Continue 3-4 weeks of collection before modeling
- Later: baselines + LightGBM with time-based validation in MLflow, FastAPI/Docker, AWS ECR + App Runner

## Open problems
- `AGENTS.md` remains in remote history via `a0d69d6`; full removal requires history rewrite + force push
- Free Postgres provider not selected
- `ruff` not in Phase 1 requirements; add with CI
- Feed timestamp parsing needs validation (`+00:00Z` suffix)
- `extra.uid` is not unique; use top-level `id` as station key
- Parent folder ownership issue resolved
