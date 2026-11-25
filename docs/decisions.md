# Decisions

Format: `### Title` then one line each for **Context**, **Decision**, **Why**, **Consequences**.

### GitHub Actions cron instead of Airflow
- Context: need a scheduled collector with minimal infrastructure.
- Decision: use GitHub Actions cron.
- Why: free for public repos, no orchestrator to run or maintain.
- Consequences: cron can be delayed; no complex DAGs. Scheduling was later moved to AWS (see below).

### LightGBM global model
- Context: little per-station history at the start.
- Decision: train one global model across all stations.
- Why: shares patterns across stations; simpler to serve.
- Consequences: station identity must be a feature; per-station calibration can come later.

### Time-based validation
- Context: forecasting future availability.
- Decision: validate on later time blocks, never random splits.
- Why: random splits leak future information and overstate skill.
- Consequences: metrics reflect forward forecasting; need enough weeks of data.

### Postgres free tier for storage
- Context: need durable storage for scheduled collection.
- Decision: use a free Postgres tier.
- Why: SQL is familiar, cheap, and fits time-stamped observations.
- Consequences: limits on connections/retention; never commit `DATABASE_URL` (use env vars, GitHub Secrets or Lambda env vars).

### CityBikes v2 feed and 10-minute polling
- Context: need a first station-status source and polling cadence.
- Decision: use the CityBikes v2 `bicing` network endpoint; poll every 10 minutes.
- Why: no API key, 545 stations; revised from 15 minutes to get finer temporal resolution and more training points.
- Consequences: roughly 78k rows/day at 544–545 stations, so monitor free-tier storage and add retention if needed; delayed or missed scheduler runs create gaps; validate `+00:00Z` timestamps and use top-level `id` as station key.

### EventBridge Scheduler + Lambda instead of GitHub Actions cron
- Context: GitHub Actions fired ~3 of ~150 expected 10-minute runs in a day; cron syntax was valid and GitHub documents load-related delays/drops.
- Decision: run the collector as an AWS Lambda invoked by EventBridge Scheduler `rate(10 minutes)` in the project region `eu-north-1`; keep GitHub Actions `workflow_dispatch` only.
- Why: reliable timing and retries, Python code reused unchanged, and it builds the AWS skills already in the plan.
- Consequences: `DATABASE_URL` now lives in a Lambda environment variable; the deployment zip excludes `pandas`; new-experience accounts are locked to their assigned region, so Supabase Frankfurt is accessed cross-region.
