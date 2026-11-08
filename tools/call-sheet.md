# Call Sheet

Output of `tools/signal_scorer.py` run on `data/target_accounts.csv`. Each account earns points for buying signals and loses points when a parent company controls the stack; the total sets the tier.

| Rank | Account | Score | Tier | Lead with | Trigger |
|---|---|---|---|---|---|
| 1 | Knox Systems | 70 | Tier 1: call this week | Containers catalog + FIPS images across hosted tenants | [$25M Series A and new Arlington HQ; FedRAMP managed cloud for SaaS providers](https://knoxsystems.com/blog/knox-systems-opens-arlington-virginia-headquarters-to-accelerate-federal-mission-support) (2026-07-22) |
| 2 | Cyera | 65 | Tier 1: call this week | FIPS images + CVE SLA for continuous monitoring | [FedRAMP Class D (High) certified](https://finance.yahoo.com/technology/ai/articles/cyera-earns-fedramp-high-class-120000411.html) (2026-10-26) |
| 3 | Pegasystems | 60 | Tier 1: call this week | FIPS + STIG-hardened images | [Pega Blueprint for Government launched; FedRAMP High and IL5 environment](https://www.businesswire.com/news/home/20260407428509/en/Pega-Helps-Federal-Government-Modernize-Legacy-IT-Systems-with-Launch-of-Pega-Blueprint-for-Government) (2026-04-07) |
| 4 | MongoDB | 45 | Tier 2: sequence now | FIPS images + CVE SLA ahead of FedRAMP High and IL5 | [Committed to FedRAMP High and IL5 for Atlas for Government](https://investors.mongodb.com/news-releases/news-release-details/mongodb-announces-commitment-achieve-fedramp-high-and-impact) (2025-06-30) |
| 5 | Rapid7 | 35 | Tier 2: sequence now | Containers catalog for InsightGovCloud | [InsightGovCloud FedRAMP Moderate authorized](https://www.rapid7.com/about/press-releases/rapid7-achieves-fedramp-authorization-for-insightgovcloud-platform/) (2025-07-28) |
| 6 | Commvault | 30 | Tier 3: narrow angle | Per-image pricing for the government cloud | [FedRAMP authorized Commvault Cloud for Government](https://en.wikipedia.org/wiki/Commvault) (2024-06) |
| 7 | UiPath | 30 | Tier 3: narrow angle | Per-image pricing for Automation Cloud Public Sector | [FedRAMP authorized Automation Cloud Public Sector](https://www.businesswire.com/news/home/20240326577805/en/UiPath-Announces-FedRAMP%C2%AE-Authorization-for-Its-Automation-Cloud%E2%84%A2-Public-Sector) (2024-03-26) |
| 8 | Qlik | 30 | Tier 3: narrow angle | Per-image pricing for Qlik Cloud Government | [FedRAMP Moderate for Qlik Cloud Government](https://community.qlik.com/t5/Product-Innovation/Qlik-reaches-milestone-with-FedRAMP-Moderate-Authorization-for/ba-p/1991886) (2022-10-12) |
| 9 | Boomi | 30 | Tier 3: narrow angle | Per-image pricing for the federal iPaaS | [FedRAMP authorization expanded to Workflow Automation](https://www.businesswire.com/news/home/20220829005191/en/Boomis-Industry-Leading-Platform-Expands-Existing-FedRAMP-Authorization-to-Include-Workflow-Automation-Service) (2022-08-29) |
| 10 | SAP NS2 | 5 | Tier 3: narrow angle | FIPS + STIG images for one workload | [$1B U.S. Army ERP modernization contract](https://en.wikipedia.org/wiki/SAP_NS2) (2025-10-01) |

Signal weights: fedramp active +20, recent trigger +15, high or il5 +15, cloud native saas +10, hosts other saas +10, security vendor +5, parent controlled stack -15.

Tiers: 50 and up = call this week; 35 to 49 = sequence now; under 35 = narrow angle.

Regenerate with `python3 tools/signal_scorer.py data/target_accounts.csv --md tools/call-sheet.md`.
