import logging
import os
from datetime import datetime, timezone

import requests
from dotenv import load_dotenv
from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
)
from sqlalchemy.dialects.postgresql import insert

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ENDPOINT = "https://api.citybik.es/v2/networks/bicing"

metadata = MetaData()

station_observations = Table(
    "station_observations",
    metadata,
    Column("station_id", String, primary_key=True),
    Column("observed_at", DateTime(timezone=True), primary_key=True),
    Column("station_timestamp", DateTime(timezone=True)),
    Column("name", String),
    Column("latitude", Float),
    Column("longitude", Float),
    Column("free_bikes", Integer),
    Column("empty_slots", Integer),
)


def fetch_payload():
    response = requests.get(ENDPOINT, timeout=30)
    response.raise_for_status()  # raises an exception for bad HTTP status
    payload = response.json()

    stations = payload.get("network", {}).get("stations")
    if not isinstance(stations, list):
        raise ValueError("Expected payload['network']['stations'] to be a list")

    logger.info("Fetched %s stations", len(stations))
    return payload

def parse_timestamp(value):
    """Parse a CityBikes timestamp into a UTC-aware datetime."""
    if value is None:
        return None
    value = str(value).strip()
    if value.endswith("+00:00Z"):
        value = value[:-1]  # "+00:00Z" -> "+00:00"
    elif value.endswith("Z"):
        value = value[:-1] + "+00:00"  # "Z" -> "+00:00"
    dt = datetime.fromisoformat(value)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt
    
def parse_observations(payload, observed_at):
    stations = payload["network"]["stations"]
    rows = []

    for station in stations:
        station_id = station.get("id")
        free_bikes = station.get("free_bikes")
        empty_slots = station.get("empty_slots")
        latitude = station.get("latitude")
        longitude = station.get("longitude")

        # Required fields: skip incomplete rows instead of crashing the whole batch
        if station_id is None:
            logger.warning("Skipping station without id: %s", station)
            continue
        if any(value is None for value in [free_bikes, empty_slots, latitude, longitude]):
            logger.warning("Skipping station %s: missing required fields", station_id)
            continue

        row = {
            "station_id": str(station_id),
            "observed_at": observed_at,
            "station_timestamp": parse_timestamp(station.get("timestamp")),
            "name": station.get("name"),
            "latitude": float(latitude),
            "longitude": float(longitude),
            "free_bikes": int(free_bikes),
            "empty_slots": int(empty_slots),
        }
        rows.append(row)

    return rows


def write_observations(engine, rows):
    if not rows:
        logger.info("No rows to write")
        return

    stmt = insert(station_observations).values(rows)
    stmt = stmt.on_conflict_do_nothing(index_elements=["station_id", "observed_at"])

    with engine.begin() as conn:
        result = conn.execute(stmt)
        # rowcount can be -1 on some drivers; don't rely on it being exact
        logger.info("Insert executed for %s rows", len(rows))


def main():
    load_dotenv()
    database_url = os.environ["DATABASE_URL"]
    engine = create_engine(database_url)
    metadata.create_all(engine)

    observed_at = datetime.now(timezone.utc)
    payload = fetch_payload()
    rows = parse_observations(payload, observed_at)
    write_observations(engine, rows)
    logger.info("Collected %s station observations", len(rows))


if __name__ == "__main__":
    main()
