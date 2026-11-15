# Costs

This file compares what each stage would cost per month if it ran all the time. The numbers come from the AWS Pricing Calculator, region Asia Pacific (Mumbai), On-Demand prices, Linux. These are estimates for a full month, 24 hours a day. In practice we only ran each stage for a short time, and our usage was paid from AWS free plan credits.

The exported estimates are in `docs/cost-estimates/` and the screenshots in `docs/screenshots/`.

## Stage A: laptop

0 USD. It runs on a laptop that we already own. The cost of the laptop's electricity and our own time is not counted.

## Stage B: one EC2 machine

Estimate: `docs/cost-estimates/stageB-cost-estimate.pdf` and `docs/screenshots/stageB-cost-estimate.png`.

| Item | Setting | Monthly cost (USD) |
|------|---------|--------------------|
| Amazon EC2 | One `t3.micro`, Linux, On-Demand, 100 percent of the month. The line also includes a 20 GB gp3 disk, detailed monitoring and 1 GB per month of data out to the internet | 12.21 |
| Public IPv4 address (Amazon VPC) | One address in use (our Elastic IP) | 3.65 |
| **Total Stage B** | | **15.86** |

For a full year the calculator shows 190.32 USD.

## Stage C: EC2 machine plus RDS

Estimate: `docs/cost-estimates/stageC-cost-estimate.pdf` and `docs/screenshots/stageC-cost-estimate.png`.

The app still runs on the same EC2 machine, so Stage C has everything in Stage B and adds the database.

| Item | Setting | Monthly cost (USD) |
|------|---------|--------------------|
| Amazon EC2 (same as Stage B) | `t3.micro`, 20 GB disk, detailed monitoring, 1 GB out | 12.21 |
| Public IPv4 address (same as Stage B) | One address in use | 3.65 |
| Amazon RDS for PostgreSQL | `db.t4g.micro`, Single AZ, 20 GB gp3, On-Demand | 17.95 |
| **Total Stage C** | | **33.81** |

For a full year the calculator shows 405.72 USD.

## Comparison

| | Stage A | Stage B | Stage C |
|---|---------|---------|---------|
| Estimated monthly cost (USD) | 0 | 15.86 | 33.81 |
| Estimated cost for 12 months (USD) | 0 | 190.32 | 405.72 |
| Extra cost compared with the stage before | | 15.86 | 17.95 (about 113 percent more than Stage B) |
| Who looks after the database | us | us | AWS |

Moving the database to RDS added about 18 USD a month. For that money AWS takes over the database backups, the patching and the operating system of the database machine. In Stage B and Stage A those jobs would be ours.

## What we changed in the calculator, and why

When we added RDS the calculator first showed 61.02 USD for the database line. Three optional add ons were switched on by default and we did not use them:

- RDS Proxy (a connection pooler in front of the database)
- CloudWatch Database Insights (extra monitoring)
- RDS Extended Support (paid support for old database versions)

Our app connects to the database directly, we only use the basic monitoring graphs, and we run a current PostgreSQL version (16). With the three set to No the RDS line is 17.95 USD. This shows that the calculator can overestimate a lot if its defaults are left on, so each option should be read before it is accepted.

## What is not in the estimates

- Taxes. The calculator says it does not include them.
- Backups beyond the free amount. Our automatic backup retention is one day and the database is small.
- Data transfer in. Data sent into AWS is free.
- The time we spent. We do not count labour.

## The real bill after Stage C setup

The estimates above are for a full month. To check them, we opened the AWS Bills page after Stage B had been running for 64 hours and the RDS database for about 21.5 hours. Screenshots: `docs/screenshots/cost-actual-so-far-1.png` and `cost-actual-so-far-2.png`.

| Item on the bill | Usage | Charge (USD) |
|------------------|-------|--------------|
| EC2 `t3.micro` instance hours | 64 hours at 0.0112 per hour | 0.72 |
| EBS gp3 disk storage | 20.528 GB-months at 0.0912 | 1.87 |
| RDS `db.t4g.micro` Single-AZ, PostgreSQL | 21.524 hours at 0.021 per hour | 0.45 |
| RDS gp3 storage | 0.626 GB-months at 0.131 | 0.08 |
| Public IPv4 address in use | 65.284 hours at 0.005 per hour | 0.33 |
| CloudWatch (first 10 metrics are free) | 0.233 metrics | 0.00 |
| Data transfer, S3, Glue, Key Management Service | | 0.00 |
| **Total before credits** | | **3.45** |
| Tax | | 0.00 |

Every service total on the page reads 0.00 because AWS applies a matching credit line to each one. So we paid nothing in cash. The credits page (`docs/screenshots/cost-credits-so-far.png`) shows 160 USD of credits issued: 100 USD from the AWS Free Tier plus three tasks of 20 USD each (launch an instance with EC2, set up a cost budget, create an RDS database). The estimated amount used so far is 9.79 USD and the estimated amount remaining is 150.21 USD. AWS updates these numbers about every 24 hours.

### Do the estimates match the real prices?

Yes. The unit prices on the bill give the same monthly numbers as the Pricing Calculator:

| Item | Price on the bill | Over a 730 hour month | Calculator |
|------|-------------------|-----------------------|------------|
| Public IPv4 address | 0.005 per hour | 3.65 | 3.65 |
| RDS `db.t4g.micro` instance | 0.021 per hour | 15.33 | |
| RDS gp3 storage, 20 GB | 0.131 per GB-month | 2.62 | |
| RDS total | | 17.95 | 17.95 |

So the estimates were right. The real bill is much lower only because each stage ran for hours, not for a whole month.

### Budget

We set a monthly cost budget of 110 USD with three email alerts (`docs/screenshots/budget-alert-checked.png`). At the time of the screenshot the spend was 3.45 USD, which is 3.14 percent of the budget, and AWS forecast 8.70 USD for the month. The alert email address shows as verified and the alert status is OK, so none of the thresholds has been reached.
