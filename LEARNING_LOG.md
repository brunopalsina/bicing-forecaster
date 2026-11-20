# Learning log

| Date | What I tried | What broke | Why | Fix |
| --- | --- | --- | --- | --- |
| 2026-11-20 | Check Python env before scaffolding | `python` not found; project folder root-owned | PATH lacked venv; parent dir owned by root | Activated `../venv/bin/activate`; ran `sudo chown bruno:bruno /home/bruno/agentcoding` |
