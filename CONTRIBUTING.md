# Contributing

Thanks for helping keep this list accurate. Vendors, maintainers and users are all welcome to add or correct entries. Every entry follows the same rules, including Northflank's.

## Ways to contribute

- **Correct a fact.** Open a PR that edits [`data/platforms.json`](data/platforms.json) or [`data/databases.json`](data/databases.json). Include the official source URL and a verbatim quote.
- **Add a platform, tool or database.** Check the [inclusion criteria](methodology.md#scope), then add an entry (template below).
- **Add a learning resource** (tutorial, talk, engineering write-up). Edit the [Learning resources](README.md#learning-resources) section of the README. Prefer resources that teach something concrete, and keep the description neutral and under 20 words.
- **Improve a guide or example.** PRs to `guides/` and `examples/` are welcome. Examples should run as written, or say clearly what you must fill in.

## Rules for data

1. **Official sources only:** vendor docs, pricing pages, the vendor's own blog or changelog, or its official repository.
2. **Every non-null fact needs `source` and `quote`.** The one exception is `"license": "Proprietary"` for a closed-source service that publishes no license text; give it a `note` instead. The quote is copied verbatim from the page, so a reviewer can find it with Ctrl+F. Use `...` to join fragments from the same page.
3. **Don't guess.** If something isn't documented, set `"value": null` and add a `"note"` saying why. Null renders as *not published*.
4. **Neutral wording.** No marketing language ("blazing fast", "best-in-class") in `summary` or values.
5. **Vendors editing their own entry** should say so in the PR description. That's fine and encouraged. The same sourcing rules apply.

## Entry template (`data/platforms.json`)

```json
{
  "id": "example",
  "name": "Example",
  "category": "full-stack",
  "website": "https://example.com",
  "preview_docs": "https://example.com/docs/previews",
  "feature_name": "Preview Environments",
  "github": null,
  "last_verified": "2026-10-23",
  "summary": "One neutral sentence: what it is and how its previews work.",
  "summary_short": "Up to ~15 words for the README table.",
  "facts": {
    "scope":     {"value": "Full-stack containers + databases", "source": "https://...", "quote": "..."},
    "hosting":   {"value": "Managed or BYOC", "source": "https://...", "quote": "..."},
    "git":       {"value": "GitHub, GitLab", "source": "https://...", "quote": "..."},
    "trigger":   {"value": "PR opened or updated", "source": "https://...", "quote": "..."},
    "databases": {"value": null, "source": null, "quote": null, "note": "Not documented."},
    "cleanup":   {"value": "Yes, on PR close", "source": "https://...", "quote": "..."},
    "access":    {"value": "Password or SSO", "source": "https://...", "quote": "..."},
    "license":   {"value": "Proprietary", "source": "https://...", "quote": "..."},
    "pricing":   {"value": "Billed as normal compute; free tier", "source": "https://...", "quote": "..."}
  },
  "capabilities": {
    "backend": "yes", "database": "yes", "data_copy": "partial", "own_cloud": "no",
    "pr_close": "yes", "expiry": "yes", "protection": null,
    "on_demand_triggers": "yes", "teardown_hooks": null, "multi_repo": "no"
  },
  "caveats": []
}
```

Platforms (not tools) also need `capabilities`: `yes`, `partial`, `no` or `null` (not documented), matching the facts. `on_demand_triggers`, `data_copy`, `teardown_hooks` and `multi_repo` also need sourced facts of the same name. See the [matrix legend](comparisons/preview-environment-platform-comparison.md#at-a-glance).

Categories: `full-stack`, `kubernetes`, `frontend`, `self-hosted-paas`, `open-source-tool` and `ci-native`. Database tools use `engine`, `method`, `per_pr_automation`, `cleanup`, `data`, `hosting`, `license` and `pricing` instead. See [`data/databases.json`](data/databases.json) for examples.

## Before you open the PR

```bash
python3 scripts/validate.py          # required fields and sources
python3 scripts/generate.py          # regenerate tables in the Markdown files
python3 scripts/check_quotes.py --only <id>   # confirm your quotes appear on their source pages
```

Commit the regenerated Markdown along with your data change. CI fails if the generated tables are stale.
