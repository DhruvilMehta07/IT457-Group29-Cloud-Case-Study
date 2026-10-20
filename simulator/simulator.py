"""
Telemetry simulator.

Pretends to be a small fleet of vehicles and sends one reading per vehicle
every few seconds to the app. It only uses the Python standard library, so
there is nothing to install.

Examples:
  python simulator/simulator.py                                  # 5 vehicles, local app
  python simulator/simulator.py --vehicles 50 --interval 1       # heavier load
  python simulator/simulator.py --url http://YOUR-EC2-IP/api/telemetry
"""
import argparse
import json
import math
import random
import time
import urllib.request

KINDS = ["Fleet Edge", "iRA", "Zconnect"]  # product names used in the Tata Motors case (commercial, passenger, electric)


def make_vehicle(i):
    return {
        "id": f"MH12-{KINDS[i % 3].replace(' ', '')}-{i:03d}",
        "lat": 18.52 + random.uniform(-0.05, 0.05),
        "lon": 73.85 + random.uniform(-0.05, 0.05),
        "speed": random.uniform(20, 60),
        "level": random.uniform(60, 100),
        "temp": random.uniform(70, 90),
        "heading": random.uniform(0, 2 * math.pi),
    }


def step(v, dt):
    v["speed"] = max(0, min(110, v["speed"] + random.uniform(-6, 6)))
    v["heading"] += random.uniform(-0.2, 0.2)
    km = v["speed"] * dt / 3600
    v["lat"] += (km / 111) * math.cos(v["heading"])
    v["lon"] += (km / 111) * math.sin(v["heading"])
    v["level"] = max(5, v["level"] - random.uniform(0, 0.05))
    v["temp"] = max(60, min(115, v["temp"] + random.uniform(-1.5, 1.5)))


def send(url, v):
    body = json.dumps({
        "vehicle_id": v["id"],
        "speed_kmph": round(v["speed"], 1),
        "fuel_or_battery_pct": round(v["level"], 1),
        "engine_temp_c": round(v["temp"], 1),
        "lat": round(v["lat"], 5),
        "lon": round(v["lon"], 5),
    }).encode()
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=5) as resp:
        return resp.status


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--url", default="http://localhost:8080/api/telemetry")
    p.add_argument("--vehicles", type=int, default=5)
    p.add_argument("--interval", type=float, default=2.0, help="seconds between rounds")
    p.add_argument("--rounds", type=int, default=0, help="0 means run forever")
    args = p.parse_args()

    fleet = [make_vehicle(i) for i in range(args.vehicles)]
    print(f"Sending data for {args.vehicles} vehicles to {args.url} every {args.interval}s. Ctrl+C to stop.")
    n = 0
    while args.rounds == 0 or n < args.rounds:
        t0 = time.time()
        ok = fail = 0
        for v in fleet:
            step(v, args.interval)
            try:
                send(args.url, v)
                ok += 1
            except Exception as exc:
                fail += 1
                last = exc
        n += 1
        print(f"round {n}: sent {ok}, failed {fail}" + (f" ({last})" if fail else ""))
        time.sleep(max(0, args.interval - (time.time() - t0)))


if __name__ == "__main__":
    main()
