---
name: hugo-maf
description: >-
  Master skill for the content-creator multi-agent backend on Azure AI Foundry and api.integrations.at.
  Delegates to the correct leaf skill based on what needs to be built, wired, deployed, or evaluated.
  Use when working on agent workflows, tool/provider wiring, .NET↔Python API bridge, deployment,
  or evaluation for the content-creator-team.
  Triggers on: "content creator", "article pipeline", "hosted agent", "content team", "agent workflow",
  "maf agent", "foundry agent", "content-creator-team".
license: Complete terms in LICENSE.txt
---

# hugo-maf — Content Creator Backend Router

Routes content-creator backend requests to the appropriate leaf skill. Do not implement directly — delegate immediately.

## When to Use This Skill

- Adding or editing agents in the content-creator-team Python project
- Wiring external tools or provider interfaces (Nimble, Firecrawl, File Search)
- Bridging JSON contracts between the Python agent and the .NET API
- Deploying the agent container and API together
- Running evaluations or prompt optimization on the hosted agent

**Trigger keywords:** `content creator`, `article pipeline`, `agent workflow`, `hosted agent`, `maf`, `foundry agent`, `content-creator-team`, `researcher`, `publisher`

## Delegate Map

| Request type | Leaf skill to invoke |
| --- | --- |
| Add/edit agents, change workflow topology, HITL gates, retry logic | `hugo-maf-workflow` |
| Wire providers, swap vendors, configure File Search vector stores | `hugo-maf-tools` |
| Coordinate .NET ↔ Python contracts, new API endpoints, DTOs | `hugo-maf-api-bridge` |
| Deploy container + API, `azd up`, verify post-deploy health | `hugo-maf-deploy` |
| Eval datasets, batch eval, prompt optimization, compare runs | `hugo-maf-eval` |

> If the request is ambiguous or spans multiple concerns, pick the dominant concern and delegate. If it truly spans all, break it into sequential steps across leaf skills.

## Project Context

| Component | Location |
| --- | --- |
| Agent source (Python) | `src/content-creator-team/` |
| API source (.NET) | `src/api.integrations.at/` |
| Specs | `docs/spec/hugo-content-creators/` |
| Agent team doc | `docs/tooling-agent-team.md` |
| Foundry project | `agentic-hugo` on `agentic-hugo-cms.services.ai.azure.com` |
| Model | `gpt-4.1` |

## Owning Agents

- **MAF Agent** (`.github/agents/maf.agent.md`) — Python agent code, Foundry management
- **.NET Expert** (`.github/agents/dotnet.agent.md`) — API controllers, services, DTOs

Both agents have documented handoff triggers. See `docs/tooling-agent-team.md` § ".NET ↔ MAF Agent Collaboration".

## Docs Handoff

When any leaf skill updates `docs/spec/hugo-content-creators/`, `docs/tooling-agent-team.md`, or agent files, produce a docs agent handoff block. See `hugo-docs` → [`docs-handoff-convention`](./../hugo-docs/references/docs-handoff-convention.md).

## Example Prompts

- "Add a Researcher agent to the content-creator workflow."
- "Wire Nimble Search as the web_search provider."
- "Add a POST /content/article endpoint with the matching .NET service."
- "Deploy the latest content-creator container and verify."
- "Run a batch eval on the Writer agent prompts."
