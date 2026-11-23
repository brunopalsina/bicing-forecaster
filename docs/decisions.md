# Decisions

Format: `### Title` then one line each for **Context**, **Decision**, **Why**, **Consequences**.

### GitHub Actions cron instead of Airflow
- Context: need a scheduled collector with minimal infrastructure.
- Decision: use GitHub Actions cron.
- Why: free for public repos, no orchestrator to run or maintain.
- Consequences: cron can be delayed; no complex DAGs.

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
- Consequences: limits on connections/retention; never commit `DATABASE_URL` (use env vars and GitHub Secrets).

### CityBikes v2 feed and 15-minute polling
- Context: need a first station-status source and polling cadence.
- Decision: use the CityBikes v2 `bicing` network endpoint; poll every 15 minutes.
- Why: no API key, 545 stations; most trips take slightly under 15 minutes, so 15-minute snapshots may capture net bicycle flow better than 10 minutes while staying within GitHub Actions cron limits.
- Consequences: coarser than 10-minute polling; delayed or missed GitHub Actions runs create larger gaps; validate `+00:00Z` timestamps and use top-level `id` as station key.
