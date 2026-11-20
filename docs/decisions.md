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
