# hugo-maf-tools — Provider Interfaces & External Tools

## When to Use

- Implementing a new provider interface in `tools/providers/`
- Swapping a vendor (e.g. Nimble → Tavily, or vice versa)
- Configuring a File Search vector store for knowledge grounding
- Adding a new external tool to an agent
- Reviewing tool costs or the provider abstraction pattern

## Prerequisites

- API keys in `src/content-creator-team/.env` and `src/api.integrations.at/appsettings.Development.json`
- Provider abstraction convention understood (see below)

## Key Files

| File | Purpose |
| --- | --- |
| `src/content-creator-team/tools/providers/` | Provider interface implementations |
| `src/content-creator-team/.env` | API keys (NIMBLE_API_KEY, FIRECRAWL_API_KEY) |
| `src/api.integrations.at/appsettings.Development.json` | .NET-side API key config |
| `docs/spec/hugo-content-creators/tools-and-skills.spec.md` | Full tool spec per agent per phase |

## Provider Abstraction Principle

**All paid external tools MUST be behind a provider interface.** The agent calls a fixed contract; the implementation picks the vendor.

```
Agent → web_search(query) → Provider → Nimble / Tavily / ...
Agent → url_extract(url) → Provider → Nimble / Firecrawl / ...
Agent → knowledge_search(query) → File Search vector store
```

### Cost Growth Strategy

```
Free tier → Pay-as-you-go → Monthly plan
```

Never commit to monthly costs before the pipeline generates revenue.

## Current Providers (Phase 3)

| Provider function | Current vendor | Tier | Unit cost |
| --- | --- | --- | --- |
| `web_search` | Nimble Search API | PAYG | $1.00/1K search inputs |
| `url_extract` | Nimble Extract API (Firecrawl fallback) | PAYG | $0.90–1.45/1K URLs |
| `knowledge_search` | Foundry File Search | Free (1 GB) | $0.11/GB/day after 1 GB |

## Implementing a New Provider

1. Create `src/content-creator-team/tools/providers/<name>.py`
2. Expose a function tool with the standard contract:
   ```python
   @tool
   def web_search(query: str) -> str:
       """Search the web for current information."""
       # Implementation calls Nimble, Tavily, etc.
   ```
3. Import in `tools/providers/__init__.py`
4. Wire into the agent's `tools=[...]` list in `main.py`
5. Add API key to `.env` and `appsettings.Development.json`
6. Update the tools table in `tools-and-skills.spec.md`
7. If the .NET API needs the config, hand off to .NET Expert

## File Search Vector Store Setup

```python
from azure.ai.projects import AIProjectClient

# Create vector store
vector_store = await client.agents.create_vector_store(
    name="integrations-at-knowledge",
    file_ids=[...],  # uploaded content files
)

# Attach to agent
FileSearchTool(vector_store_ids=[vector_store.id])
```

- Auto-chunking: 800 tokens, 400 overlap
- Hybrid search + reranking
- 1 GB free, $0.11/GB/day after

## Swapping a Vendor

1. Write the new implementation in the provider file
2. Keep the old implementation as fallback (feature flag or env var)
3. Test with a sample query
4. Update the provider table in the spec
5. Update `.env` with new API key if needed

## Spec Reference

Full tool tables and config: [tools-and-skills.spec.md](../../../docs/spec/hugo-content-creators/tools-and-skills.spec.md)
