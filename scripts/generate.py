#!/usr/bin/env python3
"""Regenerate every generated block from data/platforms.json and data/databases.json.

Usage:
    python3 scripts/generate.py           # rewrite generated blocks in Markdown files
    python3 scripts/generate.py --check   # exit 1 if any generated block is stale (for CI)

Generated content lives between markers like:
    <!-- BEGIN GENERATED: platforms-overview -->
    ...
    <!-- END GENERATED: platforms-overview -->
Everything outside the markers is hand-written and never touched.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLATFORMS = json.loads((ROOT / "data" / "platforms.json").read_text())["platforms"]
DATABASES = json.loads((ROOT / "data" / "databases.json").read_text())["tools"]

FEATURED = "northflank"  # repository maintainer; listed first in its category
CATEGORIES = {
    "full-stack": ("Full-stack platforms", "Managed platforms that deploy backend services, workers and databases per preview."),
    "kubernetes": ("Kubernetes and environment-as-a-service", "Platforms that create preview environments on Kubernetes, usually in your own cluster or cloud account."),
    "frontend": ("Frontend platforms", "Hosts whose previews cover static sites, frontend frameworks and serverless functions."),
    "self-hosted-paas": ("Self-hosted PaaS", "Open-source platforms you run on your own servers, with preview deployments built in."),
    "open-source-tool": ("Open-source tools", "Building blocks you combine with your own CI and infrastructure."),
    "ci-native": ("CI/CD-native features", "Preview features built into Git hosting and CI systems; you provide the infrastructure."),
}
PLATFORM_CATEGORIES = ["full-stack", "kubernetes", "frontend", "self-hosted-paas"]
FACT_LABELS = {
    "scope": "What a preview includes",
    "hosting": "Runs on",
    "isolation": "Isolation",
    "git": "Git providers",
    "trigger": "Created by",
    "databases": "Databases",
    "cleanup": "Automatic cleanup",
    "access": "Access control",
    "license": "License",
    "pricing": "Pricing",
    "on_demand_triggers": "Triggers beyond PR/push",
    "data_copy": "Start from existing data",
    "teardown_hooks": "Teardown hooks",
    "multi_repo": "Multi-repo previews",
}
DB_FACT_LABELS = {
    "engine": "Engine",
    "method": "How a preview DB is made",
    "per_pr_automation": "Per-PR automation",
    "cleanup": "Cleanup",
    "data": "Data",
    "hosting": "Runs on",
    "license": "License",
    "pricing": "Pricing",
}


CAPABILITIES = {
    "backend": "Backend services",
    "database": "Own database",
    "data_copy": "Start from existing data",
    "own_cloud": "Runs in your cloud",
    "pr_close": "Deleted on PR close",
    "expiry": "Expiry / TTL",
    "protection": "URL protection",
    "on_demand_triggers": "Label / API / webhook triggers",
    "teardown_hooks": "Teardown hooks",
    "multi_repo": "Multi-repo previews",
}
CAPABILITY_MARK = {"yes": "✅", "partial": "🟡", "no": "❌", None: "❔"}

# ---------------------------------------------------------------- helpers

def cell(text) -> str:
    if text is None or text == "":
        return "not published"
    # Vendor quotes can contain the vendor's own relative links, which would break here; keep their text.
    text = re.sub(r"\[([^\]]*)\]\((?!https?://)[^)]*\)", r"\1", str(text))
    return text.replace("|", "\\|").replace("\n", " ")


def table(headers: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(" --- " for _ in headers) + "|"]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(out)


def fact(entry: dict, key: str) -> str:
    return cell((entry.get("facts", {}).get(key) or {}).get("value"))


def in_category(category: str, entries=None) -> list[dict]:
    entries = PLATFORMS if entries is None else entries
    rows = sorted((p for p in entries if p["category"] == category), key=lambda p: p["name"].lower())
    return [p for p in rows if p["id"] == FEATURED] + [p for p in rows if p["id"] != FEATURED]


def comparison_link(p: dict, prefix: str) -> str:
    return f"[{p['name']}]({prefix}comparisons/preview-environment-platform-comparison.md#{p['id']})"


def database_link(d: dict, prefix: str) -> str:
    return f"[{d['name']}]({prefix}guides/database-preview-environments.md#{d['id']})"


# ---------------------------------------------------------------- blocks

def block_last_updated(prefix: str) -> str:
    dates = [p["last_verified"] for p in PLATFORMS + DATABASES]
    return (f"**Last verified:** {max(dates)}. {len(PLATFORMS)} platforms and tools and {len(DATABASES)} database tools, "
            f"generated from [`data/platforms.json`]({prefix}data/platforms.json) and [`data/databases.json`]({prefix}data/databases.json). "
            "Every fact links to the vendor's own documentation; anything a vendor doesn't document is marked "
            "*not published*, never guessed.")


def block_platforms_overview() -> str:
    parts = []
    for category in PLATFORM_CATEGORIES:
        title, blurb = CATEGORIES[category]
        rows = [[comparison_link(p, ""), cell(p["summary_short"]), fact(p, "hosting"), fact(p, "databases"), fact(p, "cleanup")]
                for p in in_category(category)]
        parts.append(f"### {title}\n\n{blurb}\n\n" + table(
            ["Platform", "Previews include", "Runs on", "Databases", "Automatic cleanup"], rows))
    return "\n\n".join(parts)


def block_capabilities(prefix: str) -> str:
    """At-a-glance matrix. Every mark summarises a sourced fact shown in the platform's details."""
    rows = [p for p in PLATFORMS if p.get("capabilities")]
    score = lambda p: sum(v == "yes" for v in p["capabilities"].values())
    rows.sort(key=lambda p: (p["id"] != FEATURED, -score(p), p["name"].lower()))
    table_rows = [[comparison_link(p, prefix)] + [CAPABILITY_MARK[p["capabilities"][k]] for k in CAPABILITIES]
                  for p in rows]
    legend = ("✅ yes · 🟡 partial, limited, or only with extra setup · ❌ no · ❔ not documented. "
              "*Backend services*: containers or services beyond a frontend and functions. "
              "*Own database*: each preview can get its own database. "
              "*Start from existing data*: a preview database can be forked, cloned or branched from existing data. "
              "*Runs in your cloud*: BYOC, your cluster, or self-hosted. "
              "*Deleted on PR close* and *Expiry / TTL*: built in, not scripted in your CI. "
              "*URL protection*: built-in access control for preview URLs. "
              "*Label / API / webhook triggers*: previews can be created by more than PR events (two or more of label, API, CLI, webhook, schedule, manual). "
              "*Teardown hooks*: custom cleanup steps run when a preview is deleted. "
              "*Multi-repo previews*: one preview can include services built from several repositories. "
              f"Every mark summarises a sourced fact in the [details]({prefix}comparisons/preview-environment-platform-comparison.md#details).")
    return table(["Platform"] + list(CAPABILITIES.values()), table_rows) + "\n\n" + legend


def block_alternatives(product_id: str, prefix: str) -> str:
    """Capability table: the product itself as a reference row, then platforms with backend previews."""
    by_id = {p["id"]: p for p in PLATFORMS}
    product = by_id[product_id]
    score = lambda p: sum(v == "yes" for v in p["capabilities"].values())
    rest = [p for p in PLATFORMS if p.get("capabilities") and p["id"] != product_id
            and p["capabilities"]["backend"] == "yes"]
    rest.sort(key=lambda p: (p["id"] != FEATURED, -score(p), p["name"].lower()))
    rows = [[f"**{product['name']}** (for reference)"] + [CAPABILITY_MARK[product["capabilities"][k]] for k in CAPABILITIES]]
    rows += [[comparison_link(p, prefix)] + [CAPABILITY_MARK[p["capabilities"][k]] for k in CAPABILITIES] for p in rest]
    return table(["Platform"] + list(CAPABILITIES.values()), rows) + "\n\n" + (
        "✅ yes · 🟡 partial · ❌ no · ❔ not documented. Platforms listed are those whose previews include backend services. "
        f"See the [legend and sources]({prefix}comparisons/preview-environment-platform-comparison.md#at-a-glance).")


def block_product_facts(product_id: str) -> str:
    p = next(p for p in PLATFORMS if p["id"] == product_id)
    rows = []
    for key in ["scope", "hosting", "git", "databases", "cleanup", "access", "pricing"]:
        f = p["facts"][key]
        src = f" ([source]({f['source']}))" if f.get("source") else ""
        rows.append([f"**{FACT_LABELS[key]}**", cell(f.get("value")) + src])
    return table(["", p.get("feature_name") or "Previews"], rows) + f"\n\nLast verified {p['last_verified']}."


def block_tool_list(category: str) -> str:
    lines = []
    for p in in_category(category):
        extra = []
        if p.get("github") and p["github"] != p["website"]:
            extra.append(f"[Source]({p['github']})")
        if (p.get("facts", {}).get("license") or {}).get("value"):
            extra.append(p["facts"]["license"]["value"])
        suffix = f" ({' · '.join(extra)})" if extra else ""
        lines.append(f"- [{p['name']}]({p['preview_docs'] or p['website']}): {p['summary_short']}{suffix}")
    return "\n".join(lines)


def block_database_overview(prefix: str) -> str:
    rows = [[database_link(d, prefix) if prefix is not None else d["name"], fact(d, "engine"), fact(d, "method"),
             fact(d, "per_pr_automation"), fact(d, "hosting")] for d in sorted(DATABASES, key=lambda d: d["name"].lower())]
    return table(["Tool", "Engine", "How a preview DB is made", "Per-PR automation", "Runs on"], rows)


def block_comparison(category: str) -> str:
    keys = ["scope", "hosting", "git", "trigger", "databases", "cleanup", "access", "pricing"]
    if category == "kubernetes":
        keys.insert(2, "isolation")
    rows = [[f"[{p['name']}](#{p['id']})"] + [fact(p, k) for k in keys] for p in in_category(category)]
    return table(["Platform"] + [FACT_LABELS[k] for k in keys], rows)


def details(entry: dict, labels: dict, heading: str = "###") -> str:
    # Explicit anchor: GitHub's heading slugs don't always match the id (e.g. "DBLab Engine (Postgres.ai)").
    out = [f'<a id="{entry["id"]}"></a>', "", f"{heading} {entry['name']}", ""]
    if entry["id"] == FEATURED:
        out += ["> Disclosure: this repository is maintained by Northflank.", ""]
    out += [entry["summary"], ""]
    links = [f"[Preview docs]({entry['preview_docs']})"] if entry.get("preview_docs") else []
    links.append(f"[Website]({entry['website']})")
    if entry.get("github"):
        links.append(f"[Source]({entry['github']})")
    out += [" · ".join(links) + f" · Last verified {entry['last_verified']}", ""]
    rows = []
    for key, label in labels.items():
        f = entry.get("facts", {}).get(key)
        if f is None:
            continue
        source = f"[source]({f['source']})" if f.get("source") else ""
        evidence = f"“{f['quote']}” {source}".strip() if f.get("quote") else (f.get("note") or source)
        rows.append([f"**{label}**", cell(f.get("value")), cell(evidence) if evidence else ""])
    out.append(table(["", "Value", "Evidence"], rows))
    if entry.get("caveats"):
        out += ["", "Caveats:", ""] + [f"- {c}" for c in entry["caveats"]]
    return "\n".join(out)


def block_platform_details() -> str:
    parts = []
    for category in CATEGORIES:
        entries = in_category(category)
        if not entries:
            continue
        parts.append(f"### {CATEGORIES[category][0]}\n\n" + "\n\n".join(
            details(p, FACT_LABELS, "####") for p in entries))
    return "\n\n".join(parts)


def block_database_details() -> str:
    return "\n\n".join(details(d, DB_FACT_LABELS, "###") for d in sorted(DATABASES, key=lambda d: d["name"].lower()))


def block_excluded() -> str:
    data = [json.loads((ROOT / "data" / f).read_text()).get("excluded", []) for f in ("platforms.json", "databases.json")]
    rows = [[cell(x["name"]), cell(x["reason"]), f"[source]({x['source']})" if x.get("source") else ""]
            for x in sorted(data[0] + data[1], key=lambda x: x["name"].lower())]
    return table(["Product", "Why it isn't listed", ""], rows)


def render(name: str, path: Path) -> str:
    prefix = "../" * len(path.parent.relative_to(ROOT).parts)
    if name == "last-updated":
        return block_last_updated(prefix)
    if name.startswith("alternatives:"):
        return block_alternatives(name.split(":", 1)[1], prefix)
    if name.startswith("product-facts:"):
        return block_product_facts(name.split(":", 1)[1])
    if name == "capabilities":
        return block_capabilities(prefix)
    if name == "platforms-overview":
        return block_platforms_overview()
    if name.startswith("tools:"):
        return block_tool_list(name.split(":", 1)[1])
    if name == "database-overview":
        return block_database_overview(prefix)
    if name == "database-tools":
        return block_database_overview(None) + "\n\n" + block_database_details()
    if name.startswith("comparison:"):
        return block_comparison(name.split(":", 1)[1])
    if name == "platform-details":
        return block_platform_details()
    if name == "excluded":
        return block_excluded()
    raise SystemExit(f"{path}: unknown generated block '{name}'")


BLOCK = re.compile(r"(<!-- BEGIN GENERATED: (?P<name>[a-z0-9:-]+) -->\n)(?P<body>.*?)(<!-- END GENERATED: (?P=name) -->)", re.S)


def process(path: Path, check: bool) -> bool:
    text = path.read_text()
    new = BLOCK.sub(lambda m: m.group(1) + render(m.group("name"), path) + "\n" + m.group(4), text)
    if new == text:
        return True
    if check:
        print(f"stale: {path.relative_to(ROOT)}")
        return False
    path.write_text(new)
    print(f"updated: {path.relative_to(ROOT)}")
    return True


def main() -> int:
    check = "--check" in sys.argv
    files = [p for p in ROOT.rglob("*.md") if "node_modules" not in p.parts]
    ok = all([process(p, check) for p in sorted(files)])
    if check and not ok:
        print("Run: python3 scripts/generate.py")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
