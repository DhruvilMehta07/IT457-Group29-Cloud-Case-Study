# Stage C: RDS Creation Log

Stage C replaces the Postgres container on the EC2 machine with a managed database, Amazon RDS for PostgreSQL. This file records how we created the database and what we chose. The move of the data and the app is in `docs/stageC/migration-log.md`.

## What we created

| Setting | Value |
|---------|-------|
| Database name (identifier) | `telemetry-db` |
| Engine | PostgreSQL 16 (16.15) |
| Instance class | `db.t4g.micro` (2 vCPU, 1 GB memory) |
| Deployment | Single AZ (one copy of the database, no standby) |
| Storage | 20 GiB, General Purpose SSD (gp3), 3000 IOPS, 125 MiBps |
| Storage autoscaling | Disabled |
| Encryption | Enabled |
| Automated backup retention | 1 day |
| Deletion protection | Disabled (this is a test environment) |
| Public access | No. The database has no public address that works from the internet |
| Network | Same VPC and the same Availability Zone (`ap-south-1b`) as the EC2 machine |
| First database and user | Database `telemetry`, user `telemetry` |
| Parameter group | `default.postgres16` |
| RDS Extended Support | Disabled |

The password is not written here. It is only used in the `.env` file on the EC2 machine, which is ignored by Git.

## How the EC2 machine is allowed to connect

In the create form we chose **Connect to an EC2 compute resource** and picked our machine `telemetry-stage-b`. AWS then made two security groups for us:

- `ec2-rds-1`, attached to the EC2 machine
- `rds-ec2-1`, attached to the database

The database group has exactly one inbound rule: PostgreSQL, TCP, port 5432, and the source is the group `ec2-rds-1`, not an IP address. So only our EC2 machine can talk to the database. Nothing else on the internet can. This is checked in `docs/screenshots/stageC-rds-security.png` and `docs/screenshots/stageC-rds-connected-ec2.png`.

## Why these choices

| Choice | Reason |
|--------|--------|
| `db.t4g.micro` | The smallest class on offer, so the cost stays low. Our load is small |
| Single AZ | Multi AZ would double the instance cost. We do not need a standby for a test |
| Same zone as EC2 | The database and the app are close, so the network delay is small and traffic between them stays inside the zone |
| No public access | The database is private. Only the app machine needs to reach it |
| Standard PostgreSQL, not Aurora | Our app and our backup file are plain PostgreSQL. This keeps Stage C the same app as Stage B, only with a different place for the database |
| 20 GiB gp3 | The same disk size as the EC2 machine, so the comparison is fair |

## Measures

| Measure | Value |
|---------|-------|
| Fields or options changed from the defaults in the create form | About 11 |
| Time from clicking Create database until the status was Available | About 8 minutes |
| Backups, patching and the operating system | Done by AWS. We do not manage them |

## Problems and fixes

| Problem | Fix |
|---------|-----|
| The RDS console first offered Aurora PostgreSQL Express as the default. It works only with IAM login and has no VPC | We switched to the standard PostgreSQL option with the Free tier template and the full configuration |
| We expected a cost estimate box on the create form. This version of the form has none | We used the AWS Pricing Calculator instead (`docs/costs.md`) |
