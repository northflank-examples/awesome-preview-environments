# Preview environment security: secrets, fork pull requests and protecting preview URLs

Preview environments run unreviewed code, often from many contributors, on infrastructure that has some access to your systems. Treat every preview as **untrusted code with whatever credentials you give it**.

## Threats, and what to do about them

| Threat | Mitigation |
| --- | --- |
| A PR's code reads the preview's secrets and sends them out | Give previews their **own** credentials (test API keys, sandbox payment accounts, preview-only OAuth apps), never production ones. Assume anything in a preview is readable by the PR author. |
| A fork PR runs your CI with your secrets | Don't run fork code with secrets. On GitHub, avoid `pull_request_target` workflows that check out PR code ([pwn requests](https://securitylab.github.com/resources/github-actions-preventing-pwn-requests/)). Require maintainer approval before a fork gets a preview. |
| Preview URLs are guessable and public | Put previews behind auth: platform SSO or team-only access, basic auth, IP allowlists, or an identity-aware proxy. At minimum, add `X-Robots-Tag: noindex`. |
| Real customer data in previews | Use seeded or synthetic data, schema-only branches, or anonymised snapshots. See [database preview environments](database-preview-environments.md). |
| One preview reaches another's database or services | Isolate the network: one network or namespace per preview, plus NetworkPolicy on Kubernetes. Use per-preview database credentials. |
| The CI credential that creates previews is too powerful | Scope it to the preview project, namespace prefix or cloud account. On Kubernetes, give it RBAC on `pr-*` namespaces only. Prefer OIDC federation over long-lived keys. |
| Previews call production side effects (emails, webhooks, payments) | Point integrations at sandboxes. Use email catchers instead of real SMTP. Disable outbound webhooks or route them to a test endpoint. |
| Subdomain takeover after teardown | Delete DNS records with the preview. Use a wildcard record pointing at infrastructure you keep, rather than one record per preview pointing at deleted resources. |
| Cookies leak across previews on a shared parent domain | Serve previews from a separate registrable domain (for example `example-preview.com`), not a subdomain of your production domain, or scope cookies tightly. |

## Getting secrets into a preview

In order of preference:

1. **Platform-managed, scoped secret groups.** Most preview platforms let you define secrets once and inject them only into preview resources. Some also generate per-preview credentials, such as a database password for that preview's database.
2. **Generated at creation.** Generate random per-preview secrets (database passwords, session keys) when the preview is created, and store them only in that environment. The [Kubernetes example](../examples/kubernetes-namespace-per-pr/chart/templates/postgres.yaml) does this.
3. **CI environment secrets.** Store preview-only values in a separate GitHub environment or GitLab environment scope, so a preview job can't read production secrets.
4. **External secret managers** (Vault, cloud secret managers, External Secrets Operator), with a policy that only grants the preview path.

Never commit secrets into preview templates. Don't print them in logs either. In GitHub Actions, mask derived values with `::add-mask::`.

> **On Northflank:** resources in a preview get a preview tag by default, and secret groups scoped to that tag are only available inside that preview. Preview URLs can be protected per port with SSO, basic auth or IP policies. See the [preview blueprint example](../examples/northflank-preview-blueprint/).

Further reading: [How to control access to preview environments across enterprise teams](https://northflank.com/blog/control-access-preview-environments-enterprise-teams) and [secure preview environments with isolated sandboxes](https://northflank.com/blog/secure-preview-environments-with-isolated-sandboxes) (Northflank).

## Access control checklist

- [ ] Preview URLs require authentication, or at least aren't indexed
- [ ] Preview credentials are separate from production and limited in scope
- [ ] Fork PRs can't trigger previews with secrets without a maintainer's approval
- [ ] No production personal data in preview databases
- [ ] Network isolation between previews
- [ ] DNS records and certificates are removed on teardown
- [ ] Outbound side effects (email, payments, webhooks) go to sandboxes
