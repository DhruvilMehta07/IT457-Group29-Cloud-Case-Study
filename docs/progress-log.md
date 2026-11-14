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
| Set a monthly budget. The alert email still has to be verified | In progress | `docs/notes/aws-notes.md` |
| Learned the AWS services that appear in our two cases (EC2, EKS, CloudWatch, RDS, IoT Core) and wrote what each one does | Done | `docs/notes/aws-notes.md` |
| Rough cost estimate for the three stages with the AWS Pricing Calculator | To do | `docs/notes/aws-notes.md` |
| Prepared the steps for Stage B (EC2) and Stage C (RDS) | Done | `infra/aws-setup-notes.md` |
| Launched the Stage B EC2 machine with a fixed Elastic IP, opened ports 80 and 22, and logged in over SSH | Done | `docs/stageB/ec2-launch-log.md`, `docs/screenshots/` |
| Deployed the app and database on the EC2 machine with Docker and Nginx, live at the Elastic IP | Done | `docs/stageB/deploy-log.md`, `infra/deploy-ec2.sh`, `infra/nginx-telemetry.conf` |

### Jeet (research)

| Work | Status | Files |
|------|--------|-------|
| Collected and read sources for Titan and Tata Motors | Done | `docs/notes/research-notes.md` |
| Pulled out architecture, cost and outcome facts from the sources | Done | `docs/notes/research-notes.md` |
| Checking the Week 1 summary against the sources and rewriting it in our own words | In progress | `docs/week1-summary.md` |
| Looking for the original AWS case study for Tata Motors | In progress | `docs/notes/research-notes.md` |
| Report outline | Draft ready, being reviewed | `docs/report-outline.md` |

## Week 2 

| Who | Work | Status | Files |
|-----|------|--------|-------|
| | | | |

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
- The original AWS page for Tata Motors is still not found. To search in Week 2 if not found this week.
- Who does what is not fixed. We update the rows above each week when the split changes.
