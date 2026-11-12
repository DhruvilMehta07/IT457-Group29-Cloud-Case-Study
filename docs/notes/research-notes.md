# Research Notes, Week 1

Week 1 goal from the project plan: find primary sources, pull out architecture, cost and outcome data, and write a one page summary of the sources and the main points of the case study.

Rule for these notes: every fact has a source next to it. If we cannot find a source for something, we write "not found yet" and we do not guess.

## 1. Week 1 checklist

- [x] Find primary sources for Titan (the AWS case study)
- [x] Find sources for Tata Motors (Tata Elxsi pages, news reports, AWS blog, security reports, see section 4)
- [ ] Find the original AWS case study video for Tata Motors (the AWS India blog links to it, but we have not opened the video itself)
- [x] Pull out architecture facts for each company
- [x] Pull out cost facts for Titan
- [ ] Pull out cost facts for Tata Motors (none found for Tata Motors itself, only an unnamed client in section 4)
- [x] Pull out outcome facts for each company
- [x] Check every fact in `docs/week1-summary.md` against its source (all pages re-opened, except one row marked Not checked in section 4)
- [x] Write the one page summary in our own words (`docs/week1-summary.md`)
- [x] Write down open questions for the TA (section 6)

## 2. Where to look

- AWS customer stories: https://aws.amazon.com/solutions/case-studies/ (search for "Titan" and "Tata Motors")
- Titan case study on AWS: https://aws.amazon.com/solutions/case-studies/titan-case-study/
- Titan Company investor relations and annual reports (on the Titan website)
- Tata Motors annual reports and press releases (on the Tata Motors website)
- Tata Elxsi press release and TETHER pages (https://www.tataelxsi.com/services/cloud)
- AWS Summit India and re:Invent session lists for Titan or Tata Motors talks

## 3. Facts so far: Titan

Source for all rows: the AWS case study on Titan (link above). Every row was compared with the page.

| Fact | Checked |
|------|---------|
| Titan was founded in 1984 and has 16 brands (jewellery, watches, eyewear, fashion, fragrances) | Yes |
| AWS reports Titan revenue of over $6 billion in 2025 (the page does not name the currency) | Yes |
| Dhanteras is a three day festival with a big share of yearly jewellery sales | Yes |
| Titan has 850 stores, and the point of sale (POS) and CRM systems must handle thousands of transactions | Yes |
| In 2024 the POS and CRM systems had performance and scaling problems at the festival peak, so some stores processed sales by hand and customers queued | Yes |
| After 2024, Titan worked with its AWS Technical Account Manager and used AWS Countdown Premium, which complements AWS Enterprise Support | Yes |
| They did a Well-Architected review, resized EC2 instances and EKS workloads, tuned databases, added CloudWatch monitoring and API health checks | Yes |
| Result: jewellery sales up at Dhanteras 2025. The page is not consistent: the outcome section says 10 to 15 percent, the overview and benefits list say 15 percent | Yes, with this difference |
| Result: monthly cloud cost lowered by around $10,000 | Yes |
| Result: support tickets down 50 percent during the festival period | Yes |
| The benefits list shows a 100 percent reduction in database recovery time, with no baseline or method given anywhere on the page | Yes |
| The same approach was used at Akshaya Tritiya in April 2026. The page says store systems stayed fast and reliable | Yes |

## 4. Facts so far: Tata Motors

| Fact | Source | Checked |
|------|--------|---------|
| Tata Motors completed onboarding 500,000 vehicles onto a connected vehicle platform for its commercial, passenger and electric vehicles | DT Next (based on a Tata Elxsi statement), Tata Elxsi press release | Yes |
| The platform is Tether (a connected vehicle platform) from Tata Elxsi, described as a cloud based Internet of Things (IoT) data platform | DT Next. The Tata Elxsi press release calls it a modular, 5G ready platform | Yes |
| Tata Motors and Tata Elxsi started working together on Tether in early 2019 (the article gives the start of the collaboration, not a separate go live date) | DT Next, Tata Elxsi press release | Yes, with this caveat |
| It runs under the names Fleet Edge (commercial), iRA (passenger) and Zconnect (electric) | DT Next | Yes |
| Features include track and trace, geo-fencing and alerts, driver behaviour monitoring and fuel efficiency monitoring | DT Next, Automotive World, Tata Elxsi press release | Yes |
| The Automotive World page does not give a number of features, and does not call Tether cloud based or mention AWS. Our earlier note about more than 40 features is removed | Automotive World | Yes (removed) |
| Tata Elxsi says its cloud first digital platforms, for example for connected cars, are supported by AWS. No AWS service is named. The same page has a banner about the 500,000 vehicle milestone but does not say AWS runs that platform | Tata Elxsi cloud page | Yes |
| The Tether Auto page says it is a cloud based, vendor agnostic platform with over 2.3 million vehicles on the road, over 600 TB of data per month, 250 ms processing latency and a January 2020 launch. It names Tata Motors as a customer but names no cloud provider. These numbers are for the whole platform, not only Tata Motors | Tata Elxsi Tether Auto page | Yes |
| An unnamed "leading automotive enterprise" used an AWS based connected car analytics pipeline built by Tata Elxsi: Kafka for live data, Spark on Amazon EMR, Airflow on EC2, Amazon S3 as data lake, Elasticsearch for dashboards. Claimed results: 30 percent lower cloud cost, 3 times faster analytics, over $400K annual savings, 99.9 percent availability. The page does not name Tata Motors, so we only use it as an example of such a design. Its headline says 30 percent better processing efficiency, its impact section says 30 percent lower cloud cost, so treat the number with care | Tata Elxsi case study on real time vehicle analytics | Yes |
| AWS featured a Tata Motors case study (the post says "watch the Tata Motors AWS Case Study") and says Tata Motors uses AWS for development environments right after a project starts, saving four to six weeks of setup time | AWS News Blog, "In the Works: AWS Region in India" | Yes (we have not opened the case study video itself) |
| ITGlobal, a cloud services company, says Tata Motors moved to the cloud and quotes a Tata Motors IT head saying the move increased the working speed of business critical services. The page never names AWS or any cloud provider and gives no numbers. It is promotional | ITGlobal success story | Yes |
| A hosting partner says the Tata Motors corporate websites run on AWS services such as EC2, load balancers, RDS, S3, CloudFront and ElastiCache (partner claim, not from Tata Motors or AWS) | Allindia case study page | Not checked, the page could not be opened in our last check. Keep it out of the report unless someone opens it |
| A security researcher reported exposed AWS keys on Tata Motors web platforms. One set (E Dukaan) was in plain text, and a FleetEdge set was encrypted but could be decrypted with JavaScript in the browser. Over 70 TB of data in Amazon S3 buckets was exposed, and some website buckets were writable. Reported to the Indian CERT-In in August 2023, published in October 2025. Fixes took until early January 2024 with repeated follow up | eaton-works.com report, TechRepublic | Yes |
| Tata Motors said the issues were "promptly and fully addressed" and did not confirm whether affected users were told | TechRepublic, Outlook Business | Yes |

## 5. Architecture, cost and outcome table

| | Titan | Tata Motors |
|---|-------|-------------|
| Architecture (what is known) | POS and CRM apps on EC2 and EKS, databases, CloudWatch monitoring, API health checks | Cloud based connected vehicle platform (Tether) by Tata Elxsi. AWS supports Tata Elxsi platforms in general. Exact AWS services for Tata Motors not confirmed. A similar design (Kafka, EMR, S3) exists for an unnamed client |
| Cost data | About $10,000 less per month after tuning. No other numbers found | Nothing for Tata Motors itself. Only the unnamed client's claim of 30 percent lower cloud cost. Time saved: 4 to 6 weeks of setup for development environments |
| Outcome data | Sales up 10 to 15 percent (15 percent elsewhere on the page), tickets down 50 percent (AWS reported) | 500,000 vehicles on the platform. Tether overall: 2.3 million vehicles, 600 TB per month, 250 ms latency (Tata Elxsi claims) |
| Gaps to fill | How the database recovery number was measured | The Tata Motors AWS case study video itself, which AWS services Tata Motors uses, any cost numbers |

## 6. Open questions

1. Is the Titan case (scaling and readiness) acceptable for our topic, with the IoT part coming from Tata Motors?
2. The AWS India blog links to a Tata Motors AWS case study video. Can we find and watch it?
3. Numbers from AWS, Tata Elxsi and other vendors are claims, not audited results. We say so in the report.
4. The security report is useful as a risk lesson for moving to the cloud. We present it as one researcher's account plus the company's short statement.

## 7. Reminders for the summary

- Write in our own words. Do not copy sentences from the pages.
- Keep each fact tied to its source.
- Say clearly when something is a claim by a vendor and not something we checked.
