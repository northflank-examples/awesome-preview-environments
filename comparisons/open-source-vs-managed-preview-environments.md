# Open-source vs managed preview environments: build it yourself or use a platform?

There are four ways to get preview environments. They trade setup and maintenance effort against control and cost.

| Approach | Examples | You maintain | Best when |
| --- | --- | --- | --- |
| **Managed platform** | Northflank, Render, Heroku, Railway, Vercel, Netlify | Config only | You want previews working this week, and your stack fits the platform |
| **Managed control plane, your infrastructure (BYOC)** | Northflank BYOC, Qovery, Bunnyshell, Okteto, Signadot | Your cloud account or cluster | Data residency or compliance, existing cloud discounts, or a VPC-only dependency |
| **Self-hosted open-source PaaS** | Coolify, Dokploy | The PaaS, its servers and its upgrades | Small teams on their own servers, cost-sensitive |
| **DIY from building blocks** | GitHub Actions or GitLab CI + Helm, Argo CD ApplicationSets, Flux Operator, vCluster, Garden, PullPreview | Everything: pipelines, DNS, TLS, cleanup, quotas, access | You already run Kubernetes or GitOps and have platform engineers |

The [platform comparison](preview-environment-platform-comparison.md) lists which category each tool falls in, with sourced details.

## What DIY actually involves

A minimal per-PR pipeline (see [`examples/kubernetes-namespace-per-pr`](../examples/kubernetes-namespace-per-pr/)) takes about 150 lines and an afternoon. Making it reliable for a team usually also needs:

- [ ] wildcard DNS and TLS, and cleaning up DNS on teardown
- [ ] a scheduled sweep for environments whose teardown failed
- [ ] per-preview databases with realistic but safe data, plus migrations and seeds
- [ ] multi-repo or multi-service previews (which PR's version of each service?)
- [ ] access control on preview URLs
- [ ] resource quotas, TTLs and scale-to-zero
- [ ] safe handling of fork PRs and secrets
- [ ] a place for people to see what's running: links, logs, status

Managed platforms are mostly selling this list. For a side-by-side view of how one managed platform covers each item, see the [Northflank preview blueprint example](../examples/northflank-preview-blueprint/README.md#what-you-get-without-writing-a-pipeline). DIY makes sense when you need control over something on it that platforms don't give you, or when the platform cost at your scale exceeds the engineering time.

## Questions to decide

1. **Do your previews need backend services and databases, or only a frontend?** Frontend-only previews are a solved problem on most frontend hosts. Full-stack previews are where the options diverge.
2. **Where must the code and data run?** If it has to run in your own cloud account, you need BYOC, self-hosted or DIY.
3. **Do you already run Kubernetes and GitOps?** If so, ApplicationSets or Flux plus namespaces are a natural extension. If not, adopting Kubernetes just for previews is a large step.
4. **How many open PRs, and how big is each preview?** Multiply them out ([cost guide](../guides/reduce-preview-environment-costs.md)). The answer often decides between per-PR full stacks and shared-baseline routing.
5. **Who maintains it in a year?** DIY pipelines tend to rot when their author moves on.
