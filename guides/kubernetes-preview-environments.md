# Kubernetes preview environments: namespace per PR, vCluster, request routing and GitOps

If you already run on Kubernetes, you can build previews yourself. The main decision is **how much each preview gets its own copy of**, which trades isolation against cost and speed. These approaches aren't mutually exclusive: a full-stack copy usually lives in a namespace, and request routing needs a shared baseline somewhere.

| Pattern | Each preview gets | Isolation | Cost per preview | Good fit |
| --- | --- | --- | --- | --- |
| [1. Full stack per PR](#1-full-stack-per-pr) | Every service and database | Strong | High | Small-to-medium apps; teams that want previews to behave like production |
| [2. Namespace per PR](#2-namespace-per-pr) | A namespace on a shared cluster | Medium (RBAC, NetworkPolicy, quotas) | Medium | Most teams starting out on Kubernetes |
| [3. Shared baseline + request routing](#3-shared-baseline--request-routing) | Only the changed services | Logical (routing headers) | Low | Many microservices, where copying the whole system is too slow or expensive |
| [4. Virtual cluster per PR](#4-virtual-cluster-per-pr) | Its own Kubernetes API server | Strong at the API level | Medium | Apps that install CRDs or operators, or need cluster-scoped resources |

## 1. Full stack per PR

Deploy everything your app needs: every service, a fresh or forked database, caches and queues. Tests behave like production, and one PR can't break another. The costs are startup time, since every service builds and boots, and money, multiplied by the number of open PRs. Data is the hardest part. See [database preview environments](database-preview-environments.md).

## 2. Namespace per PR

The pragmatic default. One `helm upgrade --install` into `pr-<number>`, and teardown is a single `kubectl delete namespace`. A namespace on its own isn't a security boundary. Add:

- **ResourceQuota and LimitRange**, so one PR can't starve the cluster.
- **NetworkPolicy**, so previews can't reach each other's databases. This requires a CNI that enforces policies.
- **Scoped RBAC for CI.** The deploy credential should be able to manage `pr-*` namespaces and nothing else.
- **Wildcard DNS and TLS.** Point `*.preview.example.com` at the ingress controller. Issue a wildcard certificate with a [DNS-01 solver](https://cert-manager.io/docs/configuration/acme/dns01/), rather than one certificate per preview, which runs into Let's Encrypt rate limits.

Working example: [`examples/kubernetes-namespace-per-pr`](../examples/kubernetes-namespace-per-pr/) (push-based, GitHub Actions + Helm).

### Push vs pull (GitOps)

- **Push:** CI runs `helm`/`kubectl` with cluster credentials. Simple, but CI holds a kubeconfig.
- **Pull:** The cluster watches open PRs and deploys them itself. Two options are the Argo CD [ApplicationSet Pull Request generator](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/) and Flux Operator's [ResourceSets](https://fluxoperator.dev/docs/resourcesets/github-pull-requests/). CI only builds images. Working example: [`examples/argocd-applicationset`](../examples/argocd-applicationset/).

## 3. Shared baseline + request routing

Run one long-lived baseline of every service. For a PR, deploy only the services that changed, then route requests carrying the PR's header (or a session cookie) to those forks. Every other hop goes to the baseline. This needs context propagation through every service, using something like OpenTelemetry baggage or a propagated header, and a mesh or proxy that routes on it. Lyft's "staging overrides" ([InfoQ summary](https://www.infoq.com/news/2022/03/scaling-testing-acceptance-lyft/)) and Uber's [SLATE](https://www.uber.com/blog/simplifying-developer-testing-through-slate/) are well-known write-ups. Signadot and mirrord productise the approach.

The trade-off is that shared databases and queues are still shared. Writes from a preview land in the baseline's data, unless you also isolate data at the tenant or schema level.

## 4. Virtual cluster per PR

A [vCluster](https://www.vcluster.com/docs) runs a separate Kubernetes control plane inside a namespace of the host cluster. Each preview gets its own API server, so CRDs, cluster roles and operators can be installed per PR without colliding. It costs more than a namespace, because each one runs a control plane, but much less than a real cluster per PR.

## Lifecycle essentials (any pattern)

- Create on PR open or push, update on push, delete on close or merge.
- Label everything (`preview=true`, `pr=<number>`), and run a scheduled sweep for leaks.
- Set TTLs, and scale idle previews to zero. See [cost optimization](reduce-preview-environment-costs.md).
- Keep production credentials out of preview namespaces. See [security and secrets](preview-environment-security.md).

## Managed previews on your own cluster

If you want previews in your own cloud account but don't want to run the pipelines, DNS, TLS and cleanup above, several platforms manage that layer on infrastructure you own. For example, Northflank runs [preview blueprints](../examples/northflank-preview-blueprint/) on clusters it provisions in your AWS, GCP, Azure, Oracle, Civo, CoreWeave or Nebius account, or on an existing cluster you import. It can also pause previews outside working hours there. *(Disclosure: Northflank maintains this list.)*

Further reading: [Preview environments for microservices](https://northflank.com/blog/preview-environments-microservices) and [Kubernetes preview environment platforms compared](https://northflank.com/blog/kubernetes-preview-environments-comparison) (Northflank).

## Tools

Platforms that implement these patterns on your cluster (Okteto, Signadot, Bunnyshell, Qovery, vCluster and others) are compared in the [platform comparison](../comparisons/preview-environment-platform-comparison.md#kubernetes). Open-source building blocks are listed in the [README](../README.md#open-source-tools).
