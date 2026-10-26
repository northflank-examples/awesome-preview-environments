# How to create preview environments for pull requests with GitHub Actions

GitHub Actions doesn't create preview environments for you. [Deployment environments](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments) give you a named target with protection rules, scoped secrets and a URL shown on the PR. Your workflow still has to provision the infrastructure, deploy to it and tear it down. This guide covers the parts every per-PR workflow needs. For a working example, see [`examples/kubernetes-namespace-per-pr`](../examples/kubernetes-namespace-per-pr/).

## The lifecycle in one workflow

Listen to the `pull_request` event with the `closed` type added, and branch on the action:

```yaml
on:
  pull_request:
    types: [opened, synchronize, reopened, closed]

jobs:
  deploy:
    if: github.event.action != 'closed'
    # build, deploy to an environment named after the PR, comment the URL
  teardown:
    if: github.event.action == 'closed'
    # delete everything created for this PR
```

- `synchronize` fires on every push to the PR branch, which redeploys the preview.
- `closed` fires for both merged and unmerged PRs. Use `github.event.pull_request.merged` if you need to tell them apart.
- Name everything after `github.event.pull_request.number`, such as namespaces, databases, DNS names and image tags, so the teardown job can find it again without state.

## Concurrency: never deploy twice at once

```yaml
concurrency:
  group: preview-${{ github.event.pull_request.number }}
  cancel-in-progress: ${{ github.event.action != 'closed' }}
```

Two quick pushes would otherwise race. Cancel superseded deploys, but never cancel a teardown, or you'll leak an environment.

## Forks and secrets: the most common mistake

On the `pull_request` event, workflows triggered from forks get a read-only `GITHUB_TOKEN` and no repository secrets. That's deliberate. The tempting fix is `pull_request_target`, which does run with secrets. But if it checks out and builds the PR's code, anyone can open a PR that exfiltrates them. GitHub Security Lab calls these ["pwn requests"](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/).

Safe options:

1. **Skip previews for forks** (what the examples do): `if: github.event.pull_request.head.repo.full_name == github.repository`.
2. **Require a maintainer's approval.** Gate deployment behind an environment with [required reviewers](https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/manage-environments#required-reviewers), or a label that only maintainers can add, after they've read the diff.
3. **Split build and deploy.** Build untrusted code in an unprivileged `pull_request` workflow that uploads an artifact. Deploy it from a separate `workflow_run` workflow that never executes PR code.
4. **Let a platform do it.** Hosted preview platforms receive the Git webhook directly, so your CI secrets aren't involved. Check how each platform handles fork PRs before you enable them.

## Showing the URL on the PR

- Set `environment.url` on the deploy job. GitHub shows a **View deployment** button on the PR.
- Post or update a sticky comment, for example with `actions/github-script`, as in the example. Update one comment instead of adding one per push.

## Cleaning up what the `closed` event missed

Teardown jobs fail, workflows get disabled, and runners hit errors. Add a scheduled sweep:

```yaml
on:
  schedule:
    - cron: "0 3 * * *"
```

List what's running (namespaces labelled `preview=true`, database branches named `preview/pr-*`, and so on). Then delete anything whose PR is closed, or that's older than your maximum lifetime. Some database tools support an expiry timestamp at creation, which is a cheap second safety net. See [`examples/neon-branch-per-pr`](../examples/neon-branch-per-pr/).

## Or skip the workflow

Everything above is code you maintain: teardown jobs, sweeps, fork handling and URL comments. Platforms with built-in previews receive the Git webhook directly, so no CI secrets are involved. For example, a [Northflank preview blueprint](../examples/northflank-preview-blueprint/) creates, updates and deletes full-stack previews (services, databases, secrets and URLs) from PR events, and can comment the URL on the PR. Compare the options in the [platform comparison](../comparisons/preview-environment-platform-comparison.md#at-a-glance).

## Checklist

- [ ] `closed` is in `types:` and has its own teardown job
- [ ] Concurrency group per PR, and teardown never cancelled
- [ ] Every resource named or labelled with the PR number
- [ ] No `pull_request_target` that runs PR code
- [ ] Credentials scoped to preview infrastructure only, not production
- [ ] URL on the PR (environment URL or sticky comment)
- [ ] Scheduled sweep for leaked environments
- [ ] Resource limits per preview. See [cost optimization](reduce-preview-environment-costs.md)

## Further reading

- [Events that trigger workflows: `pull_request`](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request)
- [Control the concurrency of workflows and jobs](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency)
- [Keeping your GitHub Actions and workflows secure: preventing pwn requests](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/)
