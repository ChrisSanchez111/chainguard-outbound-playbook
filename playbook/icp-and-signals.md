# ICP, Personas and Trigger Signals

The goal of this page: decide who to call and when, so every touch has a reason behind it.

## The product map (what I'm actually selling)

| Layer | Product | One-line value |
|---|---|---|
| Containers | Chainguard Containers | Hardened, minimal images with 97.6% fewer CVEs than open source equivalents, plus FIPS and STIG variants |
| Hosts | Chainguard VMs | Hardened VM images with a 7-day critical / 14-day high CVE SLA |
| Dependencies | Chainguard Libraries | Python, Java and JavaScript packages built from source |
| Pipeline | Chainguard Actions | Hardened GitHub Actions for CI/CD |

The licensing line that drives deals: the free tier gives five images with only `:latest` tags and no CVE SLA. Paid plans (per image or full catalog) add the contractual SLA and every supported version. Anyone with a compliance deadline needs the SLA, so "who is on the hook when a critical CVE drops?" is the most important qualification question.

---

## Segment 1: FedRAMP software providers (focus of this playbook)

Who: SaaS and software companies selling into the federal government, authorized or in process.

Pain: Monthly continuous monitoring. Every high CVE needs a fix within 30 days or a POA&M entry, and most findings come from base images. FedRAMP's 2026 Consolidated Rules add new vulnerability rulesets due December 7, 2026, ahead of wider Consolidated Rules adoption on January 1, 2027.

Chainguard angle: Fewer findings before the scan runs, FIPS-validated images for High, and an SLA tighter than FedRAMP's own windows.

Personas
- Economic: CISO / VP Engineering
- Owner: Head of Product Security / Director of Security Engineering
- Champion: Staff Security Engineer, DevSecOps lead
- Influencer: GRC / compliance lead who files the POA&Ms

Trigger signals
- FedRAMP authorization, Class change (for example, to Class D) or In Process status
- Pursuing DoD IL4 / IL5
- New government product inside the boundary
- Federal contract wins that add workloads
- New CISO or Head of Product Security

---

## Segment 2: Regulated enterprises

Who: Financial services, healthcare and critical infrastructure running containers at scale.

Pain: Auditors and customers ask for SBOMs and clean scans; security teams drown in findings they didn't create.

Chainguard angle: SBOMs on every image, fewer findings, FIPS where regulators require it.

Trigger signals: New regulation or audit finding, security incident at a peer, new CISO, cloud migration.

---

## Segment 3: AI and fast-growing software companies

Who: AI labs and high-growth SaaS shipping many images quickly (OpenAI and Snowflake are existing Chainguard customers, which shows the pattern).

Pain: Speed. Engineers don't want to stop shipping to patch base images.

Chainguard angle: Clean images by default, so security doesn't slow releases.

Trigger signals: Large funding round, enterprise or government expansion, SOC 2 or FedRAMP pursuit.

---

## Segment 4: Teams running their own hardening program

Who: Companies that build and maintain hardened images in-house (Knox Systems is an example on the target list).

Pain: Headcount and on-call burden for work that isn't their product.

Chainguard angle: Buy instead of build. Compare engineer hours against the catalog price.

Trigger signals: Hiring for "container security" or "image hardening" roles, public posts about their own hardened image program.

---

## Signal weights used in `tools/signal_scorer.py`

| Signal | Weight | Reasoning |
|---|---|---|
| FedRAMP authorized or in process | +20 | Remediation deadlines apply every month |
| Recent trigger (2026) | +15 | A fresh event creates urgency |
| FedRAMP High or IL5 | +15 | FIPS and STIG requirements raise the bar |
| Cloud-native SaaS | +10 | Ships containers, so image hygiene is daily work |
| Hosts other SaaS companies | +10 | One deal covers many tenants' workloads |
| Security vendor | +5 | Their own product has to pass a scanner |
| Parent company controls the stack | −15 | Narrows the opening to one workload |

Weights are a starting hypothesis to be tuned against which meetings actually convert to opportunities.

---

## Sources

- Chainguard: [Containers](https://www.chainguard.dev/containers), [Pricing](https://www.chainguard.dev/pricing), [FedRAMP solution](https://www.chainguard.dev/solutions/fedramp), [Customers](https://www.chainguard.dev/customers)
- FedRAMP 2026 Consolidated Rules: [Crowell & Moring](https://www.crowell.com/en/insights/client-alerts/time-for-a-change-fedramp-fundamentally-revamps-program-with-consolidated-rules-for-2026)
- Chainguard Enterprise BDR posting (personas and responsibilities): [Built In](https://www.builtincolorado.com/job/enterprise-business-development-representative-east/8878296)
