# Bicing availability forecaster

> Result: MAE vs best baseline — _to be filled_

## Architecture

Data collection is handled outside GitHub Actions: an AWS Lambda (`bicing-collector`) runs every 10 minutes via Amazon EventBridge Scheduler (project region `eu-north-1`) and writes station observations to Supabase Postgres. GitHub Actions keeps only a manual `workflow_dispatch` trigger for debugging.

## How to run

## Modeling

## Deployment

## Next steps
