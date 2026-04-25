# Hugo Expert — Team Delegation Pattern

Complete delegation map for the Hugo Expert orchestrator. Covers all 11 master skills, 2 cross-layer agents, and the handoff conventions that connect them.

## Full Team Map

### Master Skills (invokable by Hugo Expert)

| # | Skill | Owns | Key files |
| --- | --- | --- | --- |
| 1 | `hugo-create` | Pages, layouts, partials, content types, Angular Elements | `src/website/layouts/`, `src/website/content/` |
| 2 | `hugo-design` | CSS variables, colors, images, banners, typography | `src/website/static/css/`, `src/website/static/images/` |
| 3 | `hugo-debug` | Layout bugs, UI verification, dry runs | — (reads any file, writes none) |
| 4 | `hugo-plan` | Feature planning, spec creation, stepwise execution | `docs/spec/`, `docs/features/` |
| 5 | `hugo-docs` | All doc writes, doc promotion, labs | `docs/` |
| 6 | `hugo-config` | Feature flags, site config, Bicep IaC | `hugo.toml`, `infra/` |
| 7 | `hugo-deploy` | CI/CD, GitHub Actions, SWA, OIDC | `.github/workflows/` |
| 8 | `hugo-seo` | SEO audits, structured data, Core Web Vitals | `.seo/`, meta tags |
| 9 | `hugo-maf` | Content-creator backend (agent workflows, tools, deploy, eval) | `src/content-creator-team/`, `src/api.integrations.at/` |
| 10 | `hugo-learn` | Session analysis, doc distribution, learning extraction | `.conversation/`, `docs/` |
| 11 | `hugo-mcp-reference` | MCP server capabilities reference | — (read-only) |

### Cross-Layer Agents (delegated via `hugo-maf`)

| Agent | Owns | Key files |
| --- | --- | --- |
| MAF Agent | Python agent code, Foundry project, agent prompts, tools/providers | `src/content-creator-team/` |
| .NET Expert | ASP.NET Core API, controllers, services, EF Core, DTOs | `src/api.integrations.at/` |

### Standalone Agents (not skill-routed)

| Agent | Owns |
| --- | --- |
| Angular Expert | Angular source code, Web Component builds |
| GitHub Codespaces | Dev container setup, environment configuration |

## Delegation Decision Tree

```
User request arrives
│
├── Hugo site content/layout? → hugo-create
├── Visual/CSS/images? → hugo-design
├── Something broken/looks wrong? → hugo-debug
├── Needs planning (3+ files)? → hugo-plan
├── Documentation write/update? → hugo-docs
├── Config/feature flag/infra? → hugo-config
├── CI/CD/deploy/domains? → hugo-deploy
├── SEO/meta/vitals? → hugo-seo
├── Content-creator backend? → hugo-maf
│   ├── Agent workflow/prompts/tools → hugo-maf-workflow / hugo-maf-tools
│   ├── New API endpoint/.NET service → hugo-maf-api-bridge
│   ├── Deploy container+API → hugo-maf-deploy
│   └── Eval/prompt optimization → hugo-maf-eval
├── Session review/learnings? → hugo-learn
│   ├── Analyze conversation → hugo-learn-analyze
│   └── Distribute doc updates → hugo-learn-distribute → hugo-docs
├── Angular source code? → Angular Expert (direct)
└── Ambiguous? → hugo-expert (self — ask clarifying question)
```

## Handoff Conventions

### Docs Handoff (mandatory)

Any skill or agent that edits files under `docs/`, `docs/spec/`, agent files, or skill routing docs **must** produce a handoff block:

```
## Docs Agent Handoff

**Files changed:**
- {file} — {what changed}

**Why:** {reason}

**Action:** @hugo-documentation verify changes and update cross-references.
```

See `hugo-docs` → `docs-handoff-convention` for full spec.

### .NET ↔ MAF Handoff (for content-creator work)

| Scenario | From → To | Payload |
| --- | --- | --- |
| New API endpoint needed | MAF Agent → .NET Expert | Endpoint path, request/response DTO shape |
| Agent JSON output changed | MAF Agent → .NET Expert | Updated JSON schema |
| New FoundryAgents config | .NET Expert → MAF Agent | Agent name, model, endpoint |
| New external service config | MAF Agent → .NET Expert | Config section + keys |
| Deploy | Either → Both verify | Coordinate container + API |

### Learn/Analyze Handoff (post-session)

After sessions that produced significant changes, invoke `hugo-learn`:
1. `hugo-learn-analyze` reviews the session for patterns and gaps
2. `hugo-learn-distribute` produces docs handoff blocks for each affected doc
3. `hugo-docs` receives and executes the doc updates

## Parallel Dispatch Rules

| Agents | Can run in parallel? | Condition |
| --- | --- | --- |
| hugo-create + hugo-design | Yes | Always (different file domains) |
| hugo-create + hugo-deploy | Yes | Unless deploy depends on new layout |
| MAF Agent + .NET Expert | Yes | When working on independent files; No when sharing a JSON contract |
| hugo-learn-analyze + hugo-docs | No | Analyze must complete before distribute triggers docs |

## Handoff Context Block (Mandatory)

Every delegation from the orchestrator (Hugo Expert) to any specialist agent or skill **must** include a Handoff Context Block. This ensures the receiving agent reads the right docs instead of searching from scratch.

### Format

```
## Handoff Context

**Task:** [one-line description]
**Scope:** [what this is about — e.g., "Hugo CMS backend, MAF + .NET bridge"]

**Read first (mandatory):**
1. `docs/spec/hugo-content-creators/readme.md` — current phase status
2. `docs/spec/hugo-content-creators/api-integration.spec.md` — API contracts
3. `docs/tooling-agent-team.md` — team ownership map

**Do NOT search for:** [scope exclusions — e.g., "Azure Functions, Hugo site layouts"]

**Goal:** [what done looks like]
```

### Rules

1. Every handoff includes 2–5 doc references under "Read first"
2. The receiving agent's **first action** is to read every file listed — before any `grep_search`, `semantic_search`, or `file_search`
3. If no spec exists for the task, the orchestrator must state: "No existing spec — create from scratch" and still pass `docs/basics-project-structure.md` as baseline context
4. Priority for the receiving agent: **docs → specs → inform user if a doc/spec is missing or outdated**
5. "Do NOT search for" prevents agents from wasting tokens exploring unrelated code

### Doc-Reference Lookup Table

The orchestrator uses this table to select which docs to include per task type:

| Task type | Always include in handoff |
| --- | --- |
| Hugo templates/layouts | `docs/content-layout-patterns.md`, `docs/content-template-boilerplate.md` |
| CSS/design | `docs/design-design-system.md` |
| Content-creator backend (MAF) | `docs/spec/hugo-content-creators/readme.md`, `docs/tooling-agent-team.md` |
| Content-creator API (.NET) | `docs/spec/hugo-content-creators/api-integration.spec.md`, `docs/tooling-agent-team.md` |
| Infrastructure/Bicep | `docs/basics-infra-configuration.md` |
| CI/CD/deploy | `docs/basics-infra-configuration.md` |
| Doc writes/updates | Target doc + `docs/readme.md` (for cross-refs) |
| Session analysis | `.conversation/analysis/patterns.json`, `docs/tooling-agent-learning-loop.md` |
| Feature planning | `docs/spec/{name}/readme.md` (if exists), `docs/content-layout-patterns.md` |
| SEO | `docs/seo-audit-system.md` |

## Anti-Patterns

| Don't | Do instead |
| --- | --- |
| Pre-read files before delegating to a specialist | Describe the problem + goal, let the specialist diagnose |
| Delegate without doc references | Always include 2–5 docs in the Handoff Context Block |
| Edit `docs/` directly from a non-docs agent | Produce a docs handoff block, let hugo-docs write |
| Send .NET API work directly to .NET Expert | Route through hugo-maf for contract coordination |
| Skip hugo-learn after convention changes | Always run analyze + distribute to catch gaps |
| Chain sequential dispatches without confirming dependency | Default to parallel; only serialize on explicit data dependency |
| Search the codebase before reading handoff docs | Read the "Read first" docs, then search only for gaps |
