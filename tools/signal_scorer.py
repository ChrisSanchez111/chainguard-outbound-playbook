#!/usr/bin/env python3
"""
Chainguard signal scorer.

Ranks FedRAMP-bound accounts by buying signals and prints a call sheet.
Standard library only.

Usage:
    python3 tools/signal_scorer.py data/target_accounts.csv
    python3 tools/signal_scorer.py data/target_accounts.csv --out output/call_sheet.csv
"""

import argparse
import csv
import os
import sys

# Weights mirror playbook/icp-and-signals.md. Tune against real conversion data.
WEIGHTS = {
    "fedramp_active": 20,           # authorized or in process: CVE remediation deadlines apply
    "recent_trigger": 15,           # FedRAMP, funding or leadership event in 2026
    "high_or_il5": 15,              # High / IL5: FIPS and STIG requirements raise the bar
    "cloud_native_saas": 10,        # ships containers, so image hygiene is daily work
    "hosts_other_saas": 10,         # one deal covers many tenants' workloads
    "security_vendor": 5,           # their own product has to pass a scanner
    "parent_controlled_stack": -15, # parent company sets the base images
}


def yes(value):
    return str(value).strip().lower() in {"yes", "y", "true", "1"}


def score(row):
    total, hits = 0, []
    for field, weight in WEIGHTS.items():
        if yes(row.get(field, "")):
            total += weight
            hits.append(f"{field}({weight:+d})")
    return total, hits


def tier(points):
    if points >= 50:
        return "Tier 1: call this week"
    if points >= 35:
        return "Tier 2: sequence now"
    return "Tier 3: narrow angle"


def build_call_sheet(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    sheet = []
    for row in rows:
        points, hits = score(row)
        sheet.append({
            "account": row.get("account", ""),
            "score": points,
            "tier": tier(points),
            "trigger_date": row.get("trigger_date", ""),
            "lead_with": row.get("lead_with", ""),
            "trigger": row.get("signal_note", ""),
            "signals": "; ".join(hits),
            "source": row.get("source", ""),
        })
    sheet.sort(key=lambda r: (r["score"], r["trigger_date"]), reverse=True)
    return sheet


def print_sheet(sheet):
    print(f"\n{'#':>2}  {'Account':<18}{'Score':>6}  {'Tier':<24}Lead with")
    print("-" * 90)
    for i, r in enumerate(sheet, 1):
        print(f"{i:>2}  {r['account']:<18}{r['score']:>6}  {r['tier']:<24}{r['lead_with']}")
        print(f"{'':>4}trigger: {r['trigger']} ({r['trigger_date']})")
    tier1 = sum(1 for r in sheet if r["tier"].startswith("Tier 1"))
    print(f"\n{len(sheet)} accounts scored, {tier1} tier-1.\n")


def write_markdown(sheet, path):
    lines = [
        "# Call Sheet",
        "",
        "Output of `tools/signal_scorer.py` run on `data/target_accounts.csv`. Each account earns points for buying signals and loses points when a parent company controls the stack; the total sets the tier.",
        "",
        "| Rank | Account | Score | Tier | Lead with | Trigger |",
        "|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(sheet, 1):
        trigger = f"{r['trigger']} ({r['trigger_date']})"
        if r["source"]:
            trigger = f"[{r['trigger']}]({r['source']}) ({r['trigger_date']})"
        lines.append(f"| {i} | {r['account']} | {r['score']} | {r['tier']} | {r['lead_with']} | {trigger} |")
    weights = ", ".join(f"{k.replace('_', ' ')} {v:+d}" for k, v in WEIGHTS.items())
    lines += ["", f"Signal weights: {weights}.", "",
              "Tiers: 50 and up = call this week; 35 to 49 = sequence now; under 35 = narrow angle.",
              "", "Regenerate with `python3 tools/signal_scorer.py data/target_accounts.csv --md tools/call-sheet.md`."]
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Markdown call sheet written to {path}")


def main():
    parser = argparse.ArgumentParser(description="Score accounts on Chainguard buying signals.")
    parser.add_argument("csv_path", help="Input account CSV (see data/target_accounts.csv)")
    parser.add_argument("--out", help="Optional path to write the call sheet CSV")
    parser.add_argument("--md", help="Optional path to write the call sheet as a Markdown page")
    args = parser.parse_args()

    if not os.path.exists(args.csv_path):
        sys.exit(f"File not found: {args.csv_path}")

    sheet = build_call_sheet(args.csv_path)
    print_sheet(sheet)

    if args.out:
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        with open(args.out, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(sheet[0].keys()))
            writer.writeheader()
            writer.writerows(sheet)
        print(f"Call sheet written to {args.out}")

    if args.md:
        write_markdown(sheet, args.md)


if __name__ == "__main__":
    main()
