"""
Vehicle telemetry dashboard (IT457, Group 29).

One small Flask app used in all three stages of our exercise:
  Stage A: runs in Docker on a laptop, database is a Postgres container
  Stage B: same containers on one EC2 machine (lift and shift)
  Stage C: same app, database moved to Amazon RDS (managed service)

The only thing that changes between stages is the DATABASE_URL setting.
If DATABASE_URL is not set, the app uses a local SQLite file so it can be
run quickly without Docker while developing.
"""
import os
import time
from datetime import datetime, timezone

from flask import Flask, jsonify, render_template, request

DATABASE_URL = os.environ.get("DATABASE_URL", "")
STAGE = os.environ.get("STAGE", "local")  # label shown on the dashboard

app = Flask(__name__)

USE_POSTGRES = DATABASE_URL.startswith("postgres")

if USE_POSTGRES:
    import psycopg2
    import psycopg2.extras
    PH = "%s"  # placeholder style for postgres
else:
    import sqlite3
    PH = "?"  # placeholder style for sqlite
    SQLITE_PATH = os.environ.get("SQLITE_PATH", "telemetry.db")


def get_conn():
    if USE_POSTGRES:
        return psycopg2.connect(DATABASE_URL)
    conn = sqlite3.connect(SQLITE_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create the table. Retries a few times because the database container
    may still be starting when the app starts."""
    last_error = None
    for _ in range(30):
        try:
            conn = get_conn()
            cur = conn.cursor()
            if USE_POSTGRES:
                cur.execute(
                    """CREATE TABLE IF NOT EXISTS readings (
                        id SERIAL PRIMARY KEY,
                        vehicle_id TEXT NOT NULL,
                        speed_kmph REAL,
                        fuel_or_battery_pct REAL,
                        engine_temp_c REAL,
                        lat REAL,
                        lon REAL,
                        recorded_at TIMESTAMPTZ NOT NULL
                    )"""
                )
                cur.execute(
                    "CREATE INDEX IF NOT EXISTS idx_readings_time "
                    "ON readings (recorded_at DESC)"
                )
            else:
                cur.execute(
                    """CREATE TABLE IF NOT EXISTS readings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        vehicle_id TEXT NOT NULL,
                        speed_kmph REAL,
                        fuel_or_battery_pct REAL,
                        engine_temp_c REAL,
                        lat REAL,
                        lon REAL,
                        recorded_at TEXT NOT NULL
                    )"""
                )
            conn.commit()
            conn.close()
            return
        except Exception as exc:  # database not ready yet
            last_error = exc
            time.sleep(1)
    raise RuntimeError(f"Could not connect to database: {last_error}")


def rows_to_dicts(cur, rows):
    if USE_POSTGRES:
        cols = [c[0] for c in cur.description]
        return [dict(zip(cols, r)) for r in rows]
    return [dict(r) for r in rows]


@app.route("/")
def index():
    return render_template("index.html", stage=STAGE)


@app.route("/health")
def health():
    """Used by load balancers and by us to check the app and database work."""
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.fetchone()
        conn.close()
        return jsonify(status="ok", stage=STAGE, db="postgres" if USE_POSTGRES else "sqlite")
    except Exception as exc:
        return jsonify(status="error", detail=str(exc)), 500


@app.route("/api/telemetry", methods=["POST"])
def add_reading():
    data = request.get_json(silent=True) or {}
    vehicle_id = data.get("vehicle_id")
    if not vehicle_id:
        return jsonify(error="vehicle_id is required"), 400
    now = datetime.now(timezone.utc)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        f"""INSERT INTO readings
            (vehicle_id, speed_kmph, fuel_or_battery_pct, engine_temp_c, lat, lon, recorded_at)
            VALUES ({PH},{PH},{PH},{PH},{PH},{PH},{PH})""",
        (
            vehicle_id,
            data.get("speed_kmph"),
            data.get("fuel_or_battery_pct"),
            data.get("engine_temp_c"),
            data.get("lat"),
            data.get("lon"),
            now if USE_POSTGRES else now.isoformat(),
        ),
    )
    conn.commit()
    conn.close()
    return jsonify(status="stored"), 201


@app.route("/api/latest")
def latest():
    """Latest reading for each vehicle."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """SELECT r.* FROM readings r
           JOIN (SELECT vehicle_id, MAX(id) AS max_id FROM readings GROUP BY vehicle_id) m
             ON r.id = m.max_id
           ORDER BY r.vehicle_id"""
    )
    rows = rows_to_dicts(cur, cur.fetchall())
    conn.close()
    for r in rows:
        r["recorded_at"] = str(r["recorded_at"])
    return jsonify(rows)


@app.route("/api/history/<vehicle_id>")
def history(vehicle_id):
    """Last 60 readings for one vehicle, used for the chart."""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        f"""SELECT speed_kmph, fuel_or_battery_pct, engine_temp_c, recorded_at
            FROM readings WHERE vehicle_id = {PH}
            ORDER BY id DESC LIMIT 60""",
        (vehicle_id,),
    )
    rows = rows_to_dicts(cur, cur.fetchall())
    conn.close()
    for r in rows:
        r["recorded_at"] = str(r["recorded_at"])
    rows.reverse()
    return jsonify(rows)


@app.route("/api/stats")
def stats():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*), COUNT(DISTINCT vehicle_id) FROM readings")
    total, vehicles = cur.fetchone()
    conn.close()
    return jsonify(total_readings=total, vehicles=vehicles, stage=STAGE)


init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
