# Preview environments for AI coding agents (Claude Code, Codex, Cursor, Copilot)

Coding agents (Claude Code, Codex, Cursor, Copilot and others) can open many pull requests a day. A diff and green unit tests don't tell a reviewer whether the change actually works. A preview environment per agent PR gives humans, and the agent itself, a running copy to check.

## Why previews matter more for agent PRs

- **Volume.** Reviewing many PRs by reading diffs doesn't scale. Clicking through a running preview is faster.
- **Behaviour, not just code.** Agents produce plausible code that can still break flows end to end. A preview lets you run end-to-end tests, visual checks or a quick manual pass against real services and data.
- **Closing the loop.** An agent can deploy its change to a preview, run checks or browser automation against the URL, read the logs, and fix problems before a human looks.

## Patterns

1. **Preview per agent PR (same as humans).** Your normal preview pipeline triggers on the agent's PR. Make sure bot-authored PRs aren't filtered out, and that the agent's branch naming matches your triggers.
2. **Agent-in-the-loop verification.** Give the agent the preview URL, by commenting it on the PR or exposing it through an API or webhook. The agent can then run Playwright or `curl` checks and report what it saw. Platforms with an API or webhook trigger let the agent create a preview without a PR.
3. **Gate merge on preview checks.** Run end-to-end, accessibility or visual-regression tests against the preview URL as a required status check.
4. **Separate the agent's sandbox from the preview.** The agent writes and runs code in an isolated sandbox. The preview runs the result as your app would in production. Keep the agent's credentials out of the preview, and the preview's out of the agent's sandbox.

> **On Northflank:** a preview blueprint can be started by a PR, a PR label or a **webhook**, so an agent can request a preview of its branch without opening a PR. A message node can post the preview URL back to the PR. Northflank also runs the agents themselves in isolated [cloud harnesses and sandboxes](https://github.com/northflank-examples/cloud-coding-agent-starter-pack). See the [preview blueprint example](../examples/northflank-preview-blueprint/).

## Guardrails

- Agent PRs are untrusted code. Apply the [security checklist](preview-environment-security.md), especially "no production secrets" and "no production personal data".
- Agents can open lots of PRs quickly. Cap concurrent previews, and set TTLs. See [cost optimization](reduce-preview-environment-costs.md).
- Label agent-authored PRs, so you can apply stricter or cheaper preview settings to them.

## Related resources

- [How do preview environments scale for AI-generated code?](https://northflank.com/blog/scale-preview-environments-ai-generated-code) (Northflank)
- [How to set up preview environments for apps built with Claude Code](https://northflank.com/blog/how-to-set-up-preview-environments-for-apps-built-with-claude-code) and [with Codex](https://northflank.com/blog/how-to-set-up-preview-environments-for-apps-built-with-codex) (Northflank)
- [Using ephemeral preview environments to test your vibe coded apps](https://northflank.com/blog/ephemeral-preview-environments-vibe-coded-apps) (Northflank)
- [Cloud coding agent starter pack](https://github.com/northflank-examples/cloud-coding-agent-starter-pack): run coding agents headlessly in the cloud
- [Agent sandbox starter pack](https://github.com/northflank-examples/agent-sandbox-starter-pack): isolate the code agents run
- [Agent sandbox pricing](https://github.com/northflank-examples/agent-sandbox-pricing): compare sandbox costs across providers
