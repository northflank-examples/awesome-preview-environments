# Preview environment platform comparison (2026)

A side-by-side comparison of preview environment platforms and tools: what each preview can contain, where it runs, which Git providers it supports, how databases are handled, how previews are cleaned up and protected, and how they're billed.

> **Disclosure:** this repository is maintained by [Northflank](https://northflank.com), one of the platforms compared. Every entry, including Northflank's, follows the same [methodology](../methodology.md). Every value links to the vendor's own documentation, with a verbatim quote, and corrections are welcome via [pull request](../CONTRIBUTING.md).

<!-- BEGIN GENERATED: last-updated -->
**Last verified:** 2026-10-26. 31 platforms and tools and 8 database tools, generated from [`data/platforms.json`](../data/platforms.json) and [`data/databases.json`](../data/databases.json). Every fact links to the vendor's own documentation; anything a vendor doesn't document is marked *not published*, never guessed.
<!-- END GENERATED: last-updated -->

**How to read this:** *not published* means the vendor doesn't document it. It doesn't mean "no". Values are summaries; the [details](#details) below give the quote and source for each one.

## At a glance

<!-- BEGIN GENERATED: capabilities -->
| Platform | Backend services | Own database | Start from existing data | Runs in your cloud | Deleted on PR close | Expiry / TTL | URL protection | Label / API / webhook triggers | Teardown hooks | Multi-repo previews |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Northflank](../comparisons/preview-environment-platform-comparison.md#northflank) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Release](../comparisons/preview-environment-platform-comparison.md#release) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Bunnyshell](../comparisons/preview-environment-platform-comparison.md#bunnyshell) | ✅ | ✅ | 🟡 | ✅ | ✅ | ❔ | ✅ | ✅ | ✅ | ✅ |
| [Qovery](../comparisons/preview-environment-platform-comparison.md#qovery) | ✅ | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ❔ |
| [Okteto](../comparisons/preview-environment-platform-comparison.md#okteto) | ✅ | ✅ | 🟡 | ✅ | 🟡 | ✅ | ✅ | 🟡 | ✅ | ✅ |
| [Signadot](../comparisons/preview-environment-platform-comparison.md#signadot) | 🟡 | ✅ | 🟡 | ✅ | 🟡 | ✅ | ✅ | ✅ | ✅ | ✅ |
| [Heroku](../comparisons/preview-environment-platform-comparison.md#heroku) | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❌ | ✅ | ✅ | ❌ |
| [Shipyard](../comparisons/preview-environment-platform-comparison.md#shipyard) | ✅ | ✅ | ✅ | ❌ | 🟡 | 🟡 | ✅ | ✅ | ❔ | ✅ |
| [Netlify](../comparisons/preview-environment-platform-comparison.md#netlify) | 🟡 | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ✅ | 🟡 | ❔ |
| [Railway](../comparisons/preview-environment-platform-comparison.md#railway) | ✅ | ✅ | ✅ | ❌ | ✅ | ❔ | ❌ | ✅ | ❔ | 🟡 |
| [Render](../comparisons/preview-environment-platform-comparison.md#render) | ✅ | ✅ | ❌ | ❌ | ✅ | ✅ | ❔ | ✅ | ❔ | 🟡 |
| [vCluster Platform (Loft)](../comparisons/preview-environment-platform-comparison.md#vcluster-platform) | ✅ | ❔ | 🟡 | ✅ | 🟡 | ✅ | ✅ | ✅ | 🟡 | ❔ |
| [Coolify](../comparisons/preview-environment-platform-comparison.md#coolify) | ✅ | ❌ | ❔ | ✅ | ✅ | ❔ | ❔ | ✅ | ❔ | ❌ |
| [Vercel](../comparisons/preview-environment-platform-comparison.md#vercel) | 🟡 | 🟡 | 🟡 | ❌ | ❌ | ✅ | ✅ | ✅ | 🟡 | ❔ |
| [AWS Amplify Hosting](../comparisons/preview-environment-platform-comparison.md#aws-amplify-hosting) | 🟡 | 🟡 | ❌ | ❌ | ✅ | ❔ | ✅ | 🟡 | ❔ | 🟡 |
| [Azure Static Web Apps](../comparisons/preview-environment-platform-comparison.md#azure-static-web-apps) | 🟡 | ❌ | ❔ | ❌ | ✅ | ❔ | ✅ | 🟡 | 🟡 | ❌ |
| [Cloudflare (Pages + Workers Previews)](../comparisons/preview-environment-platform-comparison.md#cloudflare) | 🟡 | ❌ | ❌ | ❌ | ❌ | 🟡 | ✅ | ✅ | 🟡 | ❌ |
| [Dokploy](../comparisons/preview-environment-platform-comparison.md#dokploy) | 🟡 | ❌ | ❔ | ✅ | ✅ | ❔ | ❔ | 🟡 | ❔ | ❌ |
| [Firebase Hosting](../comparisons/preview-environment-platform-comparison.md#firebase-hosting) | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❔ | ❔ |

✅ yes · 🟡 partial, limited, or only with extra setup · ❌ no · ❔ not documented. *Backend services*: containers or services beyond a frontend and functions. *Own database*: each preview can get its own database. *Start from existing data*: a preview database can be forked, cloned or branched from existing data. *Runs in your cloud*: BYOC, your cluster, or self-hosted. *Deleted on PR close* and *Expiry / TTL*: built in, not scripted in your CI. *URL protection*: built-in access control for preview URLs. *Label / API / webhook triggers*: previews can be created by more than PR events (two or more of label, API, CLI, webhook, schedule, manual). *Teardown hooks*: custom cleanup steps run when a preview is deleted. *Multi-repo previews*: one preview can include services built from several repositories. Every mark summarises a sourced fact in the [details](../comparisons/preview-environment-platform-comparison.md#details).
<!-- END GENERATED: capabilities -->

## Contents

- [Full-stack platforms](#full-stack)
- [Kubernetes and environment-as-a-service](#kubernetes)
- [Frontend platforms](#frontend)
- [Self-hosted PaaS](#self-hosted-paas)
- [Open-source tools](#open-source-tools)
- [CI/CD-native features](#cicd-native-features)
- [Details, quotes and sources](#details)
- [Excluded](#excluded)
- Looking to replace a specific product? See [alternatives to Vercel, Netlify, Heroku, Render and Railway previews](alternatives/).

<a id="full-stack"></a>

## Full-stack platforms

Managed platforms that deploy backend services, workers and databases for each preview, not just a frontend.

<!-- BEGIN GENERATED: comparison:full-stack -->
| Platform | What a preview includes | Runs on | Git providers | Created by | Databases | Automatic cleanup | Access control | Pricing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Northflank](#northflank) | Full-stack: services, jobs, databases, volumes, secret groups, URLs | Managed, BYOC in your cloud account, or your own cluster (BYOK) | GitHub, GitLab, Bitbucket, Azure DevOps; self-hosted GitLab, GHES, Gitea, Forgejo | PR, push, PR label, check suite, release, cron, webhook, API or manual run | Fresh database per preview, forked from a snapshot, seeded by a job, or shared | On PR close or branch delete, plus optional expiry (resets on update) and teardown steps | Per-port IP policies, basic auth or SSO | Previews billed as normal per-second compute; free Sandbox tier |
| [Heroku](#heroku) | Full Heroku app: dynos + add-ons from app.json | Managed (Heroku cloud, incl. Private Spaces) | GitHub only | PR opened (automatic) or manual via Dashboard/CLI | Yes, add-ons (e.g. Heroku Postgres) provisioned per app; seed via postdeploy | Yes, on PR close; optional 1-30 day inactivity | Public URL, random name by default | Dynos and add-ons billed as normal apps, per second |
| [Railway](#railway) | Full-stack: project services (incl. database services) | Managed (Railway-operated hardware) | GitHub | PR opened; optional for bot-authored PRs | Yes, own DB services; optional volume data copy (beta) | Yes, on PR merge/close | Railway-provided public domains if base env uses them | Usage-based compute; Hobby $5 / Pro $20 minimum usage |
| [Release](#release) | Static sites to multi-service apps with cloud dependencies | Managed (Release cloud) or BYOC (AWS, GCP) | GitHub, GitLab, Bitbucket (GitHub most complete) | PR opened or code push; manual via UI | Instant Datasets: pooled DBs from production snapshots | Yes, on PR close/merge; default 3-day expiry | Public or private (VPC) URLs; route-level auth | not published |
| [Render](#render) | Full-stack: services, datastores, environment groups | Managed (Render cloud) | GitHub, GitLab, Bitbucket (service previews) | Every PR (automatic) or opt-in via PR title/label (manual) | Yes, new empty Postgres/Key Value per preview; seedable | Yes, on PR merge/close; optional inactivity expiry | not published | Billed as normal compute; full-stack previews need Pro plan+ |
| [Shipyard](#shipyard) | Full-stack from Docker Compose (multiple services) | Managed (Shipyard Cloud) | GitHub, GitLab, Bitbucket | PR opened; also CLI, API, GitHub Action (Business+) | Per-env containers; volume snapshots via CLI | Spun down on merge; idle sleep via Since Last Visit | SSO-protected links | From $500/mo for 3 concurrent envs; 30-day free trial |
<!-- END GENERATED: comparison:full-stack -->

<a id="kubernetes"></a>

## Kubernetes and environment-as-a-service

These platforms create previews on Kubernetes, usually in **your** cluster or cloud account. The *Isolation* column matters most here: a namespace per preview, a virtual cluster per preview, or only the changed services routed on a shared baseline. See the [Kubernetes guide](../guides/kubernetes-preview-environments.md) for the trade-offs.

<!-- BEGIN GENERATED: comparison:kubernetes -->
| Platform | What a preview includes | Runs on | Isolation | Git providers | Created by | Databases | Automatic cleanup | Access control | Pricing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Bunnyshell](#bunnyshell) | Full-stack: Docker Compose, Helm, K8s manifests, Terraform | Your Kubernetes cluster (AWS, Azure, GCP, DO, private); trial cluster | Namespace per environment (NetworkPolicies need Calico/Cilium) | GitHub, GitLab, Bitbucket, Azure DevOps (incl. self-hosted) | PR opened, or API from CI pipeline | Container DB per env; seeding guides; Neon branching connector | Yes, on PR close/merge (configurable) | Public by default; IP allowlist via security.access | $0.007 per env-minute (Startup); 14-day free trial |
| [Okteto](#okteto) | Full-stack apps defined in Okteto manifest (Compose/Helm/K8s) | Self-hosted (Helm) or BYOC (AWS, GCP) | Namespace per preview | GitHub, GitLab (Bitbucket, Azure DevOps 'coming soon') | PR via CI (GitHub Actions, GitLab CI/CD) | Deployed per preview; volume snapshots to clone data | CI destroys on PR close; GC sleeps 1h, deletes after 7 days | Public or private endpoints (Okteto login) | Free up to 5 users; Scale/Enterprise per user |
| [Qovery](#qovery) | Full-stack: apps, databases, Helm charts, Terraform | BYOC (your AWS/GCP/Azure/Scaleway account); BYOK | Namespace per environment | GitHub, GitLab, Bitbucket | PR to base branch, or /qovery preview PR comment; CLI | Cloned or shared per preview; seeding via Lifecycle Jobs | Yes, on PR merge/close; optional inactivity expiry | Public by default; IP allowlist and basic auth options | From $299/mo (billed yearly); 14-day free trial |
| [Signadot](#signadot) | Changed services only; rest served by shared baseline | Your Kubernetes cluster + managed control plane | Request-based routing on shared baseline cluster | Via CI: GitHub Actions, GitLab, Bitbucket, Jenkins | CI pipeline / CLI / MCP; GitHub Action per PR | Temporary schemas/DBs via resource plugins | CLI teardown on PR close, TTL, or GitHub App label | Authenticated preview URLs (login or API key) | Free tier (50 sandboxes/mo); Business $250/mo |
| [vCluster Platform (Loft)](#vcluster-platform) | Any Kubernetes workloads inside a virtual cluster | Your clusters; platform self-hosted or vCluster Cloud | Virtual cluster (vCluster) per PR | GitHub (documented via GitHub Actions); CI-driven | CI workflow on pull request (vcluster CLI) | not published | CI deletes on PR close/merge; auto-sleep and auto-delete | Optional ingress auth limited to platform users | OSS and Free tier; Enterprise custom (Auto Sleep) |
<!-- END GENERATED: comparison:kubernetes -->

<a id="frontend"></a>

## Frontend platforms

Previews for static sites, frontend frameworks and serverless functions. Databases and backend services are usually shared, or come from an integration.

<!-- BEGIN GENERATED: comparison:frontend -->
| Platform | What a preview includes | Runs on | Git providers | Created by | Databases | Automatic cleanup | Access control | Pricing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [AWS Amplify Hosting](#aws-amplify-hosting) | Frontend/SSR + optional per-PR Amplify backend | Managed (AWS) | GitHub, Bitbucket, GitLab, AWS CodeCommit | Pull request opened against an enabled branch | Optional temporary backend env per PR (private repos only), or shared | Yes, preview and backend deleted on PR close | Basic-auth username/password per branch or app-wide | Pay-as-you-go (build $0.01/min); 12-month free tier |
| [Azure Static Web Apps](#azure-static-web-apps) | Static frontend + managed Azure Functions APIs | Managed (Azure) | GitHub (Actions) only for auto PR envs; Azure DevOps manual | PR against a watched branch (GitHub Actions workflow) | not published | Yes, deleted when PR closes | Public by default; password for staging (Standard plan) | Free plan (3 staging envs); Standard (10 staging envs) |
| [Cloudflare (Pages + Workers Previews)](#cloudflare) | Frontend + Workers; per-preview Durable Objects/containers | Managed (Cloudflare network) | GitHub, GitLab (Pages and Workers Builds); others via CI + Wrangler | Branch push/PR (Git integration), `wrangler preview`, or CI | No auto-provisioned DB; bind D1/KV/R2 per preview manually | Workers: oldest Preview deleted at limit; manual/CI delete. Pages: manual | Public by default; Cloudflare Access to require sign-in | Free plan available; Workers Paid from $5/month |
| [Firebase Hosting](#firebase-hosting) | Static frontend; uses the project's live backend | Managed (Google/Firebase) | GitHub (via official GitHub Action); any CI via CLI | CLI command or GitHub Action on PR commits | Shared only (real project backend) | Yes, TTL: expires after 7 days by default (max 30) | Public (unguessable URL), no built-in protection | No-cost Spark plan (10 GB storage); Blaze pay-as-you-go |
| [Netlify](#netlify) | Frontend + serverless functions (+ Netlify Database branch) | Managed (Netlify cloud) | GitHub, GitLab, Bitbucket, Azure DevOps, Cursor Origin | PR/MR opened; Netlify agent run | Yes: Netlify Database branch per preview, copied from production | Deploys auto-deleted after 30 days (90 on paid); not on PR close | Password (Pro+); team login/SSO and previews-only scope (Enterprise) | Unlimited deploy previews on Free; Pro $20/mo |
| [Vercel](#vercel) | Frontend + serverless functions | Managed (Vercel cloud) | GitHub, GitLab, Bitbucket, Origin, Azure Pipelines; CLI for others | Any non-production branch push, PR, or CLI deploy | Per-preview Neon branch via Marketplace integration | Retention policy: previews deleted after 180 days (Pro) / 30 days (Hobby) | Vercel Authentication (all plans); password (Pro add-on); SSO/IPs (Enterprise) | Unlimited deployments on all plans; Hobby free, Pro $20/mo |
<!-- END GENERATED: comparison:frontend -->

<a id="self-hosted-paas"></a>

## Self-hosted PaaS

Open-source platforms that you install on your own servers, with preview deployments built in.

<!-- BEGIN GENERATED: comparison:self-hosted-paas -->
| Platform | What a preview includes | Runs on | Git providers | Created by | Databases | Automatic cleanup | Access control | Pricing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Coolify](#coolify) | Application or Docker Compose stack per PR | Self-hosted (free) or Coolify Cloud control plane on your servers | GitHub, GitLab, Bitbucket, Gitea | PR/MR opened or updated via GitHub App or webhook; API | None built in; use non-prod external DBs | Yes, on PR/MR close or merge | not published | Self-hosted free; Cloud $5/mo (2 servers) |
| [Dokploy](#dokploy) | Single application per PR | Self-hosted, or Dokploy Cloud managing your servers | GitHub only | PR opened against target branch; optional label filter | not published | Yes, on PR close/merge | Inherits app's security/redirect config; traefik.me URL | Self-hosted free; Cloud from $4.50/mo per server |
<!-- END GENERATED: comparison:self-hosted-paas -->

## Open-source tools

Building blocks: you supply the CI pipeline and infrastructure, and the tool handles part of the preview lifecycle.

<!-- BEGIN GENERATED: comparison:open-source-tool -->
| Platform | What a preview includes | Runs on | Git providers | Created by | Databases | Automatic cleanup | Access control | Pricing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Argo CD ApplicationSet Pull Request generator](#argo-cd-pr-generator) | Any Kubernetes manifests/Helm/Kustomize per PR | Self-hosted on your Kubernetes cluster | GitHub, GitLab, Gitea, Bitbucket Server/Cloud, Azure DevOps | Open PR matching filters (labels, state); polling or webhook | not published | Yes, Application removed when PR no longer matches | not published | Free (open source); you run the cluster |
| [DigitalOcean App Platform PR previews (app_action)](#digitalocean-app-platform) | App Platform app from app spec (services etc.) | Managed (DigitalOcean); action runs in GitHub Actions | GitHub (GitHub Actions) | GitHub Actions pull_request workflow | not published | Yes, via delete action on PR close/merge | Public live URL posted as PR comment | Billed as normal App Platform apps; from $5/month |
| [Flux Operator ResourceSets](#flux-operator-resourceset) | Any Flux-managed Kubernetes resources (e.g. Helm release) per PR | Self-hosted on your Kubernetes cluster | GitHub, GitLab, Gitea/Forgejo, Azure DevOps | PR label filter; polling or webhook Receiver | not published | Yes, Helm release uninstalled after merge | not published | Free (open source); you run the cluster |
| [Fly.io PR Review Apps (superfly/fly-pr-review-apps)](#fly-pr-review-apps) | Single Fly app by default; extra apps/DB attach via workflow | Managed (Fly.io); action runs in GitHub Actions | GitHub (GitHub Actions) | GitHub Actions on pull_request events | Optional: new DB in an existing Fly Postgres cluster | Yes, app destroyed on PR close event | Public *.fly.dev URL | Billed as normal Fly Machines usage |
| [Garden](#garden) | Full-stack K8s apps (Dockerfiles, manifests, Helm) | Self-hosted (your Kubernetes cluster); optional Garden Cloud | Any (driven from your CI pipeline) | CI job or CLI (garden deploy) | not published | Beta: inactivity pause/cleanup agent (paid Garden Cloud) | not published | not published |
| [Laravel Harbor](#laravel-harbor) | Laravel app site + database on a Forge server | Your own Laravel Forge-managed server | GitHub, GitLab (incl. self-hosted), custom; Bitbucket not yet | GitHub Actions on pull request | Yes, per-preview database created (optional) | Yes, teardown workflow on PR merge/close | not published | not published |
| [pr-preview-action](#pr-preview-action) | Static frontend only (GitHub Pages) | Managed (GitHub Pages) | GitHub only; no fork PRs | pull_request opened/reopened/synchronize | None (static sites) | Yes, on PR close | not published | not published |
| [PullPreview](#pullpreview) | Full-stack Docker Compose apps; Helm charts | BYOC: AWS Lightsail or Hetzner | GitHub only | Adding a label to a PR | not published | On label removal; optional TTL | Optional IP/CIDR allowlist; HTTPS via Let's Encrypt | 300€/year per org for commercial use, plus your cloud costs |
| [vCluster](#vcluster) | Isolated virtual Kubernetes cluster per PR | Self-hosted on your Kubernetes cluster | GitHub Actions guide documented | GitHub Actions on pull request | not published | Yes, via a destroy workflow on PR close/merge | not published | OSS free; Platform has Free and Enterprise tiers |
<!-- END GENERATED: comparison:open-source-tool -->

## CI/CD-native features

Preview features built into Git hosting and CI systems. They track environments and run teardown jobs, but you provide everything they deploy to.

<!-- BEGIN GENERATED: comparison:ci-native -->
| Platform | What a preview includes | Runs on | Git providers | Created by | Databases | Automatic cleanup | Access control | Pricing |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Azure Pipelines Review App (Kubernetes environments)](#azure-pipelines-review-app) | Kubernetes manifests deployed to a per-PR namespace | Your Kubernetes cluster (AKS or other) | PRs from your Git repo; GitHub comment documented | Pipeline run on PR create/update | not published | not published | not published | Billed as Azure Pipelines parallel jobs; free tier |
| [GitHub Actions deployment environments](#github-actions-environments) | None itself; tracks deployments your workflow performs | not published | GitHub only | Workflow referencing an environment (auto-created) | not published | not published | not published | Free plans: public repos only; Pro/Team for private |
| [GitLab Review Apps](#gitlab-review-apps) | Whatever your CI deploy job deploys | Your own infrastructure (Kubernetes via Auto DevOps optional) | GitLab only | CI pipeline per branch or merge request | not published | Yes, stop job on MR merge/close; auto_stop_in TTL | not published | Available on Free, Premium, Ultimate tiers |
<!-- END GENERATED: comparison:ci-native -->

## Details

<!-- BEGIN GENERATED: platform-details -->
### Full-stack platforms

<a id="northflank"></a>

#### Northflank

> Disclosure: this repository is maintained by Northflank.

Full-stack container platform. A preview blueprint, built in a visual editor or as JSON kept in Git, builds each pull request or branch and deploys its services, jobs, databases, volumes, secret groups and URLs as an isolated preview environment, on Northflank's cloud or in your own cloud account.

[Preview docs](https://northflank.com/docs/v1/application/release/set-up-preview-blueprints) · [Website](https://northflank.com/product/preview-environments) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Full-stack: services, jobs, databases, volumes, secret groups, URLs | “Each preview environment is an isolated instance of your application with its own services, databases, and URLs.” [source](https://northflank.com/docs/v1/application/release/set-up-preview-blueprints) |
| **Runs on** | Managed, BYOC in your cloud account, or your own cluster (BYOK) | “Bring your own cloud (BYOC) runs Northflank workloads in your cloud account...You can also import an existing Kubernetes cluster (BYOK) for Northflank to manage.” [source](https://northflank.com/docs/v1/application/bring-your-own-cloud/use-other-cloud-providers-with-northflank) |
| **Git providers** | GitHub, GitLab, Bitbucket, Azure DevOps; self-hosted GitLab, GHES, Gitea, Forgejo | “Northflank integrates with GitHub, GitLab, Bitbucket, Azure DevOps, and Cursor Origin to build and deploy code from your repositories.” [source](https://northflank.com/docs/v1/application/getting-started/link-your-git-account) |
| **Created by** | PR, push, PR label, check suite, release, cron, webhook, API or manual run | “Preview blueprints can create or update environments from Git events, webhook requests, or a schedule.” [source](https://northflank.com/docs/v1/application/release/set-up-preview-blueprints) |
| **Databases** | Fresh database per preview, forked from a snapshot, seeded by a job, or shared | “Build your application, provision a fresh database for the preview, deploy the application, and inject the database credentials....Alternatively, fork your database from a snapshot to restore pre-seeded data more efficiently.” [source](https://northflank.com/docs/v1/application/release/set-up-preview-blueprints) |
| **Automatic cleanup** | On PR close or branch delete, plus optional expiry (resets on update) and teardown steps | “Git providers can also request preview deletion when a pull request closes or its branch is deleted.” [source](https://northflank.com/docs/v1/application/release/manage-preview-blueprints) |
| **Access control** | Per-port IP policies, basic auth or SSO | “To configure a port-wide security policy, expand the custom domains & security rules menu for a port and add a new IP policy, credentials, or select an organisation for SSO access control.” [source](https://northflank.com/docs/v1/application/network/add-security-policies-for-ports) |
| **License** | Proprietary | Closed-source commercial service; no open-source license is published. |
| **Pricing** | Previews billed as normal per-second compute; free Sandbox tier | “Up to $20 a month of free resources on Northflank Cloud, across 2 services, 2 jobs, and 1 database.” [source](https://northflank.com/pricing) |
| **Triggers beyond PR/push** | PR label, webhook, API, cron, manual run | “Starts a preview run for a pull request with matching labels...Starts a preview run on a UTC schedule...Starts a preview run from a GET or POST request” [source](https://northflank.com/docs/v1/application/release/set-up-preview-blueprints) |
| **Start from existing data** | Fork a database from a snapshot | “Alternatively, fork your database from a snapshot to restore pre-seeded data more efficiently.” [source](https://northflank.com/docs/v1/application/release/set-up-preview-blueprints) |
| **Teardown hooks** | Teardown specification runs on preview deletion | “Add a teardown specification for cleanup when a preview environment is deleted. Use it for external resources or cleanup jobs that normal preview deletion does not handle.” [source](https://northflank.com/docs/v1/application/release/set-up-preview-blueprints) |
| **Multi-repo previews** | Multiple Git triggers and build nodes in one blueprint | “This request sets `frontend` to branch `feature` and `backend` to branch `develop`” [source](https://northflank.com/docs/v1/application/release/run-and-manage-workflows) |

Caveats:

- Active hours (pause previews outside working hours, resume in the morning) is only available for projects in your own cloud account (https://northflank.com/docs/v1/application/release/set-up-preview-blueprints).
- A teardown specification can clean up external resources, such as OpenTofu-managed infrastructure, when a preview is deleted (https://northflank.com/docs/v1/application/release/set-up-preview-blueprints).
- With GitOps and 'use branch contents', each preview runs the blueprint file from its own branch, so a PR can change its own preview infrastructure (https://northflank.com/docs/v1/application/release/set-up-preview-blueprints).
- A message node can comment the preview URL on the pull request, or post it to Slack or a webhook (https://northflank.com/docs/v1/application/infrastructure-as-code/template-nodes).
- Webhook-triggered previews: anyone with the webhook URL can request a preview run, so treat it as a credential (https://northflank.com/docs/v1/application/release/set-up-preview-blueprints).

<a id="heroku"></a>

#### Heroku

Managed PaaS (Salesforce) where each GitHub pull request in a Pipeline can get a disposable Heroku app configured by app.json, including add-ons.

[Preview docs](https://devcenter.heroku.com/articles/github-integration-review-apps) · [Website](https://www.heroku.com) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Full Heroku app: dynos + add-ons from app.json | “Review apps run the code in any GitHub pull request in a complete, disposable Heroku app.” [source](https://devcenter.heroku.com/articles/github-integration-review-apps) |
| **Runs on** | Managed (Heroku cloud, incl. Private Spaces) | “In most cases, Heroku defaults to using the least expensive dyno available in your plan for review apps. However, apps in Private Spaces default to using private-m dynos.” [source](https://devcenter.heroku.com/articles/github-integration-review-apps) |
| **Git providers** | GitHub only | “Your app must enable both Heroku Pipelines and GitHub integration to use review apps.” [source](https://devcenter.heroku.com/articles/github-integration-review-apps) |
| **Created by** | PR opened (automatic) or manual via Dashboard/CLI | “With automatic creation, Heroku creates a review app as soon as a pull request is opened on your app’s connected GitHub repo.” [source](https://devcenter.heroku.com/articles/github-integration-review-apps) |
| **Databases** | Yes, add-ons (e.g. Heroku Postgres) provisioned per app; seed via postdeploy | “Copying full database contents to a review app isn’t currently supported. ... Instead, we recommend seeding databases” [source](https://devcenter.heroku.com/articles/github-integration-review-apps) |
| **Automatic cleanup** | Yes, on PR close; optional 1-30 day inactivity | “Review apps exist only for the life of their associated pull request. You can set to destroy them automatically after 1, 2, 5, 14 or 30 days of inactivity” [source](https://devcenter.heroku.com/articles/github-integration-review-apps) |
| **Access control** | Public URL, random name by default | “After enabling review apps, visit the pipeline’s Settings tab to check and update the URL pattern. The default is set to random.” [source](https://devcenter.heroku.com/articles/github-integration-review-apps) |
| **License** | Proprietary | Closed-source commercial service; no open-source license is published (inferred). |
| **Pricing** | Dynos and add-ons billed as normal apps, per second | “Heroku charges dynos and add-ons in review apps in exactly the same way as for normal apps. Costs are pro-rated to the second, and you’re only charged for the time that the review app exists.” [source](https://devcenter.heroku.com/articles/github-integration-review-apps) |
| **Triggers beyond PR/push** | Dashboard button, CLI, Platform API | “From the dashboard, you can manually create review apps for a listed pull request with the Create button next to it. You can also manually create review apps from a connected repository via the Heroku CLI with heroku reviewapps:create: ... It allows you to enable, disable, create, and delete review apps.” [source](https://devcenter.heroku.com/articles/github-integration-review-apps) |
| **Start from existing data** | Seed scripts only; DB copy unsupported | “Copying full database contents to a review app isn’t currently supported.” [source](https://devcenter.heroku.com/articles/github-integration-review-apps) |
| **Teardown hooks** | pr-predestroy script in app.json | “You can optionally specify a pr-predestroy script on your app.json file. This script runs when review apps are destroyed when the associated pull request is merged or closed. ... Use the pr-predestroy script to tear down any resources provisioned during postdeploy and to do other clean-up.” [source](https://devcenter.heroku.com/articles/github-integration-review-apps) |
| **Multi-repo previews** | One pipeline = one connected GitHub repo | “connect your pipeline to the corresponding GitHub repository. ... An app.json file is required in the root of your app’s GitHub repo for review apps to work.” [source](https://devcenter.heroku.com/articles/github-integration-review-apps) |

Caveats:

- Requires Heroku Pipelines and an app.json in the repo root (https://devcenter.heroku.com/articles/github-integration-review-apps).
- Closing a PR only destroys review apps that were created automatically; manually created ones persist (same page).
- Review apps are not auto-created for PRs from forks of public repos (same page).
- Predictable review-app URLs are not planned for Fir-generation apps; Review Apps themselves are listed as supported on both generations (https://devcenter.heroku.com/articles/generations).
- Auto-created review app costs are charged to the user who connected the app to GitHub (same page).

<a id="railway"></a>

#### Railway

Managed PaaS where enabling PR Environments spins up a temporary copy of a project environment (its services) for each GitHub pull request.

[Preview docs](https://docs.railway.com/guides/environments) · [Website](https://railway.com) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Full-stack: project services (incl. database services) | “Railway can spin up a temporary environment whenever you open a Pull Request. ... When enabled, a temporary environment is spun up to support the Pull Request deploy.” [source](https://docs.railway.com/guides/environments) |
| **Runs on** | Managed (Railway-operated hardware) | “It is built on hardware that we own and operate in datacenters around the world.” [source](https://docs.railway.com/railway-metal) |
| **Git providers** | GitHub | “How come my GitHub PR won't deploy? Railway will not deploy a PR branch from a user who is not in your workspace or invited to your project without their associated GitHub account.” [source](https://docs.railway.com/guides/environments) |
| **Created by** | PR opened; optional for bot-authored PRs | “You can enable automatic PR environment creation for PRs opened by GitHub bots using the Enable Bot PR Environments toggle” [source](https://docs.railway.com/guides/environments) |
| **Databases** | Yes, own DB services; optional volume data copy (beta) | “you can now automatically copy volume data from one environment to another for all services when spinning up new PR environments. ... This feature is currently in beta.” [source](https://railway.com/changelog/2024-12-13-volume-data-transfer) |
| **Automatic cleanup** | Yes, on PR merge/close | “These environments are deleted as soon as these PRs are merged or closed.” [source](https://docs.railway.com/guides/environments) |
| **Access control** | Railway-provided public domains if base env uses them | “Services in PR environments will only receive domains automatically when their corresponding base environment” [source](https://docs.railway.com/guides/environments) |
| **License** | Proprietary | Closed-source commercial service; no open-source license is published (inferred). |
| **Pricing** | Usage-based compute; Hobby $5 / Pro $20 minimum usage | “Hobby $ 5 minimum usage ... Includes $5 of monthly usage credits After credits are used, you'll only be charged for extra resource usage” [source](https://railway.com/pricing) |
| **Triggers beyond PR/push** | Dashboard button, CLI, API (generic environments) | “Create, delete, edit, or link an environment. ... railway environment new staging --duplicate production” [source](https://docs.railway.com/cli/environment) |
| **Start from existing data** | Copy volume data from base environment | “you can now automatically copy volume data from one environment to another for all services when spinning up new PR environments. To get started, navigate to PR Environments in the Environments section of your project settings. From there, set a base environment and toggle the Enable Copy Volume Data switch.” [source](https://railway.com/changelog/2024-12-13-volume-data-transfer) |
| **Teardown hooks** | Not documented | “These environments are deleted as soon as these PRs are merged or closed.” [source](https://docs.railway.com/environments) |
| **Multi-repo previews** | Project can mix services from several repos | “Services connected to the PR repo that are affected by changed files” [source](https://docs.railway.com/environments) |

Caveats:

- PR branches from users not in the workspace/project are not deployed (https://docs.railway.com/guides/environments).
- Focused PR Environments and volume-data copy are labelled beta (https://docs.railway.com/guides/environments; https://railway.com/changelog/2024-12-13-volume-data-transfer).

<a id="release"></a>

#### Release

Environments-as-a-service platform that builds Docker Compose/Helm/static apps into Kubernetes environments in Release's cloud or your own, creating an ephemeral environment per pull request.

[Preview docs](https://docs.release.com/) · [Website](https://release.com) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Static sites to multi-service apps with cloud dependencies | “Release can build environments in our cloud or yours, from the simplest applications (static JavaScript) to the most complex (microservices with many cloud-native dependencies).” [source](https://docs.release.com/) |
| **Runs on** | Managed (Release cloud) or BYOC (AWS, GCP) | “Release can build environments in our cloud or yours” [source](https://docs.release.com/) |
| **Isolation** | Namespace per environment | “When it runs, Release will remove your environment from the UI and remove the namespace along with all corresponding objects from Kubernetes.” [source](https://docs.release.com/reference-documentation/application-settings/application-template/schema-definition) |
| **Git providers** | GitHub, GitLab, Bitbucket (GitHub most complete) | “You can integrate Release with GitHub , Bitbucket , and GitLab . GitHub integration includes full support for pull requests, comments, and more.” [source](https://docs.release.com/integrations/source-control-integrations) |
| **Created by** | PR opened or code push; manual via UI | “These environments can then be automatically generated and updated whenever you push a code change or create a PR. They can also be manually deployed via the Release user interface.” [source](https://docs.release.com/) |
| **Databases** | Instant Datasets: pooled DBs from production snapshots | “With minimal set up, you can have production-replica data available to any of your environments, instantly, regardless of dataset size.” [source](https://docs.release.com/reference-documentation/instant-datasets-aws) |
| **Automatic cleanup** | Yes, on PR close/merge; default 3-day expiry | “Closed pull request: Destroy an ephemeral environment when the pull request is closed or merged.” [source](https://docs.release.com/integrations/source-control-integrations/github) |
| **Access control** | Public or private (VPC) URLs; route-level auth | “Routes allow for edge routing rewrites, authentication and provide full support for ngnix ingress rules.” [source](https://docs.release.com/reference-documentation/application-settings/application-template/schema-definition) |
| **License** | Proprietary | “Request a demo of Release to get started” [source](https://docs.release.com/) |
| **Pricing** | not published | release.com/pricing is client-rendered and returned no plan details when fetched; docs mention a Premium plan without prices. |
| **Triggers beyond PR/push** | PR label, REST API, CLI | “You can integrate your Release account or application with [GitHub labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels) to create an environment in Release when you add a label to a pull request.” [source](https://docs.release.com/reference-documentation/application-settings/github) |
| **Start from existing data** | Instant Datasets from RDS snapshots | “Instant Datasets are a collection of databases that are ready to be used by an ephemeral environment. These datasets are based on the production snapshots created for you by Amazon RDS.” [source](https://docs.release.com/reference-documentation/instant-datasets-aws) |
| **Teardown hooks** | Workflow teardown stage | “The teardown stage is run when an environment is either expired or deleted. You can use the teardown stage to remove any extra infrastructure, permanent entries, or storage created elsewhere that Release is not aware of.” [source](https://docs.release.com/reference-documentation/workflows-in-release/stages-of-workflows) |
| **Multi-repo previews** | App Imports | “our solution to a microservices architecture is the App Imports feature. App Imports creates single-direction dependencies from one application to another with all services being brought up in the same namespace.” [source](https://docs.release.com/guides-and-examples/advanced-guides/microservices-architecture) |

Caveats:

- Bitbucket and GitLab integrations are described as 'more limited' than GitHub (https://docs.release.com/integrations/source-control-integrations).
- Some plans cannot change ephemeral expiration; Premium can extend or disable it (https://docs.release.com/reference-documentation/environment-expiration).

<a id="render"></a>

#### Render

Managed PaaS that can create a copy of a Blueprint-defined environment (services, datastores, env groups) for each pull request, or a preview of a single web service/static site.

[Preview docs](https://render.com/docs/preview-environments) · [Website](https://render.com) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Full-stack: services, datastores, environment groups | “automatically creating a fresh copy of your production environment (including services, datastores, and environment groups) with every pull request” [source](https://render.com/docs/preview-environments) |
| **Runs on** | Managed (Render cloud) | “Connect your repo, and go Deploy up to 25 services ... Single-service previews ... Full-stack previews” [source](https://render.com/pricing) |
| **Git providers** | GitHub, GitLab, Bitbucket (service previews) | “On GitHub, preview instances are represented as deployments associated with your PR ... On GitLab, Bitbucket, and Cursor Origin, Render adds a comment to your PR with a link to your preview instance.” [source](https://render.com/docs/service-previews) |
| **Created by** | Every PR (automatic) or opt-in via PR title/label (manual) | “Manual By default, Render does not create PR previews. To create a preview for a specific PR, do any of the following: Add the label render-preview to the PR (GitHub/GitLab only). Include the string [render preview] in your PR's title” [source](https://render.com/docs/service-previews) |
| **Databases** | Yes, new empty Postgres/Key Value per preview; seedable | “Copies of datastores and persistent disks do not include data from their corresponding "base" resource (you can seed sample data as part of preview environment initialization ).” [source](https://render.com/docs/preview-environments) |
| **Automatic cleanup** | Yes, on PR merge/close; optional inactivity expiry | “automatically destroys them when the original pull request is merged or closed. You can also set up an expiry time to automatically clean up preview environments after a period of inactivity.” [source](https://render.com/docs/preview-environments) |
| **Access control** | not published | Docs reviewed do not describe access protection for preview URLs. |
| **License** | Proprietary | Closed-source commercial service; no open-source license is published (inferred). |
| **Pricing** | Billed as normal compute; full-stack previews need Pro plan+ | “Preview environments require a Pro workspace plan or higher. ... Preview resources are billed the same as other Render services and are prorated by the second.” [source](https://render.com/docs/preview-environments) |
| **Triggers beyond PR/push** | PR label/title opt-in, REST API (image-backed service previews) | “To create a preview for a specific PR, do any of the following: - Add the label `render-preview` to the PR (GitHub/GitLab only). ... For image-backed services, you can create a service preview using the Render API.” [source](https://render.com/docs/service-previews) |
| **Start from existing data** | Empty/seeded datastores only | “Copies of datastores and persistent disks do _not_ include data from their corresponding "base" resource (you can seed sample data as part of preview environment initialization).” [source](https://render.com/docs/preview-environments) |
| **Teardown hooks** | Not documented | “You might want to run custom initialization for your preview environment after it is created but not on subsequent deploys” [source](https://render.com/docs/preview-environments) |
| **Multi-repo previews** | Blueprint can pull services from other repos (default branch) | “For Git-based services, the URL of the Git provider repo to use. Your Git provider account must have access to the repo. If omitted, Render uses the repo that contains the Blueprint file. ... Render uses the repo's default branch (most commonly `main` or `master`) if the service uses a different repo from the Blueprint file.” [source](https://render.com/docs/blueprint-spec) |

Caveats:

- Preview environments require a Blueprint (render.yaml); `previews.expireAfterDays` sets inactivity expiry, default is no expiry (https://render.com/docs/preview-environments).
- Preview environments do not currently support Render Workflows (https://render.com/docs/preview-environments).
- Single-service PR previews are listed on the Hobby plan; full-stack preview environments on Pro and above (https://render.com/pricing).
- Image-backed service previews are created via API and are not auto-deleted (https://render.com/docs/service-previews).

<a id="shipyard"></a>

#### Shipyard

Managed ephemeral-environment platform that builds a full-stack copy of an app from its Docker Compose file for every pull request; acquired by StackGen in 2026.

[Preview docs](https://docs.stackgen.com/shipyard/getting-started/what-is-shipyard) · [Website](https://shipyard.build) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Full-stack from Docker Compose (multiple services) | “Shipyard automatically generates a full-stack ephemeral environment on every pull request” [source](https://docs.stackgen.com/shipyard/getting-started/what-is-shipyard) |
| **Runs on** | Managed (Shipyard Cloud) | “Resources run in Shipyard Cloud” [source](https://shipyard.build/pricing/) |
| **Isolation** | Independent environment per PR (Compose to K8s) | “Each of these environments is independent, meaning that if a new bug or regression is introduced, it will not prevent other tests from running.” [source](https://docs.stackgen.com/shipyard/getting-started/what-is-shipyard) |
| **Git providers** | GitHub, GitLab, Bitbucket | “assuming you have integrated with GitHub , GitLab , or Bitbucket” [source](https://docs.stackgen.com/shipyard/environments/deploy-an-environment) |
| **Created by** | PR opened; also CLI, API, GitHub Action (Business+) | “It creates ephemeral, on-demand copies of your app every time you open a PR.” [source](https://docs.stackgen.com/shipyard/getting-started/what-is-shipyard) |
| **Databases** | Per-env containers; volume snapshots via CLI | “Load a volume snapshot in an environment” [source](https://docs.stackgen.com/shipyard/environments/cli) |
| **Automatic cleanup** | Spun down on merge; idle sleep via Since Last Visit | “Our environments are designed to be short-lived, and are automatically spun down upon merge. Shipyard's Since Last Visit (SLV) timeout can be set to spin down environments after a set amount of time has passed without visitors.” [source](https://shipyard.build/blog/heroku-review-apps-vs-shipyard/) |
| **Access control** | SSO-protected links | “You can share these environments with SSO-enabled links” [source](https://docs.stackgen.com/shipyard/getting-started/what-is-shipyard) |
| **License** | Proprietary | “Startup If you're just getting started $500 / month” [source](https://shipyard.build/pricing/) |
| **Pricing** | From $500/mo for 3 concurrent envs; 30-day free trial | “Startup If you're just getting started $500 / month Try free for 30 days ✓ 3 Drydocks (concurrent envs)” [source](https://shipyard.build/pricing/) |
| **Triggers beyond PR/push** | PR label opt-in, API, CLI (detached envs) | “If this is enabled, pull request environments will only be created for pull requests with the labels specified.” [source](https://docs.stackgen.com/shipyard/environments/build-behavior) |
| **Start from existing data** | Volume snapshots inherited from base env | “PR environments will automatically inherit the base environment's most recent snapshot.” [source](https://docs.stackgen.com/shipyard/environments/configuration/volume-management) |
| **Teardown hooks** | Not documented | “shipyard.lifecycle.preStop.exec.command ... Command to run on Kubernetes pre-stop event (as JSON string)” [source](https://docs.stackgen.com/shipyard/environments/configuration/docker-compose) |
| **Multi-repo previews** | Multi-repo applications | “Shipyard supports both mono and multi-repo applications. Each repo within a Shipyard app must have a valid Docker Compose file.” [source](https://docs.stackgen.com/shipyard/environments/configuration/multi-repo) |

Caveats:

- Acquired by StackGen (announced Sep 29, 2026); docs moved to docs.stackgen.com (https://stackgen.com/blog/shipyard-joins-stackgen).
- Plans are limited by 'Drydocks' (concurrent running environments) (https://docs.stackgen.com/shipyard/environments/deploy-an-environment).

### Kubernetes and environment-as-a-service

<a id="bunnyshell"></a>

#### Bunnyshell

Environment-as-a-service that deploys environments defined in bunnyshell.yaml (Compose, Helm, manifests, Terraform) to Kubernetes clusters; ephemeral environments are copies of a primary environment created per pull request.

[Preview docs](https://documentation.bunnyshell.com/docs/quickstart-ephemeral-environments) · [Website](https://www.bunnyshell.com) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Full-stack: Docker Compose, Helm, K8s manifests, Terraform | “all components of kind Helm , KubernetesManifest , GenericComponent are deleted by running their defined scripts / commands from the destroy attribute of each.” [source](https://documentation.bunnyshell.com/docs/environment-workflows-destroy) |
| **Runs on** | Your Kubernetes cluster (AWS, Azure, GCP, DO, private); trial cluster | “Bunnyshell Kubernetes Cluster AWS Kubernetes Cluster Azure Kubernetes Cluster GCP Kubernetes Cluster DigitalOcean Kubernetes Cluster Scaleway Kubernetes Cluster DT Cloud Kubernetes Cluster Private Kubernetes Cluster” [source](https://documentation.bunnyshell.com/docs/quickstart-ephemeral-environments) |
| **Isolation** | Namespace per environment (NetworkPolicies need Calico/Cilium) | “each environment is deployed in its own namespace” [source](https://documentation.bunnyshell.com/docs/kubernetes-clusters-bunnyshell) |
| **Git providers** | GitHub, GitLab, Bitbucket, Azure DevOps (incl. self-hosted) | “Supported Git Version Control Systems (VCS) GitHub , including self-hosted Gitlab , including self-hosted Bitbucket Azure DevOps including self-hosted” [source](https://documentation.bunnyshell.com/docs/git-providers) |
| **Created by** | PR opened, or API from CI pipeline | “With Bunnyshell, ephemeral environments are automatically created very simply, either when creating a Pull Request or via API from your current CI/CD pipeline.” [source](https://documentation.bunnyshell.com/docs/quickstart-ephemeral-environments) |
| **Databases** | Container DB per env; seeding guides; Neon branching connector | “Bunnyshell can leverage Neon to create database branches when an Environment is deployed, and have them destroyed when an Environment is deleted from Bunnyshell.” [source](https://documentation.bunnyshell.com/docs/connectors-neon-database) |
| **Automatic cleanup** | Yes, on PR close/merge (configurable) | “Closed Pull Request - Destroy an ephemeral environment when the Pull Request is closed or merged.” [source](https://documentation.bunnyshell.com/docs/git-providers) |
| **Access control** | Public by default; IP allowlist via security.access | “For example, you can have a non-public environment, that can be accessed only from certain IP ranges.” [source](https://documentation.bunnyshell.com/docs/ref-envyaml-definition-security) |
| **License** | Proprietary | “Startup Only pay for what you use. No contracts, no capacity planning. $0.007 / min per env” [source](https://www.bunnyshell.com/pricing/) |
| **Pricing** | $0.007 per env-minute (Startup); 14-day free trial | “14-day free trial Startup Only pay for what you use. No contracts, no capacity planning. $0.007 / min per env Pay-as-you-go. No contracts.” [source](https://www.bunnyshell.com/pricing/) |
| **Triggers beyond PR/push** | API (from CI), CLI environment clone | “With Bunnyshell, ephemeral environments are automatically created very simply, either when creating a Pull Request or via API from your current CI/CD pipeline.” [source](https://documentation.bunnyshell.com/docs/quickstart-ephemeral-environments) |
| **Start from existing data** | Branching via Neon/PlanetScale connectors; RDS snapshot via Terraform | “Bunnyshell can leverage Neon to create database branches when an Environment is deployed, and have them destroyed when an Environment is deleted from Bunnyshell.” [source](https://documentation.bunnyshell.com/docs/connectors-neon-database) |
| **Teardown hooks** | destroy scripts per component | “all components of kind Helm , KubernetesManifest , GenericComponent are deleted by running their defined scripts / commands from the destroy attribute of each.” [source](https://documentation.bunnyshell.com/docs/environment-workflows-destroy) |
| **Multi-repo previews** | Yes; each component sets its own repo | “When a pull request opens in any connected Git repository, Bunnyshell automatically provisions a complete, isolated environment containing every service in your stack — regardless of which repo each service lives in.” [source](https://www.bunnyshell.com/per-pr-environments-microservices/) |

Caveats:

- Ephemeral environments are only created once the primary environment has deployed successfully (https://documentation.bunnyshell.com/docs/quickstart-ephemeral-environments).
- Namespace isolation NetworkPolicies require a CNI such as Calico or Cilium (https://documentation.bunnyshell.com/docs/namespace-isolation).

<a id="okteto"></a>

#### Okteto

Kubernetes development-environment platform (self-hosted or BYOC) whose CI integrations deploy an Okteto manifest into a namespace per pull request.

[Preview docs](https://www.okteto.com/docs/previews/) · [Website](https://www.okteto.com) · [Source](https://github.com/okteto/okteto) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Full-stack apps defined in Okteto manifest (Compose/Helm/K8s) | “Okteto deploys your application using your Okteto manifest , creating an isolated environment in response to the CI/CD trigger” [source](https://www.okteto.com/docs/previews/) |
| **Runs on** | Self-hosted (Helm) or BYOC (AWS, GCP) | “Deployment model Starter Self-Hosted Scale Self-Hosted Enterprise Self-Hosted or BYOC” [source](https://www.okteto.com/pricing/) |
| **Isolation** | Namespace per preview | “A Preview Environment's Namespace is the same as its name, so if you change one, change the other.” [source](https://www.okteto.com/docs/tutorials/preview-environments/) |
| **Git providers** | GitHub, GitLab (Bitbucket, Azure DevOps 'coming soon') | “When you create or update a PR in GitHub or GitLab, your CI/CD workflow triggers an Okteto Preview Environment automatically” [source](https://www.okteto.com/docs/previews/) |
| **Created by** | PR via CI (GitHub Actions, GitLab CI/CD) | “When you create or update a PR in GitHub or GitLab, your CI/CD workflow triggers an Okteto Preview Environment automatically” [source](https://www.okteto.com/docs/previews/) |
| **Databases** | Deployed per preview; volume snapshots to clone data | “Okteto Volume Snapshots allow you to initialize Persistent Volume Claims (PVCs) with data from a previously created snapshot.” [source](https://www.okteto.com/docs/core/use-volume-snapshots) |
| **Automatic cleanup** | CI destroys on PR close; GC sleeps 1h, deletes after 7 days | “Preview Environments Sleep period: 1h Delete period: 7 days” [source](https://www.okteto.com/docs/admin/cleanup) |
| **Access control** | Public or private endpoints (Okteto login) | “Private endpoints can only be accessed by Okteto users who have access to your Okteto namespace, and they'll need to provide their credentials before being granted access.” [source](https://www.okteto.com/docs/core/endpoints/private-endpoints/) |
| **License** | Proprietary platform; CLI is Apache-2.0 | “Apache License Version 2.0, January 2004” [source](https://github.com/okteto/okteto/blob/master/LICENSE) |
| **Pricing** | Free up to 5 users; Scale/Enterprise per user | “Perfect for exploring Okteto with a small team. Free for up to 5 users, no credit card needed.” [source](https://www.okteto.com/pricing/) |
| **Triggers beyond PR/push** | CLI (okteto preview deploy, any branch) | “Run okteto preview deploy to automatically deploy a Preview Environment for your branch.” [source](https://www.okteto.com/docs/reference/okteto-cli/) |
| **Start from existing data** | Volume snapshots to initialize PVCs | “Okteto Volume Snapshots allow you to initialize Persistent Volume Claims (PVCs) with data from a previously created snapshot. ... Restoring a database (PostgreSQL, MySQL, etc.) with real data for development and testing” [source](https://www.okteto.com/docs/core/use-volume-snapshots) |
| **Teardown hooks** | Manifest destroy section runs on preview destroy | “Run okteto preview destroy to destroy a Preview Environment by name. If the Okteto Manifest includes destroy commands, they will be executed as part of this command.” [source](https://www.okteto.com/docs/reference/okteto-cli/) |
| **Multi-repo previews** | Manifest dependencies (other repos) | “A list of repositories you want to deploy as part of your development environment.” [source](https://www.okteto.com/docs/reference/okteto-manifest/) |

Caveats:

- Pricing is per user, not per environment: 'You pay per user, never per environment or agent.' (https://www.okteto.com/pricing/)
- Previews can be marked Persistent to exempt them from sleep and garbage collection (https://www.okteto.com/docs/admin/previews/).

<a id="qovery"></a>

#### Qovery

Platform that operates Kubernetes clusters in your own cloud account; preview environments are clones of a 'blueprint' environment created per pull request.

[Preview docs](https://www.qovery.com/docs/configuration/environment) · [Website](https://www.qovery.com) · [Source](https://github.com/Qovery/engine) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Full-stack: apps, databases, Helm charts, Terraform | “The frontend, backend, PostgreSQL and Redis instances are cloned!” [source](https://www.qovery.com/docs/getting-started/guides/use-cases/preview-environments) |
| **Runs on** | BYOC (your AWS/GCP/Azure/Scaleway account); BYOK | “No. Your apps run in your own AWS, GCP, Azure or Scaleway account, on infrastructure you own. Qovery is the execution layer on top, it operates what you already run and does not host it.” [source](https://www.qovery.com/pricing) |
| **Isolation** | Namespace per environment | “An environment is a group of applications, databases, and services running within the same Kubernetes namespace.” [source](https://www.qovery.com/docs/configuration/environment) |
| **Git providers** | GitHub, GitLab, Bitbucket | “Qovery fetches your code from Git (GitHub, GitLab, Bitbucket) based on the branch configured for your environment” [source](https://www.qovery.com/docs/getting-started/basic-concepts) |
| **Created by** | PR to base branch, or /qovery preview PR comment; CLI | “Qovery automatically creates a Preview Environment for every pull request targeting your base branch. ... Developers manually trigger Preview Environment creation by commenting on pull requests.” [source](https://www.qovery.com/docs/configuration/environment) |
| **Databases** | Cloned or shared per preview; seeding via Lifecycle Jobs | “Optionally include databases (clones or shared) ... Populate Preview Environment databases with test data using Lifecycle Jobs.” [source](https://www.qovery.com/docs/configuration/environment) |
| **Automatic cleanup** | Yes, on PR merge/close; optional inactivity expiry | “Qovery keeps your preview environments up to date on every commit and automatically destroys them when the original pull request is merged or closed. You can also set up an expiry time to automatically clean up preview environments after a period of inactivity.” [source](https://www.qovery.com/docs/getting-started/guides/use-cases/preview-environments) |
| **Access control** | Public by default; IP allowlist and basic auth options | “Allows you to specify IP CIDR ranges allowed to access your service. Use this for IP whitelisting. ... Default Value: 0.0.0.0/0” [source](https://www.qovery.com/docs/configuration/service-advanced-settings) |
| **License** | Proprietary platform; engine is GPL-3.0 | “GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007” [source](https://github.com/Qovery/engine/blob/engine-public/LICENSE) |
| **Pricing** | From $299/mo (billed yearly); 14-day free trial | “Starter For startups shipping their first production app on their own cloud $299 per month Start 14-days free trial Billed yearly” [source](https://www.qovery.com/pricing) |
| **Triggers beyond PR/push** | PR comment (/qovery preview), CLI/API environment clone, Console clone | “Developers manually trigger Preview Environment creation by commenting on pull requests. ... Developers comment /qovery preview on PRs to trigger creation ... Click the Clone button in environment settings” [source](https://www.qovery.com/docs/configuration/environment) |
| **Start from existing data** | No; DB clone copies config only, seed via Lifecycle Jobs | “Note that only the instance configuration will be copied, not the data contained within the database.” [source](https://www.qovery.com/docs/configuration/database) |
| **Teardown hooks** | Lifecycle Job on Delete event | “A Lifecycle Job is a Kubernetes job that is triggered by environment lifecycle events (deploy, stop, or delete). ... Delete Event : Triggered when the environment is deleted. Use for: Cleaning up external resources Deleting cloud resources” [source](https://www.qovery.com/docs/configuration/lifecycle-job) |
| **Multi-repo previews** | not published | Only evidence is an archived 2022 community-forum answer, not vendor documentation. |

Caveats:

- Cloud compute for previews is billed by your own cloud provider, on top of the Qovery subscription (https://www.qovery.com/pricing).
- Qovery recommends running previews on a separate cluster from production (https://www.qovery.com/docs/getting-started/guides/use-cases/preview-environments).

<a id="signadot"></a>

#### Signadot

Kubernetes operator plus SaaS control plane that creates lightweight 'sandboxes' deploying only changed services and routing requests by header on a shared baseline cluster.

[Preview docs](https://www.signadot.com/docs/guides/set-up-pr-sandboxes) · [Website](https://www.signadot.com) · [Source](https://github.com/signadot/cli) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Changed services only; rest served by shared baseline | “Unchanged services are served from the shared cluster, so a sandbox is a lightweight delta, not a full environment clone.” [source](https://www.signadot.com/docs/overview) |
| **Runs on** | Your Kubernetes cluster + managed control plane | “Signadot installs into your Kubernetes cluster and connects to a remote control plane.” [source](https://www.signadot.com/docs/overview) |
| **Isolation** | Request-based routing on shared baseline cluster | “Both approaches use standard header propagation protocols like OpenTelemetry or B3 to split traffic between sandbox and baseline environments.” [source](https://www.signadot.com/docs/overview) |
| **Git providers** | Via CI: GitHub Actions, GitLab, Bitbucket, Jenkins | “Setting up the Signadot CLI with Bitbucket ... Setting up the Signadot CLI with GitLab” [source](https://www.signadot.com/docs/guides/integrate-ci) |
| **Created by** | CI pipeline / CLI / MCP; GitHub Action per PR | “Integrate the template into your CI/CD pipeline to automatically create sandboxes for each pull request.” [source](https://www.signadot.com/docs/guides/set-up-pr-sandboxes) |
| **Databases** | Temporary schemas/DBs via resource plugins | “These plugins create temporary schemas or databases for sandboxes with minimal overhead, enabling proper isolation of data changes while maintaining efficiency in shared resources.” [source](https://www.signadot.com/docs/overview) |
| **Automatic cleanup** | CLI teardown on PR close, TTL, or GitHub App label | “Once the PR is closed, the sandbox can be torn down. This can be done using the Signadot CLI. Alternatively, you can set a Time To Live (TTL) for the sandbox.” [source](https://www.signadot.com/docs/guides/integrate-ci) |
| **Access control** | Authenticated preview URLs (login or API key) | “All preview endpoints are authenticated and require a Signadot API” [source](https://www.signadot.com/docs/reference/sandboxes/preview-urls) |
| **License** | Proprietary platform; CLI is Apache-2.0 | “Apache License Version 2.0, January 2004” [source](https://github.com/signadot/cli/blob/main/LICENSE) |
| **Pricing** | Free tier (50 sandboxes/mo); Business $250/mo | “Sandboxes are billed per creation. Updates to existing Sandboxes don't count toward billing.” [source](https://www.signadot.com/pricing/) |
| **Triggers beyond PR/push** | CLI, REST API, MCP server | “Agents interact with Signadot through an MCP server, so any agent running in Cursor, Claude Code, VS Code, or any MCP-compatible environment can spin up sandboxes, run tests, and validate changes as part of its own workflow, without human intervention. ... the CLI for developers and the MCP server for agents” [source](https://www.signadot.com/docs/overview) |
| **Start from existing data** | Copy-on-write branch via Neon/Xata resource plugins | “A copy-on-write branch of a Neon or Xata database ... A branch starts with all of the parent's schema and data, but writes to it never reach the parent.” [source](https://www.signadot.com/docs/concepts/resources) |
| **Teardown hooks** | Resource plugin delete steps | “It is created when the sandbox is created, and destroyed when the sandbox is deleted, including when the sandbox's TTL expires. ... Resources are created and deleted by resource plugins . A plugin is a short YAML spec plus the scripts that create and delete one kind of resource.” [source](https://www.signadot.com/docs/concepts/resources) |
| **Multi-repo previews** | Route groups join sandboxes from several PRs/repos | “a route group joins the sandboxes under one routing key, so one preview URL sends requests through all of them ... Each service repository runs its own copy with SERVICE set to the service it builds; in a monorepo like HotROD, detect the changed service instead.” [source](https://www.signadot.com/docs/tutorials/multi-pr-feature-testing) |

Caveats:

- Request isolation requires header propagation (OpenTelemetry/B3) through your services; routing via built-in devmesh or Istio/Linkerd (https://www.signadot.com/docs/overview).
- Free Starter plan: 50 sandboxes/month, 1 Kubernetes cluster (https://www.signadot.com/pricing/).

<a id="vcluster-platform"></a>

#### vCluster Platform (Loft)

Virtual-cluster platform; its documented preview workflow uses GitHub Actions to create a virtual (tenant) Kubernetes cluster per pull request on a shared host cluster, with sleep mode for idle environments.

[Preview docs](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments) · [Website](https://www.vcluster.com) · [Source](https://github.com/loft-sh/vcluster) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Any Kubernetes workloads inside a virtual cluster | “The example creates a new tenant cluster for each pull request and installs Argo CD into it as a stand-in workload.” [source](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments) |
| **Runs on** | Your clusters; platform self-hosted or vCluster Cloud | “With vCluster Cloud, vCluster hosts the platform for you, while your host and virtual clusters still run in your infrastructure.” [source](https://www.vcluster.com/pricing) |
| **Isolation** | Virtual cluster (vCluster) per PR | “This gives you preview environments that are fast to create, isolated like separate Kubernetes clusters, and free of cost while unused.” [source](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments) |
| **Git providers** | GitHub (documented via GitHub Actions); CI-driven | “This guide shows how to use vCluster and GitHub Actions to deploy preview environments on every pull request.” [source](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments) |
| **Created by** | CI workflow on pull request (vcluster CLI) | “On every pull request, this workflow creates a tenant cluster, installs Argo CD, and exposes it through an ingress.” [source](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments) |
| **Databases** | not published | Preview guide does not cover database provisioning or seeding. |
| **Automatic cleanup** | CI deletes on PR close/merge; auto-sleep and auto-delete | “Create a separate workflow that deletes the tenant cluster as soon as the pull request is closed or merged” [source](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments) |
| **Access control** | Optional ingress auth limited to platform users | “enable ingress authentication in the template's advanced options, to allow only users with access to your platform instance to reach the preview environments.” [source](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments) |
| **License** | vCluster OSS Apache-2.0; Platform proprietary | “Apache License Version 2.0, January 2004” [source](https://github.com/loft-sh/vcluster/blob/main/LICENSE) |
| **Pricing** | OSS and Free tier; Enterprise custom (Auto Sleep) | “Enterprise Custom Deploy mission-critrical virtual clusters at enterprise scale with maximum confidence.” [source](https://www.vcluster.com/pricing) |
| **Triggers beyond PR/push** | CLI, UI (from template), Platform API | “Tenant clusters referring to templates can be created in the UI or using the vCluster CLI.” [source](https://vcluster.com/docs/platform/use-platform/virtual-clusters/create/create-with-template) |
| **Start from existing data** | Snapshot clone of tenant cluster; volumes need Velero | “You can use snapshots to clone an existing tenant cluster and create a new tenant cluster from that snapshot. When creating a new tenant cluster from a snapshot, it also restores all workloads in the tenant cluster.” [source](https://vcluster.com/docs/vcluster/manage/backup-restore/restore) |
| **Teardown hooks** | Your CI deletes the tenant cluster on PR close | “Create a separate workflow that deletes the tenant cluster as soon as the pull request is closed or merged” [source](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments) |
| **Multi-repo previews** | Not documented | The preview guide installs a stand-in workload and says to add an Argo CD Application 'that points at your repository'; deploying services from multiple repos into one tenant cluster is not documented (a tenant cluster is a generic Kubernetes cluster, so it is plausible but unverified). |

Caveats:

- Free plan covers 'Unlimited virtual clusters for up to 64 CPUs or 32 GPUs'; Auto Sleep is listed under Enterprise (https://www.vcluster.com/pricing).
- Previews are a documented recipe (GitHub Actions + CLI), not a turnkey PR integration.

### Frontend platforms

<a id="aws-amplify-hosting"></a>

#### AWS Amplify Hosting

AWS-managed hosting that deploys each pull request to a unique preview URL and can optionally create a temporary Amplify backend environment per PR, deleted when the PR closes.

[Preview docs](https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html) · [Website](https://aws.amazon.com/amplify/hosting/) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Frontend/SSR + optional per-PR Amplify backend | “With fullstack previews, you can set up ephemeral fullstack environments on every pull request.” [source](https://docs.amplify.aws/react/deploy-and-host/amplify-hosting/pr-previews/) |
| **Runs on** | Managed (AWS) | “A web preview deploys every pull request made to your repository to a unique preview URL which is completely different from the URL your main site uses.” [source](https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html) |
| **Git providers** | GitHub, Bitbucket, GitLab, AWS CodeCommit | “Amplify supports GitHub, Bitbucket, GitLab, and AWS CodeCommit.” [source](https://docs.aws.amazon.com/amplify/latest/userguide/getting-started-next.html) |
| **Created by** | Pull request opened against an enabled branch | “The next time you submit a pull request for the branch, Amplify builds and deploys your PR to a preview URL.” [source](https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html) |
| **Databases** | Optional temporary backend env per PR (private repos only), or shared | “For apps with backend environments provisioned using the Amplify CLI or Amplify Studio, every pull request (private Git repositories only) creates a temporary backend that is deleted when the PR is closed.” [source](https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html) |
| **Automatic cleanup** | Yes, preview and backend deleted on PR close | “After the pull request is closed, the preview URL is deleted, and any temporary backend environment linked to the pull request is deleted.” [source](https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html) |
| **Access control** | Basic-auth username/password per branch or app-wide | “When access control is set on a branch, users are prompted for a user name and password when they attempt to access the URL for the branch.” [source](https://docs.aws.amazon.com/amplify/latest/userguide/access-control.html) |
| **License** | Proprietary | Closed-source commercial managed service; vendor publishes no source code or license for the platform itself (inferred, no explicit license statement fetched). |
| **Pricing** | Pay-as-you-go (build $0.01/min); 12-month free tier | “No cost up to 1,000 build minutes per month” [source](https://aws.amazon.com/amplify/pricing/) |
| **Triggers beyond PR/push** | API (branch environments, not PR previews) | “CreateBranch Creates a new branch for an Amplify app.” [source](https://docs.aws.amazon.com/amplify/latest/APIReference/API_CreateBranch.html) |
| **Start from existing data** | New temporary backend or shared dev backend | “For example, you might want all your preview branches to point to the backend resources deployed by the dev branch so you can reuse seed data, users, and groups.” [source](https://docs.amplify.aws/react/deploy-and-host/amplify-hosting/pr-previews/) |
| **Teardown hooks** | Auto-delete only; no custom hook documented | “After the pull request is closed, the preview URL is deleted, and any temporary backend environment linked to the pull request is deleted.” [source](https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html) |
| **Multi-repo previews** | Frontend repo points at backend from another repo | “You might have different frontend and backend teams that maintain their own repositories. With Amplify Gen 2, you can deploy repositories that have backend-only code, so frontend and backend teams can operate independently of each other.” [source](https://docs.amplify.aws/react/deploy-and-host/amplify-hosting/mono-and-multi-repos/) |

Caveats:

- Each PR counts toward the quota of 50 branches per app (https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html).
- Previews cannot be enabled for public repos on apps needing an IAM service role (backends, WEB_COMPUTE/SSR) to prevent untrusted code running with your role (https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html).
- GitHub previews require the Amplify GitHub App; OAuth-connected apps must migrate first (https://docs.aws.amazon.com/amplify/latest/userguide/pr-previews.html).

<a id="azure-static-web-apps"></a>

#### Azure Static Web Apps

Azure service for static frontends with managed Azure Functions APIs; its generated GitHub Actions workflow deploys each pull request to a staging environment that is deleted when the PR closes.

[Preview docs](https://learn.microsoft.com/en-us/azure/static-web-apps/review-publish-pull-requests) · [Website](https://azure.microsoft.com/en-us/products/app-service/static) · [Source](https://github.com/Azure/static-web-apps-deploy) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Static frontend + managed Azure Functions APIs | “\| APIs via Azure Functions \| Managed \| Managed or Bring your own Functions app \|” [source](https://learn.microsoft.com/en-us/azure/static-web-apps/plans) |
| **Runs on** | Managed (Azure) | “A pre-production environment is a fully functional staged version of your application that includes changes not available in production.” [source](https://learn.microsoft.com/en-us/azure/static-web-apps/review-publish-pull-requests) |
| **Git providers** | GitHub (Actions) only for auto PR envs; Azure DevOps manual | “Pull request environments are not automatically supported for Azure DevOps, but you can use named environments to set them up manually.” [source](https://learn.microsoft.com/en-us/azure/static-web-apps/review-publish-pull-requests) |
| **Created by** | PR against a watched branch (GitHub Actions workflow) | “Azure Static Web Apps generates a YAML workflow in the repo. When a pull request is created against a branch that the workflow watches, the pre-production environment gets built.” [source](https://learn.microsoft.com/en-us/azure/static-web-apps/review-publish-pull-requests) |
| **Databases** | not published | No per-preview database documented. The Database Connections feature is retired: 'Retirement notice: Database Connections for Static Web Apps ends November 30, 2025.' (https://learn.microsoft.com/en-us/azure/static-web-apps/database-overview) |
| **Automatic cleanup** | Yes, deleted when PR closes | “The lifecycle of a pre-production environment is tied to the pull request. Once the pull request is closed, the pre-production environment is automatically deleted.” [source](https://learn.microsoft.com/en-us/azure/static-web-apps/review-publish-pull-requests) |
| **Access control** | Public by default; password for staging (Standard plan) | “select Protect staging environments only to protect only your app's pre-production environments or select Protect both production and staging environments to protect all environments.” [source](https://learn.microsoft.com/en-us/azure/static-web-apps/password-protection) |
| **License** | Proprietary service; deploy Action MIT | “"spdx_id": "MIT"” [source](https://api.github.com/repos/Azure/static-web-apps-deploy) |
| **Pricing** | Free plan (3 staging envs); Standard (10 staging envs) | “\| Staging environments \| 3 per app \| 10 per app \| 20 per app \|” [source](https://learn.microsoft.com/en-us/azure/static-web-apps/plans) |
| **Triggers beyond PR/push** | CLI (swa deploy, default env 'preview') | “--env [environment] : the type of deployment environment where to deploy the project (default: " preview ")” [source](https://learn.microsoft.com/en-us/azure/static-web-apps/static-web-apps-cli-deploy) |
| **Start from existing data** | Not documented | “Retirement notice: Database Connections for Static Web Apps ends November 30, 2025.” [source](https://learn.microsoft.com/en-us/azure/static-web-apps/database-overview) |
| **Teardown hooks** | Generated close_pull_request_job in your workflow | “close_pull_request_job: if: github.event_name == 'pull_request' && github.event.action == 'closed' runs-on: ubuntu-latest name: Close Pull Request Job steps: - name: Close Pull Request id: closepullrequest uses: Azure/static-web-apps-deploy@v1 with: ... action: "close"” [source](https://learn.microsoft.com/en-us/azure/static-web-apps/build-configuration) |
| **Multi-repo previews** | Linked backends not allowed on PR environments | “Bring your own API backends cannot be linked to a Static Web Apps pull request environment.” [source](https://learn.microsoft.com/en-us/azure/static-web-apps/apis-overview) |

Caveats:

- Pre-production environments aren't geo-distributed (https://learn.microsoft.com/en-us/azure/static-web-apps/review-publish-pull-requests).
- The Dedicated plan was retired effective October 31, 2025 (https://learn.microsoft.com/en-us/azure/static-web-apps/plans).
- Database Connections (Data API builder) feature retired November 30, 2025 (https://learn.microsoft.com/en-us/azure/static-web-apps/database-overview).
- Azure/static-web-apps-deploy repo last pushed 2024-09-11 (GitHub API).

<a id="cloudflare"></a>

#### Cloudflare (Pages + Workers Previews)

Cloudflare Pages creates a preview deployment per branch/PR on pages.dev; Workers (Cloudflare's recommended platform for new projects) has Previews, an isolated per-branch copy of a Worker created with `wrangler preview` or Workers Builds.

[Preview docs](https://developers.cloudflare.com/workers/previews/) · [Website](https://www.cloudflare.com/developer-platform/) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Frontend + Workers; per-preview Durable Objects/containers | “Cloudflare automatically provisions a new Durable Object namespace and container instances for each Preview. KV, D1, R2, and other resources are isolated when you bind the Preview to a separate resource.” [source](https://developers.cloudflare.com/workers/previews/) |
| **Runs on** | Managed (Cloudflare network) | “Previews give each branch an isolated, production-like environment under the same Worker.” [source](https://developers.cloudflare.com/workers/previews/) |
| **Git providers** | GitHub, GitLab (Pages and Workers Builds); others via CI + Wrangler | “Cloudflare supports connecting Cloudflare Pages to your GitHub and GitLab repositories. Pages does not currently support connecting self-hosted instances of GitHub or GitLab.” [source](https://developers.cloudflare.com/pages/configuration/git-integration/) |
| **Created by** | Branch push/PR (Git integration), `wrangler preview`, or CI | “enable Preview Builds and confirm the Preview command is npx wrangler preview. Workers Builds creates the Preview. For GitHub and GitLab repositories, it also comments the Preview URL on the pull request.” [source](https://developers.cloudflare.com/workers/previews/examples/) |
| **Databases** | No auto-provisioned DB; bind D1/KV/R2 per preview manually | “Use your base branch to configure one staging database that all Previews share by default. A branch that needs an isolated database overrides that binding in its own configuration.” [source](https://developers.cloudflare.com/workers/previews/resources/) |
| **Automatic cleanup** | Workers: oldest Preview deleted at limit; manual/CI delete. Pages: manual | “When a limit is reached, Cloudflare automatically deletes the oldest to make room: Preview limit: the Preview that was deployed to least recently is deleted.” [source](https://developers.cloudflare.com/workers/previews/) |
| **Access control** | Public by default; Cloudflare Access to require sign-in | “Preview URLs are public by default. Use Cloudflare Access to require sign-in. You can protect all Previews on an account, one Worker's Previews, or specific hostnames.” [source](https://developers.cloudflare.com/workers/previews/) |
| **License** | Proprietary | Closed-source commercial managed service; vendor publishes no source code or license for the platform itself (inferred, no explicit license statement fetched). Wrangler CLI is open source (repo metadata not fetched). |
| **Pricing** | Free plan available; Workers Paid from $5/month | “The Workers Paid plan includes Workers, Pages Functions, Workers KV, Hyperdrive, and Durable Objects usage for a minimum charge of $5 USD per month for an account.” [source](https://developers.cloudflare.com/workers/platform/pricing/) |
| **Triggers beyond PR/push** | CLI (wrangler preview / pages deploy --branch), Pages Deploy Hooks, dashboard upload | “Running `npx wrangler preview` creates or updates a Preview for your current branch under the same Worker.” [source](https://developers.cloudflare.com/workers/previews/) |
| **Start from existing data** | Shared or separately bound resources only | “Two Previews bound to the same account-level resource ID or name share its data or instances. Bind a Preview to a different resource to isolate it.” [source](https://developers.cloudflare.com/workers/previews/resources/) |
| **Teardown hooks** | Own CI on PR close (documented example) | “Delete closed pull request Previews ... The workflow trigger above includes the `closed` event. Add this cleanup job under `jobs`:” [source](https://developers.cloudflare.com/workers/previews/examples/) |
| **Multi-repo previews** | Cross-Worker previews bind to production | “Today, if Worker A has a service binding to Worker B and you deploy a Preview of Worker A, the Preview of Worker A can only bind to the production Worker B. It does not automatically bind to a matching Preview of Worker B.” [source](https://developers.cloudflare.com/workers/previews/resources/) |

Caveats:

- Cloudflare now steers new projects to Workers: 'Workers supports most Pages use cases and offers a broader feature set ... Start new projects with Workers.' (https://developers.cloudflare.com/pages/). Pages is not announced as deprecated.
- Worker Previews launched in Sept 2026 and require Wrangler 4.135.0+; service bindings, routes and cron triggers from a Preview still target production (https://developers.cloudflare.com/workers/previews/).
- Cloudflare recommends against using Version URLs / aliased Version URLs for PR previews because they use production resources (https://developers.cloudflare.com/workers/previews/compare-workflows/).
- Pages PR previews are only created for PRs originating from the repository itself, not forks (https://developers.cloudflare.com/pages/configuration/preview-deployments/).

<a id="firebase-hosting"></a>

#### Firebase Hosting

Google's static/web hosting where `firebase hosting:channel:deploy` or the official GitHub Action deploys to a temporary preview channel URL that expires after a TTL; previews talk to the project's real backend.

[Preview docs](https://firebase.google.com/docs/hosting/test-preview-deploy) · [Website](https://firebase.google.com/products/hosting) · [Source](https://github.com/FirebaseExtended/action-hosting-deploy) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Static frontend; uses the project's live backend | “Reminder: When using preview URLs, your app interacts with the real backend resources of your Firebase project.” [source](https://firebase.google.com/docs/hosting/github-integration) |
| **Runs on** | Managed (Google/Firebase) | “If you need your teammates to view and test your changes, Hosting can create sharable, temporary preview URLs for your site.” [source](https://firebase.google.com/docs/hosting/test-preview-deploy) |
| **Git providers** | GitHub (via official GitHub Action); any CI via CLI | “Creates a new preview channel (and its associated preview URL) for every PR on your GitHub repository.” [source](https://firebase.google.com/docs/hosting/github-integration) |
| **Created by** | CLI command or GitHub Action on PR commits | “firebase hosting:channel:deploy CHANNEL_ID” [source](https://firebase.google.com/docs/hosting/test-preview-deploy) |
| **Databases** | Shared only (real project backend) | “Reminder: When using preview URLs, your app interacts with the real backend resources of your Firebase project.” [source](https://firebase.google.com/docs/hosting/github-integration) |
| **Automatic cleanup** | Yes, TTL: expires after 7 days by default (max 30) | “By default, a preview channel expires 7 days from its creation date, but your site's live channel will never expire. When a preview channel expires, the channel, along with its releases and associated versions, are scheduled for deletion within 24 hours.” [source](https://firebase.google.com/docs/hosting/manage-hosting-resources) |
| **Access control** | Public (unguessable URL), no built-in protection | “Note that although preview URLs are difficult to guess (as they contain a random hash), they are public. So, anyone who knows the URL can access it.” [source](https://firebase.google.com/docs/hosting/test-preview-deploy) |
| **License** | Proprietary service; GitHub Action Apache-2.0 | “"spdx_id": "Apache-2.0"” [source](https://api.github.com/repos/FirebaseExtended/action-hosting-deploy) |
| **Pricing** | No-cost Spark plan (10 GB storage); Blaze pay-as-you-go | “No-cost up to 10 GB” [source](https://firebase.google.com/pricing) |
| **Triggers beyond PR/push** | CLI, REST API | “From the root of your local project directory, run the following command: firebase hosting:channel:deploy CHANNEL_ID” [source](https://firebase.google.com/docs/hosting/test-preview-deploy) |
| **Start from existing data** | Previews use the real (shared) backend | “When using a preview URL, your web app interacts with your real backend for all project resources (with the exception of any "pinned" functions in your rewrites config).” [source](https://firebase.google.com/docs/hosting/test-preview-deploy) |
| **Teardown hooks** | Expiry/delete only; no hook documented | “When a preview channel expires, the channel, along with its releases and associated versions, are scheduled for deletion within 24 hours.” [source](https://firebase.google.com/docs/hosting/manage-hosting-resources) |
| **Multi-repo previews** | Not documented | “(Optional) Deploys the current state of your GitHub repo to your live channel when the PR is merged.” [source](https://firebase.google.com/docs/hosting/github-integration) |

Caveats:

- Previews share production backend resources (Firestore, Auth, etc.) except functions 'pinned' in rewrites config (https://firebase.google.com/docs/hosting/test-preview-deploy).
- Redeploying within 7 days of expiry auto-extends the channel by 7 days (https://firebase.google.com/docs/hosting/manage-hosting-resources).
- This entry covers Firebase Hosting; Firebase App Hosting is a separate product and was not assessed.

<a id="netlify"></a>

#### Netlify

Managed web platform that automatically builds a Deploy Preview with a unique URL for each pull/merge request (and agent run), including functions, with an on-page feedback drawer.

[Preview docs](https://docs.netlify.com/deploy/deploy-types/deploy-previews/) · [Website](https://www.netlify.com) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Frontend + serverless functions (+ Netlify Database branch) | “Your functions are version-controlled, built, and deployed along with the rest of your Netlify site, giving you the power of Deploy Previews” [source](https://docs.netlify.com/build/functions/overview/) |
| **Runs on** | Managed (Netlify cloud) | “When you open a pull / merge request in a connected site repository from GitHub, GitLab, Bitbucket, Azure DevOps, or Cursor Origin, Netlify automatically builds a Deploy Preview for you.” [source](https://docs.netlify.com/deploy/deploy-types/deploy-previews/) |
| **Git providers** | GitHub, GitLab, Bitbucket, Azure DevOps, Cursor Origin | “open pull / merge requests in a connected site repository from GitHub, GitLab, Bitbucket, Azure DevOps, or Cursor Origin.” [source](https://docs.netlify.com/deploy/deploy-types/deploy-previews/) |
| **Created by** | PR/MR opened; Netlify agent run | “By default, Netlify automatically builds Deploy Previews when you do one of the following: start an agent run...open pull / merge requests in a connected site repository” [source](https://docs.netlify.com/deploy/deploy-types/deploy-previews/) |
| **Databases** | Yes: Netlify Database branch per preview, copied from production | “Deploy previews get their own database branch, with a copy of the production data taken when the deploy preview is first created; any changes to the data or the schema made during the lifecycle of the deploy preview will not affect the production database” [source](https://docs.netlify.com/build/data-and-storage/netlify-db/) |
| **Automatic cleanup** | Deploys auto-deleted after 30 days (90 on paid); not on PR close | “By default, Netlify will delete deploys after 30 days (or 90 days on paid plans). This includes deploys triggered by either source control changes, the Netlify UI or CLI, manual uploads, or third-party integrations.” [source](https://docs.netlify.com/deploy/manage-deploys/manage-deploys-overview/) |
| **Access control** | Password (Pro+); team login/SSO and previews-only scope (Enterprise) | “Basic password protection for your entire site is available on all Pro plans. All basic password protection and team login protection options are available on Enterprise plans.” [source](https://docs.netlify.com/manage/security/secure-access-to-sites/password-protection/) |
| **License** | Proprietary | Closed-source commercial managed service; vendor publishes no source code or license for the platform itself (inferred, no explicit license statement fetched). |
| **Pricing** | Unlimited deploy previews on Free; Pro $20/mo | “Unlimited deploy previews” [source](https://www.netlify.com/pricing/) |
| **Triggers beyond PR/push** | Agent run, CLI draft deploy, API, build hook | “By default, Netlify automatically builds Deploy Previews when you do one of the following: start an agent run” [source](https://docs.netlify.com/deploy/deploy-types/deploy-previews/) |
| **Start from existing data** | Netlify DB branch with copy of production data | “Deploy previews get their own database branch, with a copy of the production data taken when the deploy preview is first created; any changes to the data or the schema made during the lifecycle of the deploy preview will not affect the production database” [source](https://docs.netlify.com/build/data-and-storage/netlify-db/) |
| **Teardown hooks** | 'Deploy deleted' outgoing webhook (manual deletes only) | “Deploy deleted: event emitted when a deploy is manually deleted.” [source](https://docs.netlify.com/deploy/deploy-notifications/) |
| **Multi-repo previews** | Not documented | “When you open a pull / merge request in a connected site repository from GitHub, GitLab, Bitbucket, Azure DevOps, or Cursor Origin, Netlify automatically builds a Deploy Preview for you.” [source](https://docs.netlify.com/deploy/deploy-types/deploy-previews/) |

Caveats:

- Password protection is not available on credit-based Free and Personal plans (https://docs.netlify.com/manage/security/secure-access-to-sites/password-protection/).
- Deploy Previews only build when the PR's base branch is the production branch or has branch deploys enabled (https://docs.netlify.com/deploy/deploy-types/deploy-previews/).
- Netlify Database preview branches start as a snapshot of production data, so production data (incl. PII) is copied into previews (https://docs.netlify.com/build/data-and-storage/netlify-db/).

<a id="vercel"></a>

#### Vercel

Managed frontend cloud that builds an immutable preview deployment, with its own URL, for every push to a non-production branch, every pull request, or every CLI deploy without --prod.

[Preview docs](https://vercel.com/docs/deployments/environments#preview-environment-pre-production) · [Website](https://vercel.com) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Frontend + serverless functions | “When you deploy your application, Vercel automatically sets up the tools and optimizations for your chosen framework. It ensures low latency by routing traffic through Vercel's CDN, and placing your functions in a specific region when you need more control over data locality.” [source](https://vercel.com/docs/functions) |
| **Runs on** | Managed (Vercel cloud) | “Preview environments allow you to deploy and test changes in a live setting, without affecting your production site.” [source](https://vercel.com/docs/deployments/environments) |
| **Git providers** | GitHub, GitLab, Bitbucket, Origin, Azure Pipelines; CLI for others | “Vercel allows for automatic deployments on every branch push and merges onto the production branch of your GitHub, GitLab, Bitbucket, Origin, and Azure DevOps Pipelines projects.” [source](https://vercel.com/docs/git) |
| **Created by** | Any non-production branch push, PR, or CLI deploy | “Push a commit to a branch that is not your production branch (commonly main)...Create a pull request (PR) on GitHub, GitLab, Bitbucket, or Origin” [source](https://vercel.com/docs/deployments/environments) |
| **Databases** | Per-preview Neon branch via Marketplace integration | “Connects your Vercel project to your Neon database to create a database branch for each preview deployment.” [source](https://vercel.com/marketplace/neon) |
| **Automatic cleanup** | Retention policy: previews deleted after 180 days (Pro) / 30 days (Hobby) | “\| Hobby \| 30 days \| 30 days \| 30 days \| 30 days \| ... \| Pro and Enterprise \| 30 days \| 90 days \| 180 days \| 1 year \|” [source](https://vercel.com/docs/deployment-retention) |
| **Access control** | Vercel Authentication (all plans); password (Pro add-on); SSO/IPs (Enterprise) | “Vercel Authentication: Restricts access to only Vercel users with suitable access rights ... Password Protection: ... Available on Pro for $20 per month per protected project ... Trusted IPs: ... Available on the Enterprise plan” [source](https://vercel.com/docs/deployment-protection) |
| **License** | Proprietary | Closed-source commercial managed service; vendor publishes no source code or license for the platform itself (inferred, no explicit license statement fetched). |
| **Pricing** | Unlimited deployments on all plans; Hobby free, Pro $20/mo | “Unlimited Deployments” [source](https://vercel.com/pricing) |
| **Triggers beyond PR/push** | CLI, Deploy Hooks (webhook), REST API | “By default, Vercel creates a preview deployment when you: ... Deploy using the CLI without the `--prod` flag, for example just `vercel`” [source](https://vercel.com/docs/deployments/environments) |
| **Start from existing data** | Neon DB branch per preview (Marketplace) | “Connects your Vercel project to your Neon database to create a database branch for each preview deployment.” [source](https://vercel.com/marketplace/neon) |
| **Teardown hooks** | deployment.cleanup webhook only | “deployment.cleanup ... Occurs whenever a deployment is permanently deleted after the recovery period. ... This webhook does not fire immediately when a deployment is marked for deletion” [source](https://vercel.com/docs/webhooks/webhooks-api) |
| **Multi-repo previews** | not published | Microfrontends combine separate projects by path routing; a single preview built from several repositories is not documented. |

Caveats:

- Previews are protected by 'Standard Protection' scope when enabled; password protection costs $20/month per project on Pro and is unavailable on Hobby (https://vercel.com/docs/deployment-protection).
- Pull requests from forks of public repos require authorization from a team member before deploying (https://vercel.com/docs/git).
- Hobby teams cannot deploy from private repos in GitHub orgs / GitLab groups / Bitbucket workspaces (https://vercel.com/docs/git).
- Neon branching comes from the Neon Marketplace integration, not a built-in Vercel database (https://vercel.com/marketplace/neon).

### Self-hosted PaaS

<a id="coolify"></a>

#### Coolify

Open-source, self-hostable PaaS that can deploy each pull/merge request of an application (including Docker Compose stacks) to its own domain on your servers.

[Preview docs](https://coolify.io/docs/applications/deployments/preview-deployments) · [Website](https://coolify.io) · [Source](https://github.com/coollabsio/coolify) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Application or Docker Compose stack per PR | “A preview deployment runs the code from a pull request or merge request separately from the production application. ... Docker Compose previews can have a separate domain for each service.” [source](https://coolify.io/docs/applications/deployments/preview-deployments) |
| **Runs on** | Self-hosted (free) or Coolify Cloud control plane on your servers | “Just connect your servers, Coolify runs on our managed infrastructure.” [source](https://coolify.io/pricing) |
| **Git providers** | GitHub, GitLab, Bitbucket, Gitea | “GitLab, Gitea, and Bitbucket pull requests from other repositories require public preview deployments to be enabled.” [source](https://coolify.io/docs/applications/deployments/preview-deployments) |
| **Created by** | PR/MR opened or updated via GitHub App or webhook; API | “Choose how Coolify receives pull-request or merge-request events for the application. GitHub App Repository webhook” [source](https://coolify.io/docs/applications/deployments/preview-deployments) |
| **Databases** | None built in; use non-prod external DBs | “Use non-production credentials for preview databases, storage, and external services.” [source](https://coolify.io/docs/applications/deployments/preview-deployments) |
| **Automatic cleanup** | Yes, on PR/MR close or merge | “Coolify deletes an automatically created preview after its pull request or merge request is closed or merged.” [source](https://coolify.io/docs/applications/deployments/preview-deployments) |
| **Access control** | not published | Docs describe who can trigger previews (Repository members only vs Public), not URL protection. |
| **License** | Open source, Apache-2.0 | “Apache-2.0” [source](https://github.com/coollabsio/coolify) |
| **Pricing** | Self-hosted free; Cloud $5/mo (2 servers) | “Self-hosted Free forever ... $5 /month base price (connect 2 servers) + $3 /month per additional server” [source](https://coolify.io/pricing) |
| **Triggers beyond PR/push** | Dashboard 'Deploy preview' / manual preview, REST API, CLI, repo webhook | “In the Pull requests dialog, select Deploy preview beside each request that needs a preview. ... For a Docker Image application, open Preview Deployments and use Manual preview. ... Creating or redeploying a preview requires deploy:” [source](https://coolify.io/docs/applications/deployments/preview-deployments) |
| **Start from existing data** | Not documented | “Use non-production credentials for preview databases, storage, and external services.” [source](https://coolify.io/docs/applications/deployments/preview-deployments) |
| **Teardown hooks** | Not documented | “A preview container is temporary, but data written to an external service can remain after Coolify deletes the preview. ... Closing or deleting a preview removes only its own containers and Coolify-created networks and volumes.” [source](https://coolify.io/docs/applications/deployments/preview-deployments) |
| **Multi-repo previews** | Previews are per application (one repo) | “A preview deployment runs the code from a pull request or merge request separately from the production application.” [source](https://coolify.io/docs/applications/deployments/preview-deployments) |

Caveats:

- Fork PRs are blocked by default ('Repository members only'); docs warn a PR can run code on the deployment server (https://coolify.io/docs/applications/deployments/preview-deployments).
- PRs open before previews were enabled are not auto-deployed (same page).
- GitHub API (2026-10-23): ~63.5k stars, active.

<a id="dokploy"></a>

#### Dokploy

Self-hostable PaaS whose GitHub-integrated applications can automatically get a preview deployment per pull request on a generated domain.

[Preview docs](https://docs.dokploy.com/docs/core/applications/preview-deployments) · [Website](https://dokploy.com) · [Source](https://github.com/Dokploy/dokploy) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Single application per PR | “Preview deployments allow you to test and review your application changes in an isolated environment before merging to production.” [source](https://docs.dokploy.com/docs/core/applications/preview-deployments) |
| **Runs on** | Self-hosted, or Dokploy Cloud managing your servers | “Self Hosted Install on-prem or in your own cloud” [source](https://dokploy.com/pricing) |
| **Git providers** | GitHub only | “Preview deployments are a powerful feature specifically designed for applications with GitHub integration.” [source](https://docs.dokploy.com/docs/core/applications/preview-deployments) |
| **Created by** | PR opened against target branch; optional label filter | “preview deployments are automatically created whenever a pull request is opened against your target branch” [source](https://docs.dokploy.com/docs/core/applications/preview-deployments) |
| **Databases** | not published | Docs do not describe per-preview databases. |
| **Automatic cleanup** | Yes, on PR close/merge | “Clean up when the pull request is closed or merged” [source](https://docs.dokploy.com/docs/core/applications/preview-deployments) |
| **Access control** | Inherits app's security/redirect config; traefik.me URL | “If you have security or redirects created in your application, it will inherit the same configuration for the preview deployment.” [source](https://docs.dokploy.com/docs/core/applications/preview-deployments) |
| **License** | Open-core: Apache-2.0 plus proprietary directory | “All content that resides under a "/proprietary" directory of this repository, if that directory exists, is licensed under the license defined in "LICENSE_PROPRIETARY". * Content outside of the above mentioned directories ... is available under the "Apache License 2.0"” [source](https://github.com/Dokploy/dokploy/blob/canary/LICENSE.MD) |
| **Pricing** | Self-hosted free; Cloud from $4.50/mo per server | “Hobby Everything an individual developer needs $ 4.50 /mo per server” [source](https://dokploy.com/pricing) |
| **Triggers beyond PR/push** | PR label opt-in | “If you only want pull requests with a specific label to create preview deployments, you can specify one or multiple in the preview settings.” [source](https://docs.dokploy.com/docs/core/applications/preview-deployments) |
| **Start from existing data** | Not documented | “Preview deployments are a powerful feature specifically designed for applications with GitHub integration.” [source](https://docs.dokploy.com/docs/core/applications/preview-deployments) |
| **Teardown hooks** | Not documented | “Clean up when the pull request is closed or merged” [source](https://docs.dokploy.com/docs/core/applications/preview-deployments) |
| **Multi-repo previews** | Previews are per application (one repo) | “Preview deployments are a powerful feature specifically designed for applications with GitHub integration.” [source](https://docs.dokploy.com/docs/core/applications/preview-deployments) |

Caveats:

- Disabled by default; docs recommend not using previews on public repos because outsiders can run builds on your server (https://docs.dokploy.com/docs/core/applications/preview-deployments).
- Default limit of 3 previews per application (same page).
- GitHub API reports license NOASSERTION; LICENSE.MD is Apache-2.0 with a proprietary-directory carve-out. ~38k stars, active.

### Open-source tools

<a id="argo-cd-pr-generator"></a>

#### Argo CD ApplicationSet Pull Request generator

Argo CD ApplicationSet generator that polls (or takes webhooks from) a Git host for open pull requests and templates one Argo CD Application per matching PR on your Kubernetes cluster.

[Preview docs](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/) · [Website](https://argo-cd.readthedocs.io) · [Source](https://github.com/argoproj/argo-cd) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Any Kubernetes manifests/Helm/Kustomize per PR | “This fits well with the style of building a test environment when you create a pull request.” [source](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/) |
| **Runs on** | Self-hosted on your Kubernetes cluster | “Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes.” [source](https://argo-cd.readthedocs.io/en/stable/) |
| **Git providers** | GitHub, GitLab, Gitea, Bitbucket Server/Cloud, Azure DevOps | “Specify the organization, project and repository from which you want to fetch pull requests.” [source](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/) |
| **Created by** | Open PR matching filters (labels, state); polling or webhook | “An Application will be generated when a Pull Request is discovered when the configured criteria is met - i.e. for GitHub when a Pull Request matches the specified `labels` and/or `pullRequestState`.” [source](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/) |
| **Databases** | not published | No database provisioning; anything beyond what the templated manifests define is up to you. |
| **Automatic cleanup** | Yes, Application removed when PR no longer matches | “Application will be removed when a Pull Request no longer meets the specified criteria.” [source](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/) |
| **Access control** | not published | Not handled by the generator. Ingress and auth come from your own manifests. |
| **License** | Open source, Apache-2.0 | “Apache License Version 2.0, January 2004” [source](https://github.com/argoproj/argo-cd/blob/master/LICENSE) |
| **Pricing** | Free (open source); you run the cluster | “Apache License Version 2.0, January 2004” [source](https://github.com/argoproj/argo-cd/blob/master/LICENSE) |

Caveats:

- The generator only creates Argo CD Applications. Building images, DNS/ingress and secrets are up to you. Polling defaults to every 30 minutes unless you configure the ApplicationSet webhook (https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/).

<a id="digitalocean-app-platform"></a>

#### DigitalOcean App Platform PR previews (app_action)

DigitalOcean's official GitHub Action can deploy an App Platform app per pull request in 'PR preview' mode and delete it when the PR closes; there is no built-in dashboard preview toggle documented.

[Preview docs](https://github.com/digitalocean/app_action#launch-a-preview-app-per-pull-request) · [Website](https://www.digitalocean.com/products/app-platform) · [Source](https://github.com/digitalocean/app_action) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | App Platform app from app spec (services etc.) | “deploy_pr_preview: Deploy the app as a PR preview. The app name will be derived from the PR, the app spec will be modified to exclude conflicting configuration like domains and alerts” [source](https://github.com/digitalocean/app_action) |
| **Runs on** | Managed (DigitalOcean); action runs in GitHub Actions | “Deploy a DigitalOcean App Platform app using GitHub Actions.” [source](https://github.com/digitalocean/app_action) |
| **Git providers** | GitHub (GitHub Actions) | “all Github references to the current repository will be updated to point to the PR's branch.” [source](https://github.com/digitalocean/app_action) |
| **Created by** | GitHub Actions pull_request workflow | “The following 2 actions implement a "Preview Apps" feature, that provide a per-PR app to check if the deployment would work.” [source](https://github.com/digitalocean/app_action) |
| **Databases** | not published | README does not describe database handling for preview apps. |
| **Automatic cleanup** | Yes, via delete action on PR close/merge | “Once the PR is closed or merged, the respective app is deleted again.” [source](https://github.com/digitalocean/app_action) |
| **Access control** | Public live URL posted as PR comment | “If the deployment succeeds, a comment is posted with the live URL of the app.” [source](https://github.com/digitalocean/app_action) |
| **License** | Open source, MIT (the Action) | “MIT License” [source](https://github.com/digitalocean/app_action/blob/main/LICENSE) |
| **Pricing** | Billed as normal App Platform apps; from $5/month | “Start for as little as $ 5 /month” [source](https://www.digitalocean.com/products/app-platform) |

Caveats:

- DigitalOcean's product page advertises 'automatic preview environments for every pull request' via CI-driven workflows like GitHub Actions (https://www.digitalocean.com/products/app-platform); the documented mechanism is the app_action GitHub Action.
- GitHub API (2026-10-23): ~157 stars, not archived, last push 2026-04-13.

<a id="flux-operator-resourceset"></a>

#### Flux Operator ResourceSets

The Flux Operator (by ControlPlane) uses a ResourceSetInputProvider to discover open PRs/MRs and a ResourceSet to template Flux resources (e.g. a Helm release) per PR on your cluster.

[Preview docs](https://fluxoperator.dev/docs/resourcesets/github-pull-requests/) · [Website](https://fluxoperator.dev) · [Source](https://github.com/controlplaneio-fluxcd/flux-operator) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Any Flux-managed Kubernetes resources (e.g. Helm release) per PR | “Flux Operator installs a Helm release using the PR number and the commit SHA inputs to deploy the app and chart changes in the cluster.” [source](https://fluxoperator.dev/docs/resourcesets/github-pull-requests/) |
| **Runs on** | Self-hosted on your Kubernetes cluster | “The Flux Operator is a Kubernetes CRD controller that manages the lifecycle of CNCF Flux CD” [source](https://github.com/controlplaneio-fluxcd/flux-operator) |
| **Git providers** | GitHub, GitLab, Gitea/Forgejo, Azure DevOps | “GitHub Pull Requests, GitLab Merge Requests, Azure DevOps Pull Requests, and Gitea/Forgejo Pull Requests.” [source](https://fluxoperator.dev/docs/crd/resourcesetinputprovider/) |
| **Created by** | PR label filter; polling or webhook Receiver | “Another developer reviews the changes and labels the Pull Request with the `deploy/flux-preview` label.” [source](https://fluxoperator.dev/docs/resourcesets/github-pull-requests/) |
| **Databases** | not published | No database provisioning documented; databases must be in the templated resources. |
| **Automatic cleanup** | Yes, Helm release uninstalled after merge | “Once the PR is approved and merged, the Flux Operator uninstalls the Helm release from the cluster.” [source](https://fluxoperator.dev/docs/resourcesets/github-pull-requests/) |
| **Access control** | not published | Not handled by the operator. Exposure and auth depend on your ingress configuration. |
| **License** | Open source, AGPL-3.0 | “GNU AFFERO GENERAL PUBLIC LICENSE Version 3, 19 November 2007” [source](https://github.com/controlplaneio-fluxcd/flux-operator/blob/main/LICENSE) |
| **Pricing** | Free (open source); you run the cluster | “GNU AFFERO GENERAL PUBLIC LICENSE Version 3, 19 November 2007” [source](https://github.com/controlplaneio-fluxcd/flux-operator/blob/main/LICENSE) |

Caveats:

- This is the Flux Operator (controlplaneio-fluxcd), not core Flux CD. It's licensed AGPL-3.0, unlike Flux itself, which is Apache-2.0.
- A GitLab MR guide also exists: https://fluxoperator.dev/docs/resourcesets/gitlab-merge-requests/

<a id="fly-pr-review-apps"></a>

#### Fly.io PR Review Apps (superfly/fly-pr-review-apps)

Official Fly.io GitHub Action (superfly org) that wraps flyctl to create, deploy and destroy a Fly app per pull request; documented in Fly's own docs.

[Preview docs](https://fly.io/docs/blueprints/review-apps-guide/) · [Website](https://fly.io) · [Source](https://github.com/superfly/fly-pr-review-apps) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Single Fly app by default; extra apps/DB attach via workflow | “The workflow described above will spin up a single application without other resources; if data stores, multiple Fly Apps, or other resources are required, see Customizing your workflow .” [source](https://fly.io/docs/blueprints/review-apps-guide/) |
| **Runs on** | Managed (Fly.io); action runs in GitHub Actions | “This GitHub action wraps the Fly.io CLI to automatically deploy pull requests to fly.io for review.” [source](https://github.com/superfly/fly-pr-review-apps) |
| **Git providers** | GitHub (GitHub Actions) | “This guide will teach you how to automatically generate ephemeral “review apps” on Fly.io for each pull request (PR) using GitHub Actions.” [source](https://fly.io/docs/blueprints/review-apps-guide/) |
| **Created by** | GitHub Actions on pull_request events | “Run this workflow on every PR event. Existing review apps will be updated when the PR is updated. pull_request : types : [ opened , reopened , synchronize , closed ]” [source](https://fly.io/docs/blueprints/review-apps-guide/) |
| **Databases** | Optional: new DB in an existing Fly Postgres cluster | “you can attach it using the postgres action input. flyctl postgres attach will be used, which automatically creates a new database in the cluster named after the Fly app and sets DATABASE_URL.” [source](https://github.com/superfly/fly-pr-review-apps) |
| **Automatic cleanup** | Yes, app destroyed on PR close event | “This action will create, deploy, and destroy Fly apps.” [source](https://github.com/superfly/fly-pr-review-apps) |
| **Access control** | Public *.fly.dev URL | “By default, review apps will be available at `https://pr-<PR number>-<repository owner>-<repository name>.fly.dev` .” [source](https://fly.io/docs/blueprints/review-apps-guide/) |
| **License** | Open source, Apache-2.0 | “Apache License Version 2.0, January 2004” [source](https://github.com/superfly/fly-pr-review-apps/blob/main/LICENSE) |
| **Pricing** | Billed as normal Fly Machines usage | “Started Machine, shared-cpu-1x with 256MB RAM $2.19/month Smallest Machine size.” [source](https://fly.io/docs/about/pricing/) |

Caveats:

- Maintained in the official superfly org; GitHub API (2026-10-23): ~205 stars, not archived, last push 2026-02-27, latest release 1.6.0 (2026-02-27). Fly docs guide still pins older @1.2.1.
- Requires FLY_API_TOKEN secret; org accounts need an org token (https://github.com/superfly/fly-pr-review-apps).
- Fly guide notes the approach can be adapted to other Git services, but the action itself is GitHub Actions only (https://fly.io/docs/blueprints/review-apps-guide/).

<a id="garden"></a>

#### Garden

Open-source DevOps automation CLI that re-uses Dockerfiles, manifests and Helm charts to deploy isolated environments into namespaces on a remote Kubernetes cluster, typically run from CI per pull request.

[Preview docs](https://docs.garden.io/overview/use-cases/on-demand-preview-envs) · [Website](https://garden.io) · [Source](https://github.com/garden-io/garden) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Full-stack K8s apps (Dockerfiles, manifests, Helm) | “Garden lets them re-use these resources to create isolated preview environments on-demand” [source](https://docs.garden.io/overview/use-cases/on-demand-preview-envs) |
| **Runs on** | Self-hosted (your Kubernetes cluster); optional Garden Cloud | “Developers run the `garden deploy` command from their laptops to create a preview environment in their own namespace in the team's remote Kubernetes cluster.” [source](https://docs.garden.io/overview/use-cases/on-demand-preview-envs) |
| **Isolation** | Namespace per environment (templated per user/PR) | “Garden's powerful templating engine ensures that namespaces and hostnames are unique across users and CI runs” [source](https://docs.garden.io/overview/use-cases/on-demand-preview-envs) |
| **Git providers** | Any (driven from your CI pipeline) | “Garden can be run from CI pipelines to create isolated preview environments with each pull request, using e.g. the pull request number to isolate the environment.” [source](https://docs.garden.io/overview/use-cases/on-demand-preview-envs) |
| **Created by** | CI job or CLI (garden deploy) | “For example, you may have a CI job that runs `garden deploy --env preview`.” [source](https://docs.garden.io/overview/use-cases/on-demand-preview-envs) |
| **Databases** | not published | Preview docs do not describe per-preview database provisioning or cloning. |
| **Automatic cleanup** | Beta: inactivity pause/cleanup agent (paid Garden Cloud) | “The Automatic Environment Cleanup (AEC) feature allows you to automatically clean up or pause environments in your Kubernetes cluster after a period of inactivity or on a scheduled basis.” [source](https://docs.garden.io/using-garden-with/kubernetes/automatic-environment-cleanup) |
| **Access control** | not published | Preview docs do not describe URL protection; depends on your cluster ingress. |
| **License** | Open source, MPL-2.0 | “Mozilla Public License Version 2.0” [source](https://github.com/garden-io/garden/blob/main/LICENSE.md) |
| **Pricing** | not published | No pricing page found (garden.io redirects to docs.garden.io); CLI is free/open source, AEC needs a paid Garden Cloud subscription. |

Caveats:

- garden.io now redirects to docs.garden.io; releases continue (0.13.65 published 2026-08-24 per GitHub releases).
- A tool rather than a platform: you supply the cluster, CI wiring and ingress.

<a id="laravel-harbor"></a>

#### Laravel Harbor

CLI run from GitHub Actions that provisions a per-PR site, database and workers on a Laravel Forge server and tears it down when the PR is merged or closed.

[Preview docs](https://laravel-harbor.com/docs/introduction/) · [Website](https://laravel-harbor.com) · [Source](https://github.com/mehrancodes/laravel-harbor) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Laravel app site + database on a Forge server | “Harbor seamlessly leverages GitHub Actions to provision a dedicated site on the Laravel Forge server.” [source](https://laravel-harbor.com/docs/introduction/) |
| **Runs on** | Your own Laravel Forge-managed server | “Harbor seamlessly leverages GitHub Actions to provision a dedicated site on the Laravel Forge server.” [source](https://laravel-harbor.com/docs/introduction/) |
| **Git providers** | GitHub, GitLab (incl. self-hosted), custom; Bitbucket not yet | “Bitbucket bitbucket not supported yet” [source](https://laravel-harbor.com/docs/features/git-providers/) |
| **Created by** | GitHub Actions on pull request | “Harbor seamlessly leverages GitHub Actions to provision a dedicated site on the Laravel Forge server.” [source](https://laravel-harbor.com/docs/introduction/) |
| **Databases** | Yes, per-preview database created (optional) | “server:create-databases FORGE_DB_CREATION_REQUIRED” [source](https://laravel-harbor.com/docs/configuration/) |
| **Automatic cleanup** | Yes, teardown workflow on PR merge/close | “Running the harbor teardown removes the previously created task scheduler, database, database user, and finally, the site for the related site on Forge.” [source](https://laravel-harbor.com/docs/teardown/) |
| **Access control** | not published | Not documented. |
| **License** | Open source, MIT | “MIT License” [source](https://github.com/mehrancodes/laravel-harbor/blob/main/LICENSE) |
| **Pricing** | not published | Pricing isn't documented. The tool is MIT; it needs a Laravel Forge account and servers, which are billed by Forge and your host. |

Caveats:

- Laravel/PHP-specific and needs Laravel Forge.

<a id="pr-preview-action"></a>

#### pr-preview-action

GitHub Action that deploys a built static site for each PR into a subdirectory of the repository's GitHub Pages branch and removes it when the PR closes.

[Preview docs](https://github.com/rossjrw/pr-preview-action) · [Website](https://github.com/rossjrw/pr-preview-action) · [Source](https://github.com/rossjrw/pr-preview-action) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Static frontend only (GitHub Pages) | “GitHub Action that deploys previews of pull requests to GitHub Pages. Works on any repository with a GitHub Pages site.” [source](https://github.com/rossjrw/pr-preview-action) |
| **Runs on** | Managed (GitHub Pages) | “Creates and deploys previews of pull requests to your GitHub Pages site” [source](https://github.com/rossjrw/pr-preview-action) |
| **Git providers** | GitHub only; no fork PRs | “This Action does not currently support deploying previews for PRs from forks” [source](https://github.com/rossjrw/pr-preview-action) |
| **Created by** | pull_request opened/reopened/synchronize | “it will deploy the preview when the event type is `opened`, `reopened` and `synchronize`, and remove it on `closed` events.” [source](https://github.com/rossjrw/pr-preview-action) |
| **Databases** | None (static sites) | “GitHub Action that deploys previews of pull requests to GitHub Pages.” [source](https://github.com/rossjrw/pr-preview-action) |
| **Automatic cleanup** | Yes, on PR close | “Cleans up after itself &mdash; removes deployed previews when the pull request is closed” [source](https://github.com/rossjrw/pr-preview-action) |
| **Access control** | not published | Not documented in the README. Previews are served from the repository's GitHub Pages site. |
| **License** | Open source, MIT | “MIT License” [source](https://github.com/rossjrw/pr-preview-action/blob/main/LICENSE) |
| **Pricing** | not published | Pricing isn't documented in the README. The Action is MIT; GitHub Pages/Actions pricing applies. |

Caveats:

- The README quote contains an HTML entity (&mdash;) as written in the source markdown.

<a id="pullpreview"></a>

#### PullPreview

GitHub Action that provisions a VM in your own AWS Lightsail or Hetzner account per labelled PR and deploys the app with Docker Compose or Helm.

[Preview docs](https://github.com/pullpreview/action) · [Website](https://pullpreview.com) · [Source](https://github.com/pullpreview/action) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Full-stack Docker Compose apps; Helm charts | “It can work with any application that has a valid Docker Compose file. Also supports Helm charts.” [source](https://github.com/pullpreview/action) |
| **Runs on** | BYOC: AWS Lightsail or Hetzner | “PullPreview supports Lightsail and Hetzner while keeping your code and infrastructure under your control.” [source](https://github.com/pullpreview/action) |
| **Git providers** | GitHub only | “A GitHub Action for running live preview environments for pull requests in your own cloud account.” [source](https://github.com/pullpreview/action) |
| **Created by** | Adding a label to a PR | “Adding the label triggers the deployment.” [source](https://github.com/pullpreview/action) |
| **Databases** | not published | No per-preview database feature documented; databases run as Compose services on the preview VM. |
| **Automatic cleanup** | On label removal; optional TTL | “When the label is removed, the preview environment is automatically destroyed.” [source](https://github.com/pullpreview/action) |
| **Access control** | Optional IP/CIDR allowlist; HTTPS via Let's Encrypt | “The IP address, or range of IP addresses in CIDR notation, that are allowed to connect to the instance” [source](https://github.com/pullpreview/action/blob/master/action.yml) |
| **License** | Source-available (Prosperity Public License 3.0.0) | “This license allows you to use and share this software for noncommercial purposes for free and to try this software for commercial purposes for thirty days.” [source](https://github.com/pullpreview/action/blob/master/LICENSE) |
| **Pricing** | 300€/year per org for commercial use, plus your cloud costs | “300€ / year, per organization” [source](https://pullpreview.com/) |

Caveats:

- The license is not OSI open source. It's the Prosperity Public License 3.0.0, and commercial use needs a paid license (https://pullpreview.com/). The GitHub API reports the license as NOASSERTION.

<a id="vcluster"></a>

#### vCluster

Virtual Kubernetes clusters (tenant clusters) running on a host cluster. The docs show GitHub Actions workflows that create one virtual cluster per PR and delete it on close.

[Preview docs](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments) · [Website](https://www.vcluster.com) · [Source](https://github.com/loft-sh/vcluster) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Isolated virtual Kubernetes cluster per PR | “On every pull request, this workflow creates a tenant cluster, installs Argo CD, and exposes it through an ingress.” [source](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments) |
| **Runs on** | Self-hosted on your Kubernetes cluster | “Each gets its own API server, CRDs and RBAC, and runs on an existing cluster or standalone on bare metal.” [source](https://github.com/loft-sh/vcluster) |
| **Git providers** | GitHub Actions guide documented | “This guide shows how to use vCluster and GitHub Actions to deploy preview environments on every pull request.” [source](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments) |
| **Created by** | GitHub Actions on pull request | “On every pull request, this workflow creates a tenant cluster, installs Argo CD, and exposes it through an ingress.” [source](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments) |
| **Databases** | not published | No per-preview database feature documented. |
| **Automatic cleanup** | Yes, via a destroy workflow on PR close/merge | “Create a separate workflow that deletes the tenant cluster as soon as the pull request is closed or merged” [source](https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments) |
| **Access control** | not published | Not documented for previews. Exposure is through your ingress. |
| **License** | Open source, Apache-2.0 (Platform is commercial) | “vCluster is licensed under the Apache 2.0 License.” [source](https://github.com/loft-sh/vcluster) |
| **Pricing** | OSS free; Platform has Free and Enterprise tiers | “An actually useful free plan for additional features beyond the open source” [source](https://www.vcluster.com/pricing) |

Caveats:

- The official preview-environments guide logs into vCluster Platform (PLATFORM_URL/ACCESS_KEY) and relies on Platform sleep mode: "It uses the sleep mode feature of vCluster Platform so that idle environments consume no resources." (https://www.vcluster.com/docs/vcluster/third-party-integrations/github-actions/preview-environments). Pure OSS use means scripting the `vcluster` CLI yourself.
- It's a building block (cluster isolation), not a preview-environment product.

### CI/CD-native features

<a id="azure-pipelines-review-app"></a>

#### Azure Pipelines Review App (Kubernetes environments)

Azure Pipelines can deploy each pull request into a dynamically created Kubernetes namespace resource in an environment and comment the review app link on GitHub.

[Preview docs](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/environments-kubernetes) · [Website](https://azure.microsoft.com/products/devops/pipelines) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Kubernetes manifests deployed to a per-PR namespace | “The review app deploys every pull request from your Git repository to a dynamic Kubernetes resource in the environment, and posts a GitHub comment linking to the review app.” [source](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/environments-kubernetes) |
| **Runs on** | Your Kubernetes cluster (AKS or other) | “You can connect to public or private Kubernetes clusters in Azure Kubernetes Service (AKS) or other cloud providers.” [source](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/environments-kubernetes) |
| **Git providers** | PRs from your Git repo; GitHub comment documented | “The review app deploys every pull request from your Git repository to a dynamic Kubernetes resource in the environment, and posts a GitHub comment linking to the review app.” [source](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/environments-kubernetes) |
| **Created by** | Pipeline run on PR create/update | “The second job runs when a PR is created or updated to the `main` branch, and deploys against a dynamic review app resource it creates in the cluster on demand.” [source](https://learn.microsoft.com/en-us/azure/devops/pipelines/process/environments-kubernetes) |
| **Databases** | not published | Not documented. |
| **Automatic cleanup** | not published | No automatic namespace cleanup is documented on this page. |
| **Access control** | not published | Not documented. The example exposes a LoadBalancer IP. |
| **License** | Proprietary | Closed-source commercial service; no open-source license is published (inferred). |
| **Pricing** | Billed as Azure Pipelines parallel jobs; free tier | “1 free parallel job with 1,800 minutes” [source](https://azure.microsoft.com/en-us/pricing/details/devops/azure-devops-services/) |

Caveats:

- Set up through the 'Deploy to Azure Kubernetes Services' template's 'Enable Review App flow for Pull Requests' option (https://learn.microsoft.com/en-us/azure/devops/pipelines/process/environments-kubernetes).

<a id="github-actions-environments"></a>

#### GitHub Actions deployment environments

GitHub's environments track deployments and gate jobs with protection rules. They're a building block for PR previews, but don't provision or host anything.

[Preview docs](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments) · [Website](https://github.com) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | None itself; tracks deployments your workflow performs | “Environments are used to describe a general deployment target like `production`, `staging`, or `development`.” [source](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments) |
| **Runs on** | not published | No hosting. You deploy to your own infrastructure or a third-party platform from the workflow. |
| **Git providers** | GitHub only | “When a workflow references an environment, the environment will appear in the repository's deployments.” [source](https://docs.github.com/en/actions/concepts/workflows-and-actions/deployment-environments) |
| **Created by** | Workflow referencing an environment (auto-created) | “Running a workflow that references an environment that does not exist will create an environment with the referenced name.” [source](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) |
| **Databases** | not published | Not applicable. No provisioning. |
| **Automatic cleanup** | not published | No automatic per-PR environment deletion documented. You can delete environments manually or via the API. |
| **Access control** | not published | Protection rules gate deployments, not preview URL access. |
| **License** | Proprietary | “Users with GitHub Free plans can only configure environments for public repositories.” [source](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) |
| **Pricing** | Free plans: public repos only; Pro/Team for private | “Organizations with GitHub Team and users with GitHub Pro can configure environments for private repositories.” [source](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) |

Caveats:

- This isn't a preview-environment system. Teams combine it with a hosting target and their own create/teardown jobs.

<a id="gitlab-review-apps"></a>

#### GitLab Review Apps

GitLab CI/CD feature built on dynamic environments: a pipeline job deploys each branch/MR to infrastructure you supply, and GitLab tracks the environment, links it in the MR and runs stop jobs.

[Preview docs](https://docs.gitlab.com/ci/review_apps/) · [Website](https://about.gitlab.com) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **What a preview includes** | Whatever your CI deploy job deploys | “You must set up the infrastructure to host and deploy the review apps.” [source](https://docs.gitlab.com/ci/review_apps/) |
| **Runs on** | Your own infrastructure (Kubernetes via Auto DevOps optional) | “If you have a Kubernetes cluster, you can set up review apps automatically using Auto DevOps.” [source](https://docs.gitlab.com/ci/review_apps/) |
| **Git providers** | GitLab only | “Review apps are temporary testing environments that are created automatically for each branch or merge request.” [source](https://docs.gitlab.com/ci/review_apps/) |
| **Created by** | CI pipeline per branch or merge request | “Built on dynamic environments, review apps provide a unique environment for each branch or merge request.” [source](https://docs.gitlab.com/ci/review_apps/) |
| **Databases** | not published | No built-in per-review-app database. Your deploy scripts would have to provision one. |
| **Automatic cleanup** | Yes, stop job on MR merge/close; auto_stop_in TTL | “After the time period passes, GitLab automatically starts a job to stop the environment.” [source](https://docs.gitlab.com/ci/environments/) |
| **Access control** | not published | No built-in URL protection documented for review apps. It depends on your hosting. |
| **License** | Open core (MIT core, proprietary ee/) | “All content that resides under the "ee/" directory of this repository, if that directory exists, is licensed under the license defined in "ee/LICENSE".” [source](https://gitlab.com/gitlab-org/gitlab/-/raw/master/LICENSE) |
| **Pricing** | Available on Free, Premium, Ultimate tiers | “Tier: Free, Premium, Ultimate” [source](https://docs.gitlab.com/ci/review_apps/) |

Caveats:

- GitLab orchestrates; it doesn't host. You write the deploy and stop jobs yourself (https://docs.gitlab.com/ci/review_apps/).
<!-- END GENERATED: platform-details -->

## Excluded

Products we checked that aren't listed, and why. If one of these is wrong, please [open a PR](../CONTRIBUTING.md) with a source.

<!-- BEGIN GENERATED: excluded -->
| Product | Why it isn't listed |  |
| --- | --- | --- |
| CapRover | No preview/PR deployment feature found in official docs (CI/CD integration and getting-started pages have no mention of previews or pull requests). | [source](https://caprover.com/docs/ci-cd-integration.html) |
| Kargo | Skipped. It's a promotion/release orchestration tool, not a per-PR preview tool. | [source](https://github.com/akuity/kargo) |
| MongoDB Atlas | No documented database branching / per-PR preview feature found; skipped per scope. | [source](https://www.mongodb.com/docs/atlas/) |
| Preevy | Inactive: no commits to the default branch since the v0.0.67 release on 2025-06-30, and its maintainer Livecycle now redirects to an unrelated AI product. | [source](https://github.com/livecycle/preevy) |
| Tilt | No official preview-environment feature; only a 2022 blog experiment that says Tilt had no plans to build a hosted preview service. | [source](https://blog.tilt.dev/2022/02/17/preview-environments.html) |
| Tonic Ephemeral | No longer present in Tonic docs (docs.tonic.ai/ephemeral 404, not in sitemap) and product URL redirects to homepage; appears discontinued (not confirmed by an announcement). | [source](https://docs.tonic.ai/sitemap.md) |
| Uffizzi | Appears inactive: last commit to the main repo Aug 7, 2024 (v2.4.10); uffizzi.com failed TLS handshake and app.uffizzi.com did not resolve when checked 2026-10-23. No official shutdown notice found; docs.uffizzi.com still online. | [source](https://github.com/UffizziCloud/uffizzi) |
<!-- END GENERATED: excluded -->
