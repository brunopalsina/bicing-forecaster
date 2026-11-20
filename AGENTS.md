# AGENTS.md

## Project context
Goal: predict bikes available at each Bicing station 30 and 60 minutes ahead.
Owner: junior data scientist (MSc Data Science; physics/nanotech background). Strong Python/pandas/scikit-learn; learning Git, Docker and AWS.

Stack:
- Scheduled collector: GitHub Actions cron -> free Postgres.
- Features/model: pandas + LightGBM, time-aware validation, MLflow tracking.
- Serving: FastAPI in Docker, deployed on AWS (ECR + App Runner).
- CI: pytest + ruff.

Definition of done: public repo with PRs, 3-4 weeks of collected data, baselines vs model in MLflow, containerized API deployed once, README opens with a one-line result (MAE vs best baseline), and a learning log.

## Structure
```
bicing/
├── src/
│   ├── collect.py      # empty placeholder (you write the first collector)
│   ├── features.py     # empty placeholder
│   ├── train.py        # empty placeholder
│   └── api.py          # empty placeholder
├── tests/
├── notebooks/
├── models/
├── docs/
│   └── decisions.md
├── .github/workflows/
├── AGENTS.md
├── PROGRESS.md
├── LEARNING_LOG.md
├── README.md
├── .gitignore
├── .dockerignore
└── requirements.txt
```

The Python venv lives outside the repo at `../venv` (`/home/bruno/agentcoding/venv`, Python 3.14.4). Activate it from the project root with `source ../venv/bin/activate`. Do not create a new venv.

## Commands
- `source ../venv/bin/activate` — activate the existing venv
- `python -m pip install -r requirements.txt` — install Phase 1 dependencies
- `python -m pytest` — run tests (once tests exist)
- `ruff check src tests` — lint (ruff will be added with CI later)
- `git status` — inspect repo state before committing

## Working rules
1. Explain what you plan to do before making changes, and wait for my OK on anything beyond the scaffolding in this message.
2. I write the code for the things I'm trying to learn: first Git commits, branches and pull requests, the first collector, the first Dockerfile, the first AWS deployment. For those, guide me with explanations and review my work; don't write the solution unless I ask.
3. You may draft boilerplate (tests, CI YAML, README structure, lint config), but show me the diff and explain it so I understand it.
4. Never put secrets (keys, DATABASE_URL, passwords) in files. Use environment variables and GitHub Secrets.
5. Keep PROGRESS.md short and current. Record the reasons behind decisions.
6. Features used in training must be computable at serving time in the API.
