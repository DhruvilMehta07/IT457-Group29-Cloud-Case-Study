# IT457 Cloud Computing, Group 29

**Case study:** Titan Industries and Tata Motors on AWS (digital business, IoT and telemetry)
**Exercise theme:** Migration (local Docker, then lift and shift to a cloud VM, then refactor to a managed service)

## Team

| Name | Student ID |
|------|-----------|
| Dhruvil Mehta | 202301061 |
| Jay Rathod | 202301006 |
| Jeet Patel | 202611037 |

Tasks are shared and can change as the project goes on. What each of us is working on each week is written in `docs/progress-log.md`.

## Live URL

To be added after deployment: `http://<our-ec2-address>/`

## What this project is

We study how Titan (retail systems at peak festival demand) and Tata Motors (connected vehicles, 500,000 vehicles on a cloud IoT platform) use AWS. Then we build a small vehicle telemetry dashboard and move it through three stages, measuring effort, cost and speed at each stage.

| Stage | Description |
|-------|-------------|
| A | App and Postgres in Docker on a laptop |
| B | Same containers on one AWS EC2 machine (lift and shift) |
| C | Database moved to Amazon RDS (refactor to a managed service) |

## Repository layout

```
app/          Flask app (API and dashboard page)
simulator/    Fake vehicle data generator
docker/       Dockerfile and docker compose files (local/EC2 and RDS versions)
loadtest/     Locust load test
infra/        AWS setup checklist
docs/         Plan, progress log, week 1 summary, report outline, viva prep
docs/notes/   Working notes (research notes, AWS notes)
docs/measurements/   Load test results and the comparison table
docs/screenshots/    Proof screenshots for each stage
```

## Run it on your laptop

You need Docker Desktop. From the repo root:

```
docker compose -f docker/docker-compose.yml up --build
```

Open http://localhost:8080 for the dashboard. Open a second terminal tab and send fake data:

```
python3 simulator/simulator.py --vehicles 5 --interval 2
```

The simulator keeps running until you press Ctrl+C. A minute is enough to check that it works. Before a demo, start it a few minutes early so the charts have history.

To stop everything, press Ctrl+C in both tabs and run:

```
docker compose -f docker/docker-compose.yml down
```

Useful addresses: `/health` (status check), `/api/latest`, `/api/stats`.

## Run without Docker (backup option)

This uses a local SQLite file instead of Postgres. On a Mac use `python3`, and a virtual environment keeps things clean:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r app/requirements.txt
python app/app.py        # runs on http://localhost:5000
```

In a second terminal tab, from the repo root:

```
source .venv/bin/activate
python simulator/simulator.py --url http://localhost:5000/api/telemetry
```

## Load test

Needs the app running (Docker version on port 8080). In a new terminal tab, from the repo root:

```
python3 -m venv .venv          # only the first time
source .venv/bin/activate
pip install locust             # only the first time
locust -f loadtest/locustfile.py --host http://localhost:8080
```

Open http://localhost:8089, enter the number of users and the spawn rate, and click Start. Use the same settings at every stage so the results can be compared. For a run without the web page:

```
locust -f loadtest/locustfile.py --host http://localhost:8080 --headless -u 50 -r 5 -t 2m --csv docs/measurements/stageA_u50
```

## Status

| Item | State |
|------|-------|
| Week 1 source summary | In progress |
| Stage A (local Docker with Postgres) | Done and checked on a laptop, screenshots in `docs/screenshots/` |
| Baseline load test (Stage A) | Done, results in `docs/measurements/` |
| AWS account and billing alarm | In progress |
| Stage B (EC2) | Not started |
| Stage C (RDS) | Not started |
| Report | Not started, outline ready |

See `docs/progress-log.md` for the weekly log.

## Security rules

No passwords, keys, `.env` files or `.pem` files in this repo. Secrets go in environment variables on the server.