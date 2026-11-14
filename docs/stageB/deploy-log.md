# Stage B: Deploy Log

Stage B is the lift and shift: the same containers as Stage A (the app and its own Postgres database), now running on one EC2 machine. The code did not change. Only the place it runs changed.

Live URL: `http://3.111.13.17/`

## What we did

1. Logged in to the EC2 machine over SSH with the key pair.
2. Installed Docker, Docker Compose, git, curl, Nginx and the PostgreSQL client with `apt`.
3. Added the `ubuntu` user to the `docker` group and logged in again so the change applied.
4. Cloned the repo and started the app and database with `STAGE=B-ec2 docker compose -f docker/docker-compose.yml up --build -d`.
5. Checked the app on the machine: `curl http://localhost:8080/health` returned status ok, stage B-ec2, db postgres.
6. Put Nginx in front on port 80 and forwarded it to the app on port 8080 (`infra/nginx-telemetry.conf`).
7. Opened `http://3.111.13.17/health` and the dashboard from a laptop browser.
8. Ran the simulator with 5 vehicles, one reading every 2 seconds, against the live address.

The steps are collected in `infra/deploy-ec2.sh`. The script has 14 commands. Only port 80 and port 22 are open to the internet. The app port 8080 and the database port 5432 are not.

## Result

| Measure | Value |
|---------|-------|
| Total readings after the simulator run | 930 |
| Vehicles | 5 |
| Failed requests from the simulator | 0 (rounds 1 to 42 all sent 5, failed 0 in the screenshot) |
| Time from the first SSH login to the live URL working | About 70 minutes, including the problems below |

Screenshots in `docs/screenshots/`: `stageB-simulator.png`, `stageB-health.png`, `stageB-stats.png`, `stageB-dashboard.png`. The simulator was started from a terminal on the EC2 machine but sent its data to the public address, so the traffic still went through port 80 and Nginx.

## Problems and fixes

| Problem | Fix |
|---------|-----|
| The SSH command was run with the word `ELASTIC_IP` from the guide, so it could not find the host | Used the real Elastic IP address |
| The first install command left out the PostgreSQL client, and the package name was then typed as a command | Installed it with `sudo apt install -y postgresql-client` |
| The SSH session dropped after being idle | Logged in again. The containers kept running because they were started in the background |
| The Compose command was first run on a laptop instead of the EC2 machine, so nothing was deployed yet | Stopped it on the laptop and ran the same command on EC2. The prompt shows which machine you are on |
| After the Nginx config was added, port 80 returned a 404 page from Nginx itself | The reload had not removed the old default site. A full restart of Nginx fixed it |

## Simplifications

- The database container uses the default development password from the compose file. Its port is not published, so only the app container can reach it.
- The site uses plain HTTP on port 80. There is no certificate.
- The app and the database share one small machine, so a stop or crash takes both down.
- The data lives on a Docker volume on the machine disk. Nothing is backed up except a manual dump.
