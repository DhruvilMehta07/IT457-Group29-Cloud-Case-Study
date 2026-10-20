# AWS Setup Notes (Jay's checklist)

Check the current AWS free tier and credit rules on the AWS pricing pages before starting, because they change. Never put access keys, passwords or `.pem` files in Git.

## Day one

1. Create the AWS account (one person owns it, share costs fairly).
2. Turn on MFA for the root user. Create an IAM user for daily work and stop using root.
3. **Billing alarm:** Billing and Cost Management, then Budgets, create a monthly cost budget with email alerts at a low limit.
4. Pick one region and stay in it (for example Asia Pacific Mumbai, ap-south-1).

## Stage B: EC2 (lift and shift)

1. Launch an Ubuntu EC2 instance (start small, for example t3.micro or t3.small).
2. Create a key pair, keep the `.pem` file safe and out of Git.
3. Security group: allow 80 and 443 from anywhere, allow 22 only from your own IP.
4. Allocate an Elastic IP and attach it so the address stays the same.
5. Install Docker:
   ```
   sudo apt update && sudo apt install -y docker.io docker-compose-v2 git
   sudo usermod -aG docker $USER   # log out and in again
   ```
6. Clone the repo and run:
   ```
   git clone <repo url>
   cd <repo>
   STAGE=B-ec2 docker compose -f docker/docker-compose.yml up --build -d
   ```
7. The app listens on port 8080. Either open 8080 in the security group for testing, or put Nginx on port 80 in front of it (proxy to localhost:8080).
8. Check `http://<elastic ip>/health`.
9. Note down: time taken, number of manual steps, problems we hit. This is data for the report.

## Stage C: RDS

1. Create an RDS PostgreSQL instance (smallest size, single AZ for testing).
2. Put it in the same VPC as the EC2 instance. Security group for RDS: allow port 5432 only from the EC2 security group.
3. Create database `telemetry` and a user.
4. On the EC2 machine create `.env` (never commit it):
   ```
   DATABASE_URL=postgresql://USER:PASSWORD@RDS-ENDPOINT:5432/telemetry
   STAGE=C-rds
   ```
5. Stop the Stage B stack and start the RDS version:
   ```
   docker compose -f docker/docker-compose.yml down
   docker compose -f docker/docker-compose.rds.yml --env-file .env up --build -d
   ```
6. Check `/health` shows the app working and data being stored.
7. Note down time taken, what changed in code (almost nothing, only the database setting), and the cost difference.

## Optional extras

- HTTPS with a free certificate (Let's Encrypt and Nginx, needs a domain name).
- Amazon S3 for static files.
- AWS IoT Core plus DynamoDB for the telemetry path (closest to the Tata Motors story, more work).

## After testing

Stop or delete anything not needed. RDS and Elastic IPs that are unused still cost money. Keep one stage running for the viva and take screenshots of the others before shutting them down.
