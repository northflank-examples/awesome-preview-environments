# How to reduce preview environment costs

A preview environment's cost is roughly **(number of open PRs) × (resources per preview) × (hours alive)**. Each lever below shrinks one of those factors.

## 1. Fewer previews

- **Opt in instead of every PR.** Trigger on a label (`preview`), on PRs that touch deployable paths, or skip drafts. Most platforms and CI systems support path or label filters.
- **Skip bot PRs.** Dependency-update bots can open dozens of PRs a week that nobody previews.
- **Cap concurrency.** Limit the number of previews per repository, and evict the oldest when the cap is reached.

## 2. Smaller previews

- **Right-size.** Previews serve a handful of reviewers, not production traffic. Use the smallest instance size, one replica and no autoscaling.
- **Deploy only what changed.** Share stable services, or a seeded staging database, across previews. Fork only what the PR touches. See the request-routing pattern in the [Kubernetes guide](kubernetes-preview-environments.md#3-shared-baseline--request-routing).
- **Use copy-on-write databases.** Database branching and thin clones cost little until data diverges, unlike a full restore per preview. See [database preview environments](database-preview-environments.md).
- **Set hard limits.** Use a ResourceQuota per namespace, or spending limits at the platform level, so a broken PR can't scale up indefinitely.

## 3. Shorter lifetimes

- **Delete on close or merge.** This is table stakes. Make sure it actually happens, with a scheduled sweep as a backstop.
- **Set a TTL or inactivity expiry.** Delete previews that haven't had a push in N days, even if the PR is still open. Many platforms support this natively. Otherwise, run a nightly job.
- **Scale to zero when idle.** Pause previews outside working hours, or after inactivity, and wake them on request. Serverless databases with auto-suspend help here too.
- **Use spot or preemptible nodes.** Previews tolerate interruption. Put them on a spot node pool on Kubernetes or BYOC.

> **On Northflank:** preview blueprints support expiry that resets on each update, trigger rules (labels, branch patterns, file paths) to create fewer previews, and per-node resource plans. In your own cloud account, **active hours** pauses previews outside working hours and resumes them in the morning. Compute is billed per second. See the [example](../examples/northflank-preview-blueprint/README.md#keep-costs-down).

## 4. Where the bill lands

- **Managed platforms** usually bill previews like any other compute, sometimes with a separate cap or plan requirement. Check whether the platform bills per second while running, and whether paused or sleeping previews are free. See the [platform comparison](../comparisons/preview-environment-platform-comparison.md).
- **BYOC and self-hosted** previews run on your cloud bill, so committed-use discounts and credits apply. You also pay for the idle capacity they sit on.
- **Hidden costs:** build minutes, container registry storage for per-PR image tags, load balancers or IPs created per preview, NAT and egress, and log ingestion. Prune per-PR image tags after merge, and share a single ingress or load balancer across previews.

Further reading: [How do ephemeral environments reduce infrastructure costs?](https://northflank.com/blog/how-do-ephemeral-environments-reduce-infrastructure-costs) (Northflank).

## Quick estimate

```
monthly cost ≈ avg open PRs with previews
             × hourly cost of one preview (all services + DB)
             × hours each preview is actually running per month
```

Example: 15 open previews × $0.10/hour × 200 running hours (weekday working hours only) ≈ **$300/month**. The same previews left running 24/7 (730 hours) cost about $1,095. Lifetime controls usually save more than right-sizing.
