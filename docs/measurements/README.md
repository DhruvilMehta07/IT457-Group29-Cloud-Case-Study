# Measurements

Raw results and the comparison table for the three stages. We use the same load test settings at every stage so the results can be compared fairly.

## Load test settings (same for all stages)

- Tool: Locust 2.46.7, headless mode
- Users: 50, ramp up 5 per second, duration 2 minutes
- Command: `locust -f loadtest/locustfile.py --host <URL> --headless -u 50 -r 5 -t 2m --csv docs/measurements/stage<X>_u50`
- Traffic mix (from `loadtest/locustfile.py`): about 5 parts POST /api/telemetry, 2 parts GET /api/latest and 1 part GET /api/history

## Comparison table

For the response time rows we use the middle run of the three (the one with the middle average), so one unusually good or bad run does not decide the result. The same choice is used in the graphs. All three runs are listed in the next table.

| Measure | Stage A (local) | Stage B (EC2) | Stage C (RDS) |
|---------|-----------------|---------------|---------------|
| Hours spent on setup | Not measured | About 70 minutes from the first SSH login to the live URL, including the problems (`docs/stageB/deploy-log.md`) | About 8 minutes for RDS to become Available, then the move itself was a few commands and the restore took 0.139 seconds (`docs/stageC/rds-log.md`, `docs/stageC/migration-log.md`) |
| Number of manual steps | Not counted | 8 steps in the deploy log (14 commands in `infra/deploy-ec2.sh`) | 8 steps in the migration log, plus about 11 fields changed in the RDS create form |
| Problems we hit | psycopg2-binary failed to install on Python 3.14 when running without Docker (fixed by updating the pinned version). The `python` command was not found on macOS (use `python3`) | 5 problems, for example the Nginx default site still answering with a 404 until Nginx was restarted fully (`docs/stageB/deploy-log.md`) | 2 in the migration log: a dollar sign in the password had to be written as `%24`, and the simulator needs the full address ending in `/api/telemetry`. More in `docs/stageC/rds-log.md` |
| Code lines changed vs previous stage | None (baseline) | None. Same containers, only the place changed | No app code changed. One new compose file of 17 lines (web container only) and a `.env` file that is not committed |
| Monthly cost (Pricing Calculator) | 0 (runs on a laptop) | 15.86 USD | 33.81 USD |
| Cost from the real bill so far | 0 | Stage B and C share one account bill: 3.45 USD before credits and 0 USD paid | The same bill. The RDS part of it is 0.53 USD (`docs/costs.md`) |
| Average response time (ms), middle run | 8.9 | 72.9 | 175.1 |
| 95th percentile response time (ms), middle run | 14 | 130 | 320 |
| Requests per second at 50 users, middle run | 47.7 | 45.2 | 41.0 |
| Failure rate | 0% (0 of 5684 requests, no failures in any run) | 0% (0 of 5399 requests, no failures in any run) | 0% (0 of 4895 requests, no failures in any run) |
| Time to recover after restart | Not measured | 2.09 s on average (2.75, 1.51, 2.02) | 1.30 s on average (1.23, 1.22, 1.44) |
| Who maintains the database (us or AWS) | us | us | AWS |

Response time is the time from sending a request to getting the full answer. The 95th percentile (p95) is the time that 95 out of 100 requests were faster than, so it shows how slow the slower requests are.

### All runs

Each run is 50 users, ramp up 5 per second, 2 minutes. The long run is the same but 10 minutes.

| Stage | Run | Requests | Failures | Average (ms) | p95 (ms) | Requests per second |
|-------|-----|----------|----------|--------------|----------|---------------------|
| A | run 1 | 5714 | 0 | 8.7 | 14 | 47.9 |
| A | run 2 | 5684 | 0 | 8.9 | 14 | 47.7 |
| A | run 3 | 5703 | 0 | 8.9 | 15 | 47.8 |
| B | run 1 | 5407 | 0 | 63.1 | 100 | 45.3 |
| B | run 2 | 5399 | 0 | 72.9 | 130 | 45.2 |
| B | run 3 | 5309 | 0 | 80.7 | 150 | 44.5 |
| B | long (10 min) | 27386 | 0 | 87.3 | 180 | 45.7 |
| C | run 1 | 4945 | 0 | 161.3 | 320 | 41.4 |
| C | run 2 | 4871 | 0 | 184.6 | 380 | 40.8 |
| C | run 3 | 4895 | 0 | 175.1 | 320 | 41.0 |
| C | long (10 min) | 24844 | 0 | 195.8 | 380 | 41.5 |

Graphs: `response-time-comparison.png` (average and p95 of the middle run) and `response-time-over-time.png` (average response time during the run).

## Stage A results in detail

Run on 20 Oct 2026, from 15:02 to 15:04 local time.

| Request | Count | Average (ms) | Median (ms) | 95% (ms) | 99% (ms) | Max (ms) |
|---------|-------|--------------|-------------|----------|----------|----------|
| POST /api/telemetry | 3610 | 8.1 | 8 | 13 | 17 | 51 |
| GET /api/latest | 1376 | 10.3 | 10 | 15 | 20 | 31 |
| GET /api/history | 728 | 8.5 | 8 | 13 | 18 | 24 |
| All requests | 5714 | 8.7 | 8 | 14 | 18 | 51 |

## Stage B results in detail

Middle run (run 2), 50 users for 2 minutes. Locust ran on a laptop outside AWS and sent its traffic over the internet to the Elastic IP.

| Request | Count | Average (ms) | Median (ms) | 95% (ms) | 99% (ms) | Max (ms) |
|---------|-------|--------------|-------------|----------|----------|----------|
| POST /api/telemetry | 3392 | 64.1 | 52 | 120 | 250 | 681 |
| GET /api/latest | 1324 | 98.6 | 84 | 160 | 300 | 934 |
| GET /api/history | 683 | 66.8 | 54 | 130 | 210 | 618 |
| All requests | 5399 | 72.9 | 62 | 130 | 260 | 934 |

Long run, 10 minutes:

| Request | Count | Average (ms) | Median (ms) | 95% (ms) | 99% (ms) | Max (ms) |
|---------|-------|--------------|-------------|----------|----------|----------|
| POST /api/telemetry | 17248 | 71.3 | 58 | 130 | 280 | 785 |
| GET /api/latest | 6789 | 134.9 | 110 | 250 | 450 | 1062 |
| GET /api/history | 3349 | 73.2 | 60 | 130 | 260 | 821 |
| All requests | 27386 | 87.3 | 71 | 180 | 350 | 1062 |

## Stage C results in detail

Middle run (run 3), same settings and the same laptop and network as Stage B. Only the database moved to RDS.

| Request | Count | Average (ms) | Median (ms) | 95% (ms) | 99% (ms) | Max (ms) |
|---------|-------|--------------|-------------|----------|----------|----------|
| POST /api/telemetry | 2995 | 167.4 | 150 | 310 | 630 | 803 |
| GET /api/latest | 1224 | 199.8 | 180 | 350 | 550 | 776 |
| GET /api/history | 676 | 164.3 | 150 | 300 | 530 | 790 |
| All requests | 4895 | 175.1 | 160 | 320 | 590 | 803 |

Long run, 10 minutes:

| Request | Count | Average (ms) | Median (ms) | 95% (ms) | 99% (ms) | Max (ms) |
|---------|-------|--------------|-------------|----------|----------|----------|
| POST /api/telemetry | 15543 | 182.0 | 160 | 360 | 560 | 1508 |
| GET /api/latest | 6210 | 238.9 | 210 | 440 | 650 | 1432 |
| GET /api/history | 3091 | 178.2 | 160 | 350 | 540 | 1338 |
| All requests | 24844 | 195.8 | 170 | 380 | 590 | 1508 |

## CloudWatch graphs

Screenshots in `docs/screenshots/`. CPU values are the highest 5 minute average in the graph.

| Measure | Stage B | Stage C |
|---------|---------|---------|
| EC2 CPU utilization, peak | 70.47% (`stageB-cloudwatch-cpu.png`) | 37.29% (`stageC-cloudwatch-cpu.png`) |
| RDS CPU utilization, peak | Not applicable | 88.26% (`stageC-rds-cpu.png`) |
| RDS database connections, peak | Not applicable | 7 (`stageC-rds-connections.png`) |
| RDS freeable memory | Not applicable | Fell from about 172 MB to about 162 MB (`stageC-rds-memory.png`) |
| RDS CPU credit balance | Not applicable | Rose to about 215 before the tests, then fell to about 191 and never came near zero (`stageC-rds-cpu-credits.png`) |

Stage B also has the network graphs (`stageB-cloudwatch-network-in.png` and `stageB-cloudwatch-network-out.png`) and the CPU alarm (`stageB-alarm.png`).

## How these tests were set up

- Stage A: Dhruvil's MacBook Air with Docker Desktop and Python 3.14. The app, the Postgres container and the load generator (Locust) all ran on the same laptop, so they shared the same CPU and there was no internet between them.
- Stage B: one EC2 `t3.micro` (2 vCPU, 1 GB of memory) in Mumbai (`ap-south-1`) with the app and a Postgres container in Docker, and Nginx in front on port 80. Locust ran on a laptop outside AWS and sent traffic over the internet to the Elastic IP.
- Stage C: the same EC2 machine and the same laptop and network, but the Postgres container was gone. The database was Amazon RDS for PostgreSQL 16 on a `db.t4g.micro`, Single-AZ, 20 GB gp3 storage, in the same region.

## What the numbers show

- **Stage A to B.** The average response time went from about 9 ms to about 73 ms. Most of this is probably the network. In Stage A everything ran on one laptop with no network at all, and from Stage B on every request travels from a laptop to Mumbai and back. We did not measure the network time on its own, so Stage A is a baseline and not a fair like for like comparison.
- **Stage B to C.** Same laptop, same network, same load. The average went from 72.9 ms to 175.1 ms, which is about 2.4 times slower, the p95 from 130 ms to 320 ms, and the requests per second fell from 45.2 to 41.0 (about 9% lower). Because only the database changed, the extra time comes from the cloud side.
- **Why.** The graphs point at the database. EC2 CPU fell from 70% to 37%, while the RDS instance reached 88% CPU. The work did not disappear, it moved to a small database machine that became the busiest part of the system. The RDS instance is a burstable type, which slows down when its CPU credits run out. The credit balance only fell from about 215 to about 191 during the tests, so it never ran out and the slowdown was not caused by missing credits. The instance was simply working at high CPU for the whole run. This fits the result, but we did not prove it, for example by running the same test on a bigger RDS instance.
- **The slowest request.** `GET /api/latest` is the slowest in every stage. Its answer is the biggest, about 32 KB on average in the Stage C middle run.
- **Failures.** No run at any stage had a failed request, so 50 users did not break any of the setups.
- **Restart.** The app came back after a restart in about 2.1 s in Stage B and about 1.3 s in Stage C. These are small numbers and we only claim a slight difference.
- **Cost against speed.** Stage C costs about 18 USD a month more than Stage B (`docs/costs.md`) and was slower in this test. What the extra money buys is that AWS takes over the database backups, patching and the database machine. It does not buy speed unless the instance is large enough.

## Limits of these tests

- One laptop on one Wi-Fi network generated all the load, so part of every response time is the network from that laptop.
- Three runs of 2 minutes per stage, plus one run of 10 minutes for Stage B and Stage C. The runs of one stage differ by up to about 23 ms in the average, so small differences should not be over read.
- Only 50 users. Nothing failed, so we do not know where each setup starts to fail.
- The RDS instance is the smallest type, and we did not try a bigger one. So we can say the small instance was busy, but not how much faster a bigger one would have been.
- The tests were run from one region and the data set was small (under 1000 readings at the start of the tests).

## Files in this folder

- `stageA_u50_*`, `stageB_u50_*` and `stageC_u50_*`: Locust results. For each run there are four files: `_stats.csv` (summary per request type), `_stats_history.csv` (numbers for every second of the run), `_failures.csv` and `_exceptions.csv`. The failures and exceptions files are empty, because there were no failures or exceptions.
- `stageA_u50_*` without a run number is the first Stage A run. `run2` and `run3` are the repeats. `stageB_u50_long_*` and `stageC_u50_long_*` are the 10 minute runs.
- `response-time-comparison.png` and `response-time-over-time.png`: the graphs made by `loadtest/plot_results.py`.
