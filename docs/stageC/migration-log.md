# Stage C: Migration Log

Stage C moves the database from the Postgres container on the EC2 machine to Amazon RDS. The app code did not change. Only the place the data lives changed, and the app now reaches it through the `DATABASE_URL` setting.

Live URL: `http://3.111.13.17/`

How the RDS database was created is in `docs/stageC/rds-log.md`. This file covers the move of the data and the switch of the app.

## What we did

1. Before the move, the Stage B database held 930 readings from 5 vehicles. A plain SQL backup of it was already on the EC2 machine as `~/stageB_start.sql` (78,753 bytes).
2. Wrote a `.env` file on the EC2 machine with two lines: `DATABASE_URL` (the connection address of the RDS database) and `STAGE=C-rds`. The file is listed in `.gitignore`, so it is never committed.
3. Loaded the file into the shell and tested the connection with `psql "$DATABASE_URL" -c "select 1;"`. It returned `1`, which shows the EC2 machine can reach RDS through the security group rule.
4. Restored the backup into RDS with `psql "$DATABASE_URL" -f ~/stageB_start.sql`. This was done before the app was pointed at RDS, so the app did not create its own empty table first.
5. Counted the rows in RDS: 930 readings and 5 vehicles, the same as before the move.
6. Switched the app over: `docker compose -f docker/docker-compose.yml down` (no `-v`, so the old data volume was kept), then `docker compose -f docker/docker-compose.rds.yml --env-file .env up --build -d`. The new compose file starts only the web container, because there is no database container any more.
7. Checked the app: `/health` returned status ok, stage C-rds, db postgres, and `/api/stats` returned 930 readings and 5 vehicles.
8. Opened the live address from a laptop, sent 50 new readings with the simulator (5 vehicles, 10 rounds, one per second) and checked the dashboard. It showed 980 readings and the label Stage: C-rds.

## Result

| Measure | Value |
|---------|-------|
| Rows before the move (Stage B) | 930 readings, 5 vehicles |
| Rows in RDS after the restore | 930 readings, 5 vehicles |
| Size of the backup file | 78,753 bytes |
| Time to restore the backup into RDS | 0.139 seconds |
| Stopping the old containers | About 1 second |
| Building and starting the new web container | About 2 seconds |
| A full stop and start of the Stage C stack, timed | 2.955 seconds until `/health` answered |
| Simulator rounds after the move | 10 rounds, all sent 5, failed 0 |
| Readings after the simulator run | 980 |

The cutover itself was not timed on the first run. The 2.955 second figure is a second run of the same two commands, so it is the best measure we have of how long the app is unavailable during a switch: a few seconds.

Screenshots in `docs/screenshots/`: `stageC-health.png`, `stageC-stats.png`, `stageC-simulator.png`, `stageC-dashboard.png`.

## Restart time

To compare how fast the app comes back after a restart, we restarted the web container three times in each stage and timed it until `/health` answered.

| Stage | Run 1 | Run 2 | Run 3 | Average |
|-------|-------|-------|-------|---------|
| B (database in a container on the same machine) | 2.75 s | 1.51 s | 2.02 s | 2.09 s |
| C (database on RDS) | 1.23 s | 1.22 s | 1.44 s | 1.30 s |

The app comes back a little faster in Stage C. The numbers are small and close, so we only claim a slight difference. Screenshots: `stageB-restart-time.png` and `stageC-restart-time.png`.

## Problems and fixes

| Problem | Fix |
|---------|-----|
| The database password contains a dollar sign. In a `.env` file and in the shell, `$` followed by digits is read as a variable, so the password would have been changed silently | Wrote the dollar sign as `%24` inside `DATABASE_URL`. The database driver decodes it back to `$` |
| The first simulator command for Stage C gave only the server address. The simulator does not add a path, so every request would have gone to the home page | Gave the full address, ending in `/api/telemetry` |

## Going back

The old Postgres container was removed, but its data volume was kept, and the backup file is still on the machine. To go back to Stage B, stop the RDS version with `docker compose -f docker/docker-compose.rds.yml down` and start the original one with `docker compose -f docker/docker-compose.yml up -d`.

## Simplifications

- The data was moved with a plain SQL backup while no load test was running. A real system would use a tool that copies changes while the app keeps running, such as AWS Database Migration Service.
- The app was down for a few seconds during the switch. The site has no second copy of the app to take over.
- The password lives in a `.env` file on the EC2 machine. A real system would keep it in AWS Secrets Manager.
- The RDS database is Single-AZ with a one day backup, so it is not protected against the loss of one availability zone.
