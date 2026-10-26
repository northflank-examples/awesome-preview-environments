# Methodology

How entries are chosen, how facts are collected, and how the maintainer's conflict of interest is handled.

## Scope

**Platforms and tools.** An entry is included if developers can use it to create **an isolated, temporary deployment per pull request, merge request or branch**, and it is one of:

- a managed or self-hosted platform with a documented preview feature,
- an open-source building block whose documentation shows the per-PR workflow, or
- a CI/CD or Git-hosting feature designed for per-PR environments.

Open-source projects must be maintained: not archived, and with commits to the default branch in the last 18 months. Products that have been shut down, or whose preview feature has been removed, are listed under [excluded](comparisons/preview-environment-platform-comparison.md#excluded) with the reason and a source.

**Database tools.** Included if the tool creates a database per preview, by branching, cloning or provisioning, or prepares safe data for previews (masking, subsetting), and is documented for that use.

**Not included:** general deployment tools with no per-PR workflow, local development tools, and cloud development environments (Codespaces and the like). Those serve a different purpose.

## Sources

- Only **official sources** are used: vendor documentation, pricing pages, the vendor's own blog or changelog, and official repositories. Third-party comparisons, including Northflank's own blog comparison, aren't used as sources.
- Every fact in [`data/platforms.json`](data/platforms.json) and [`data/databases.json`](data/databases.json) has a `source` URL and a short **verbatim** `quote` from that page.
- [`scripts/check_quotes.py`](scripts/check_quotes.py) fetches every source and confirms each quote still appears on it. Run it before bumping `last_verified`.
- Each entry has a `last_verified` date. Entries are re-checked at least quarterly, and whenever a vendor announces a change.

## Fields

| Field | Meaning |
| --- | --- |
| What a preview includes | Static frontend, frontend + functions, full-stack containers, databases and other dependencies |
| Runs on | Managed (vendor cloud), BYOC (your cloud account, vendor-managed), or self-hosted |
| Git providers | Which Git hosts trigger previews automatically |
| Created by | PR opened, branch push, label, CLI, API, CI pipeline |
| Databases | Whether a preview can get its own database, and how: provisioned, forked, branched, seeded, or shared only |
| Automatic cleanup | Whether previews are deleted on PR close or merge, or after a TTL or inactivity |
| Access control | How preview URLs are protected |
| Pricing | How previews are billed, and any free tier. Not normalised into per-hour prices, because preview usage varies too much. |

## At-a-glance marks

Each platform has a `capabilities` block of ✅ yes, 🟡 partial, ❌ no or ❔ not documented marks, shown in the matrix at the top of the README and the comparison. Six marks summarise the facts above. Four (`on_demand_triggers`, `data_copy`, `teardown_hooks` and `multi_repo`) are backed by sourced facts of the same name, and the validator rejects a mark without a source. 🟡 means the capability exists with limits: a third-party integration, a beta, your own CI, or only some preview types. The criteria are in the matrix legend.

## Missing and uncertain data

- **not published** means the vendor doesn't document the value, or it couldn't be verified. It never means "no", "free" or "unlimited".
- When a vendor's documentation is ambiguous, the entry says so under **Caveats**.
- Feature names differ by vendor ("Deploy Previews", "Review Apps", "Preview Environments", "preview blueprints"). Each entry uses the vendor's own name.

## Generated content

Tables between `<!-- BEGIN GENERATED -->` markers are produced by [`scripts/generate.py`](scripts/generate.py) from the data files. Never edit them by hand. CI runs [`scripts/validate.py`](scripts/validate.py) and `generate.py --check`, and fails if the tables are stale or a fact has a value but no source.

## Conflict of interest

This repository is maintained by [Northflank](https://northflank.com), which sells a preview environment platform. To keep that from biasing the content:

- Northflank's entry follows the same schema and sourcing rules as every other entry, and is marked with a disclosure.
- Category tables are alphabetical, and the at-a-glance matrix is sorted by the number of ✅ marks. In both, Northflank is listed first as the maintainer, with a disclosure. Matrix marks are summaries of the sourced facts, and no entry gets an overall score or rank.
- Inclusion is based on the scope above, not on whether a product competes with Northflank.
- Corrections from any vendor or user are welcome. See [CONTRIBUTING](CONTRIBUTING.md). A correction with an official source is accepted even if it makes Northflank look worse by comparison.
