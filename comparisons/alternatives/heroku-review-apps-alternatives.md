# Heroku Review Apps alternatives (2026): preview environments for every pull request

Heroku Review Apps popularised per-PR environments. Each GitHub pull request in a pipeline gets a disposable app with its own add-ons, which is deleted when the PR closes. Teams look for alternatives when they move off Heroku, use GitLab or Bitbucket, need previews protected or running in their own cloud, or want more control over data and cost.

> Disclosure: this list is maintained by [Northflank](https://northflank.com/product/preview-environments), one of the alternatives below. Every fact links to the vendor's own documentation. See the [methodology](../../methodology.md).

## What Heroku Review Apps do

<!-- BEGIN GENERATED: product-facts:heroku -->
|  | Review Apps |
| --- | --- |
| **What a preview includes** | Full Heroku app: dynos + add-ons from app.json ([source](https://devcenter.heroku.com/articles/github-integration-review-apps)) |
| **Runs on** | Managed (Heroku cloud, incl. Private Spaces) ([source](https://devcenter.heroku.com/articles/github-integration-review-apps)) |
| **Git providers** | GitHub only ([source](https://devcenter.heroku.com/articles/github-integration-review-apps)) |
| **Databases** | Yes, add-ons (e.g. Heroku Postgres) provisioned per app; seed via postdeploy ([source](https://devcenter.heroku.com/articles/github-integration-review-apps)) |
| **Automatic cleanup** | Yes, on PR close; optional 1-30 day inactivity ([source](https://devcenter.heroku.com/articles/github-integration-review-apps)) |
| **Access control** | Public URL, random name by default ([source](https://devcenter.heroku.com/articles/github-integration-review-apps)) |
| **Pricing** | Dynos and add-ons billed as normal apps, per second ([source](https://devcenter.heroku.com/articles/github-integration-review-apps)) |

Last verified 2026-10-26.
<!-- END GENERATED: product-facts:heroku -->

## Why teams look for alternatives

- **GitHub only.** Review Apps work with GitHub repositories connected to a Heroku Pipeline.
- **Preview URLs are public by default,** with a random app name.
- **Heroku's cloud only.** Private Spaces add isolation, but previews can't run in your own cloud account.
- **Configured in `app.json`, with add-ons provisioned per app.** Seeding happens through a `postdeploy` script.

These limits only matter for some teams. See [when to stay](#when-to-stay-with-heroku).

## Alternatives at a glance

<!-- BEGIN GENERATED: alternatives:heroku -->
| Platform | Backend services | Own database | Start from existing data | Runs in your cloud | Deleted on PR close | Expiry / TTL | URL protection | Label / API / webhook triggers | Teardown hooks | Multi-repo previews |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Heroku** (for reference) | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| [Northflank](../../comparisons/preview-environment-platform-comparison.md#northflank) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Release](../../comparisons/preview-environment-platform-comparison.md#release) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Bunnyshell](../../comparisons/preview-environment-platform-comparison.md#bunnyshell) | ✅ | ✅ | 🟡 | ✅ | ✅ | ❔ | ✅ | ✅ | ✅ | ✅ |
| [Qovery](../../comparisons/preview-environment-platform-comparison.md#qovery) | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❔ |
| [Okteto](../../comparisons/preview-environment-platform-comparison.md#okteto) | ✅ | ✅ | 🟡 | ✅ | 🟡 | ✅ | ✅ | 🟡 | ✅ | ✅ |
| [Shipyard](../../comparisons/preview-environment-platform-comparison.md#shipyard) | ✅ | ✅ | ✅ | ❌ | 🟡 | 🟡 | ✅ | ✅ | ❔ | ✅ |
| [Railway](../../comparisons/preview-environment-platform-comparison.md#railway) | ✅ | ✅ | ✅ | ❌ | ✅ | ❔ | ❌ | ✅ | ❔ | 🟡 |
| [Render](../../comparisons/preview-environment-platform-comparison.md#render) | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❔ | ✅ | ❔ | 🟡 |
| [vCluster Platform (Loft)](../../comparisons/preview-environment-platform-comparison.md#vcluster-platform) | ✅ | ❔ | 🟡 | ✅ | 🟡 | ✅ | ✅ | ✅ | 🟡 | ❔ |
| [Coolify](../../comparisons/preview-environment-platform-comparison.md#coolify) | ✅ | ❌ | ❔ | ✅ | ✅ | ❔ | ❔ | ✅ | ❔ | ❌ |

✅ yes · 🟡 partial · ❌ no · ❔ not documented. Platforms listed are those whose previews include backend services. See the [legend and sources](../../comparisons/preview-environment-platform-comparison.md#at-a-glance).
<!-- END GENERATED: alternatives:heroku -->

Each platform's full details, with quotes and sources, are in the [platform comparison](../preview-environment-platform-comparison.md). To build previews yourself instead, see [open source vs managed](../open-source-vs-managed-preview-environments.md) and the [Kubernetes example](../../examples/kubernetes-namespace-per-pr/).

## Full-stack previews on Northflank

A [Northflank preview blueprint](../../examples/northflank-preview-blueprint/) builds each pull request and creates its services, jobs, a fresh or snapshot-forked database, preview-scoped secrets and URLs. It comments the URL on the PR and deletes everything when the PR closes. It works with GitHub, GitLab, Bitbucket and Azure DevOps, and runs on Northflank's cloud or in your own cloud account.

## When to stay with Heroku

Stay with Heroku Review Apps if your production apps are on Heroku, your repos are on GitHub, and public preview URLs with throwaway add-ons are acceptable.

## FAQ

### What replaces Heroku Review Apps?

Any platform that creates a full app with a database per pull request and deletes it on close. The table above shows which platforms do that, and which also support GitLab or Bitbucket, protect preview URLs, or run in your own cloud account.

### Do Heroku Review Apps work with GitLab?

No. Review Apps work with GitHub. See the [sourced details](../preview-environment-platform-comparison.md#heroku).

### Can I keep using app.json when I move?

Not directly. Most platforms define previews in their own template or blueprint format. The concepts map closely, though: services, add-ons or databases, environment variables, and a post-deploy seed step.

## Further reading

- [Northflank vs Heroku: which platform fits your applications and team?](https://northflank.com/blog/northflank-vs-heroku) (Northflank)
- [Heroku, alternatives, and how to migrate](https://northflank.com/blog/heroku-alternatives-and-how-to-migrate) (Northflank)
- [Top Heroku alternatives](https://northflank.com/blog/top-heroku-alternatives) (Northflank)
