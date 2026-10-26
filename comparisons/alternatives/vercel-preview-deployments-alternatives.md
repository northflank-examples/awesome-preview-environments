# Vercel preview deployments alternatives (2026): full-stack previews with backend services and databases

Vercel's preview deployments are a great fit for frontends: every push to a branch or pull request gets its own URL. Teams usually start looking for alternatives when a preview has to include the **backend**, meaning long-running services, workers, queues and a real database, rather than a frontend and serverless functions.

> Disclosure: this list is maintained by [Northflank](https://northflank.com/product/preview-environments), one of the alternatives below. Every fact links to the vendor's own documentation. See the [methodology](../../methodology.md).

## What Vercel preview deployments do

<!-- BEGIN GENERATED: product-facts:vercel -->
|  | Preview Deployments |
| --- | --- |
| **What a preview includes** | Frontend + serverless functions ([source](https://vercel.com/docs/functions)) |
| **Runs on** | Managed (Vercel cloud) ([source](https://vercel.com/docs/deployments/environments)) |
| **Git providers** | GitHub, GitLab, Bitbucket, Origin, Azure Pipelines; CLI for others ([source](https://vercel.com/docs/git)) |
| **Databases** | Per-preview Neon branch via Marketplace integration ([source](https://vercel.com/marketplace/neon)) |
| **Automatic cleanup** | Retention policy: previews deleted after 180 days (Pro) / 30 days (Hobby) ([source](https://vercel.com/docs/deployment-retention)) |
| **Access control** | Vercel Authentication (all plans); password (Pro add-on); SSO/IPs (Enterprise) ([source](https://vercel.com/docs/deployment-protection)) |
| **Pricing** | Unlimited deployments on all plans; Hobby free, Pro $20/mo ([source](https://vercel.com/pricing)) |

Last verified 2026-10-26.
<!-- END GENERATED: product-facts:vercel -->

## Why teams look for alternatives

- **Previews cover a frontend and serverless functions.** Containers, background workers and long-running services aren't part of a Vercel preview.
- **A per-preview database comes from an integration.** Neon branching through the Vercel Marketplace provides it, rather than the platform itself.
- **Previews aren't deleted when the PR closes.** They're removed by a retention policy instead (30 days on Hobby, 180 on Pro, configurable).
- **Previews run on Vercel's cloud only.** There's no option to run them in your own cloud account.

These limits only matter for some teams. See [when to stay](#when-to-stay-with-vercel).

## Alternatives at a glance

<!-- BEGIN GENERATED: alternatives:vercel -->
| Platform | Backend services | Own database | Start from existing data | Runs in your cloud | Deleted on PR close | Expiry / TTL | URL protection | Label / API / webhook triggers | Teardown hooks | Multi-repo previews |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Vercel** (for reference) | 🟡 | 🟡 | 🟡 | ❌ | ❌ | ✅ | ✅ | ✅ | 🟡 | ❔ |
| [Northflank](../../comparisons/preview-environment-platform-comparison.md#northflank) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Release](../../comparisons/preview-environment-platform-comparison.md#release) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Bunnyshell](../../comparisons/preview-environment-platform-comparison.md#bunnyshell) | ✅ | ✅ | 🟡 | ✅ | ✅ | ❔ | ✅ | ✅ | ✅ | ✅ |
| [Qovery](../../comparisons/preview-environment-platform-comparison.md#qovery) | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❔ |
| [Okteto](../../comparisons/preview-environment-platform-comparison.md#okteto) | ✅ | ✅ | 🟡 | ✅ | 🟡 | ✅ | ✅ | 🟡 | ✅ | ✅ |
| [Heroku](../../comparisons/preview-environment-platform-comparison.md#heroku) | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| [Shipyard](../../comparisons/preview-environment-platform-comparison.md#shipyard) | ✅ | ✅ | ✅ | ❌ | 🟡 | 🟡 | ✅ | ✅ | ❔ | ✅ |
| [Railway](../../comparisons/preview-environment-platform-comparison.md#railway) | ✅ | ✅ | ✅ | ❌ | ✅ | ❔ | ❌ | ✅ | ❔ | 🟡 |
| [Render](../../comparisons/preview-environment-platform-comparison.md#render) | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❔ | ✅ | ❔ | 🟡 |
| [vCluster Platform (Loft)](../../comparisons/preview-environment-platform-comparison.md#vcluster-platform) | ✅ | ❔ | 🟡 | ✅ | 🟡 | ✅ | ✅ | ✅ | 🟡 | ❔ |
| [Coolify](../../comparisons/preview-environment-platform-comparison.md#coolify) | ✅ | ❌ | ❔ | ✅ | ✅ | ❔ | ❔ | ✅ | ❔ | ❌ |

✅ yes · 🟡 partial · ❌ no · ❔ not documented. Platforms listed are those whose previews include backend services. See the [legend and sources](../../comparisons/preview-environment-platform-comparison.md#at-a-glance).
<!-- END GENERATED: alternatives:vercel -->

Each platform's full details, with quotes and sources, are in the [platform comparison](../preview-environment-platform-comparison.md). To build previews yourself instead, see [open source vs managed](../open-source-vs-managed-preview-environments.md) and the [Kubernetes example](../../examples/kubernetes-namespace-per-pr/).

## Full-stack previews on Northflank

A [Northflank preview blueprint](../../examples/northflank-preview-blueprint/) builds each pull request and creates its services, jobs, a fresh or snapshot-forked database, preview-scoped secrets and URLs. It comments the URL on the PR and deletes everything when the PR closes. It works with GitHub, GitLab, Bitbucket and Azure DevOps, and runs on Northflank's cloud or in your own cloud account.

## When to stay with Vercel

Stay with Vercel when your app is a frontend or a Next.js app whose backend already lives elsewhere, and each preview can point at a shared or branched API and database. Many teams keep Vercel for the frontend and use a full-stack platform for backend previews.

## FAQ

### Can Vercel preview deployments include a database?

Yes, through the Neon integration on the Vercel Marketplace, which can create a database branch for each preview deployment. Vercel doesn't provision databases itself. Platforms in the table above with ✅ under *Own database* create one per preview natively.

### Are Vercel preview deployments deleted when a PR is merged?

Not on merge or close. Vercel deletes preview deployments according to its retention policy (30 days on Hobby, 180 days on Pro by default). See the [sourced details](../preview-environment-platform-comparison.md#vercel).

### What is the best Vercel alternative for full-stack preview environments?

Look for ✅ under *Backend services*, *Own database* and *Deleted on PR close* in the table above. If previews must run in your own cloud account, add *Runs in your cloud*. Northflank (this list's maintainer), Qovery and Release cover all of these.

## Further reading

- [Northflank vs Vercel: which platform should you choose?](https://northflank.com/blog/northflank-vs-vercel) (Northflank)
- [Can you use Vercel for backend? What works and when to use something else](https://northflank.com/blog/vercel-backend-limitations) (Northflank)
- [BYOC alternatives to Vercel](https://northflank.com/blog/best-byoc-alternatives-to-vercel) (Northflank)
