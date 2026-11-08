# Product Quick Reference

A one-page cheat sheet for live calls. It ties each product to the use case, persona and pain, plus the one question that qualifies it.

## The line that decides deals

| | Free | Per Image | Catalog |
|---|---|---|---|
| Cost | Free, business email required | Enterprise quote | Starts at $19K for a team of 10, scales with engineering org size |
| What you get | Up to five images, five users, `:latest` tags only | The specific images you license, all supported tags | 3,000+ images, plus requests for new ones |
| CVE SLA | None | Contractual | Contractual |
| Right for | Trying it on a real pipeline | A targeted set of images, like one FedRAMP boundary | Making Chainguard the standard source for every image |

Free is the on-ramp. The SLA is what customers pay for, and FedRAMP providers need it because the deadline is contractual on their side too.

Qualifying questions: "How many images are inside your FedRAMP boundary?" and "Who fixes a critical CVE in a base image today, and how fast?"

---

## Products → use case → persona

| Product | What it does | Use case | Persona | Pain it solves | Discovery question |
|---|---|---|---|---|---|
| Chainguard Containers | Hardened, minimal container images with 97.6% fewer CVEs than open source equivalents, built from source with SBOMs | Replacing base images across a product | Head of Product Security, Platform Engineering lead | Monthly scan findings from code the team didn't write | "What share of your findings come from base images?" |
| FIPS images | 1,200+ FIPS 140-3 validated container variants | FedRAMP High, IL5, regulated workloads | Head of Product Security, Compliance lead | FIPS crypto requirements slowing authorization | "Which workloads in your boundary need FIPS-validated crypto?" |
| STIG hardening | OS-level STIG hardening on images; STIG-hardened hosts through Chainguard VMs | DoD and High workloads | Director of Cloud Security | Manual STIG work on every image | "Who applies STIGs to your images today, and how long does it take?" |
| Chainguard VMs | Hardened VM images with a 7-day critical / 14-day high, medium and low CVE SLA | Hosts under the containers | Platform Engineering lead | Findings at the host layer | "What runs underneath your containers, and who patches it?" |
| Chainguard Libraries | Python, Java and JavaScript libraries built from source, with backported CVE patches (Python today) | Securing dependencies, not just images | AppSec lead | Malicious or vulnerable packages from public registries | "How do you vet packages pulled from PyPI or npm?" |
| Chainguard Actions | 1,000+ hardened GitHub Actions with a hardening report per action | Securing the CI/CD pipeline | DevSecOps lead | Supply chain risk in third-party Actions | "How many third-party GitHub Actions run in your pipelines?" |
| EmeritOSS | Maintained forks of mature or deprecated open source projects (like Kaniko and ingress-nginx) | Keeping retired projects patched | Platform Engineering lead | Running software nobody upstream maintains anymore | "Do you run anything that's been deprecated upstream?" |

---

## Proof points to use
- 97.6% fewer CVEs than open source equivalents, and CVEs accumulate about 80% more slowly.
- CVE SLA of 7 days for critical and 14 days for high, medium and low, against FedRAMP's 30/90/180-day remediation windows.
- 1,200+ FIPS 140-3 validated variants and STIG hardening.
- Forescout used Chainguard to accelerate FedRAMP High compliance.
- Customers include Anduril, Snowflake, Elastic, Cloudera, Appian, Canva, Nasdaq and GitLab.
- Named a Leader in the 2026 Gartner Magic Quadrant for Software Supply Chain Security (as reported in funding coverage).
- $356M Series D at a $3.5B valuation (April 2025), plus $280M in growth funding for go-to-market (October 2025).

---

## Competitive landscape (know it, don't bash it)

| Alternative | Where you'll see it | How to position |
|---|---|---|
| Docker Hardened Images | Free under Apache 2.0, 1,000+ images built on Debian and Alpine; paid tier promises critical fixes in under 7 days | "Built from source versus patched on top of a distro. Compare the scans side by side and ask what the SLA covers." |
| Minimus | Hardened image startup with a free community tier | "Compare catalog size, FIPS coverage and the SLA in the contract." |
| Iron Bank (U.S. Air Force) | DoD teams | "Iron Bank is a repository with its own review process. Ask how long a new image or a critical fix takes to land there." |
| Red Hat UBI, SUSE, distro images | Enterprises standardized on a distro | "A full distro carries packages you don't need, and every one of them gets scanned." |
| Build in-house | Teams with a hardening program, like Knox | "How many engineers maintain it, and what happens on a Friday critical?" |
| Scanners (Wiz, Snyk, Rapid7) | Every account | Not a competitor. "The scanner finds the CVEs. Chainguard removes most of them before the scan runs." |

---

## Objections in one line each

| Objection | Response |
|---|---|
| "We patch our own images." | "How many engineer hours a month does that take? That's the number we replace." |
| "Docker Hardened Images are free now." | "Free is a fair start. Run both through your scanner and compare, then ask who's contractually on the hook for a critical." |
| "Migrating images is a big lift." | "Start with the five images that generate the most findings. The free tier covers exactly that test." |
| "Our scanner already handles it." | "Your scanner tells you what's broken. We hand you images where most of it isn't." |
| "Send me info." | "Happy to. So I send the right thing: is it POA&M volume, engineer time, or FIPS?" |

Sources: [Chainguard Containers](https://www.chainguard.dev/containers) · [Pricing](https://www.chainguard.dev/pricing) · [FedRAMP solution](https://www.chainguard.dev/solutions/fedramp) · [Forescout case study](https://www.chainguard.dev/customers/forescout-trusts-chainguard-to-accelerate-fedramp-high-compliance-without-slowing-down-engineering) · [Customers](https://www.chainguard.dev/customers) · [Chainguard vs. Docker](https://www.chainguard.dev/compare/chainguard-vs-docker) · [Chainguard vs. Minimus](https://www.chainguard.dev/compare/chainguard-vs-minimus) · [Docker Hardened Images coverage, TechTarget](https://www.techtarget.com/searchitoperations/news/366636656/Free-Docker-Hardened-Images-challenge-Chainguard) · [Series D, Crunchbase News](https://news.crunchbase.com/cybersecurity/startup-chainguard-raise-venture-unicorn-kleiner/) · [Growth funding, SecurityWeek](https://www.securityweek.com/chainguard-raises-280-million-in-growth-funding/amp/) · [Gartner mention, Value the Markets](https://www.valuethemarkets.com/cryptocurrency/news/chainguard-secures-800-million-to-enhance-cybersecurity-for-software-supply-chains)
