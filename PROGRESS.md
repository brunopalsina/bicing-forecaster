# Progress

## Current state
- Project root: `bicing/` (fresh scaffold, no commits yet).
- Python 3.14.4 venv at `../venv`, activated for tooling.
- Phase 1 in progress.

## Done
- [x] Scaffold folders and empty `src/` placeholders
- [x] Write AGENTS.md, PROGRESS.md, docs/decisions.md, LEARNING_LOG.md, README skeleton, ignores, Phase 1 requirements
- [x] `git init -b main` (no commits, no remote)

## In progress
- Phase 1: Git and data collection
  - Configure git identity, first commit, GitHub repo, push, first branch + PR (by me)
  - Explore the Bicing feed and write the first collector (by me)

## Next
- Collect 3-4 weeks of data via GitHub Actions cron into free Postgres
- Baselines vs LightGBM with time-based validation, tracked in MLflow
- FastAPI in Docker, deployed once to AWS ECR + App Runner

## Open problems
- Bicing feed/API details not explored yet.
- Free Postgres provider not chosen yet.
- `ruff` is not in Phase 1 requirements; add it when CI is set up.
- Parent folder needed a `chown` fix before scaffolding; now resolved.
