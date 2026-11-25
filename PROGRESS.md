# Progress

## Current state
- Project root: `bicing/`; local `main` at `c61fe61`; changes below are uncommitted and ready for a PR.
- Python 3.14.4 venv at `../venv`; `.env` exists locally (gitignored) with `DATABASE_URL`.
- Phase 1 (collection) nearly done: collection now runs on AWS, not GitHub Actions cron.
- Feed: CityBikes v2 `bicing`, 10-min cadence (see `docs/decisions.md`). Supabase Postgres (Frankfurt session pooler).
- AWS: new experience/project owner via GitHub; project region `eu-north-1`; Lambda `bicing-collector` + EventBridge Scheduler `rate(10 minutes)`.
- DB was truncated on 2026-11-25; currently 0 rows, awaiting the first scheduled Lambda batch.

## Done
- [x] Scaffold directories and empty `src/` placeholders
- [x] Local-only notes; tracked docs, ignores, Phase 1 requirements
- [x] `git init -b main`; commits `a0d69d6`, `25397a5`, `86e6dbe`, `fda5b63`
- [x] SSH auth configured; `main` pushed to GitHub
- [x] First six PRs opened and merged
- [x] Bicing feed inspected; fields, station keys and cadence options identified
- [x] Align `requirements.txt` with psycopg v3 driver
- [x] Implement `src/collect.py`: fetch JSON, validate keys, parse timestamps, write via SQLAlchemy using `DATABASE_URL` from the environment
- [x] Configure free Postgres instance (Supabase); secrets only in env vars, GitHub Secrets or the Lambda env var
- [x] Diagnose GitHub Actions cron: valid YAML, but GitHub delays/drops most 10-minute runs
- [x] Add AWS Lambda collector + EventBridge Scheduler in `eu-north-1`; manual test returned `{"rows": 544}`
- [x] Remove GitHub Actions `schedule`; keep `workflow_dispatch` for manual runs
- [x] Wipe DB for a clean 10-minute time series

## To do
- [x] Delete stale `docs/neutral-progress` branch locally and on GitHub
- [x] Choose polling cadence (10 min) and record the decision
- [x] Add CityBikes v2 feed/cadence decision entry to `docs/decisions.md`
- [x] Verify whether PR #6 cron rewrite re-registers the schedule (it did not reliably)
- Verify first scheduled Lambda batch in Postgres
- Continue 3-4 weeks of collection before modeling
- Later: baselines + LightGBM with time-based validation in MLflow, FastAPI/Docker, AWS ECR + App Runner

## Open problems
- `ruff` not in Phase 1 requirements; add with CI
- No tests yet (`tests/` is empty)
- AWS CLI not installed; Lambda updates currently via console + rebuilt zip
- Lambda zip excludes `pandas`; consider a tracked `requirements-lambda.txt` to make rebuilds repeatable
- New AWS experience locks the project to `eu-north-1`; Supabase is in Frankfurt (acceptable latency)
