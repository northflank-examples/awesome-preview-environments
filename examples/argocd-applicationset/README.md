# GitOps preview environments with Argo CD

Uses the [ApplicationSet Pull Request generator](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/) to create one Argo CD `Application` per open pull request. It's an alternative to the push-based [`kubernetes-namespace-per-pr`](../kubernetes-namespace-per-pr/) workflow: CI only builds the image, and the cluster pulls everything else.

| File | What it does |
| --- | --- |
| [`previews.yaml`](previews.yaml) | An `ApplicationSet` that deploys the chart at the PR's head commit into namespace `pr-<number>` for every PR labelled `preview` |

## How it works

1. A developer opens a PR and adds the `preview` label.
2. CI builds the image and pushes it, tagged with the PR's head SHA.
3. Argo CD's PR generator finds the PR within `requeueAfterSeconds`, or immediately with a [webhook](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/Generators-Pull-Request/#webhook-configuration). It renders an Application named `your-app-pr-<number>`.
4. On every new commit, `targetRevision` and `image.tag` move to the new SHA and Argo CD syncs.
5. When the PR is closed or the label is removed, the generator drops it. The ApplicationSet then deletes the Application, and its resources are pruned.

## Set up

1. Install Argo CD. The ApplicationSet controller has shipped with it since v2.3.
2. Create a GitHub token that can read the repository's pull requests. Store it as secret `github-token` (key `token`) in the `argocd` namespace.
3. Copy the chart from [`../kubernetes-namespace-per-pr/chart`](../kubernetes-namespace-per-pr/chart) into your repository at `chart/`. Make sure CI pushes `ghcr.io/your-org/your-app:<head sha>` on every PR.
4. Edit the owner, repo, image and domain in `previews.yaml`, then `kubectl apply -f previews.yaml`.

## Gotchas

- **The namespace outlives the Application.** `CreateNamespace=true` creates `pr-<number>`, but Argo CD doesn't delete namespaces it didn't render from the chart. Either template the `Namespace` in the chart, or run a periodic cleanup of empty `pr-*` namespaces.
- **Race with CI.** Argo CD may sync before the image exists. The `retry` block covers this. Alternatively, filter the generator on a label that CI adds once the image is pushed.
- **GitLab, Bitbucket, Gitea and Azure DevOps** are supported by the same generator with a different provider block.
- **Not a database solution.** Previews get whatever the chart deploys. For realistic data, see [database preview environments](../../guides/database-preview-environments.md).
