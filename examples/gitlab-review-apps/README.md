# GitLab review apps on Kubernetes

GitLab's built-in preview environments are called [review apps](https://docs.gitlab.com/ci/review_apps/). This `.gitlab-ci.yml` deploys one namespace per merge request, shows the URL on the MR, and stops the environment when the MR is merged or closed. If nobody pushes for a week, it stops automatically.

| File | What it does |
| --- | --- |
| [`.gitlab-ci.yml`](.gitlab-ci.yml) | Builds the image into the GitLab registry, deploys the chart to `mr-<iid>`, and defines the `stop_review` job |

## The three keywords that matter

| Keyword | Effect |
| --- | --- |
| `environment.name: review/$CI_MERGE_REQUEST_IID` | One dynamic environment per MR, grouped under `review/` in **Operate > Environments** |
| `environment.on_stop: stop_review` | GitLab runs `stop_review` when the environment is stopped, which deletes the namespace |
| `environment.auto_stop_in: 1 week` | Stops forgotten environments even if no one merges or closes the MR |

`stop_review` sets `GIT_STRATEGY: none` because the source branch may already be deleted when it runs. It must use the same `rules` as the deploy job, or GitLab won't link the two jobs.

## Set up

1. Connect a cluster with the [GitLab agent for Kubernetes](https://docs.gitlab.com/user/clusters/agent/), or add a `KUBECONFIG` file variable.
2. Add the CI/CD variable `PREVIEW_DOMAIN`, and point a wildcard DNS record at your ingress controller.
3. Copy [`../kubernetes-namespace-per-pr/chart`](../kubernetes-namespace-per-pr/chart) into your repository at `chart/`.

Merge requests from forks run in the fork's project by default and can't use your project's protected variables. See GitLab's docs on [pipelines for MRs from forks](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#run-pipelines-in-the-parent-project) before you enable previews for them.
