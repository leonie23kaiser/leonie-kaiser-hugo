# hugo-maf-api-bridge — .NET ↔ Python Contract Bridge

## When to Use

- Adding a new API endpoint that calls the hosted agent (e.g. `POST /content/article`)
- Changing the JSON output format of an agent and updating the .NET deserialization
- Adding a new `FoundryAgents` config entry for a new agent
- Ensuring request DTOs, response DTOs, and agent JSON output stay in sync

## Prerequisites

- Understanding of the handoff triggers documented in `docs/tooling-agent-team.md` § ".NET ↔ MAF Agent Collaboration"
- Access to both `src/api.integrations.at/` and `src/content-creator-team/`

## Key Files

| Side | File | Purpose |
| --- | --- | --- |
| .NET | `src/api.integrations.at/Controllers/ContentController.cs` | API endpoints |
| .NET | `src/api.integrations.at/Services/ContentService.cs` | Calls hosted agent, deserializes response |
| .NET | `src/api.integrations.at/Core/AppConfig.cs` | `FoundryAgentConfig` record |
| .NET | `src/api.integrations.at/appsettings.json` | `FoundryAgents` section |
| .NET | `src/api.integrations.at/Program.cs` | DI registration |
| Python | `src/content-creator-team/main.py` | Agent router, output format |
| Spec | `docs/spec/hugo-content-creators/api-integration.spec.md` | Full contract spec |

## The Bridge Pattern

Every hosted agent operation follows this flow:

```
.NET Controller → .NET Service → AIProjectClient → Hosted Agent (Python) → JSON response → .NET Service deserializes
```

The JSON contract is the bridge. Both sides must agree on field names and types.

## Adding a New Endpoint (Step-by-Step)

### 1. Define the contract (both sides)

Agree on request and response shapes:

```json
// Request (from .NET to agent)
{ "operation": "create-article", "keyword": "...", "pillar": "...", "audience": "..." }

// Response (from agent to .NET)
{ "article": "...", "seoMeta": {...}, "socialPosts": {...}, "usage": {...} }
```

### 2. Python side (MAF Agent owns)

Update the operation router in `main.py` to handle the new operation and return the agreed JSON.

### 3. .NET side (.NET Expert owns)

a. Add request/response DTOs:
```csharp
public record CreateArticleRequest(string Keyword, string Pillar, string Audience);
public record CreateArticleResponse(string Article, SeoMeta SeoMeta, SocialPosts SocialPosts, UsageSummary Usage);
```

b. Add service method in `ContentService.cs`:
```csharp
public async Task<CreateArticleResponse> CreateArticleAsync(CreateArticleRequest request) { ... }
```

c. Add controller action in `ContentController.cs`:
```csharp
[HttpPost("article")]
public async Task<IActionResult> CreateArticle(CreateArticleRequest request) { ... }
```

d. Add `.http` test file entries.

### 4. Config (if new agent needed)

Add to `appsettings.json`:
```json
"FoundryAgents": {
  "ContentCreator": { "ProjectEndpoint": "...", "AgentName": "hugo-content-creator" }
}
```

Register named options in `Program.cs`.

### 5. Update spec

Update `api-integration.spec.md` with the new endpoint contract.

## Existing Endpoints

| Endpoint | Operation | Status |
| --- | --- | --- |
| `POST api/content/optimize` | `optimize` | Code complete |
| `POST api/content/translate` | `translate` | Code complete |
| `POST api/content/article` | `create-article` | Phase 3 (planned) |

## Handoff Triggers

| Scenario | From → To |
| --- | --- |
| Agent JSON output format changes | MAF Agent → .NET Expert |
| New API endpoint needed | MAF Agent → .NET Expert |
| New `FoundryAgents` config entry | .NET Expert → MAF Agent |
| Provider needs .NET-side config | MAF Agent → .NET Expert |

## Spec Reference

Full API contracts: [api-integration.spec.md](../../../docs/spec/hugo-content-creators/api-integration.spec.md)
