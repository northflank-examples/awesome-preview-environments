# How to set up preview environments for every pull request

This guide takes you from no previews to a preview for every pull request, in five decisions.

## 1. Decide what a preview must contain

| Your app | A preview needs | Easiest path |
| --- | --- | --- |
| Static site or SPA calling an existing API | Frontend build only | A frontend host with built-in previews |
| Frontend + serverless functions | Frontend + functions, maybe a database branch | Frontend host + [database branching](database-preview-environments.md) |
| Backend services, workers, databases | Every service, plus data | A full-stack preview platform, or DIY on Kubernetes |
| Many microservices | Only the changed services, plus a shared baseline | Request-routing tools, or namespaces with shared dependencies ([Kubernetes guide](kubernetes-preview-environments.md)) |

## 2. Decide where previews run

- **Vendor cloud:** fastest to set up.
- **Your cloud account (BYOC) or your cluster:** needed for data residency, VPC-only dependencies or existing cloud discounts.
- **Self-hosted:** you run the platform as well.

The [platform comparison](../comparisons/preview-environment-platform-comparison.md) shows the hosting model for each tool. [Open source vs managed](../comparisons/open-source-vs-managed-preview-environments.md) covers the trade-offs.

> **On Northflank:** a [preview blueprint](../examples/northflank-preview-blueprint/) covers steps 3 to 5 in one place. It creates, updates and deletes previews from Git triggers, provisions or forks a database per preview, scopes secrets to the preview, and expires forgotten previews. It runs on Northflank's cloud or in your own cloud account. *(Disclosure: Northflank maintains this list.)*

## 3. Wire up the lifecycle

Whatever tool you choose, check that it does all four:

1. **Create** on PR open, or on a label.
2. **Update** on every push.
3. **Announce** the URL on the PR.
4. **Destroy** on merge or close, with a TTL as a backstop.

On a platform, these are settings. In CI, see [GitHub Actions](github-actions-preview-environments.md) or [GitLab CI](gitlab-review-apps.md).

## 4. Handle data and secrets

- Choose a database strategy: shared, seeded, snapshot or branch. See [database preview environments](database-preview-environments.md).
- Give previews their own credentials, protect the URLs, and be careful with fork PRs. See [security and secrets](preview-environment-security.md).

## 5. Put limits in place before costs grow

Small sizes, TTLs, scale-to-zero, and a cap on concurrent previews. See [cost optimization](reduce-preview-environment-costs.md).

When previews fail, check [preview environment troubleshooting: common failures and fixes](https://northflank.com/blog/preview-environment-troubleshooting) (Northflank).

## Smallest working setups

| If you use | Start with |
| --- | --- |
| A frontend host (Vercel, Netlify, Cloudflare, Amplify...) | Connect the repo; previews are usually on by default |
| A full-stack platform with previews (Northflank, Render, Heroku, Railway...) | Enable previews and define what each preview contains. On Northflank, that's a [preview blueprint](../examples/northflank-preview-blueprint/) |
| Kubernetes + GitHub Actions | [`examples/kubernetes-namespace-per-pr`](../examples/kubernetes-namespace-per-pr/) |
| Kubernetes + Argo CD | [`examples/argocd-applicationset`](../examples/argocd-applicationset/) |
| GitLab | [`examples/gitlab-review-apps`](../examples/gitlab-review-apps/) |
| A Postgres database branch per PR | [`examples/neon-branch-per-pr`](../examples/neon-branch-per-pr/) |
