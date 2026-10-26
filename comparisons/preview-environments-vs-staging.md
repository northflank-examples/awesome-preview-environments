# Preview environments vs staging environments: differences and when to use each

**Short answer:** a preview environment is short-lived and tests **one change** in isolation, before merge. A staging environment is long-lived and tests **the integrated set of changes** that are about to ship, after merge. Most teams that adopt previews keep staging, or something like it, but use it less.

| | Preview environment | Staging environment |
| --- | --- | --- |
| What it contains | One branch or PR | The main branch, or a release candidate |
| How many | One per open PR (many at once) | Usually one (sometimes a few) |
| Lifetime | Minutes to days; deleted on merge or close | Long-lived |
| Created by | Automatically, on PR open or push | Set up once, updated by CD |
| Data | Empty, seeded, or branched per preview | Shared, long-lived, often a copy of production |
| Who uses it | PR author, reviewers, QA, design, product | QA, release managers, integration tests |
| Main question it answers | "Does this change work and look right?" | "Does everything we're about to release work together?" |
| Contention | None: every PR has its own | Teams queue for it, or step on each other's changes |
| Fidelity to production | Varies: often smaller and with fake data | Usually higher: production-like size and config |

## Related terms

| Term | Meaning |
| --- | --- |
| **Ephemeral environment** | Any environment created on demand and destroyed after use. Preview environments are the most common kind. Others include per-test-run environments and on-demand demo environments. |
| **Review app** | Heroku's and GitLab's name for a preview environment |
| **Deploy preview / preview deployment** | Netlify's and Vercel's names, often for frontend-only previews |
| **Development environment** | Where you write and debug code: a local machine, a cloud dev environment such as Codespaces or Coder, or a remote dev cluster |
| **Sandbox** | Overloaded term. Sometimes a preview environment (Signadot), sometimes an isolated runtime for untrusted code (AI agent sandboxes) |

## Do preview environments replace staging?

Sometimes. They can replace staging when:

- each preview is full-stack and production-like enough to trust, and
- you deploy small changes frequently, with feature flags and good production observability, so integration problems surface quickly and are cheap to roll back.

Keep a staging environment, or a pre-production stage in your pipeline, when:

- you need a long-running integration environment for third parties, partners or certification,
- you test at production scale (performance or load tests), or
- many changes ship together in a release, and you need to test their combination.

Further reading: [Dev, QA, preview, test, staging, and production environments. What's the deal?](https://northflank.com/blog/what-are-dev-qa-preview-test-staging-and-production-environments) (Northflank).

## How they fit together

```
feature branch ──► PR opened ──► preview env (per PR) ──► review + tests ──► merge
                                                                                │
                                                     staging (optional) ◄───────┘
                                                            │
                                                       production
```

See [getting started](../guides/set-up-preview-environments-for-pull-requests.md) to set up previews, and the [platform comparison](preview-environment-platform-comparison.md) to choose a tool.
