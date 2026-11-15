# Progress Log

IT457 Group 29. Each member keeps their own rows up to date and pushes the change. Status is one of: **Done**, **In progress**, **To do**. A row only becomes Done when the work really is finished. Exact dates are in the git history.

## Week 1

### Dhruvil

| Work | Status | Files |
|------|--------|-------|
| Created the GitHub repo, project structure and README | Done | `README.md` |
| Wrote the project plan and weekly schedule | Done | `docs/plan.md` |
| Ran Stage A on a laptop with Docker. App and Postgres work, the simulator sends data, and the dashboard shows the readings (480 readings in the test run) | Done | `docs/screenshots/` |
| Baseline load test on Stage A with Locust. 50 users for 2 minutes, 5714 requests with no failures, average response time 8.7 ms | Done | `docs/measurements/` |

### Jay (AWS)

| Work | Status | Files |
|------|--------|-------|
| Set up the AWS account: MFA on the root user and region chosen (Mumbai). No IAM user, we share the root login | Done | `docs/notes/aws-notes.md` |
| Set a monthly budget. The alert email shows as verified | Done | `docs/notes/aws-notes.md`, `docs/screenshots/budget-alert-checked.png` |
| Learned the AWS services that appear in our two cases (EC2, EKS, CloudWatch, RDS, IoT Core) and wrote what each one does | Done | `docs/notes/aws-notes.md` |
| Rough cost estimate for the three stages with the AWS Pricing Calculator | Done | `docs/costs.md`, `docs/cost-estimates/` |
| Prepared the steps for Stage B (EC2) and Stage C (RDS) | Done | `infra/aws-setup-notes.md` |
| Launched the Stage B EC2 machine with a fixed Elastic IP, opened ports 80 and 22, and logged in over SSH | Done | `docs/stageB/ec2-launch-log.md`, `docs/screenshots/` |
| Deployed the app and database on the EC2 machine with Docker and Nginx, live at the Elastic IP | Done | `docs/stageB/deploy-log.md`, `infra/deploy-ec2.sh`, `infra/nginx-telemetry.conf` |

### Jeet (research)

| Work | Status | Files |
|------|--------|-------|
| Collected and read sources for Titan and Tata Motors | Done | `docs/notes/research-notes.md` |
| Pulled out architecture, cost and outcome facts from the sources | Done | `docs/notes/research-notes.md` |
| Checking the Week 1 summary against the sources and rewriting it in our own words | Done | `docs/week1-summary.md` |
| Looking for the original AWS case study for Tata Motors | Done, the page linked from the AWS blog no longer opens | `docs/notes/research-notes.md` |
| Report outline | Done, used for the final report | `docs/report-outline.md` |

## Week 2 

| Who | Work | Status | Files |
|-----|------|--------|-------|
| Dhruvil | Repeated the Stage A load test, three runs in total | Done | `docs/measurements/` |
| Jay | Created the RDS database and checked that only the EC2 machine can reach it | Done | `docs/stageC/rds-log.md` |
| Jay | Pricing Calculator estimates for Stage B and Stage C, cost comparison, real bill, credits and budget email | Done | `docs/costs.md`, `docs/cost-estimates/` |
| Jeet | Stage B load tests (three runs and one 10 minute run), CloudWatch graphs and a CPU alarm | Done | `docs/measurements/`, `docs/screenshots/` |
| Dhruvil | Moved the data to RDS and switched the app over (930 readings checked before and after). Measured restart time three times in Stage B and in Stage C | Done | `docs/stageC/migration-log.md`, `docs/screenshots/` |
| Jeet | Stage C load tests (three runs and one 10 minute run), EC2 and RDS graphs, comparison graphs | Done | `docs/measurements/`, `docs/screenshots/` |
| Dhruvil | Filled in the comparison table and wrote what the numbers show | Done | `docs/measurements/README.md` |
| All | Final report | Done | `docs/report/` |

## Week 3 

| Who | Work | Status | Files |
|-----|------|--------|-------|
| | | | |

## Week 4 

| Who | Work | Status | Files |
|-----|------|--------|-------|
| | | | |

## Decisions and open questions

- The project document says "Titan digital business and properties on AWS with IoT". The AWS case we found for Titan is about retail system readiness at festival peak. Question for the TA: is that acceptable, and is the IoT part expected mainly from the Tata Motors side?
- The original AWS page for Tata Motors was checked at the end. The page linked from the AWS blog no longer opens, so the report uses the blog text only and says so.
- Who does what is not fixed. We update the rows above each week when the split changes.
