# Project Plan

**IT457 Cloud Computing, Group 29**
Dhruvil Mehta (202301061), Jay Rathod (202301006), Jeet Patel (202611037)
**Topic:** Titan Industries and Tata Motors on AWS (digital business, IoT and telemetry)
**Exercise theme (from the project document):** Migration

## 1. What we are doing

Part 1 is a case study of how Titan and Tata Motors use AWS (Titan for retail systems at peak demand, Tata Motors for connected vehicles and telemetry).

Part 2 is a hands-on exercise from the Migration theme: take a simple app from a local Docker container, lift and shift it to a cloud VM, then refactor one part to a managed service, and document the effort and cost differences.

Our app is a **vehicle telemetry dashboard**. A simulator sends fake vehicle readings (speed, fuel or battery level, engine temperature, GPS). The app stores them and shows them live. This links to the Tata Motors connected vehicle story. From the Titan story we borrow the ideas of load testing before peak events and monitoring with CloudWatch.

## 2. The three stages

| Stage | What we do | What we record |
|-------|-----------|----------------|
| A. Local | App and Postgres in Docker on a laptop (docker compose) | Setup time, start time, baseline latency |
| B. Lift and shift | The same containers on one EC2 instance, no code changes | Hours spent, manual steps, monthly cost, latency |
| C. Refactor | Replace the Postgres container with Amazon RDS (maybe also S3 or IoT Core if time allows) | Hours spent, what changed, cost, latency, operations effort saved |

The live URL for the viva will point to the final working stage.

## 3. Extra experiments (Week 3)

- Load test with Locust using the same settings at every stage (users, ramp up, duration).
- Record average and 95th percentile response time, requests per second, failures.
- Titan inspired check: watch CPU and response time in CloudWatch while the load test runs, then resize the instance and test again.
- Cost model with the AWS Pricing Calculator for the stages, plus a rough on premises estimate.

## 4. Weekly plan

| Week | Dates (approx) | Work | Deliverable |
|------|----------------|------|-------------|
| 1 | 14 to 21 Oct | Find sources, extract architecture, cost and outcome data. Set up repo, AWS account, starter app | One page summary (`docs/week1-summary.md`) |
| 2 | 22 to 28 Oct | Case analysis, architecture diagram, finish Stage A, write report | 10 page report: study, exercise plan, team work |
| 3 | 29 Oct to 4 Nov | Build Stages B and C, run experiments, collect measurements | Report add ons with results |
| 4 | 5 to 11 Nov | Report polish, live URL check, final submission | Final report and live URL |
| 5 | To be announced | Project viva | Everyone explains every part |

Dates are approximate because the viva and submission dates have not been announced yet.

## 5. Who works on what

We share the work and we will change who does what as the project goes on. The current focus of each member for each week is written in `docs/progress-log.md`.

Rules we follow:
- Everyone deploys at least one thing on AWS and can explain every stage in the viva.
- We swap tasks where possible, so nobody only knows one part.
- Every member contributes through their own GitHub account.

## 6. Other rules we follow

- Small, regular commits from all three accounts, with clear messages.
- Never commit passwords, keys or `.env` files.
- A billing alarm is set on the AWS account and unused resources are stopped.
- Every number in the report has a source or is marked as our own measurement.
- The progress log (`docs/progress-log.md`) is updated whenever we finish something.

## 7. Risks

| Risk | What we do |
|------|-----------|
| AWS costs run higher than expected | Billing alarm, small instances, stop or delete after tests |
| RDS setup takes longer than planned | Do Stage B first so a working live URL exists early |
| Source for Tata Motors on AWS is thin | Be clear in the report about what is confirmed and what is a claim, ask the TA |
| Work ends up on one person | Rotate tasks, check commit history every week |