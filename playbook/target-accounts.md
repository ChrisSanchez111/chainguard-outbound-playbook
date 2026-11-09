# Target Accounts: 10 East Coast FedRAMP Providers to Work Now

One persona: Head of Product Security / Director of Security Engineering at a software company selling into the federal government. This is the person who owns FedRAMP continuous monitoring, and every open CVE in their containers becomes their problem.

One geography: US East. Chainguard seems to split its enterprise BDR roles by region, and I'm based in New Jersey, so every account here is headquartered on the East Coast.

One trigger: FedRAMP. Every account here is FedRAMP authorized or working toward it, and FedRAMP's 2026 Consolidated Rules give all of them the same deadline. Providers have to adopt the new Vulnerability Detection & Response and Vulnerability Evaluation & Reporting rules by December 7, 2026, ahead of wider Consolidated Rules adoption on January 1, 2027. Vulnerability management just got a date on the calendar.

How the list was filtered
- East Coast headquarters only.
- Excluded Chainguard's public customers, including Nasdaq, Appian, Booz Allen, Shift5, Second Front, Elastic, Snowflake, Anduril, Cloudera, Forescout and GitLab.
- Excluded companies that reach FedRAMP through a partner that already handles hardened images (for example, SaaS deployed on Second Front's Game Warden).

Titles are what I'd search for in LinkedIn Sales Navigator. No individuals are named on purpose.

---

## Summary

| # | Account | HQ | Trigger (date) | Lead with | Score | Tier |
|---|---|---|---|---|---|---|
| 1 | Knox Systems | Arlington, VA | $25M Series A and new Arlington HQ; FedRAMP managed cloud for SaaS providers (Jul 2026) | Containers catalog + FIPS images across hosted tenants | 70 | 1 |
| 2 | Cyera | New York, NY | FedRAMP Class D (High) certified (Oct 2026) | FIPS images + CVE SLA for continuous monitoring | 65 | 1 |
| 3 | Pegasystems | Massachusetts | Pega Blueprint for Government launched, FedRAMP High and IL5 (Apr 2026) | FIPS + STIG-hardened images | 60 | 1 |
| 4 | MongoDB | New York, NY | Committed to FedRAMP High and IL5 for Atlas for Government (Jun 2025) | FIPS images + CVE SLA ahead of the upgrade | 45 | 2 |
| 5 | Rapid7 | Boston, MA | InsightGovCloud FedRAMP Moderate authorized (Jul 2025) | Containers catalog for InsightGovCloud | 35 | 2 |
| 6 | Commvault | Tinton Falls, NJ | FedRAMP authorized Commvault Cloud for Government (Jun 2024) | Per-image pricing for the government cloud | 30 | 3 |
| 7 | UiPath | New York, NY | FedRAMP authorized Automation Cloud Public Sector (Mar 2024) | Per-image pricing for the public sector cloud | 30 | 3 |
| 8 | Qlik | Pennsylvania | FedRAMP Moderate for Qlik Cloud Government (Oct 2022) | Per-image pricing for the government cloud | 30 | 3 |
| 9 | Boomi | Pennsylvania | FedRAMP authorization expanded to Workflow Automation (Aug 2022) | Per-image pricing for the federal iPaaS | 30 | 3 |
| 10 | SAP NS2 | Newtown Square, PA | $1B U.S. Army ERP modernization contract (Oct 2025) | FIPS + STIG images for one workload | 5 | 3 |

Scores come from [`tools/signal_scorer.py`](../tools/signal_scorer.py) run on [`data/target_accounts.csv`](../data/target_accounts.csv); see the [call sheet](../tools/call-sheet.md). Tier 1 = a fresh FedRAMP event on top of the December deadline. Tier 3 = the December deadline is the only trigger, so the angle is narrower.

---

## Account briefs

### Knox Systems
- Trigger: $25M Series A (March 2026), then a new Arlington, Virginia headquarters (July 2026) housing its security and risk operations centers. Knox runs a FedRAMP managed cloud that gets SaaS companies authorized, and it says it does it in 90 days. Recent examples include Tractian, Fieldguide and Craft.
- Pain: Every SaaS company Knox hosts brings its own containers, and every CVE in those containers lands in Knox's continuous monitoring. Knox publishes its own hardened images today, which means its team carries that maintenance.
- Use case: Chainguard's catalog as the base layer for every hosted tenant, with FIPS-validated variants for High workloads. One deal covers many companies' workloads.
- Titles: VP Security Operations · Head of Platform Engineering · CISO · Champion: DevSecOps lead
- Opening line: "Every SaaS company you bring onto Knox brings its own containers. Who owns patching those images today, you or them?"

### Cyera
- Trigger: FedRAMP Class D (formerly High) certification announced October 26, 2026, done in months rather than the usual 12 to 18. Launched "Cyera for Government." Valued at over $12B.
- Pain: Getting certified fast is the easy part. Staying certified means monthly continuous monitoring, and every high CVE needs a fix within 30 days or a POA&M entry.
- Use case: FIPS-validated images with a 7-day critical / 14-day high CVE SLA, which is tighter than FedRAMP's 30/90/180-day windows.
- Titles: Head of Product Security · Director of Security Engineering · VP Engineering, Federal · Champion: Staff Security Engineer
- Opening line: "Congrats on Class D. Now that you're in continuous monitoring, how many POA&M items come from base images versus your own code?"

### Pegasystems
- Trigger: Launched Pega Blueprint for Government in April 2026, FedRAMP High authorized and running in a DoD IL5 environment.
- Pain: High and IL5 workloads need FIPS-validated crypto and STIG hardening on top of CVE remediation, and every new government product adds images to maintain.
- Use case: FIPS-validated, STIG-hardened images as the standard base for government products.
- Titles: Head of Product Security · Director of Cloud Security · VP Engineering, Pega Cloud
- Opening line: "Blueprint for Government added another High and IL5 workload. Are your teams hardening those base images themselves today?"

### MongoDB
- Trigger: Committed in June 2025 to FedRAMP High and DoD IL5 for MongoDB Atlas for Government.
- Pain: Moving from Moderate to High raises the bar on FIPS crypto and remediation evidence across every image in the boundary.
- Use case: FIPS-validated images and a contractual CVE SLA, so the High upgrade isn't slowed down by base image findings.
- Titles: Head of Product Security · Director of Security Engineering, Atlas for Government
- Opening line: "As Atlas for Government moves toward High and IL5, how much of the remediation work is coming from base images?"

### Rapid7
- Trigger: InsightGovCloud received FedRAMP Moderate authorization in July 2025.
- Pain: A security vendor's own government cloud gets scanned like everyone else's. Findings in its own containers are both a compliance task and a credibility issue.
- Use case: Chainguard's catalog as the base for InsightGovCloud services.
- Titles: Head of Product Security · Director of Cloud Engineering, Public Sector
- Opening line: "Your customers use your scanner on their containers. What does InsightGovCloud's own scan look like before each monthly report?"

### Commvault
- Trigger: FedRAMP authorized Commvault Cloud for Government (June 2024). The December 7, 2026 vulnerability rules apply.
- Pain: Monthly continuous monitoring across a data protection platform, where downtime and findings both matter.
- Use case: Per-image pricing for the specific images inside the government boundary.
- Titles: Head of Product Security · Director of Security Engineering
- Local note: Tinton Falls, NJ, close enough for an in-person meeting.
- Opening line: "With the new FedRAMP vulnerability rules due December 7, how is the team preparing Commvault Cloud for Government?"

### UiPath
- Trigger: FedRAMP authorized Automation Cloud Public Sector (March 2024). The December 7, 2026 vulnerability rules apply.
- Pain: Keeping the public sector cloud's images clean month after month without pulling engineers off product work.
- Use case: Per-image pricing for the images inside the public sector boundary.
- Titles: Head of Product Security · Director of Cloud Security
- Opening line: "How much engineering time goes into the monthly continuous monitoring report for Automation Cloud Public Sector?"

### Qlik
- Trigger: FedRAMP Moderate for Qlik Cloud Government (October 2022), with IL4 work started. The December 7, 2026 vulnerability rules apply.
- Pain: Older authorizations carry older base images, and CVEs accumulate on them over time.
- Use case: Per-image pricing, starting with the images that generate the most findings.
- Titles: Head of Product Security · Director of Cloud Operations, Government
- Opening line: "Which base images in Qlik Cloud Government generate the most findings each month?"

### Boomi
- Trigger: FedRAMP authorization expanded to Workflow Automation (August 2022). The December 7, 2026 vulnerability rules apply.
- Pain: An integration platform touches many systems, so every image in the boundary is in scope.
- Use case: Per-image pricing for the federal iPaaS.
- Titles: Head of Product Security · Director of Security Engineering
- Opening line: "With the new FedRAMP vulnerability rules due December 7, are you planning to change how base images are patched?"

### SAP NS2
- Trigger: $1B U.S. Army contract (October 2025) to modernize Army ERP on RISE with SAP.
- Pain: Army workloads mean STIG hardening and FIPS crypto on every image.
- Use case: FIPS and STIG-hardened images for the containerized workloads NS2 controls.
- Titles: Director of Cloud Security · Head of Platform Engineering
- Tier 3: SAP sets most of the stack, so lead with one workload NS2 owns, not a platform standard.
- Opening line: "On the Army program, which containerized workloads does NS2 own the images for, versus what comes from SAP?"

---

## Sources
- FedRAMP 2026 Consolidated Rules and deadlines: [Crowell & Moring](https://www.crowell.com/en/insights/client-alerts/time-for-a-change-fedramp-fundamentally-revamps-program-with-consolidated-rules-for-2026)
- Knox Systems: [Arlington HQ announcement](https://knoxsystems.com/blog/knox-systems-opens-arlington-virginia-headquarters-to-accelerate-federal-mission-support), [Series A, Pulse 2.0](https://pulse2.com/knox-systems-25-million-series-a/), [Tractian via Knox](https://www.prnewswire.com/news-releases/tractian-achieves-fedramp-high-authorization-through-partnership-with-knox-systems-bringing-asset-health-intelligence-to-federal-agencies-302824715.html)
- Cyera: [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/cyera-earns-fedramp-high-class-120000411.html)
- Pegasystems: [Business Wire](https://www.businesswire.com/news/home/20260407428509/en/Pega-Helps-Federal-Government-Modernize-Legacy-IT-Systems-with-Launch-of-Pega-Blueprint-for-Government)
- MongoDB: [MongoDB investor relations](https://investors.mongodb.com/news-releases/news-release-details/mongodb-announces-commitment-achieve-fedramp-high-and-impact)
- Rapid7: [Rapid7 press release](https://www.rapid7.com/about/press-releases/rapid7-achieves-fedramp-authorization-for-insightgovcloud-platform/)
- Commvault: [Wikipedia](https://en.wikipedia.org/wiki/Commvault)
- UiPath: [Business Wire](https://www.businesswire.com/news/home/20240326577805/en/UiPath-Announces-FedRAMP%C2%AE-Authorization-for-Its-Automation-Cloud%E2%84%A2-Public-Sector)
- Qlik: [Qlik Community](https://community.qlik.com/t5/Product-Innovation/Qlik-reaches-milestone-with-FedRAMP-Moderate-Authorization-for/ba-p/1991886)
- Boomi: [Business Wire](https://www.businesswire.com/news/home/20220829005191/en/Boomis-Industry-Leading-Platform-Expands-Existing-FedRAMP-Authorization-to-Include-Workflow-Automation-Service)
- SAP NS2: [Wikipedia](https://en.wikipedia.org/wiki/SAP_NS2)
- Modern Data Company on Game Warden (excluded): [IT Brief](https://itbrief.news/story/the-modern-data-company-wins-fedramp-high-approval)
- Chainguard customers: [chainguard.dev/customers](https://www.chainguard.dev/customers), [Containers page](https://www.chainguard.dev/containers)
