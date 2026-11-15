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
