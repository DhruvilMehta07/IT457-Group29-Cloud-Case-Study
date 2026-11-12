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
| 3 | [Tata Elxsi interview on TETHER Auto](https://www.automotiveworld.com/news-releases/tata-elxsi-brings-new-age-solutions-for-driverless-cars-connected-vehicles-and-more-elxsi-cmo-nitin-pai/) | Automotive World (interview) | Secondary | Tata Motors as partner, the 500,000 vehicle milestone, example features. It gives no feature count and does not mention AWS |
| 4 | [Tata Elxsi cloud services page](https://www.tataelxsi.com/services/cloud) | Tata Elxsi | Primary (vendor) | Says Tata Elxsi's cloud first platforms, such as connected cars, are supported by AWS. No AWS service named |
| 5 | [In the Works: AWS Region in India](https://aws.amazon.com/blogs/aws/in-the-works-aws-region-in-india) | AWS News Blog | Primary | Links to a Tata Motors AWS case study and says Tata Motors uses AWS for development environments, saving 4 to 6 weeks of setup |
| 6 | [Hacking India's largest automaker: Tata Motors](https://eaton-works.com/2025/10/28/tata-motors-hack/) | Eaton Zveare (security researcher) | Primary (researcher's report) | Security lessons: exposed AWS keys, FleetEdge, timeline |
| 7 | [Tata Motors Breach Exposed 70TB of Sensitive Data Before Fix](https://www.techrepublic.com/article/news-tata-motors-security-flaws/) | TechRepublic | Secondary | Independent news coverage of source 6 |
| 8 | [Digital Case Studies (Tata Motors website hosting)](https://www.allindia.com/homepage-highlights/tatamotors/tatamotors.aspx) | Allindia (hosting partner) | Secondary (vendor) | Claims which AWS services host the Tata Motors corporate website. Page could not be opened in our last check, so we do not rely on it |
| 9 | [Cloud based architecture for real time vehicle analytics](https://www.tataelxsi.com/insights/case-study/cloud-based-architecture-for-real-time-vehicle-analytics) | Tata Elxsi (case study) | Primary (vendor) | An AWS based connected car pipeline (Kafka, EMR, S3) with claimed savings. Client is not named, so it is only an example |
| 10 | [Tether Auto connected vehicle platform](https://www.tataelxsi.com/insights/case-study/tether-auto-connected-vehicle-platform-of-the-future) | Tata Elxsi (case study) | Primary (vendor) | Platform scale (2.3 million vehicles, 600 TB per month, 250 ms latency), names Tata Motors as a customer, no cloud provider named |

Still to find for Week 2: the original Tata Motors AWS case study video or page, Tata Motors annual report statements on cloud and connected vehicles, and an AWS Summit or re:Invent talk if one exists.

## 2. Salient points: Titan

Based mainly on source 1, which we compared with the page.

- **Who:** Titan is an Indian retail company founded in 1984 with 16 brands (jewellery, watches, eyewear, fashion, fragrances). The AWS page reports revenue of over $6 billion in 2025.
- **Problem:** During Dhanteras 2024, a big jewellery buying festival, the point of sale and CRM systems in its 850 stores slowed down. Some stores had to process sales by hand and customers waited in long queues.
- **What they did:** Before Dhanteras 2025 Titan worked with its AWS Technical Account Manager and used AWS Countdown Premium (a peak event support service) next to AWS Enterprise Support. They ran a Well-Architected review, resized EC2 instances and EKS workloads, tuned databases, added Amazon CloudWatch monitoring and API health checks.
- **Outcome (as reported by AWS):** Jewellery sales up during Dhanteras 2025 (the page says 10 to 15 percent in one place and 15 percent in another), monthly cloud cost down by around $10,000, support tickets down by 50 percent. The page also lists a 100 percent reduction in database recovery time but gives no baseline or method, so we will treat that number carefully.
- **Repeat result:** The same approach was used for Akshaya Tritiya in April 2026 and went smoothly.
- **Services named:** EC2, EKS, CloudWatch, AWS Countdown Premium, AWS Enterprise Support.
- **Important observation:** This Titan story is about scaling and readiness of systems already on AWS, not a lift and shift migration. It also has no IoT part. Our report will say this clearly instead of forcing it into a migration story.

## 3. Salient points: Tata Motors

Based on sources 2 to 10.

- **Connected vehicle platform:** Tata Motors onboarded 500,000 vehicles onto a connected vehicle platform that covers its commercial, passenger and electric vehicles. The platform is Tether from Tata Elxsi, described as a cloud based IoT data platform. Tata Motors and Tata Elxsi started working together on it in early 2019.
- **Brands and features:** The platform runs under the names Fleet Edge (commercial), iRA (passenger) and Zconnect (electric). Features include track and trace, geo-fencing and alerts, driver behaviour monitoring and fuel efficiency monitoring.
- **AWS link:** Tata Elxsi says its cloud first platforms, for example for connected cars, are supported by AWS. No page we found says which AWS services Tether or Tata Motors use, so we do not claim specific services. Tata Elxsi has an AWS based connected car pipeline case study (Kafka, EMR, S3), but the client is not named, so we use it only as an example of how such a system can look.
- **Scale of the platform:** Tata Elxsi says Tether Auto has over 2.3 million vehicles on the road across customers, over 600 TB of data per month and 250 ms processing latency. These are vendor claims for the whole platform.
- **Earlier AWS use:** The AWS India blog links to a Tata Motors AWS case study and says Tata Motors uses AWS for development environments, saving four to six weeks of setup time. We have not opened the case study video itself.
- **Security lesson:** A researcher published in 2025 that AWS keys exposed on Tata Motors web platforms (including FleetEdge) gave access to over 70 TB of data in Amazon S3 buckets. It was reported in 2023 and fixes took until early 2024. Tata Motors said the issues were promptly and fully addressed. This is useful for our analysis of risks when moving to the cloud.

## 4. Open issues and questions

1. The project document describes Titan as "digital business and properties on AWS using IoT and telemetry". The AWS case we found for Titan is about peak load readiness for retail stores. We want to confirm with the TA that using this case, and connecting the IoT part through Tata Motors, is fine.
2. We have not opened the Tata Motors AWS case study that the AWS India blog links to. We will look for it in Week 2.
3. Numbers from vendors and AWS marketing pages are claims, not audited results. We will say so in the report.

## 5. Plan for Week 2

Detailed case analysis and architecture diagram, finish the local Docker stage of the exercise, and write the 10 page report (see `docs/plan.md`).
