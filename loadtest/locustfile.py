"""
Load test for the telemetry app, using Locust.

Install:   pip install locust
Run (UI):  locust -f loadtest/locustfile.py --host http://localhost:8080
Run (CLI): locust -f loadtest/locustfile.py --host http://YOUR-URL \
             --headless -u 50 -r 5 -t 2m --csv docs/measurements/stageB_u50

Use the SAME numbers (users, spawn rate, duration) for every stage so the
results can be compared fairly. Keep the CSV files, they go into the report.
"""
import random

from locust import HttpUser, task, between


class TelemetryUser(HttpUser):
    wait_time = between(0.5, 1.5)

    def on_start(self):
        self.vehicle = f"LOAD-{random.randint(1, 10000):05d}"

    @task(5)
    def send_reading(self):
        self.client.post(
            "/api/telemetry",
            json={
                "vehicle_id": self.vehicle,
                "speed_kmph": random.uniform(0, 100),
                "fuel_or_battery_pct": random.uniform(10, 100),
                "engine_temp_c": random.uniform(70, 105),
                "lat": 18.5 + random.random() / 10,
                "lon": 73.8 + random.random() / 10,
            },
            name="POST /api/telemetry",
        )

    @task(2)
    def view_latest(self):
        self.client.get("/api/latest", name="GET /api/latest")

    @task(1)
    def view_history(self):
        self.client.get(f"/api/history/{self.vehicle}", name="GET /api/history")
