import os

from collect import collect_once


def lambda_handler(event, context):
    rows = collect_once(os.environ["DATABASE_URL"])
    return {"rows": len(rows)}
