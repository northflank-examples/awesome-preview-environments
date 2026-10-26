# Kubernetes preview environments with GitHub Actions (namespace per PR)

A complete, copy-paste starting point. Every pull request gets its own Kubernetes namespace (`pr-<number>`) with your app, a throwaway Postgres database and a URL such as `https://pr-42.preview.example.com`. The namespace is deleted when the PR is closed or merged.

```
PR opened / pushed ──► build image ──► helm upgrade --install into ns pr-42 ──► comment URL on PR
PR closed / merged ──► kubectl delete namespace pr-42
```

| File | What it does |
| --- | --- |
| [`.github/workflows/preview.yml`](.github/workflows/preview.yml) | Builds and pushes the image to GHCR, deploys the chart, comments the URL, tears down on close |
| [`chart/templates/app.yaml`](chart/templates/app.yaml) | Your app: Deployment, Service, Ingress, plus an optional migration init container |
| [`chart/templates/postgres.yaml`](chart/templates/postgres.yaml) | Per-preview Postgres with a generated password, exposed to the app as `DATABASE_URL` |
| [`chart/templates/guardrails.yaml`](chart/templates/guardrails.yaml) | `ResourceQuota` so one PR can't eat the cluster, and a `NetworkPolicy` so previews can't reach each other |

## Prerequisites

- A Kubernetes cluster with an ingress controller (the example assumes [ingress-nginx](https://kubernetes.github.io/ingress-nginx/) in namespace `ingress-nginx`).
- A wildcard DNS record, such as `*.preview.example.com`, pointing at the ingress controller's load balancer.
- Optional: a wildcard TLS certificate. With [cert-manager](https://cert-manager.io/docs/configuration/acme/dns01/), wildcard certificates need a DNS-01 solver. Copy the certificate secret into each namespace, or use a tool like [reflector](https://github.com/emberstack/kubernetes-reflector), then set `ingress.tlsSecretName`.
- A `Dockerfile` at the repository root for an app that listens on `$PORT` (default 8080) and reads `DATABASE_URL`.

## Set up

1. Copy `.github/workflows/preview.yml` and `chart/` into your repository.
2. Create a service account that can create namespaces and deploy into them. Add its kubeconfig as the repository secret `KUBE_CONFIG`. Scope it to this job only; don't reuse a cluster-admin config.
3. Add the repository variable `PREVIEW_DOMAIN`, for example `preview.example.com`.
4. If your app runs migrations, set `app.migrateCommand` in `chart/values.yaml`, for example `["npm", "run", "db:migrate"]`.
5. Open a pull request.

## Design choices and trade-offs

- **Namespace per PR.** This is the simplest isolation that works on any cluster. Teardown is a single `kubectl delete namespace`, which also cleans up anything the chart forgot. Previews share the cluster's nodes, CRDs and control plane. If your app installs CRDs or operators, use a [virtual cluster per PR](../../guides/kubernetes-preview-environments.md#4-virtual-cluster-per-pr) instead.
- **Throwaway database.** Postgres runs on `emptyDir`, so every preview starts empty and data disappears with it. For realistic data, replace it with a branched database (see [`neon-branch-per-pr`](../neon-branch-per-pr/)) or a seed job. See [database preview environments](../../guides/database-preview-environments.md).
- **Fork PRs are skipped.** On the `pull_request` event, GitHub doesn't pass secrets to workflows from forks. Don't switch to `pull_request_target` to get around this, because it runs untrusted code with your secrets. See [security and secrets](../../guides/preview-environment-security.md).
- **Concurrency.** A new push cancels an in-flight deploy for the same PR, but a teardown is never cancelled.
- **Missed teardowns.** If a teardown run fails, the namespace stays behind. Add a scheduled job that deletes namespaces labelled `preview=true` whose PR is closed, or that are older than N days. See [cost optimization](../../guides/reduce-preview-environment-costs.md).

## Not included

Production hardening is out of scope for this example. That includes image scanning, previews for multiple services or repositories, seeding from anonymised production data, SSO in front of preview URLs, and scale-to-zero. Managed platforms in the [comparison](../../comparisons/preview-environment-platform-comparison.md) handle some or all of these for you.
