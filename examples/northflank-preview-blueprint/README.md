# Full-stack preview environments on Northflank (preview blueprints)

> Disclosure: this repository is maintained by Northflank.

The other examples in this repository show how much you have to build yourself: CI workflows, Helm charts, DNS, database branches and cleanup jobs. On [Northflank](https://northflank.com/product/preview-environments), the same lifecycle is configured once in a **preview blueprint**. A blueprint is a template that runs for every matching pull request or branch. It builds the code, then creates an isolated environment with the PR's own services, jobs, databases, volumes, secret groups and URLs. When the PR closes, Northflank deletes the whole environment.

Previews run on Northflank's cloud, or in [your own cloud account](https://northflank.com/docs/v1/application/bring-your-own-cloud/use-other-cloud-providers-with-northflank) (AWS, GCP, Azure, Oracle, Civo, CoreWeave or Nebius) or an existing Kubernetes cluster.

## What you get without writing a pipeline

| Preview lifecycle need | DIY (see the other examples) | Preview blueprint |
| --- | --- | --- |
| Create and update a preview on every PR push | CI workflow on `pull_request` | Git pull request or push trigger |
| Delete on merge or close | Teardown job, plus a sweep for missed events | Automatic on PR close or branch delete |
| Expire forgotten previews | Scheduled cleanup job | Preview expiry, optionally reset on each update |
| Own database per preview | Database branching action, or a chart with Postgres | Addon node: a fresh database, or a fork of a snapshot |
| Seed data | Init container or script | Job node after the database is ready |
| Secrets scoped to the preview | Per-namespace secrets, CI environment scoping | Secret groups restricted to the preview's tag by default |
| A URL per preview | Wildcard DNS, ingress, TLS certificates | Generated `*.northflank.app` URL, or a subdomain on your wildcard domain |
| Post the URL on the PR | `github-script` step | Message node: a PR comment, Slack or a webhook |
| Stop paying for idle previews overnight | Custom scale-down job | Active hours (in your own cloud account) |
| Clean up external resources | Extra teardown steps | Teardown specification |
| Previews in your own cloud account | You operate the cluster | Bring your own cloud (BYOC) or your own cluster (BYOK) |

## Build a full-stack preview blueprint

This recipe follows [Set up preview blueprints](https://northflank.com/docs/v1/application/release/set-up-preview-blueprints) and the [Create preview environments](https://northflank.com/docs/v1/application/use-cases/create-preview-environments) use-case guide.

**Before you start:** link your Git account, create a build service for your repository, and list the services, jobs, databases and secrets each preview needs. Decide which ones each preview creates and which it shares, and keep production credentials and data out of previews.

1. Open **Previews** in your project sidebar and click **New preview blueprint**.
2. Name it (for example `pr-previews`) and choose a naming convention. **Pull request ID** gives previews names like `pr-123`, and resource names follow the same pattern.
3. Add a **Git pull request** trigger for your repository, then click **Continue** to open the visual editor.
4. Connect these nodes:

```
Build on trigger ──► Addon (PostgreSQL: fresh, or fork from snapshot) ──► Job (seed data, optional)
                                                                              │
Message (comment URL on PR) ◄── Secret group (link addon credentials) ◄── Deploy build to service (public port)
```

5. In **Settings**, enable **Allow preview environments to expire**, so forgotten previews are deleted. Also enable **Reset duration on update**, so previews that are still active keep running.
6. Click **Save preview blueprint**. Then click **Run** and pick a commit, to test the blueprint before opening a real PR.

Each preview's services get URLs following the pattern `service-name-pr-123.project.northflank.app`. In nodes, reference a deployed service's URL as `${refs.<node-ref>.ports.0.dns}`, for example in the message node's PR comment. Reference the triggering branch and commit as `${triggers.<trigger-name>.branch}` and `${triggers.<trigger-name>.sha}`.

## Patterns from the docs

| Pattern | Nodes | Use when |
| --- | --- | --- |
| **Simple frontend or API** | Build on trigger → Create service → Expose port with generated domain | A single service, with no data dependencies |
| **Full-stack application** | Build on trigger → Create addon (e.g. PostgreSQL) → Deploy build → Link addon credentials | The most common web app setup: each preview has its own fresh database |
| **Full stack with seed data** | Build on trigger → Create addon (or fork from snapshot) → Run job (seed) → Deploy build → Link credentials | Previews must be usable immediately, with realistic data |
| **Microservices** | Build service A → Build service B → Deploy A → Deploy B → Expose A | Several services in one preview, talking over private networking |
| **Branch-specific overrides** | Build on trigger → Condition on `${triggers.repo.branch}` → full stack, or a lightweight mock | Different branches need different preview footprints |

## Triggers

| Trigger | Creates or updates a preview when |
| --- | --- |
| Git pull request | A matching PR is opened or pushed to (draft PRs can be ignored) |
| Git push | A matching branch is pushed to |
| GitHub PR label | A PR has a matching label: opt-in previews |
| Git check suite | A supported check succeeds |
| Tagged release | A provider release event happens |
| Cron schedule | On a UTC schedule, at least 10 minutes apart. Useful for nightly demo environments |
| Webhook | A GET or POST request is sent to the blueprint's webhook URL. Useful for AI agents and custom tooling. Treat the URL as a credential |

Triggers support branch-name patterns, file-path rules (preview only when certain paths change) and commit-message skip flags such as `[skip ci]`.

## Keep the blueprint in Git

Enable [GitOps](https://northflank.com/docs/v1/application/infrastructure-as-code/gitops-on-northflank) to sync the blueprint with a JSON file in your repository. With **Enable using branch contents**, each preview runs the blueprint file from its own branch, so a pull request can change its own preview infrastructure.

You can also create blueprints with the API (`POST /v1/projects/{projectId}/preview-blueprints`) or the CLI (`northflank create preview-blueprint`). The trigger and lifecycle settings look like this in the [API reference](https://northflank.com/docs/v1/api/project/preview-blueprints/create-preview-blueprint):

```json
{
  "name": "pr-previews",
  "triggers": [
    {
      "kind": "vcs-pr",
      "ref": "app",
      "spec": {
        "vcs": { "vcsService": "github", "repoUrl": "https://github.com/your-org/your-app" },
        "ignoreDrafts": true,
        "filePaths": { "enabled": true, "allowList": false, "paths": ["*.md", "docs/**"] }
      }
    }
  ],
  "options": {
    "concurrencyPolicy": "latest",
    "expiry": { "previewLifetime": 4320, "resetOnUpdate": true }
  }
}
```

`previewLifetime` is in minutes since the preview's last update: 4320 minutes is 3 days. The node graph goes in `spec`. The easiest way to get it is to build the blueprint in the visual editor and copy it from the code view, or let GitOps write the file for you.

## Operate previews

- **Find a preview:** open **Previews**. Each preview shows its PR or branch, status and creation date, and links to its resources and URLs.
- **Run without a PR:** click **Run** on the blueprint and pick a branch or commit. This is useful for testing a branch or creating a demo.
- **Re-run:** click **Run preview environment**. It reuses the arguments and configuration of the latest run.
- **Pause triggers:** turn off **Enable trigger**. Existing previews keep running, and expiry and PR-close deletion still apply.
- **Delete:** deleting a preview permanently removes all of its services, databases and volumes.

## Keep costs down

The [manage preview blueprints](https://northflank.com/docs/v1/application/release/manage-preview-blueprints) docs recommend:

- small resource plans in the blueprint's service and addon nodes,
- preview expiry,
- narrow trigger rules (labels, branch patterns, file paths), so you only create the previews you need, and
- **active hours** in your own cloud account, which pauses previews outside working hours and resumes them in the morning.

Compute is billed per second, and a free Sandbox tier is available. See [pricing](https://northflank.com/pricing).

## Learn more

- [Northflank preview environments](https://northflank.com/product/preview-environments)
- [Set up preview blueprints](https://northflank.com/docs/v1/application/release/set-up-preview-blueprints)
- [Manage preview blueprints](https://northflank.com/docs/v1/application/release/manage-preview-blueprints)
- [Create preview environments (use case)](https://northflank.com/docs/v1/application/use-cases/create-preview-environments)
- [Template nodes reference](https://northflank.com/docs/v1/application/infrastructure-as-code/template-nodes)
- [How Northflank compares with other preview platforms](../../comparisons/preview-environment-platform-comparison.md#northflank)
