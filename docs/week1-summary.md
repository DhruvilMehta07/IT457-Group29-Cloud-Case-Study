# Week 1 Summary: Sources and Salient Points

**Course:** IT457 Cloud Computing | **Group:** 29
**Team:** Dhruvil Mehta (202301061), Jay Rathod (202301006), Jeet Patel (202611037)
**Topic:** Titan Industries and Tata Motors on AWS (digital business, IoT and telemetry)
**Date:** 20 October 2026

---

## 1. Sources found

| # | Source | Publisher | Type | What it gives us |
|---|--------|-----------|------|------------------|
| 1 | [Titan strengthens retail operations during festival season with AWS Enterprise Support and AWS Countdown Premium](https://aws.amazon.com/solutions/case-studies/titan-case-study/) | AWS (case study) | Primary | Problem, AWS services, outcome numbers for Titan |
| 2 | [Tata Motors brings 500,000 vehicles onboard on data platform Tether](https://www.dtnext.in/news/business/tata-motors-brings-500000-vehicles-onboard-on-data-platform-tether) | DT Next (news, based on a Tata Elxsi statement) | Secondary | Connected vehicle platform, brand names, features, scale |
| 3 | [Tata Elxsi interview on TETHER Auto](https://www.automotiveworld.com/news-releases/tata-elxsi-brings-new-age-solutions-for-driverless-cars-connected-vehicles-and-more-elxsi-cmo-nitin-pai/) | Automotive World (interview) | Secondary | What TETHER is, number of features and vehicles |
| 4 | [Tata Elxsi cloud services page](https://www.tataelxsi.com/services/cloud) | Tata Elxsi | Primary (vendor) | How Tata Elxsi uses AWS for connected cars |
| 5 | [In the Works: AWS Region in India](https://aws.amazon.com/blogs/aws/in-the-works-aws-region-in-india) | AWS News Blog | Primary | Confirms AWS featured a Tata Motors case study video (early AWS India period) |
| 6 | [Hacking India's largest automaker: Tata Motors](https://eaton-works.com/2025/10/28/tata-motors-hack/) | Eaton Zveare (security researcher) | Primary (researcher's report) | Security lessons: exposed AWS keys, FleetEdge, timeline |
| 7 | [Tata Motors Breach Exposed 70TB of Sensitive Data Before Fix](https://www.techrepublic.com/article/news-tata-motors-security-flaws/) | TechRepublic | Secondary | Independent news coverage of source 6 |
| 8 | [Digital Case Studies (Tata Motors website hosting)](https://www.allindia.com/homepage-highlights/tatamotors/tatamotors.aspx) | Allindia (hosting partner) | Secondary (vendor) | Which AWS services host the Tata Motors corporate website |

Still to find for Week 2: the original Tata Motors AWS case study video or page, Tata Motors annual report statements on cloud and connected vehicles, and an AWS Summit or re:Invent talk if one exists.

## 2. Salient points: Titan

Based mainly on source 1.

- **Who:** Titan is an Indian retail company founded in 1984 with 16 brands (jewellery, watches, eyewear, fashion, fragrances). The AWS page reports revenue of over 6 billion US dollars in 2025.
- **Problem:** During Dhanteras 2024, a big jewellery buying festival, the point of sale and CRM systems in its 850 stores slowed down. Some stores had to process sales by hand and customers waited in long queues.
- **What they did:** Before Dhanteras 2025 Titan worked with its AWS Technical Account Manager and used AWS Countdown Premium (a peak event support service) next to AWS Enterprise Support. They ran a Well-Architected review, resized EC2 instances and EKS workloads, tuned databases, added Amazon CloudWatch monitoring and API health checks.
- **Outcome (as reported by AWS):** Jewellery sales up by 10 to 15 percent during Dhanteras 2025, monthly cloud cost down by about 10,000 US dollars, support tickets down by 50 percent. The page also lists a 100 percent reduction in database recovery time but does not explain how it was measured, so we will treat that number carefully.
- **Repeat result:** The same approach was used for Akshaya Tritiya in April 2026 and went smoothly.
- **Services named:** EC2, EKS, CloudWatch, AWS Countdown Premium, AWS Enterprise Support.
- **Important observation:** This Titan story is about scaling and readiness of systems already on AWS, not a lift and shift migration. It also has no IoT part. Our report will say this clearly instead of forcing it into a migration story.

## 3. Salient points: Tata Motors

Based on sources 2 to 8.

- **Connected vehicle platform:** Tata Motors onboarded 500,000 vehicles onto a connected vehicle platform that covers its commercial, passenger and electric vehicles. The platform is Tether from Tata Elxsi, described as a cloud based IoT data platform. Work to adopt it started in early 2019.
- **Brands and features:** The platform runs under the names Fleet Edge (commercial), iRA (passenger) and Zconnect (electric). Features include track and trace, geo-fencing and alerts, driver behaviour monitoring and fuel efficiency monitoring.
- **AWS link:** Tata Elxsi says its cloud platforms are supported by AWS for connected cars. We still need a primary source that says exactly which AWS services Tether and Tata Motors use, so we will not claim specific services yet.
- **Earlier AWS use:** AWS featured Tata Motors as an India customer. A hosting partner reports that the Tata Motors corporate websites run on EC2, load balancers, RDS, S3, CloudFront and ElastiCache. We treat this as a partner claim.
- **Security lesson:** A researcher reported in 2025 that AWS keys exposed on Tata Motors web platforms (including FleetEdge) gave access to a very large amount of data. Reporting happened in 2023 and fixes took time. This is useful for our analysis of risks when moving to the cloud.

## 4. Open issues and questions

1. The project document describes Titan as "digital business and properties on AWS using IoT and telemetry". The AWS case we found for Titan is about peak load readiness for retail stores. We want to confirm with the TA that using this case, and connecting the IoT part through Tata Motors, is fine.
2. We have not yet found the primary AWS page for Tata Motors. We will keep searching in Week 2.
3. Numbers from vendors and AWS marketing pages are claims, not audited results. We will say so in the report.

## 5. Plan for Week 2

Detailed case analysis and architecture diagram, finish the local Docker stage of the exercise, and write the 10 page report (see `docs/plan.md`).
