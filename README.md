# Awesome Preview Environments: Tools, Platforms, Examples & Best Practices (2026)

A curated list of preview environment platforms, open-source tools, tutorials and best practices for creating **ephemeral environments for pull requests and feature branches**. It covers full-stack and frontend platforms, Kubernetes and GitOps approaches, database branching, GitHub Actions and GitLab CI, security, cost, and previews for AI coding agents.

- **[At a glance](#at-a-glance):** 19 platforms checked against 10 capabilities: backend services, a database per preview, starting from existing data, running in your own cloud, automatic cleanup, URL protection, API and webhook triggers, teardown hooks, and multi-repo previews.
- **[Platform comparison](comparisons/preview-environment-platform-comparison.md):** 31 platforms and tools compared on what a preview includes, where it runs, Git providers, databases, cleanup, access control and pricing. Every value links to a verbatim quote from the vendor's docs.
- **[Guides](#guides):** GitHub Actions, GitLab CI, Kubernetes, databases, security, cost, and AI agents.
- **[Examples](#examples):** full-stack previews with a Northflank preview blueprint, plus do-it-yourself setups: a Kubernetes namespace per PR, Argo CD ApplicationSets, GitLab review apps, and a Neon database branch per PR.

<!-- BEGIN GENERATED: last-updated -->
**Last verified:** 2026-10-26. 31 platforms and tools and 8 database tools, generated from [`data/platforms.json`](data/platforms.json) and [`data/databases.json`](data/databases.json). Every fact links to the vendor's own documentation; anything a vendor doesn't document is marked *not published*, never guessed.
<!-- END GENERATED: last-updated -->

> **Disclosure:** this list is maintained by [Northflank](https://northflank.com), which offers preview environments. Contributions from all vendors and community members are welcome, and every listing follows the same published [inclusion criteria and methodology](methodology.md). Corrections with an official source are always accepted, see [CONTRIBUTING](CONTRIBUTING.md).

## Contents

- [What are preview environments?](#what-are-preview-environments)
- [Preview environment platforms](#preview-environment-platforms)
  - [At a glance](#at-a-glance)
- [Open-source tools](#open-source-tools)
- [CI/CD-native features](#cicd-native-features)
- [Database branching and seeding](#database-branching-and-seeding)
- [Preview environments by use case](#preview-environments-by-use-case)
- [Architecture patterns](#architecture-patterns)
- [Examples](#examples)
- [Guides](#guides)
- [Best practices](#best-practices)
- [Learning resources](#learning-resources)
- [FAQ](#faq)
- [Related lists](#related-lists)

## What are preview environments?

A **preview environment** is a temporary, isolated deployment of an application, created to test and review changes before they're merged into a shared branch. Preview environments are usually created automatically for each pull request. They give developers, testers, designers and product owners a unique URL where they can inspect the change, and they're destroyed when the pull request is merged or closed.

Vendors use different names for them, including deploy previews, preview deployments, review apps, PR environments, ephemeral environments and sandboxes.

| Environment | Primary purpose | Typical lifecycle |
| --- | --- | --- |
| Preview | Review and test one proposed change | Per pull request or branch; deleted on merge or close |
| Staging | Validate the integrated release before production | Long-lived, shared |
| Development | Write and debug code | Persistent or temporary, per developer |
| Ephemeral | Any short-lived environment (previews are the most common kind) | Created and destroyed on demand |

More in [preview environments vs staging](comparisons/preview-environments-vs-staging.md).

## Preview environment platforms

### At a glance

<!-- BEGIN GENERATED: capabilities -->
| Platform | Backend services | Own database | Start from existing data | Runs in your cloud | Deleted on PR close | Expiry / TTL | URL protection | Label / API / webhook triggers | Teardown hooks | Multi-repo previews |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Northflank](comparisons/preview-environment-platform-comparison.md#northflank) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Release](comparisons/preview-environment-platform-comparison.md#release) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Bunnyshell](comparisons/preview-environment-platform-comparison.md#bunnyshell) | ✅ | ✅ | 🟡 | ✅ | ✅ | ❔ | ✅ | ✅ | ✅ | ✅ |
| [Qovery](comparisons/preview-environment-platform-comparison.md#qovery) | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❔ |
| [Okteto](comparisons/preview-environment-platform-comparison.md#okteto) | ✅ | ✅ | 🟡 | ✅ | 🟡 | ✅ | ✅ | 🟡 | ✅ | ✅ |
| [Signadot](comparisons/preview-environment-platform-comparison.md#signadot) | 🟡 | ✅ | 🟡 | ✅ | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Heroku](comparisons/preview-environment-platform-comparison.md#heroku) | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| [Shipyard](comparisons/preview-environment-platform-comparison.md#shipyard) | ✅ | ✅ | ✅ | ❌ | 🟡 | 🟡 | ✅ | ✅ | ❔ | ✅ |
| [Netlify](comparisons/preview-environment-platform-comparison.md#netlify) | 🟡 | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | 🟡 | ❔ |
| [Railway](comparisons/preview-environment-platform-comparison.md#railway) | ✅ | ✅ | ✅ | ❌ | ✅ | ❔ | ❌ | ✅ | ❔ | 🟡 |
| [Render](comparisons/preview-environment-platform-comparison.md#render) | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❔ | ✅ | ❔ | 🟡 |
| [vCluster Platform (Loft)](comparisons/preview-environment-platform-comparison.md#vcluster-platform) | ✅ | ❔ | 🟡 | ✅ | 🟡 | ✅ | ✅ | ✅ | 🟡 | ❔ |
| [Coolify](comparisons/preview-environment-platform-comparison.md#coolify) | ✅ | ❌ | ❔ | ✅ | ✅ | ❔ | ❔ | ✅ | ❔ | ❌ |
| [Vercel](comparisons/preview-environment-platform-comparison.md#vercel) | 🟡 | 🟡 | 🟡 | ❌ | ❌ | ✅ | ✅ | ✅ | 🟡 | ❔ |
| [AWS Amplify Hosting](comparisons/preview-environment-platform-comparison.md#aws-amplify-hosting) | 🟡 | 🟡 | ❌ | ❌ | ✅ | ❔ | ✅ | 🟡 | ❔ | 🟡 |
| [Azure Static Web Apps](comparisons/preview-environment-platform-comparison.md#azure-static-web-apps) | 🟡 | ❌ | ❔ | ❌ | ✅ | ❔ | ✅ | 🟡 | 🟡 | ❌ |
| [Cloudflare (Pages + Workers Previews)](comparisons/preview-environment-platform-comparison.md#cloudflare) | 🟡 | ❌ | ❌ | ❌ | ❌ | 🟡 | ✅ | ✅ | 🟡 | ❌ |
| [Dokploy](comparisons/preview-environment-platform-comparison.md#dokploy) | 🟡 | ❌ | ❔ | ✅ | ✅ | ❔ | ❔ | 🟡 | ❔ | ❌ |
| [Firebase Hosting](comparisons/preview-environment-platform-comparison.md#firebase-hosting) | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❔ | ❔ |

✅ yes · 🟡 partial, limited, or only with extra setup · ❌ no · ❔ not documented. *Backend services*: containers or services beyond a frontend and functions. *Own database*: each preview can get its own database. *Start from existing data*: a preview database can be forked, cloned or branched from existing data. *Runs in your cloud*: BYOC, your cluster, or self-hosted. *Deleted on PR close* and *Expiry / TTL*: built in, not scripted in your CI. *URL protection*: built-in access control for preview URLs. *Label / API / webhook triggers*: previews can be created by more than PR events (two or more of label, API, CLI, webhook, schedule, manual). *Teardown hooks*: custom cleanup steps run when a preview is deleted. *Multi-repo previews*: one preview can include services built from several repositories. Every mark summarises a sourced fact in the [details](comparisons/preview-environment-platform-comparison.md#details).
<!-- END GENERATED: capabilities -->

Below, the same platforms grouped by what they deploy. Within each group, entries are alphabetical, with the maintainer listed first in its own group. Click a platform for its sourced details, or see the [full comparison](comparisons/preview-environment-platform-comparison.md), which also covers Git providers, triggers, access control and pricing.

<!-- BEGIN GENERATED: platforms-overview -->
### Full-stack platforms

Managed platforms that deploy backend services, workers and databases per preview.

| Platform | Previews include | Runs on | Databases | Automatic cleanup |
| --- | --- | --- | --- | --- |
| [Northflank](comparisons/preview-environment-platform-comparison.md#northflank) | Visual blueprint per PR: services, jobs, fresh or forked databases, scoped secrets and URLs; managed or BYOC | Managed, BYOC in your cloud account, or your own cluster (BYOK) | Fresh database per preview, forked from a snapshot, seeded by a job, or shared | On PR close or branch delete, plus optional expiry (resets on update) and teardown steps |
| [Heroku](comparisons/preview-environment-platform-comparison.md#heroku) | Disposable app per GitHub PR from app.json, including add-ons | Managed (Heroku cloud, incl. Private Spaces) | Yes, add-ons (e.g. Heroku Postgres) provisioned per app; seed via postdeploy | Yes, on PR close; optional 1-30 day inactivity |
| [Railway](comparisons/preview-environment-platform-comparison.md#railway) | Temporary copy of a project environment per GitHub PR | Managed (Railway-operated hardware) | Yes, own DB services; optional volume data copy (beta) | Yes, on PR merge/close |
| [Release](comparisons/preview-environment-platform-comparison.md#release) | Ephemeral environment per PR on Kubernetes, with datasets from production snapshots | Managed (Release cloud) or BYOC (AWS, GCP) | Instant Datasets: pooled DBs from production snapshots | Yes, on PR close/merge; default 3-day expiry |
| [Render](comparisons/preview-environment-platform-comparison.md#render) | Copy of a Blueprint environment per PR, with new Postgres/Key Value instances | Managed (Render cloud) | Yes, new empty Postgres/Key Value per preview; seedable | Yes, on PR merge/close; optional inactivity expiry |
| [Shipyard](comparisons/preview-environment-platform-comparison.md#shipyard) | Full-stack environment per PR from your Docker Compose file | Managed (Shipyard Cloud) | Per-env containers; volume snapshots via CLI | Spun down on merge; idle sleep via Since Last Visit |

### Kubernetes and environment-as-a-service

Platforms that create preview environments on Kubernetes, usually in your own cluster or cloud account.

| Platform | Previews include | Runs on | Databases | Automatic cleanup |
| --- | --- | --- | --- | --- |
| [Bunnyshell](comparisons/preview-environment-platform-comparison.md#bunnyshell) | Ephemeral copies of a primary environment per PR on your Kubernetes clusters | Your Kubernetes cluster (AWS, Azure, GCP, DO, private); trial cluster | Container DB per env; seeding guides; Neon branching connector | Yes, on PR close/merge (configurable) |
| [Okteto](comparisons/preview-environment-platform-comparison.md#okteto) | Preview namespace per PR from an Okteto manifest, run from CI | Self-hosted (Helm) or BYOC (AWS, GCP) | Deployed per preview; volume snapshots to clone data | CI destroys on PR close; GC sleeps 1h, deletes after 7 days |
| [Qovery](comparisons/preview-environment-platform-comparison.md#qovery) | Clones a blueprint environment per PR on Kubernetes in your cloud account | BYOC (your AWS/GCP/Azure/Scaleway account); BYOK | Cloned or shared per preview; seeding via Lifecycle Jobs | Yes, on PR merge/close; optional inactivity expiry |
| [Signadot](comparisons/preview-environment-platform-comparison.md#signadot) | Deploys only changed services and routes requests on a shared baseline cluster | Your Kubernetes cluster + managed control plane | Temporary schemas/DBs via resource plugins | CLI teardown on PR close, TTL, or GitHub App label |
| [vCluster Platform (Loft)](comparisons/preview-environment-platform-comparison.md#vcluster-platform) | Virtual Kubernetes cluster per PR, with sleep mode for idle previews | Your clusters; platform self-hosted or vCluster Cloud | not published | CI deletes on PR close/merge; auto-sleep and auto-delete |

### Frontend platforms

Hosts whose previews cover static sites, frontend frameworks and serverless functions.

| Platform | Previews include | Runs on | Databases | Automatic cleanup |
| --- | --- | --- | --- | --- |
| [AWS Amplify Hosting](comparisons/preview-environment-platform-comparison.md#aws-amplify-hosting) | PR previews for frontends/SSR, optionally with a temporary backend per PR | Managed (AWS) | Optional temporary backend env per PR (private repos only), or shared | Yes, preview and backend deleted on PR close |
| [Azure Static Web Apps](comparisons/preview-environment-platform-comparison.md#azure-static-web-apps) | Staging environment per PR for static sites and managed Functions APIs | Managed (Azure) | not published | Yes, deleted when PR closes |
| [Cloudflare (Pages + Workers Previews)](comparisons/preview-environment-platform-comparison.md#cloudflare) | Pages preview deployments and Worker Previews per branch/PR | Managed (Cloudflare network) | No auto-provisioned DB; bind D1/KV/R2 per preview manually | Workers: oldest Preview deleted at limit; manual/CI delete. Pages: manual |
| [Firebase Hosting](comparisons/preview-environment-platform-comparison.md#firebase-hosting) | Temporary preview channels for static sites, using the live backend | Managed (Google/Firebase) | Shared only (real project backend) | Yes, TTL: expires after 7 days by default (max 30) |
| [Netlify](comparisons/preview-environment-platform-comparison.md#netlify) | Deploy Preview per PR for frontends and functions, with a per-preview database branch | Managed (Netlify cloud) | Yes: Netlify Database branch per preview, copied from production | Deploys auto-deleted after 30 days (90 on paid); not on PR close |
| [Vercel](comparisons/preview-environment-platform-comparison.md#vercel) | Preview deployment per push/PR for frontends and serverless functions | Managed (Vercel cloud) | Per-preview Neon branch via Marketplace integration | Retention policy: previews deleted after 180 days (Pro) / 30 days (Hobby) |

### Self-hosted PaaS

Open-source platforms you run on your own servers, with preview deployments built in.

| Platform | Previews include | Runs on | Databases | Automatic cleanup |
| --- | --- | --- | --- | --- |
| [Coolify](comparisons/preview-environment-platform-comparison.md#coolify) | Self-hosted PaaS with per-PR preview deployments of apps and Compose stacks | Self-hosted (free) or Coolify Cloud control plane on your servers | None built in; use non-prod external DBs | Yes, on PR/MR close or merge |
| [Dokploy](comparisons/preview-environment-platform-comparison.md#dokploy) | Self-hosted PaaS with per-PR preview deployments for GitHub apps | Self-hosted, or Dokploy Cloud managing your servers | not published | Yes, on PR close/merge |
<!-- END GENERATED: platforms-overview -->

## Open-source tools

Building blocks you combine with your own CI and infrastructure. Self-hosted platforms with preview deployments (Coolify, Dokploy) are listed [above](#self-hosted-paas).

<!-- BEGIN GENERATED: tools:open-source-tool -->
- [Argo CD ApplicationSet Pull Request generator](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/): Argo CD generator that creates one Application per open PR ([Source](https://github.com/argoproj/argo-cd) · Open source, Apache-2.0)
- [DigitalOcean App Platform PR previews (app_action)](https://github.com/digitalocean/app_action#launch-a-preview-app-per-pull-request): Official GitHub Action that deploys an App Platform app per PR ([Source](https://github.com/digitalocean/app_action) · Open source, MIT (the Action))
- [Flux Operator ResourceSets](https://fluxoperator.dev/docs/resourcesets/github-pull-requests/): Flux Operator ResourceSets that template Flux resources per open PR ([Source](https://github.com/controlplaneio-fluxcd/flux-operator) · Open source, AGPL-3.0)
- [Fly.io PR Review Apps (superfly/fly-pr-review-apps)](https://fly.io/docs/blueprints/review-apps-guide/): Official GitHub Action that creates and destroys a Fly.io app per PR ([Source](https://github.com/superfly/fly-pr-review-apps) · Open source, Apache-2.0)
- [Garden](https://docs.garden.io/overview/use-cases/on-demand-preview-envs): CLI that deploys an isolated namespace per PR from your existing Dockerfiles and manifests ([Source](https://github.com/garden-io/garden) · Open source, MPL-2.0)
- [Laravel Harbor](https://laravel-harbor.com/docs/introduction/): Per-PR Laravel site and database on a Laravel Forge server ([Source](https://github.com/mehrancodes/laravel-harbor) · Open source, MIT)
- [pr-preview-action](https://github.com/rossjrw/pr-preview-action): GitHub Action that deploys static-site previews per PR to GitHub Pages (Open source, MIT)
- [PullPreview](https://github.com/pullpreview/action): GitHub Action that runs a labelled PR on a VM in your AWS Lightsail or Hetzner account ([Source](https://github.com/pullpreview/action) · Source-available (Prosperity Public License 3.0.0))
- [vCluster](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments): Open-source virtual Kubernetes clusters, usable as one cluster per PR ([Source](https://github.com/loft-sh/vcluster) · Open source, Apache-2.0 (Platform is commercial))
<!-- END GENERATED: tools:open-source-tool -->

## CI/CD-native features

Preview features built into Git hosting and CI systems. They track environments and run teardown jobs, but they don't provision infrastructure for you.

<!-- BEGIN GENERATED: tools:ci-native -->
- [Azure Pipelines Review App (Kubernetes environments)](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/environments-kubernetes): Deploys each PR to a dynamically created Kubernetes namespace (Proprietary)
- [GitHub Actions deployment environments](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments): Deployment tracking, protection rules and scoped secrets; you provision the preview (Proprietary)
- [GitLab Review Apps](https://docs.gitlab.com/ci/review_apps/): Dynamic environment per MR, with stop jobs and auto-stop (Open core (MIT core, proprietary ee/))
<!-- END GENERATED: tools:ci-native -->

## Database branching and seeding

Tools that give each preview its own database, by copy-on-write branching, thin cloning or seeding, or that prepare safe data for previews. See [database preview environments](guides/database-preview-environments.md) for strategies and the sourced details.

<!-- BEGIN GENERATED: database-overview -->
| Tool | Engine | How a preview DB is made | Per-PR automation | Runs on |
| --- | --- | --- | --- | --- |
| [DBLab Engine (Postgres.ai)](guides/database-preview-environments.md#dblab-engine) | Postgres | Thin clone (copy-on-write via ZFS/LVM2) | CI via DB Migration Checker GitHub Action (push-triggered) | Self-hosted (on-prem or cloud) |
| [Neon](guides/database-preview-environments.md#neon) | Postgres | Copy-on-write branch (full data or schema-only) | GitHub Actions (create/delete/schema-diff); Vercel integrations | Managed (AWS regions) |
| [PlanetScale](guides/database-preview-environments.md#planetscale) | MySQL (Vitess) and Postgres | Schema-only branch; data branch restored from backup | DIY: pscale CLI in GitHub Actions (setup-pscale-action) | Managed; PlanetScale Managed in your AWS/GCP/Azure |
| [Prisma Postgres](guides/database-preview-environments.md#prisma-postgres) | Postgres 17 | New empty database per PR, migrated and seeded | GitHub Actions guide; Prisma Compute branch previews | Managed |
| [Supabase Branching](guides/database-preview-environments.md#supabase-branching) | Postgres (full Supabase stack: auth, storage, APIs) | New instance; migrations + seed.sql applied | Yes, Supabase GitHub integration | Managed (Supabase Cloud, Pro plan and up) |
| [Tonic Structural](guides/database-preview-environments.md#tonic-structural) | Postgres, MySQL, SQL Server, Oracle, MongoDB, more | De-identified / subsetted copy of production | not published | Tonic Cloud or self-hosted |
| [Turso](guides/database-preview-environments.md#turso) | SQLite-compatible (Turso / libSQL) | Full copy as separate database; point-in-time option | DIY GitHub Actions example via Platform API | Managed (Turso Cloud) |
| [Xata](guides/database-preview-environments.md#xata) | Postgres (vanilla) | Copy-on-write branch | Yes, Xata GitHub App or GitHub Action | Managed cloud, BYOC, or self-hosted OSS |
<!-- END GENERATED: database-overview -->

## Preview environments by use case

| Use case | Where to start |
| --- | --- |
| **Frontend previews** (SPA, static site, Next.js and others) | [Frontend platforms](comparisons/preview-environment-platform-comparison.md#frontend), [pr-preview-action](https://github.com/rossjrw/pr-preview-action) for GitHub Pages |
| **Full-stack previews** (backend services, workers, databases) | [Full-stack platforms](comparisons/preview-environment-platform-comparison.md#full-stack), e.g. a [Northflank preview blueprint](examples/northflank-preview-blueprint/); DIY: [Kubernetes example](examples/kubernetes-namespace-per-pr/) |
| **Kubernetes previews** | [Kubernetes guide](guides/kubernetes-preview-environments.md), [Kubernetes platforms](comparisons/preview-environment-platform-comparison.md#kubernetes), [Argo CD example](examples/argocd-applicationset/) |
| **Database previews** | [Database guide](guides/database-preview-environments.md), platforms with a database per preview (*Own database* [above](#at-a-glance)), [Neon branch-per-PR example](examples/neon-branch-per-pr/) |
| **Microservices** (copying everything is too slow or expensive) | [Shared baseline + request routing](guides/kubernetes-preview-environments.md#3-shared-baseline--request-routing), [microservices architecture and pitfalls](https://northflank.com/blog/preview-environments-microservices) |
| **Monorepos** | Build and deploy only changed services: path filters on triggers, or affected-service detection (Nx, Turborepo, Bazel) in CI. See [efficient monorepo preview environments](https://northflank.com/blog/how-to-build-efficient-monorepo-preview-environments) |
| **Previews in your own cloud account** (data residency, VPC-only dependencies, cloud credits) | *Runs in your cloud* [above](#at-a-glance): BYOC platforms such as Northflank, Qovery and Release, or self-hosted options; see [open source vs managed](comparisons/open-source-vs-managed-preview-environments.md) |
| **AI coding agents** | [Preview environments for AI coding agents](guides/preview-environments-for-ai-coding-agents.md) |
| **Alternatives to Vercel, Netlify, Heroku, Render or Railway previews** | [Vercel](comparisons/alternatives/vercel-preview-deployments-alternatives.md) · [Netlify](comparisons/alternatives/netlify-deploy-previews-alternatives.md) · [Heroku Review Apps](comparisons/alternatives/heroku-review-apps-alternatives.md) · [Render](comparisons/alternatives/render-preview-environments-alternatives.md) · [Railway](comparisons/alternatives/railway-pr-environments-alternatives.md) |

## Architecture patterns

How much of the system each preview gets its own copy of. These approaches overlap rather than exclude each other: a full-stack copy usually runs inside a namespace, for example.

| Pattern | Each preview gets | Trade-off |
| --- | --- | --- |
| **Full stack per PR** | Every service and database | Strongest isolation and fidelity, but the highest cost and slowest startup |
| **Shared infrastructure, isolated services** | Changed services; shared databases and stable services | Cheaper and faster, but shared state can leak between previews |
| **Namespace per PR** (Kubernetes) | A namespace in a shared cluster | The simplest Kubernetes option. Isolation depends on RBAC, NetworkPolicy and quotas |
| **Shared baseline + request routing** | Only changed services; requests routed by header | Scales to hundreds of services, but needs context propagation through every service |
| **Virtual cluster per PR** | Its own Kubernetes API server | Supports CRDs and operators per PR, but costs more than a namespace |

The details and trade-offs are in the [Kubernetes guide](guides/kubernetes-preview-environments.md).

## Examples

Working starting points in this repository. Each one has a README covering setup, design choices and what it leaves out.

| Example | What it shows |
| --- | --- |
| [Northflank preview blueprint](examples/northflank-preview-blueprint/) | Managed full-stack previews with no pipeline to maintain: build, a fresh or forked database, seed job, scoped secrets, URL comment on the PR, expiry, and BYOC |
| [Kubernetes namespace per PR](examples/kubernetes-namespace-per-pr/) | GitHub Actions + Helm: build, deploy app + Postgres to `pr-<n>`, comment the URL, delete on close; quotas and NetworkPolicy included |
| [Argo CD ApplicationSet](examples/argocd-applicationset/) | GitOps previews with the Pull Request generator |
| [GitLab review apps](examples/gitlab-review-apps/) | `environment`, `on_stop` and `auto_stop_in` with a namespace per MR |
| [Neon branch per PR](examples/neon-branch-per-pr/) | A copy-on-write Postgres branch per PR, with migrations, an expiry safety net and deletion on close |

## Guides

- [Getting started](guides/set-up-preview-environments-for-pull-requests.md): five decisions from no previews to a preview per PR.
- [GitHub Actions](guides/github-actions-preview-environments.md): lifecycle events, concurrency, fork PRs and `pull_request_target`, cleanup sweeps.
- [GitLab CI](guides/gitlab-review-apps.md): review apps, dynamic environments, `on_stop` and `auto_stop_in`.
- [Kubernetes](guides/kubernetes-preview-environments.md): namespaces, request routing, virtual clusters, wildcard DNS and TLS, push vs GitOps.
- [Database preview environments](guides/database-preview-environments.md): shared, seeded, snapshot and branch strategies; migrations; sensitive data.
- [Security and secrets](guides/preview-environment-security.md): threat model, scoped credentials, protecting preview URLs.
- [Cost optimization](guides/reduce-preview-environment-costs.md): fewer, smaller and shorter-lived previews; a quick cost formula.
- [AI coding agents](guides/preview-environments-for-ai-coding-agents.md): using previews to verify agent-written pull requests.
- [Preview environments vs staging](comparisons/preview-environments-vs-staging.md) and [open source vs managed](comparisons/open-source-vs-managed-preview-environments.md).
- Alternatives: [Vercel preview deployments](comparisons/alternatives/vercel-preview-deployments-alternatives.md), [Netlify Deploy Previews](comparisons/alternatives/netlify-deploy-previews-alternatives.md), [Heroku Review Apps](comparisons/alternatives/heroku-review-apps-alternatives.md), [Render Preview Environments](comparisons/alternatives/render-preview-environments-alternatives.md), [Railway PR Environments](comparisons/alternatives/railway-pr-environments-alternatives.md).

## Best practices

- **Automate the whole lifecycle.** Create on PR open, update on push, and delete on merge or close. Add a TTL and a scheduled sweep, because teardown events do get missed. ([GitHub Actions](guides/github-actions-preview-environments.md#cleaning-up-what-the-closed-event-missed))
- **Keep previews production-like where it matters.** Use the same container images, configuration shape and dependency versions. Scale them down, but keep the topology the same.
- **Make data safe and realistic.** Branch or fork from a sanitised parent, seed deterministically, and never copy raw production personal data into previews. ([Databases](guides/database-preview-environments.md))
- **Use separate, scoped credentials.** Previews run unreviewed code, so give them test API keys and sandbox accounts, never production secrets. ([Security](guides/preview-environment-security.md))
- **Isolate previews from each other.** Separate namespaces or networks, per-preview database credentials, and no shared mutable state you didn't intend.
- **Protect preview URLs.** Use SSO, a password or an IP allowlist, and at minimum keep them out of search engines.
- **Be careful with fork PRs.** Never build untrusted code with secrets (avoid `pull_request_target` + checkout). Require a maintainer's approval instead.
- **Set resource limits and cost controls.** Small instance sizes, quotas, scale-to-zero when idle, and a cap on concurrent previews. ([Cost](guides/reduce-preview-environment-costs.md))
- **Post the URL where reviewers already are.** Put it on the PR, as a deployment status or a single sticky comment.
- **Run tests against the preview.** Run end-to-end, visual and accessibility checks against the preview URL as required status checks.

## Learning resources

### From the maintainer (Northflank)

- [How to auto-create preview environments on every PR](https://northflank.com/blog/how-to-auto-create-preview-environments-on-every-pr): step-by-step preview blueprints, from Git trigger to teardown.
- [What are ephemeral environments? How they work and when to use them](https://northflank.com/blog/what-are-ephemeral-environments)
- [Which database strategy should you use for preview environments?](https://northflank.com/blog/which-database-strategy-should-you-use-for-preview-environments)
- [Preview environments for microservices: Architecture and common pitfalls](https://northflank.com/blog/preview-environments-microservices)
- [How to build efficient monorepo preview environments](https://northflank.com/blog/how-to-build-efficient-monorepo-preview-environments)
- [How to control access to preview environments across enterprise teams](https://northflank.com/blog/control-access-preview-environments-enterprise-teams)
- [How do ephemeral environments reduce infrastructure costs?](https://northflank.com/blog/how-do-ephemeral-environments-reduce-infrastructure-costs)
- [Preview environment troubleshooting: Common failures and how to fix them](https://northflank.com/blog/preview-environment-troubleshooting)
- [How do preview environments scale for AI-generated code?](https://northflank.com/blog/scale-preview-environments-ai-generated-code)
- [Top 5 Kubernetes preview environments comparison for 2026](https://northflank.com/blog/kubernetes-preview-environments-comparison)
- [Best platforms for on-demand preview environments in 2026](https://northflank.com/blog/best-platforms-for-on-demand-preview-environments)

### Concepts and case studies

- [Ephemeral Environments](https://ephemeralenvironments.io/): Community guide defining ephemeral environments and their benefits for testing, collaboration, security and cost. *Shipyard, EphemeralEnvironments.io*
- [Ephemeral testing environments: Sometimes, you just need to kill your darlings](https://www.thoughtworks.com/en-us/insights/blog/testing/ephemeral-testing-environments-kill-darlings): When short-lived isolated test environments beat shared staging, what automation they need, and when they don't fit. *Richard Gall, with Effy Elden, Thoughtworks, 2025*
- [Enterprise-wide integration test environments](https://www.thoughtworks.com/en-us/radar/techniques/enterprise-wide-integration-test-environments): Radar 'Hold' entry recommending ephemeral, team-owned environments over shared enterprise-wide integration environments. *Thoughtworks Technology Radar, 2024*
- [Simplifying Developer Testing Through SLATE](https://www.uber.com/blog/simplifying-developer-testing-through-slate/): How Uber built on-demand, short-lived test environments using request tenancy alongside production dependencies. *Uber Engineering, 2022*
- [Scaling and Automating Microservice Testing at Lyft](https://www.infoq.com/news/2022/03/scaling-testing-acceptance-lyft/): Summary of Lyft's move from per-developer Onebox VMs to request isolation (staging overrides) in shared staging. *Vasco Veloso, InfoQ, 2022*
- [10 best preview environment platforms in 2026 (frontend, backend & GitOps)](https://northflank.com/blog/preview-environment-platforms): Vendor-written comparison of ten preview environment platforms and the capabilities to evaluate when choosing one. *Deborah Emeni, Northflank, 2025*

### GitHub Actions

- [Managing environments for deployment](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments): Configure GitHub deployment environments, protection rules, environment secrets and deployment branch policies. *GitHub Docs*
- [Events that trigger workflows](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows): Reference for pull_request activity types, including 'closed' for tearing previews down on merge or close. *GitHub Docs*
- [Control the concurrency of workflows and jobs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency): Use concurrency groups and cancel-in-progress so only the latest commit deploys to a PR's preview. *GitHub Docs*
- [rossjrw/pr-preview-action](https://github.com/rossjrw/pr-preview-action): Open-source action that deploys per-PR static previews to GitHub Pages and cleans up when PRs close. *GitHub, rossjrw*
- [How to Set Up Preview Environments for Pull Requests](https://developer-friendly.blog/blog/2024/06/24/how-to-set-up-preview-environments-for-pull-requests/): Label-triggered GitHub Actions previews using FluxCD, Kustomize overlays, Gateway API and wildcard TLS. *Meysam Azad, Developer Friendly Blog, 2024*

### GitLab

- [Review apps](https://docs.gitlab.com/ci/review_apps/): Per-merge-request preview environments built on dynamic environments, with on_stop and auto_stop_in cleanup. *GitLab Docs*
- [Environments](https://docs.gitlab.com/ci/environments/): Static versus dynamic environments, stopping environments, and environment lifecycle in GitLab CI/CD. *GitLab Docs*

### Kubernetes and GitOps

- [Pull Request Generator](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/): Generate one Argo CD Application per open pull request, removed automatically when the PR closes. *Argo CD Docs*
- [GitHub PRs Integration](https://fluxoperator.dev/docs/resourcesets/github-pull-requests/): Use Flux Operator ResourceSets to deploy labeled PRs into ephemeral environments and report status back. *Flux Operator Docs*
- [Ephemeral PR environment using vCluster](https://www.vcluster.com/blog/ephemeral-pr-environment-using-vcluster): Create a virtual Kubernetes cluster per labeled PR with GitHub Actions, deleting it after merge. *Saiyam Pathak, vCluster, 2025*
- [Preview Environments on Kubernetes with ArgoCD](https://piotrminkowski.com/2023/06/19/preview-environments-on-kubernetes-with-argocd/): ApplicationSets, Helm and Tekton combined to create and remove a namespace per GitHub pull request. *Piotr Minkowski, 2023*
- [Create temporary Argo CD preview environments based on pull requests](https://octopus.com/blog/creating-temporary-preview-environments-based-pull-requests-argo-cd): Step-by-step Argo CD Pull Request Generator setup for isolated, auto-removed per-PR namespaces. *Kostis Kapelonis, Octopus Deploy, 2024*
- [How to Build Ephemeral PR Preview Environments on GKE with GitHub Actions, Ingress, and Automatic TLS](https://www.freecodecamp.org/news/build-ephemeral-pr-preview-environments-on-gke-with-github-actions-ingress-automatic-tls/): End-to-end namespace-per-PR build: shared ingress, cert-manager TLS, teardown on close, and a scheduled reaper. *Amina Lawal, freeCodeCamp, 2026*
- [How we replaced shared staging with ephemeral deployment preview](https://plane.so/blog/how-we-replaced-shared-staging-with-ephemeral-deployment-preview): A real team's per-PR namespace, Postgres, DNS and TLS provisioning triggered by a PR comment. *Plane Engineering, 2026*
- [DNS01](https://cert-manager.io/docs/configuration/acme/dns01/): Configure ACME DNS-01 challenges, required for wildcard certificates covering *.preview hostnames. *cert-manager Docs*

### Databases

- [A database for every preview environment using Neon, GitHub Actions, and Vercel](https://neon.com/blog/branching-with-preview-environments): Create a database branch per PR, run migrations against it, and delete it when the PR closes. *Mahmoud Abdelwahab, Neon, 2023*
- [Create Environments with Masked Production Data Using Neon Branches](https://neon.com/blog/environments-masked-production-data): Mask PII once with PostgreSQL Anonymizer, then branch realistic non-production databases from that template. *Carlota Soto, Neon, 2025*
- [Branching](https://planetscale.com/docs/vitess/schema-changes/branching): Schema-only development branches, data branching options, and deploy requests for reviewable schema changes. *PlanetScale Docs*
- [Branching](https://supabase.com/docs/guides/deployment/branching): Per-PR preview branches built from repository migrations, optionally seeded, deleted on merge or close. *Supabase Docs*
- [PostgreSQL Anonymizer](https://postgresql-anonymizer.readthedocs.io/en/stable/): Postgres extension for declaring masking rules and producing anonymized dumps for non-production use. *PostgreSQL Anonymizer project*

### Security

- [Keeping your GitHub Actions and workflows secure Part 1: Preventing pwn requests](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/): Why pull_request_target plus checkout of untrusted PR code leaks secrets, and safer workflow patterns. *Jaroslav Lobačevski, GitHub Security Lab, 2021*
- [Keeping your GitHub Actions and workflows secure Part 2: Untrusted input](https://securitylab.github.com/resources/github-actions-untrusted-input/): How PR titles, branch names and bodies enable script injection in workflows, and how to avoid it. *Jaroslav Lobačevski, GitHub Security Lab, 2021*
- [Approving workflow runs from forks](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/approve-runs-from-forks): Require maintainer approval before workflows run on fork pull requests from outside contributors. *GitHub Docs*
- [Using secrets in GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets): Scope secrets to environments and understand why secrets are withheld from fork pull request workflows. *GitHub Docs*
- [Deployment Protection on Vercel](https://vercel.com/docs/deployment-protection): Patterns for gating preview URLs behind SSO, passwords or IP allowlists, with bypass tokens for automation. *Vercel Docs*

### Cost control

- [Cleanup policies and TTL labels](https://kyverno.io/docs/policy-types/cleanup-policy/): Delete preview namespaces and resources automatically after a TTL label expires, with Kyverno. *Kyverno Docs*
- [kedacore/http-add-on](https://github.com/kedacore/http-add-on): Scale HTTP workloads to and from zero based on traffic, useful for idle preview environments. *GitHub, KEDA project*
- [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/): Cap CPU, memory and object counts per namespace to bound the cost of each preview. *Kubernetes Docs*
- [NodePools](https://karpenter.sh/docs/concepts/nodepools/): Constrain node capacity types to spot and configure consolidation to cut idle preview cluster capacity. *Karpenter Docs*

### AI coding agents

- [Better Agentic Review with Ephemeral Deploys](https://miren.dev/blog/agentic-pr-eph): A GitHub Actions workflow where an AI agent tests a per-PR deploy and posts a merge verdict. *Evan Phoenix, Miren, 2026*
- [Agentic Workflows with Ephemeral Environments](https://ephemeralenvironments.io/impact/agentic-workflows): Why agents need isolated environments to deploy, read logs and iterate safely before human review. *Shipyard, EphemeralEnvironments.io*
- [How to set up preview environments for apps built with Claude Code](https://northflank.com/blog/how-to-set-up-preview-environments-for-apps-built-with-claude-code): Give each pull request from an AI-assisted workflow its own isolated, temporary deployment for review. *Daniel Adeboye, Northflank, 2026*

### Talks

- [Implementing Preview Environments with GitOps in Kubernetes - François Le Pape, Remazing](https://www.youtube.com/watch?v=QNAiIJRIVWA): Per-PR previews with Argo CD and Bitbucket Pipelines: secrets via Sealed Secrets, repo layout, resource cleanup. *CNCF, 2022*
- [Hundreds of Clusters Sitting in a Tree with Argo CD - Mike Tougeron, Adobe](https://www.youtube.com/watch?v=casLvZWlIDw): Adobe's per-PR full-access environments using Argo CD, vcluster and Cluster API, with cost oversight. *CNCF, 2022*
- [Ephemeral developer preview environments with Consul Service Mesh](https://www.youtube.com/watch?v=GLnJakDY-RI): Request-isolated backend previews branched off a shared baseline using service mesh traffic routing. *Amarnath Ravikumar, HashiCorp, 2023*
- [From Pull Request to Live Environment: Automating Ephemeral Environments](https://www.youtube.com/watch?v=PzJGoUJf944): GoodRx's tool that builds ephemeral environments from PRs, controlled by a comment block. *Vahan Melikyan, GoodRx, SCALE 22x, 2025*

## FAQ

### What are preview environments?

Temporary, isolated deployments of an application created for a single change, usually one per pull request, with their own URL. Reviewers can test the change before it's merged, and the environment is deleted when the PR closes. See [what are preview environments](#what-are-preview-environments).

### What is the difference between preview and staging environments?

A preview environment tests **one change** before merge, and there's one per PR. A staging environment tests **the integrated release** after merge, and there's usually one shared copy. Previews remove the queue for staging. Staging still catches problems that only show up when changes are combined. See [preview environments vs staging](comparisons/preview-environments-vs-staging.md).

### What are the best preview environment tools?

It depends on what a preview must contain and where it must run. For frontends, most frontend hosts have built-in previews. For full-stack apps, look for platforms that give each preview its own backend services and database and clean up automatically. The [at a glance](#at-a-glance) matrix shows which do: for example Northflank (this list's maintainer), Qovery and Release, which can also run previews in your own cloud account. The [full-stack](comparisons/preview-environment-platform-comparison.md#full-stack) and [Kubernetes](comparisons/preview-environment-platform-comparison.md#kubernetes) sections have the details. If you want to build it yourself, see the [open-source tools](#open-source-tools). This list doesn't rank tools. The [comparison](comparisons/preview-environment-platform-comparison.md) lays out sourced facts so you can choose.

### How do I create a preview environment for every pull request?

Either enable previews on a platform that supports them (for example, a [Northflank preview blueprint](examples/northflank-preview-blueprint/) creates and deletes full-stack previews with no CI code), or build a pipeline yourself. A pipeline runs on PR open and push, builds the image, deploys it to an isolated environment named after the PR, posts the URL, and deletes everything on PR close. See [getting started](guides/set-up-preview-environments-for-pull-requests.md), [GitHub Actions](guides/github-actions-preview-environments.md) or [GitLab CI](guides/gitlab-review-apps.md), and the [Kubernetes example](examples/kubernetes-namespace-per-pr/).

### Can preview environments include databases?

Yes. A preview can provision a fresh database and seed it, restore or fork a snapshot, or use a copy-on-write branch (Neon, Supabase, PlanetScale, Xata and others). It can also share a staging database, though that gives no isolation. Several full-stack platforms provision databases per preview themselves. Northflank, for example, can create a fresh database per preview or fork one from a snapshot, then run a seed job. See [database preview environments](guides/database-preview-environments.md).

### How do Kubernetes preview environments work?

Most commonly, each PR is deployed into its own namespace (`pr-123`) with Helm or Kustomize. A wildcard DNS record and ingress give it a URL, and quotas and NetworkPolicy keep previews apart. Alternatives include a virtual cluster per PR, or deploying only the changed services and routing requests by header on a shared baseline. GitOps tools such as the Argo CD ApplicationSet Pull Request generator and Flux Operator ResourceSets can create these automatically. See the [Kubernetes guide](guides/kubernetes-preview-environments.md).

### Are there open-source preview environment platforms?

Yes. Self-hosted PaaS options with built-in previews include [Coolify](comparisons/preview-environment-platform-comparison.md#coolify) and [Dokploy](comparisons/preview-environment-platform-comparison.md#dokploy). Open-source building blocks include Argo CD, Flux Operator, vCluster, Garden and PullPreview. See [open-source tools](#open-source-tools) and [open source vs managed](comparisons/open-source-vs-managed-preview-environments.md).

### How much do preview environments cost?

Roughly the number of open PRs × the hourly cost of one preview × the hours each one runs. Lifetime controls usually matter most: deleting on close, TTLs and scaling to zero when idle. Platform pricing models differ, so check the *Pricing* column in the [comparison](comparisons/preview-environment-platform-comparison.md) and the [cost guide](guides/reduce-preview-environment-costs.md).

### How do you automatically delete preview environments?

Delete on the PR's `closed` event, which covers both merged and unmerged PRs. Add a TTL or inactivity expiry, plus a scheduled job that removes anything whose PR is closed. Most platforms do the first two natively. The *Automatic cleanup* column in the [comparison](comparisons/preview-environment-platform-comparison.md) shows which ones.

### Can AI coding agents use preview environments?

Yes. Each agent-opened PR can get a preview, like a human's. Agents can also be given the preview URL so they can run checks against it and fix failures before a human reviews the PR. Treat agent PRs as untrusted code. See [preview environments for AI coding agents](guides/preview-environments-for-ai-coding-agents.md).

## Related lists

- [EphemeralEnvironments.io](https://ephemeralenvironments.io/): community guide to ephemeral environments, started by Shipyard.
- [Cloud coding agent starter pack](https://github.com/northflank-examples/cloud-coding-agent-starter-pack): run AI coding agents in the cloud.
- [Agent sandbox starter pack](https://github.com/northflank-examples/agent-sandbox-starter-pack): isolate code that AI agents run.
- [Agent sandbox pricing](https://github.com/northflank-examples/agent-sandbox-pricing): sandbox pricing compared across vendors.

## Contributing

Additions and corrections from vendors and users are welcome. See [CONTRIBUTING](CONTRIBUTING.md) and the [methodology](methodology.md). Tables are generated from [`data/`](data/) by `python3 scripts/generate.py`.

## License

Content (Markdown and `data/*.json`) is licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Code (`scripts/` and `examples/`) is licensed MIT. See [LICENSE](LICENSE).
