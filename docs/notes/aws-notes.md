# AWS Notes, Week 1

Week 1 goal for the AWS side: have the AWS account ready and safe, understand the services that appear in our two cases, get a rough cost picture, and be ready to start Stage B (EC2) and Stage C (RDS) next week.

The detailed step by step for Stage B and Stage C is in `infra/aws-setup-notes.md`. This file is for what we actually did and learned.

Rules: no keys, passwords or `.pem` files in this repo. If we take screenshots, we hide the AWS account ID first.

## 1. Week 1 checklist

- [ ] AWS account created
- [ ] MFA turned on for the root user
- [ ] IAM user created for daily work (we stop using root)
- [ ] Monthly budget and billing alarm set up with email alerts
- [ ] Region chosen
- [ ] Read about the services in our cases (section 3)
- [ ] Rough cost estimate done with the AWS Pricing Calculator (section 4)
- [ ] Stage B and Stage C steps read and understood

## 2. Account setup log

Fill this in as it happens.

| Step | Done (yes or no) | Notes (what we chose, what went wrong) |
|------|------------------|----------------------------------------|
| Account created | | |
| MFA on root user | | |
| IAM user created | | |
| Budget and alarm created | | |
| Region | | |

## 3. AWS services in our two cases, in simple words

Services named in the Titan AWS case study, plus the ones we plan to use in our exercise.

| Service | What it is | Where it shows up |
|---------|-----------|-------------------|
| Amazon EC2 | Virtual machines that you rent by the hour | Titan case (resized for peak demand). Our Stage B |
| Amazon EKS | AWS's managed Kubernetes service, for running containers across many machines | Titan case |
| Amazon CloudWatch | Collects metrics and logs and can raise alarms | Titan case (real time visibility). We use it during load tests |
| AWS Enterprise Support | A paid support plan with a Technical Account Manager and 24 hour expert help | Titan case |
| AWS Countdown Premium | Extra support from AWS engineers for a big event, with architecture reviews and readiness checks | Titan case |
| AWS Well-Architected Framework | A set of best practices and a review process for checking a system | Titan case |
| Amazon RDS | A managed database. AWS handles backups, patching and failover | Our Stage C |
| Amazon S3 | Object storage for files | Possible extra for us |
| AWS IoT Core | Connects devices and receives their messages (for example over MQTT) | Closest to the Tata Motors story. Possible extra for us |
| IAM, security groups, Elastic IP | Permissions, firewall rules and a fixed public address | Our Stage B |

For Tata Motors we have not confirmed which AWS services they use. We should not claim any until we find a proper source.

## 4. Cost estimate (fill from the AWS Pricing Calculator)

Use https://calculator.aws/ and write the date you checked, because prices and free tier rules change.

| Item | Size or setting | Estimated monthly cost | Date checked |
|------|-----------------|------------------------|--------------|
| EC2 instance for the app | | | |
| Elastic IP | | | |
| RDS PostgreSQL instance | | | |
| RDS storage | | | |
| Data transfer | | | |
| Total for Stage B | | | |
| Total for Stage C | | | |

Notes on the free tier and credits (check the current AWS terms and write what applies to us):

## 5. Decisions

| Decision | What we chose | Why |
|----------|--------------|-----|
| Region | | |
| EC2 instance type | | |
| RDS instance size | | |

## 6. Problems and fixes

| Problem | Fix |
|---------|-----|
| | |

## 7. Ready for Stage B?

- [ ] Key pair saved safely (not in the repo)
- [ ] Security group plan written (80 and 443 open, 22 only from our own IPs)
- [ ] Plan for the fixed address (Elastic IP)
- [ ] We know how to stop or delete everything after tests