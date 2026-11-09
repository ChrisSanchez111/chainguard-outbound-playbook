# The Sequence: (For Example) 5 Touches, 1 Persona

Persona: Head of Product Security / Director of Security Engineering at a FedRAMP software provider

Pain: Every container image in the FedRAMP boundary gets scanned monthly. Each high CVE needs a fix within 30 days or a POA&M entry, and most of those findings come from base images the team didn't write. Engineers spend their time patching other people's code instead of shipping product.

Use case: Swap base images for Chainguard's hardened, minimal images. They ship with 97.6% fewer CVEs than open source equivalents, FIPS-validated variants, STIG hardening, and a contractual CVE SLA of 7 days for critical and 14 days for high.

Value prop: Clean scans and fewer POA&Ms without pulling engineers off product work. Chainguard's SLA is tighter than FedRAMP's own 30/90/180-day remediation windows.

CTA: 20 minutes to look at where their monthly findings come from, or start with five free images on their own pipeline.

`{trigger}` and `{opening_line}` come from [`target-accounts.md`](target-accounts.md).

| Day | Touch |
|---|---|
| 1 | Email 1 |
| 3 | Call + voicemail |
| 5 | LinkedIn |
| 7 | Email 2: value (guide) |
| 10 | Closing email |

---

## Touch 1 · Email (Day 1)

Subject: {company}'s December 7 FedRAMP deadline

> Hi {first_name},
>
> FedRAMP's new vulnerability rules take effect December 7, and {trigger}. For most teams, the biggest share of monthly findings isn't their own code. It's the base images underneath it.
>
> Chainguard replaces those base images with hardened, minimal ones: 97.6% fewer CVEs than the open source versions, FIPS-validated variants, and a contractual SLA of 7 days on criticals and 14 on highs, against FedRAMP's 30-day window for highs.
>
> Worth 20 minutes to look at where {company}'s monthly findings come from?
>
> Chris

---

## Touch 2 · Call (Day 3)

Opener (permission-based)

> "Hi {first_name}, Chris Sanchez with Chainguard. This is a cold call. Can I take 30 seconds, and you tell me if it's worth more?"

Reason for calling

> "{opening_line}"
>
> Example: "Congrats on Class D. Now that you're in continuous monitoring, how many POA&M items come from base images versus your own code?"

Listen for one of three answers, then ask the follow-up

| What they say | Follow-up |
|---|---|
| "We patch base images ourselves." | "How many engineer hours a month does that take, and who owns it when a critical drops on a Friday?" |
| "We already use a scanner." | "The scanner finds the CVEs. Who fixes them? We remove most of them before the scan runs." |
| "We use Docker Hardened Images / Iron Bank." | "What's the SLA on critical fixes, and does it cover every image in your boundary?" |

Ask

> "Fair to grab 20 minutes to compare your last scan against the same images on Chainguard? How's Tuesday or Wednesday?"

Voicemail drop (~20 seconds)

> "Hi {first_name}, Chris Sanchez with Chainguard. Saw {trigger}. I'm calling because FedRAMP's new vulnerability rules take effect December 7, and most of the findings teams fight each month come from base images, not their own code. We take those off the table. I'll send a short note. Again, Chris Sanchez, {phone}."

---

## Touch 3 · LinkedIn (Day 5)

Connection note (under 300 characters)

> Hi {first_name}, saw {trigger}. I work with FedRAMP teams cutting the CVE findings that come from base images. Left you a voicemail. Happy to share how other providers handle continuous monitoring if useful.

---

## Touch 4 · Email 2: value (Day 7)

The point of this touch is to give before asking again, and to get them onto Chainguard's site. The asset is Chainguard's FedRAMP page. It lays out FedRAMP's remediation windows next to Chainguard's SLA, which is exactly the comparison this persona cares about. It's ungated, so there's no form between them and the content.

Subject: FedRAMP remediation windows vs. a 7-day SLA

> Hi {first_name},
>
> No ask in this one. Chainguard put FedRAMP's remediation timelines (30 days for high, 90 for medium, 180 for low) next to what hardened base images change, including FIPS-validated containers, STIG hardening and how POA&M volume drops.
>
> {guide_link}
>
> If it raises questions about where {company} lands ahead of December 7, happy to walk through it.
>
> Chris

Guide link: [Chainguard for FedRAMP](https://www.chainguard.dev/solutions/fedramp)

Swap the asset by account: for a FedRAMP High or IL5 account, use the [Forescout case study](https://www.chainguard.dev/customers/forescout-trusts-chainguard-to-accelerate-fedramp-high-compliance-without-slowing-down-engineering); for a team weighing free alternatives, use [Chainguard vs. Docker Hardened Images](https://www.chainguard.dev/compare/chainguard-vs-docker).

---

## Touch 5 · Closing email (Day 10)

Subject: closing the loop on {company}

> Hi {first_name},
>
> Last note from me. If base image CVEs are on your list before the January 1 FedRAMP changes, three things usually decide build vs. buy:
>
> 1. How many findings come from base images versus your own code
> 2. Who owns the fix when a critical drops
> 3. How many engineer hours that takes each month
>
> Happy to walk through how other FedRAMP providers answered those. 20 minutes, your calendar: {calendar_link}
>
> Or, if your engineers would rather test it hands on, Chainguard's free tier gives you five images to run through your own scanner.
>
> If the timing's off, reply "later" and I'll check back in Q1.
>
> Chris
