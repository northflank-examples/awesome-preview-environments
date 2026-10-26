# Database preview environments: a database per pull request with branching, forking and seeding

Data is usually the hardest part of a preview environment. Frontend previews can point at a shared API. Full-stack previews need a database that:

- has the **schema from this PR**, with the PR's migrations applied,
- has **enough realistic data** to exercise the change,
- is **isolated**, so this PR's migrations and writes can't break other previews or staging,
- contains **no data you can't give to every PR author**, and
- is **cheap and fast** to create and destroy many times a day.

## Strategies

| Strategy | How | Isolation | Realistic data | Speed / cost | Watch out for |
| --- | --- | --- | --- | --- | --- |
| **Shared database** | Every preview points at one staging DB | None | Whatever staging has | Instant, free | One PR's migration breaks every other preview |
| **Empty + migrate + seed** | New DB per preview, run migrations and a seed script | Full | Only as good as your seed | Fast for small seeds | Seed scripts rot; edge cases are missing |
| **Restore a snapshot** | Restore a (sanitised) backup per preview | Full | High | Slow and costly for large DBs | Personal data in backups; restore time grows with size |
| **Copy-on-write branch / thin clone** | Branch from a parent; storage is shared until written | Full | High (from the parent) | Seconds; pay for changes only | The parent's data is exposed to every PR; vendor-specific |
| **Schema-only branch** | Branch the schema, then seed | Full | Seed only | Fast | Same as empty + seed |
| **Per-tenant or schema isolation** | One DB, one schema or tenant per preview | Partial | Varies | Cheap | Extensions, global objects and cross-schema queries leak |

**A good default:** use a copy-on-write branch (or a fork from a snapshot) taken from a **sanitised parent**. The parent is a staging or "golden" database refreshed from production through anonymisation, or built from a rich seed. Previews get realistic data in seconds, and no production personal data reaches PR authors.

> **On Northflank:** a [preview blueprint](../examples/northflank-preview-blueprint/) can create a fresh database per preview, or fork one from a snapshot of an existing database. It can then run a seed job and inject the credentials into the preview's services through a secret group scoped to that preview. The database is deleted with the preview.

Further reading: [Which database strategy should you use for preview environments?](https://northflank.com/blog/which-database-strategy-should-you-use-for-preview-environments) (Northflank).

## Migrations

- Run migrations as a step in the preview's deploy: an init container, a pre-deploy job, or a platform release command. Don't run them at app start-up across many replicas.
- Previews are where destructive migrations should fail first. Keep migrations forward-only, and test them against realistic data volumes when you can.
- Two PRs that both add migrations will each pass alone. Your merge queue or staging still needs to catch the ordering conflict.

## Sensitive data

- Never branch previews directly from production unless every PR author is allowed to see production data.
- Use schema-only branches, masking rules, anonymised parents, or synthetic data generators.
- Remember backups, logs and analytics events inside previews. They inherit whatever data the preview has.

## Cleanup

Delete preview databases when the preview goes away, and set an expiry or TTL as a safety net. Database branches are easy to leak, because the app preview's teardown often doesn't know about them. See [`examples/neon-branch-per-pr`](../examples/neon-branch-per-pr/) for create-and-delete plus TTL.

## Tools

Database tools that create per-preview databases by branching, cloning or seeding. Facts are sourced from each vendor's docs. See the [methodology](../methodology.md).

<!-- BEGIN GENERATED: database-tools -->
| Tool | Engine | How a preview DB is made | Per-PR automation | Runs on |
| --- | --- | --- | --- | --- |
| DBLab Engine (Postgres.ai) | Postgres | Thin clone (copy-on-write via ZFS/LVM2) | CI via DB Migration Checker GitHub Action (push-triggered) | Self-hosted (on-prem or cloud) |
| Neon | Postgres | Copy-on-write branch (full data or schema-only) | GitHub Actions (create/delete/schema-diff); Vercel integrations | Managed (AWS regions) |
| PlanetScale | MySQL (Vitess) and Postgres | Schema-only branch; data branch restored from backup | DIY: pscale CLI in GitHub Actions (setup-pscale-action) | Managed; PlanetScale Managed in your AWS/GCP/Azure |
| Prisma Postgres | Postgres 17 | New empty database per PR, migrated and seeded | GitHub Actions guide; Prisma Compute branch previews | Managed |
| Supabase Branching | Postgres (full Supabase stack: auth, storage, APIs) | New instance; migrations + seed.sql applied | Yes, Supabase GitHub integration | Managed (Supabase Cloud, Pro plan and up) |
| Tonic Structural | Postgres, MySQL, SQL Server, Oracle, MongoDB, more | De-identified / subsetted copy of production | not published | Tonic Cloud or self-hosted |
| Turso | SQLite-compatible (Turso / libSQL) | Full copy as separate database; point-in-time option | DIY GitHub Actions example via Platform API | Managed (Turso Cloud) |
| Xata | Postgres (vanilla) | Copy-on-write branch | Yes, Xata GitHub App or GitHub Action | Managed cloud, BYOC, or self-hosted OSS |

<a id="dblab-engine"></a>

### DBLab Engine (Postgres.ai)

Open-source engine you run yourself that creates thin, writable copy-on-write clones (ZFS or LVM) of large Postgres databases in seconds, with a CI component for testing migrations against clones.

[Preview docs](https://postgres.ai/docs/database-lab) · [Website](https://postgres.ai) · [Source](https://github.com/postgres-ai/database-lab-engine) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **Engine** | Postgres | “cloning of 10 TiB PostgreSQL database takes less than 2 seconds when a single user is using the DBLab Engine instance” [source](https://postgres.ai/docs/database-lab) |
| **How a preview DB is made** | Thin clone (copy-on-write via ZFS/LVM2) | “Thin cloning is possible thanks to copy-on-write capabilities provided by either ZFS filesystem or LVM2” [source](https://postgres.ai/docs/database-lab) |
| **Per-PR automation** | CI via DB Migration Checker GitHub Action (push-triggered) | “a DLE component that enables integration with CI/CD tools to automatically test migrations in CI/CD pipelines” [source](https://postgres.ai/docs/database-lab/db-migration-checker) |
| **Cleanup** | Yes, idle clones auto-deleted (configurable) | “Automated deletion of clones after a specified number of minutes of inactivity (configurable)” [source](https://postgres.ai/docs/database-lab) |
| **Data** | Full-size prod copies; masking/obfuscation options | “Allows setting up dynamic masking rules without actual data changes.” [source](https://postgres.ai/docs/database-lab/masking) |
| **Runs on** | Self-hosted (on-prem or cloud) | “Works well both on-premises and in clouds.” [source](https://postgres.ai/docs/database-lab) |
| **License** | Open source (Apache-2.0); paid SE/EE editions | “DBLab Engine is distributed under Apache 2.0 license.” [source](https://postgres.ai/docs/database-lab) |
| **Pricing** | OSS free; DBLab SE from $62/mo | “Starting at $62/mo” [source](https://postgres.ai/pricing) |

Caveats:

- Clones are aimed at dev/test and CI; the documented migration-checker trigger is a push event, not a PR preview lifecycle (https://postgres.ai/docs/database-lab/db-migration-checker).
- Primary repo is on GitLab (https://gitlab.com/postgres-ai/database-lab); GitHub is a mirror.

<a id="neon"></a>

### Neon

Serverless Postgres whose copy-on-write branches can be created per PR via GitHub Actions or per Vercel preview deployment via the Vercel integrations.

[Preview docs](https://neon.com/docs/introduction/branching) · [Website](https://neon.com) · [Source](https://github.com/neondatabase/neon) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **Engine** | Postgres | “Neon is an open-source serverless Postgres database platform.” [source](https://github.com/neondatabase/neon) |
| **How a preview DB is made** | Copy-on-write branch (full data or schema-only) | “A branch is a copy-on-write clone of your data.” [source](https://neon.com/docs/introduction/branching) |
| **Per-PR automation** | GitHub Actions (create/delete/schema-diff); Vercel integrations | “this integration creates an isolated database branch for each preview deployment” [source](https://neon.com/docs/guides/neon-managed-vercel-integration) |
| **Cleanup** | Yes: on Git branch delete (Vercel), Action on PR close, or TTL | “Create branches with TTL by setting an expiration date” [source](https://neon.com/docs/introduction/branching) |
| **Data** | Parent data by default; schema-only option | “By default, branches are created with all of the data that existed in the parent branch ... Neon also supports schema-only branching.” [source](https://neon.com/docs/introduction/branching) |
| **Runs on** | Managed (AWS regions) | “Neon offers project deployment in multiple AWS regions.” [source](https://neon.com/docs/introduction/regions) |
| **License** | Open source (Apache-2.0); managed service | “Neon is an open-source serverless Postgres database platform.” [source](https://github.com/neondatabase/neon) |
| **Pricing** | Free plan (10 branches/project); paid usage-based | “Paid plans are pay-as-you-go: usage is metered hourly and billed at the end of the month, with no monthly minimum.” [source](https://neon.com/pricing) |

Caveats:

- Neon is now offered as part of Databricks; docs refer to the product as 'Lakebase Postgres' (https://neon.com/docs/guides/vercel-overview).
- With the Vercel-Managed integration, branch cleanup follows Vercel's deployment retention, which can delay deletion by months (https://neon.com/docs/guides/vercel-overview).
- The delete-branch GitHub Action is documented for cleaning up 'ephemeral branches after a pull request is merged or closed'; you wire the PR-close trigger yourself (https://neon.com/docs/guides/branching-github-actions).
- Azure regions are deprecated for new projects (https://neon.com/docs/introduction/regions).

<a id="planetscale"></a>

### PlanetScale

Managed MySQL (Vitess) and Postgres with development branches; Vitess branches are schema-only by default (data via Data Branching from backup) and schema changes merge via deploy requests; per-PR branches are scripted with the pscale CLI in GitHub Actions.

[Preview docs](https://planetscale.com/docs/vitess/schema-changes/branching) · [Website](https://planetscale.com) · [Source](https://github.com/planetscale/cli) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **Engine** | MySQL (Vitess) and Postgres | “isolated database deployments” [source](https://planetscale.com/docs/postgres/branching) |
| **How a preview DB is made** | Schema-only branch; data branch restored from backup | “Development branches provide isolated copies of your production database schema” [source](https://planetscale.com/docs/vitess/schema-changes/branching) |
| **Per-PR automation** | DIY: pscale CLI in GitHub Actions (setup-pscale-action) | “You can use `pscale branch create` to create a branch that matches your GitHub branch name.” [source](https://planetscale.com/docs/vitess/tutorials/github-actions) |
| **Cleanup** | Manual or scripted; deploy request can auto-delete branch | “`--auto-delete-branch` deletes the PlanetScale branch once the deploy request completes, so CI branches don't accumulate.” [source](https://planetscale.com/docs/vitess/tutorials/github-actions) |
| **Data** | Schema-only by default; Data Branching copies latest backup | “Creates a database branch with both the **schema and data** from the latest backup of the Base branch” [source](https://planetscale.com/docs/vitess/schema-changes/data-branching) |
| **Runs on** | Managed; PlanetScale Managed in your AWS/GCP/Azure | “Run PlanetScale in your own AWS, GCP, or Azure account, operated by our team with your data in your cloud.” [source](https://planetscale.com/docs/vitess/managed) |
| **License** | Proprietary service; pscale CLI Apache-2.0 | CLI license (Apache-2.0) from GitHub repo metadata; the database service is proprietary (Vitess itself is OSS). |
| **Pricing** | No free tier listed; Postgres from $5/mo; branches billed extra | “New branches incur additional charges.” [source](https://planetscale.com/docs/postgres/branching) |

Caveats:

- PlanetScale Postgres branches do not use deploy requests; 'There's currently no automated way to merge schema changes between PlanetScale Postgres branches' (https://planetscale.com/docs/postgres/branching).
- Data-seeded branches can't filter out tables/data (no anonymisation) and branches seeded from production are billed as production branches (https://planetscale.com/docs/vitess/schema-changes/data-branching).
- Pricing page lists Postgres PS-5 single-node from $5/month and Vitess PS-10 from $39/month (https://planetscale.com/pricing).

<a id="prisma-postgres"></a>

### Prisma Postgres

Managed Postgres without data branching; previews get a fresh database per PR (GitHub Actions guide) or per Git branch on Prisma Compute, with migrations and seed data applied.

[Preview docs](https://www.prisma.io/docs/guides/integrations/github-actions) · [Website](https://www.prisma.io/postgres) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **Engine** | Postgres 17 | “Prisma Postgres is managed PostgreSQL 17 with PgBouncer pooling on every plan” [source](https://www.prisma.io/docs/postgres) |
| **How a preview DB is made** | New empty database per PR, migrated and seeded | “applies your checked-in migrations, seeds it with sample data” [source](https://www.prisma.io/docs/guides/integrations/github-actions) |
| **Per-PR automation** | GitHub Actions guide; Prisma Compute branch previews | “The workflow provisions a database for every pull request” [source](https://www.prisma.io/docs/guides/integrations/github-actions) |
| **Cleanup** | Yes, on PR close (workflow) or Git branch delete (Compute) | “When the pull request is closed, the workflow deletes the database.” [source](https://www.prisma.io/docs/guides/integrations/github-actions) |
| **Data** | Seeded only; production data not copied | “its own new database; production data is not copied” [source](https://www.prisma.io/docs/compute/branching) |
| **Runs on** | Managed | “Prisma Postgres is managed PostgreSQL 17 with PgBouncer pooling on every plan” [source](https://www.prisma.io/docs/postgres) |
| **License** | Proprietary | Closed-source commercial service; no open-source license is published (inferred). |
| **Pricing** | Free: 50 DBs, 2 GB; paid billed per operation | “200k operations / month; 2 GB storage; 50 databases” [source](https://www.prisma.io/pricing) |

Caveats:

- No copy-on-write/data branching; each preview starts from a new database (https://www.prisma.io/docs/compute/branching).
- Compute per-branch databases apply only to databases declared in the Prisma Composer (Early Access) module (https://www.prisma.io/docs/compute/branching).

<a id="supabase-branching"></a>

### Supabase Branching

Supabase's GitHub integration creates a separate Supabase instance per Git branch/PR, runs migrations and seed.sql, and deletes preview branches when the PR is merged or closed.

[Preview docs](https://supabase.com/docs/guides/deployment/branching) · [Website](https://supabase.com) · [Source](https://github.com/supabase/supabase) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **Engine** | Postgres (full Supabase stack: auth, storage, APIs) | “a separate environment with its own Supabase instance and API credentials” [source](https://supabase.com/docs/guides/deployment/branching) |
| **How a preview DB is made** | New instance; migrations + seed.sql applied | “The migrations in the `migrations` subdirectory of your Supabase directory are automatically run when the branch is created.” [source](https://supabase.com/docs/guides/deployment/branching/github-integration) |
| **Per-PR automation** | Yes, Supabase GitHub integration | “When a new branch is created in GitHub, a corresponding branch is created in Supabase.” [source](https://supabase.com/docs/guides/deployment/branching/github-integration) |
| **Cleanup** | Yes, preview branches deleted on PR merge/close | “automatically deleted when a PR is merged or closed” [source](https://supabase.com/docs/guides/deployment/branching) |
| **Data** | No prod data by default; seed file; dashboard 'Include data' option | “By default, new branches do not start with any data or storage objects from your base project.” [source](https://supabase.com/docs/guides/deployment/branching) |
| **Runs on** | Managed (Supabase Cloud, Pro plan and up) | “run a separate development environment off your production project” [source](https://supabase.com/pricing) |
| **License** | Open source (Apache-2.0); branching is a platform feature | “Supabase is a combination of open source tools.” [source](https://github.com/supabase/supabase) |
| **Pricing** | $0.01344 per branch-hour; Pro plan and up | “$0.01344 per branch, per hour” [source](https://supabase.com/pricing) |

Caveats:

- Persistent branches are not auto-deleted or paused on PR merge/close (https://supabase.com/docs/guides/deployment/branching).
- Branching is not on the Free plan (https://supabase.com/pricing).

<a id="tonic-structural"></a>

### Tonic Structural

Commercial test-data platform that de-identifies, masks and subsets production data from many databases into realistic datasets for staging/dev; it feeds preview databases rather than provisioning them per PR.

[Preview docs](https://docs.tonic.ai/app/) · [Website](https://www.tonic.ai) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **Engine** | Postgres, MySQL, SQL Server, Oracle, MongoDB, more | “native connectors to all the leading relational and NoSQL databases, data warehouses, lakehouses, and file types.” [source](https://www.tonic.ai/products/tonic-structural) |
| **How a preview DB is made** | De-identified / subsetted copy of production | “The Tonic Structural platform creates safe, realistic datasets to use in staging environments or for local development.” [source](https://docs.tonic.ai/app/) |
| **Per-PR automation** | not published | No documented per-PR integration; vendor mentions CI/CD pipeline integration generally. |
| **Cleanup** | not published | Not documented; Structural writes datasets, does not manage preview DB lifecycle. |
| **Data** | Prod-derived, masked/synthesized, subsetting | “Automatically detect PII and PHI throughout your data” [source](https://www.tonic.ai/products/tonic-structural) |
| **Runs on** | Tonic Cloud or self-hosted | “Deploy a self-hosted instance of Structural, or work with your data in our Cloud offering.” [source](https://www.tonic.ai/products/tonic-structural) |
| **License** | Proprietary | Closed-source commercial service; no open-source license is published (inferred). |
| **Pricing** | Custom annual pricing by source-data volume | “Annual pricing for Tonic Structural is determined by the Plan you select and the amount of source data connected to Tonic.” [source](https://www.tonic.ai/pricing) |

Caveats:

- Tonic Ephemeral (its on-demand ephemeral database product) is no longer in Tonic's docs and its product URL redirects to the homepage; see excluded.
- No free tier listed for Structural (https://www.tonic.ai/pricing).

<a id="turso"></a>

### Turso

Managed SQLite-compatible (libSQL/Turso) databases where a branch is a separate database created from an existing one or a point-in-time snapshot; per-PR branches are scripted via the Platform API in GitHub Actions.

[Preview docs](https://docs.turso.tech/features/branching) · [Website](https://turso.tech) · [Source](https://github.com/tursodatabase/turso) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **Engine** | SQLite-compatible (Turso / libSQL) | “Fully backwards compatible with SQLite” [source](https://docs.turso.tech/introduction) |
| **How a preview DB is made** | Full copy as separate database; point-in-time option | “A branch is a separate database instance that is created from an existing database.” [source](https://docs.turso.tech/features/branching) |
| **Per-PR automation** | DIY GitHub Actions example via Platform API | “Automating branching is useful for creating a new database for each pull request.” [source](https://docs.turso.tech/features/branching) |
| **Cleanup** | No, manual deletion | “You will need to manually delete the database branch when you no longer need it.” [source](https://docs.turso.tech/features/branching) |
| **Data** | Copies source data; no anonymisation documented | “A branch is a separate database instance that is created from an existing database.” [source](https://docs.turso.tech/features/branching) |
| **Runs on** | Managed (Turso Cloud) | “Fully managed platform for Turso and libSQL databases” [source](https://docs.turso.tech/introduction) |
| **License** | Database MIT; Turso Cloud proprietary | MIT per GitHub repo license metadata; branching is a Turso Cloud feature. |
| **Pricing** | Free plan (100 DBs); branching adds no usage cost | “Point-in-time restore and database branching do not add usage cost.” [source](https://turso.tech/pricing) |

Caveats:

- Branches count towards the plan's database quota (https://docs.turso.tech/features/branching).
- The sample workflow triggers on ref creation, not PR events (https://docs.turso.tech/features/branching).

<a id="xata"></a>

### Xata

Open-source Postgres platform (Kubernetes/CloudNativePG-based) with copy-on-write branches; a GitHub App or GitHub Action creates a branch per pull request, with optional anonymised production clones.

[Preview docs](https://xata.io/docs/automations/vercel-github-app) · [Website](https://xata.io) · [Source](https://github.com/xataio/xata) · Last verified 2026-10-26

|  | Value | Evidence |
| --- | --- | --- |
| **Engine** | Postgres (vanilla) | “Xata runs vanilla PostgreSQL with high-performance storage, isolation, and instant branching built in.” [source](https://xata.io/) |
| **How a preview DB is made** | Copy-on-write branch | “Create copy-on-write database branches in seconds without duplicating storage.” [source](https://xata.io/docs) |
| **Per-PR automation** | Yes, Xata GitHub App or GitHub Action | “The Xata GitHub App creates a Xata branch for each pull request” [source](https://xata.io/docs/automations/vercel-github-app) |
| **Cleanup** | Yes, GitHub App deletes branch on PR close | “When the pull request closes, the Xata GitHub App deletes the Xata branch.” [source](https://xata.io/docs/automations/vercel-github-app) |
| **Data** | Prod clone with built-in anonymisation | “Data masking and anonymization for PostgreSQL dev and testing environments” [source](https://xata.io/postgres-data-masking) |
| **Runs on** | Managed cloud, BYOC, or self-hosted OSS | “Self-host on your own infrastructure.” [source](https://xata.io/pricing) |
| **License** | Open source (Apache-2.0); some features closed | “Xata - Open-source Postgres platform with CoW branching” [source](https://github.com/xataio/xata) |
| **Pricing** | OSS free; cloud pay-as-you-go, no per-branch fee | “No per-branch fees.” [source](https://xata.io/pricing) |

Caveats:

- Xata pivoted from its earlier serverless data platform to a branch-native Postgres platform; the OSS release runs on Kubernetes and the README says it is overkill for a single Postgres instance (https://github.com/xataio/xata).
- Some multi-tenant security features are kept closed source (https://github.com/xataio/xata).
- The documented GitHub Action workflow does not show a PR-close deletion step; the GitHub App does delete on close (https://xata.io/docs/automations/ga-pr).
- Cloud compute from $0.012/hr plus $0.28/GB-month storage; BYOC is quoted (https://xata.io/pricing).
<!-- END GENERATED: database-tools -->

Several application platforms can also provision or fork a database inside the preview itself. See the "Databases" column in the [platform comparison](../comparisons/preview-environment-platform-comparison.md).
