# Chainguard Outbound Playbook

A signal-driven outbound system for selling secure open source to FedRAMP software providers.

I’m Christopher Sanchez. I’m an Army veteran, business development professional, and someone who’s always been drawn to technology and the business behind it.

At my current employer, I support commercial and enterprise sales across IBM i and Mainframe products/services.

I’m particularly interested in cybersecurity, cloud infrastructure, AI, and emerging technologies. I enjoy getting beyond the surface of a product, understanding the problems it solves, and figuring out how to bring it to the right market.

I put this playbook together to explore Chainguard’s technology, market opportunities, and how I’d approach enterprise outbound. I built it as part of my applications for Chainguard’s Enterprise and Commercial BDR roles.

Thanks for taking a look.

---

## What's in here

| File | What it is | Why it matters |
|---|---|---|
| [`playbook/target-accounts.md`](playbook/target-accounts.md) | 10 East Coast FedRAMP providers to work now, each with a sourced trigger, pain, use case and target titles | Who to call and why this month |
| [`playbook/sequence.md`](playbook/sequence.md) | One 5-touch sequence for one persona (very brief): email, call with voicemail drop, LinkedIn, value email with a Chainguard guide, closing email | Tight, tailored messaging with a clear ask |
| [`playbook/product-quick-reference.md`](playbook/product-quick-reference.md) | Every product mapped to use case, persona, pain and a qualifying question, plus competitors and objections | A cheat sheet for live calls |
| [`playbook/icp-and-signals.md`](playbook/icp-and-signals.md) | The wider market: four buyer segments and the signals behind the scoring | Context for where the list came from |
| [`tools/signal_scorer.py`](tools/signal_scorer.py) ([see the output](tools/call-sheet.md)) | Scores the target list on weighted buying signals and outputs a tiered call sheet | Turns a raw list into a prioritized call sheet |
| [`calculator/index.html`](calculator/index.html) ([open it live](https://chrissanchez111.github.io/chainguard-outbound-playbook/calculator/)) | CVE patching-cost and FedRAMP POA&M calculator (runs in the browser) | A conversation opener that quantifies the pain |

---

## Why Chainguard, why now

Most of the vulnerabilities security teams chase every month aren't in their own code. They're in the base images and open source packages underneath it. Chainguard rebuilds that open source from source, so the images ship with 97.6% fewer CVEs and come with an SLA to keep them that way. The sharpest version of that pain right now is FedRAMP. Every federal software provider has to fix high CVEs within 30 days or log a POA&M, and FedRAMP's 2026 Consolidated Rules put new vulnerability requirements on the calendar: December 7, 2026, ahead of wider Consolidated Rules adoption on January 1, 2027. This playbook narrows to that conversation: one persona (Head of Product Security at a FedRAMP provider), ten East Coast accounts, and one sequence built for them.

---

## How I work

At my current employer I'm the sole BDR on a ~3,000 account IBM i and mainframe territory supporting 12 AEs across North America and EMEA. I couldn't work that list by volume, so I co-designed a Claude-powered dashboard that pulls account and contact data from our CRM and data providers and ranks accounts on live signals: news, restructuring, intent, and product whitespace. I'm its only user and maintain its logic myself.

`tools/signal_scorer.py` is the same idea, rebuilt for Chainguard's market. [Here's what it produces](tools/call-sheet.md).

Also relevant: I'm comfortable being the least technical person in the room and closing that gap fast.

---

## Quick start

```bash
# Score the target list
python3 tools/signal_scorer.py data/target_accounts.csv

# Write the call sheet to CSV
python3 tools/signal_scorer.py data/target_accounts.csv --out output/call_sheet.csv

# Write the call sheet as a readable page
python3 tools/signal_scorer.py data/target_accounts.csv --md tools/call-sheet.md
```

No dependencies, standard library only.

The calculator is live at [chrissanchez111.github.io/chainguard-outbound-playbook/calculator](https://chrissanchez111.github.io/chainguard-outbound-playbook/calculator/).

---

## Notes

- Product and market facts come from Chainguard's public site, pricing page and press coverage as of November 2026. Sources are listed in each playbook file.
- The 10 target accounts are real companies with sourced, public triggers. No individuals are named. The list excludes Chainguard's public customers and companies that reach FedRAMP through a partner that already handles hardened images.
- Signal values in `data/target_accounts.csv` are my read of public news. In a real territory they'd come from CRM, intent data and job-posting feeds.
- Calculator defaults are editable assumptions, not Chainguard benchmarks.
- I'm not affiliated with Chainguard. Feedback from anyone on the team is very welcome.

Contact: csanchez72@fordham.edu · LinkedIn: [linkedin.com/in/christopher-sanchez-fordham](https://www.linkedin.com/in/christopher-sanchez-fordham)
