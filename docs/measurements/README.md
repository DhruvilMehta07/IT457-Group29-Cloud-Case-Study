# Measurements

Raw results and the comparison table for the three stages. We use the same load test settings at every stage so the results can be compared fairly.

## Load test settings (same for all stages)

- Tool: Locust 2.46.7, headless mode
- Users: 50, ramp up 5 per second, duration 2 minutes
- Command: `locust -f loadtest/locustfile.py --host <URL> --headless -u 50 -r 5 -t 2m --csv docs/measurements/stage<X>_u50`
- Traffic mix (from `loadtest/locustfile.py`): about 5 parts POST /api/telemetry, 2 parts GET /api/latest and 1 part GET /api/history

## Comparison table

| Measure | Stage A (local) | Stage B (EC2) | Stage C (RDS) |
|---------|-----------------|---------------|---------------|
| Hours spent on setup | | | |
| Number of manual steps | | | |
| Problems we hit | psycopg2-binary failed to install on Python 3.14 when running without Docker (fixed by updating the pinned version). The `python` command was not found on macOS (use `python3`) | | |
| Code lines changed vs previous stage | None (baseline) | | |
| Monthly cost (Pricing Calculator) | 0 (runs on a laptop) | | |
| Cost from the real bill so far | 0 | | |
| Average response time (ms) | 8.7 | | |
| 95th percentile response time (ms) | 14 | | |
| Requests per second at 50 users | 47.9 average over the run, about 49 to 51 once all 50 users were active | | |
| Failure rate | 0% (0 of 5714 requests) | | |
| Time to recover after restart | Not measured yet | | |
| Who maintains the database (us or AWS) | us | us | AWS |

## Stage A results in detail

Run on 20 Oct 2026, from 15:02 to 15:04 local time.

| Request | Count | Average (ms) | Median (ms) | 95% (ms) | 99% (ms) | Max (ms) |
|---------|-------|--------------|-------------|----------|----------|----------|
| POST /api/telemetry | 3610 | 8.1 | 8 | 13 | 17 | 51 |
| GET /api/latest | 1376 | 10.3 | 10 | 15 | 20 | 31 |
| GET /api/history | 728 | 8.5 | 8 | 13 | 18 | 24 |
| All requests | 5714 | 8.7 | 8 | 14 | 18 | 51 |

## How this test was set up

- Machine: Dhruvil's MacBook Air with Docker Desktop and Python 3.14
- The app, the Postgres container and the load generator (Locust) all ran on the same laptop, so they shared the same CPU and there was no internet between them
- Instance type and region: not applicable for Stage A

## Notes for comparing with the later stages

- Stage A has no network delay. In Stage B and C, if Locust runs from a laptop, part of the extra time will be the network and not only the cloud machine. We will write down where Locust runs for each test.
- 50 users caused no failures, so this load did not stress the setup. For the cloud stages we will also try a higher number of users (for example 200) at every stage, to see where it starts to slow down.
- If possible, run each test more than once and note any big differences.

## Files in this folder

- `stageA_u50_stats.csv`: summary per request type
- `stageA_u50_stats_history.csv`: numbers for every second of the run
- `stageA_u50_failures.csv` and `stageA_u50_exceptions.csv`: empty, because there were no failures or exceptions