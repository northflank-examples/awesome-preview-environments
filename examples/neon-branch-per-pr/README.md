# A database branch per pull request (Neon + GitHub Actions)

Gives every pull request its own copy-on-write Postgres branch, so migrations and test data in one preview can't break another preview or your shared staging database. The branch is deleted when the PR closes. As a safety net, it also expires after 14 days.

The workflow only handles the database. Pair it with whatever deploys your app preview, and pass the branch's connection string (`steps.branch.outputs.db_url`) to the app as `DATABASE_URL`.

| File | What it does |
| --- | --- |
| [`.github/workflows/preview-database.yml`](.github/workflows/preview-database.yml) | Creates `preview/pr-<number>` from your default branch, runs migrations, deletes it on close |

## Set up

1. In the Neon Console, create an API key. Add it as the repository secret `NEON_API_KEY`.
2. Add your Neon project ID as the repository variable `NEON_PROJECT_ID`.
3. Replace the placeholder migration step with your migration tool.
4. Pass `db_url` to your app preview. Two common patterns are setting it as an environment variable through your hosting platform's API or CLI, or running `helm --set` as in [`kubernetes-namespace-per-pr`](../kubernetes-namespace-per-pr/).

## Options worth knowing

The [`create-branch-action`](https://github.com/neondatabase/create-branch-action) inputs used here, plus the ones you'll probably want next:

| Input | Used here | Why |
| --- | --- | --- |
| `expires_at` | 14 days | Branches are cleaned up even if the `closed` event is missed |
| `suspend_timeout` | 300 s | The branch's compute scales to zero when nobody is using the preview |
| `branch_type: schema-only` | no | Copies the schema without production data. Use it when the parent branch contains personal data |
| `masking_rules` | no | Applies data-masking rules to the new branch |
| `parent_branch` | no | Branch from a seeded or anonymised branch instead of the default branch |

If your parent branch holds real customer data, every PR author gets a copy of it. Branch from an anonymised or seeded parent, or use `schema-only`. See [database preview environments](../../guides/database-preview-environments.md).

## Alternatives

Supabase, PlanetScale, Xata and others offer similar branching, and some app platforms can provision or fork a database inside the preview itself. Compare them in [database preview environments](../../guides/database-preview-environments.md#tools).
