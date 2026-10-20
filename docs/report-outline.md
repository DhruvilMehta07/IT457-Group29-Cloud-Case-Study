# Report Outline (about 10 pages for Week 2, results added in Week 3)

Writing rules: short plain sentences, "we tried" and "we found", no copied text, no long dashes, every number has a source or is marked as our own test.

1. **Introduction and objective** (half page)
   What the project is, what we studied, what we built.
2. **Background: Titan and Tata Motors** (1 page)
   Who they are, why cloud matters to each.
3. **Case study: Titan** (2 pages)
   Problem at Dhanteras 2024, the AWS support and changes, the outcome, architecture diagram (EC2, EKS, CloudWatch, health checks), what is claimed and what is not explained.
4. **Case study: Tata Motors** (2 pages)
   Connected vehicle platform (Tether, Fleet Edge, iRA, Zconnect), 500,000 vehicles, AWS role, telemetry data flow diagram, the 2023 security findings and lessons.
5. **Analysis** (1 page)
   Benefits, risks, cost, what we would do differently. Compare the two cases: scaling an existing system versus building an IoT platform.
6. **Exercise design** (1.5 pages)
   Why the telemetry dashboard, the three stages, architecture diagrams for A, B and C, tools (Docker, EC2, RDS, Locust, CloudWatch).
7. **Team roles** (half page)
   Who did what, with commit references.
8. **Results** (added in Week 3, 2 to 3 pages)
   Effort table, cost table, latency graphs, observations.
9. **Lessons learned and conclusion** (half page)
10. **References**
    Every source from `docs/week1-summary.md` plus AWS docs and tools used.

Diagrams to draw (draw.io or similar): Titan architecture as described by AWS, Tata Motors telemetry flow, our Stage A, B and C architectures.
