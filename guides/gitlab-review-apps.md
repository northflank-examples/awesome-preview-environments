# GitLab review apps: preview environments for every merge request

GitLab has first-class support for preview environments, called [review apps](https://docs.gitlab.com/ci/review_apps/). A review app is a dynamic environment, created per branch or merge request, whose URL shows on the MR. GitLab also has a stop job that runs when the MR is merged or closed. You still bring the infrastructure. A working example is in [`examples/gitlab-review-apps`](../examples/gitlab-review-apps/).

## The keywords

```yaml
review:
  environment:
    name: review/$CI_MERGE_REQUEST_IID   # one environment per MR, grouped under review/
    url: https://mr-$CI_MERGE_REQUEST_IID.preview.example.com
    on_stop: stop_review                 # job to run when the environment stops
    auto_stop_in: 1 week                 # stop it anyway if nobody merges or closes the MR

stop_review:
  variables:
    GIT_STRATEGY: none                   # the branch may be gone by now
  environment:
    name: review/$CI_MERGE_REQUEST_IID
    action: stop
  when: manual
```

| Feature | What it gives you |
| --- | --- |
| [Dynamic environments](https://docs.gitlab.com/ci/environments/#create-a-dynamic-environment) | Environment names built from CI variables, so you get one per MR |
| [`on_stop`](https://docs.gitlab.com/ci/yaml/#environmenton_stop) | Teardown that runs automatically when the MR is merged or closed, or the branch is deleted |
| [`auto_stop_in`](https://docs.gitlab.com/ci/yaml/#environmentauto_stop_in) | A TTL for forgotten environments |
| [`resource_group`](https://docs.gitlab.com/ci/resource_groups/) | One deploy per MR at a time |
| [Protected environments](https://docs.gitlab.com/ci/environments/protected_environments/) and environment-scoped variables | Different credentials for previews and production |

The deploy and stop jobs must have matching `rules`, or GitLab can't link them and the stop job never appears.

## Forks

By default, pipelines for merge requests from forks run in the fork's project, without your project's protected variables. To build them with your infrastructure, a maintainer can [run the pipeline in the parent project](https://docs.gitlab.com/ci/pipelines/merge_request_pipelines/#run-pipelines-in-the-parent-project) after reviewing the code. Treat that as running untrusted code with your credentials.

## Kubernetes

The [GitLab agent for Kubernetes](https://docs.gitlab.com/user/clusters/agent/) gives CI jobs a kube context without storing a kubeconfig. The namespace-per-MR pattern from the [Kubernetes guide](kubernetes-preview-environments.md) works the same way. GitLab's Auto DevOps also includes a [review app stage](https://docs.gitlab.com/topics/autodevops/stages/#auto-review-apps), if you use Auto DevOps.
