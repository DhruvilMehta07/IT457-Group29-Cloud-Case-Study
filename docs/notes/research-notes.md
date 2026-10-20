# Research Notes, Week 1

Week 1 goal from the project plan: find primary sources, pull out architecture, cost and outcome data, and write a one page summary of the sources and the main points of the case study.

Rule for these notes: every fact has a source next to it. If we cannot find a source for something, we write "not found yet" and we do not guess.

## 1. Week 1 checklist

- [ ] Find primary sources for Titan (AWS pages, press releases, annual report)
- [ ] Find primary sources for Tata Motors (AWS page or video, press releases, annual report)
- [ ] Pull out architecture facts for each company
- [ ] Pull out cost facts for each company
- [ ] Pull out outcome facts for each company
- [ ] Check every fact in `docs/week1-summary.md` against its source
- [ ] Write the one page summary in our own words
- [ ] Write down open questions for the TA

## 2. Where to look

- AWS customer stories: https://aws.amazon.com/solutions/case-studies/ (search for "Titan" and "Tata Motors")
- Titan case study on AWS: https://aws.amazon.com/solutions/case-studies/titan-case-study/
- Titan Company investor relations and annual reports (on the Titan website)
- Tata Motors annual reports and press releases (on the Tata Motors website)
- Tata Elxsi press release and TETHER pages (https://www.tataelxsi.com/services/cloud)
- AWS Summit India and re:Invent session lists for Titan or Tata Motors talks

## 3. Facts so far: Titan

Source for all rows: the AWS case study on Titan (link above). Mark "Checked" after comparing with the page.

| Fact | Checked |
|------|---------|
| Titan was founded in 1984 and has 16 brands (jewellery, watches, eyewear, fashion, fragrances) | |
| AWS reports Titan revenue of over 6 billion US dollars in 2025 | |
| Dhanteras is a three day festival with a big share of yearly jewellery sales | |
| Titan has 850 stores, and the point of sale (POS) and CRM systems must handle thousands of transactions at peak | |
| In 2024 the POS and CRM systems had performance and scaling problems at the festival peak, so some stores processed sales by hand and customers queued | |
| After 2024, Titan worked with its AWS Technical Account Manager and used AWS Countdown Premium with AWS Enterprise Support | |
| They did a Well-Architected review, resized EC2 instances and EKS workloads, tuned databases, added CloudWatch monitoring and API health checks | |
| Result: jewellery sales up 10 to 15 percent at Dhanteras 2025 | |
| Result: about 10,000 US dollars lower cloud cost per month | |
| Result: support tickets down 50 percent | |
| The page also lists a 100 percent reduction in database recovery time, but does not explain how it was measured | |
| The same approach was used at Akshaya Tritiya in April 2026 and went smoothly | |

## 4. Facts so far: Tata Motors

| Fact | Source | Checked |
|------|--------|---------|
| Tata Motors onboarded 500,000 vehicles onto a connected vehicle platform for its commercial, passenger and electric vehicles | DT Next (based on a Tata Elxsi statement) | |
| The platform is Tether from Tata Elxsi, a cloud based IoT data platform | DT Next, Automotive World interview | |
| Tata Motors started adopting Tether in early 2019 | DT Next | |
| It runs under the names Fleet Edge (commercial), iRA (passenger) and Zconnect (electric) | DT Next | |
| Features include track and trace, geo-fencing and alerts, driver behaviour monitoring and fuel efficiency monitoring | DT Next | |
| Tata Elxsi talks about more than 40 connected vehicle features for almost 500,000 vehicles | Automotive World interview | |
| Tata Elxsi says its cloud platforms for connected cars are supported by AWS | Tata Elxsi cloud page | |
| A hosting partner says the Tata Motors corporate websites run on AWS services such as EC2, load balancers, RDS, S3, CloudFront and ElastiCache (partner claim, not from Tata Motors or AWS) | Allindia case study page | |
| A security researcher reported that exposed AWS keys on Tata Motors web platforms (including FleetEdge) gave access to a very large amount of data. It was reported in 2023 and the report was published in 2025 | eaton-works.com report, TechRepublic | |

## 5. Architecture, cost and outcome table

| | Titan | Tata Motors |
|---|-------|-------------|
| Architecture (what is known) | POS and CRM apps on EC2 and EKS, databases, CloudWatch monitoring, API health checks | Cloud based connected vehicle platform (Tether), exact AWS services not confirmed yet |
| Cost data | About 10,000 US dollars less per month after tuning. No other numbers found | Not found yet |
| Outcome data | Sales up 10 to 15 percent, tickets down 50 percent (AWS reported) | 500,000 vehicles on the platform. No cost or performance numbers found yet |
| Gaps to fill | How the database recovery number was measured | Which AWS services are used, any cost numbers, the original AWS case study |

## 6. Open questions

1. Is the Titan case (scaling and readiness) acceptable for our topic, with the IoT part coming from Tata Motors?
2. Is there an original AWS case study page or video for Tata Motors?
3. Which numbers are verified and which are only claims by AWS or a vendor?

## 7. Reminders for the summary

- Write in our own words. Do not copy sentences from the pages.
- Keep each fact tied to its source.
- Say clearly when something is a claim by a vendor and not something we checked.