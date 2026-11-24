# Progress

## Current state
- Project root: `bicing/`; `main` up to date with `origin/main`; local uncommitted changes in `PROGRESS.md`, `docs/decisions.md`, `src/collect.py`.
- PR #1 (`feature/feed-notes`) and PR #2 (`docs/neutral-progress`) merged; stale `docs/neutral-progress` branch deleted.
- Python 3.14.4 venv at `../venv`; `.env` exists locally (gitignored) with `DATABASE_URL`.
- Phase 1 (Git and data collection) in progress.
- Feed: CityBikes v2 `bicing`, 10-min cadence (see `docs/decisions.md`). Supabase Postgres (session pooler) selected; connection tested. `src/collect.py` implemented and ran successfully (`SELECT 1` / insert path).

## Done
- [x] Scaffold directories and empty `src/` placeholders
- [x] Local-only notes; tracked docs, ignores, Phase 1 requirements
- [x] `git init -b main`; commits `a0d69d6`, `25397a5`, `86e6dbe`, `fda5b63`
- [x] SSH auth configured; `main` pushed to GitHub
- [x] First two PRs opened and merged
- [x] Bicing feed inspected; fields, station keys and cadence options identified
- [x] Align `requirements.txt` with psycopg v3 driver

## To do
- [x] Delete stale `docs/neutral-progress` branch locally and on GitHub
- [x] Choose polling cadence (10 min) and record the decision
- [x] Add CityBikes v2 feed/cadence decision entry to `docs/decisions.md`
- [x] Implement `src/collect.py`: fetch JSON, validate key relationships, parse timestamps, write observations via SQLAlchemy using `DATABASE_URL` from the environment
- [x] Configure free Postgres instance (Supabase); store connection details only as GitHub Secrets or local env vars
- [x] Add scheduled GitHub Actions workflow (10-min cron; file ready, push + secret pending)
- Verify first scheduled rows in Postgres
- Continue 3-4 weeks of collection before modeling
- Later: baselines + LightGBM with time-based validation in MLflow, FastAPI/Docker, AWS ECR + App Runner

## Open problems
- `ruff` not in Phase 1 requirements; add with CI
- `collect.py` changes are uncommitted; push after review/commit
- `DATABASE_URL` must be added as GitHub Secret before scheduled workflow
