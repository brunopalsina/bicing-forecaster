# Progress

## Current state
- Project root: `bicing/`; git repo with `main` pushed to GitHub, branch `feature/feed-notes` checked out.
- Python 3.14.4 venv at `../venv` (activated for tooling).
- `origin/main` is at `25397a5`; `feature/feed-notes` points there too, with no unique commits yet.
- Phase 1 in progress.

## Done
- [x] Scaffold folders and empty `src/` placeholders
- [x] Write local-only AGENTS.md, plus PROGRESS.md, docs/decisions.md, LEARNING_LOG.md, README skeleton, ignores, Phase 1 requirements
- [x] `git init -b main`; first commit `a0d69d6`
- [x] Untrack AGENTS.md (`git rm --cached`) and commit `25397a5`; it stays local and is gitignored
- [x] Generate SSH key, add it to GitHub, push `main` to `origin`

## In progress
- Phase 1: Git and data collection
  - Step 5: first PR from `feature/feed-notes` into `main`
    - Branch created off `25397a5`; not pushed yet
    - This PROGRESS.md update is the intended first branch change (currently uncommitted)
  - After the PR: explore the Bicing feed and write the first collector (by you, with review)

## Next
- Stage + commit this PROGRESS.md edit, push `feature/feed-notes`, open PR, merge, clean up local branch
- Explore Bicing API/feed; write the first collector (you) with my review
- Collect 3-4 weeks of data via GitHub Actions cron into free Postgres
- Baselines vs LightGBM with time-based validation, tracked in MLflow
- FastAPI in Docker, deployed once to AWS ECR + App Runner

## Open problems
- AGENTS.md is gone from the current tree and future commits, but still exists in remote history via `a0d69d6` (pushed with main). Purging it fully needs a history rewrite + force push; decide before collaborators arrive.
- Bicing feed/API details not explored yet.
- Free Postgres provider not chosen yet.
- `ruff` is not in Phase 1 requirements; add it when CI is set up.
- Parent folder `chown` issue resolved.
