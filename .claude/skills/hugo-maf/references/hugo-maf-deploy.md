# hugo-maf-deploy — Agent + API Deployment

## When to Use

- Deploying the content-creator container and .NET API together
- Rebuilding the container after code changes
- Verifying post-deploy health of both services
- Fixing RBAC or container sizing issues
- First-time provisioning with `azd up`

## Prerequisites

- Azure CLI authenticated (`az login`)
- `azd` CLI installed
- Docker (for local container builds)
- Access to `agentic-hugo` Foundry project

## Key Files

| File | Purpose |
| --- | --- |
| `agent.yaml` (repo root) | Docker build path, CPU/memory for ACR + Foundry provisioning |
| `src/content-creator-team/agent.yaml` | Agent schema metadata for VS Code Foundry extension |
| `src/content-creator-team/Dockerfile` | Container definition |
| `src/content-creator-team/requirements.txt` | Python dependencies |
| `docs/spec/hugo-content-creators/deployment.spec.md` | Full deployment spec |

## Deploy Commands

```bash
# First time (provision + deploy)
azd up

# Subsequent (rebuild container only)
azd deploy

# Monitor logs
azd ai agent monitor

# Show status
azd ai agent show
```

Note: `azd ai agent deploy` does not exist. Use `azd deploy`.

## Deployment Checklist

### Pre-deploy
1. Both `agent.yaml` files declare matching `resources` values (e.g. `2.0 vCPU / 4 GiB`)
2. `requirements.txt` is up to date with all new dependencies
3. `.env` keys for new external services are set
4. If new `FoundryAgents` config was added, `appsettings.json` is updated

### Deploy
5. Run `azd deploy` (or `azd up` for first time)
6. Wait for container build and push to ACR

### Post-deploy
7. Verify agent is responding: `azd ai agent show`
8. Test via `.http` file: `POST api/content/optimize` with sample payload
9. Check logs for errors: `azd ai agent monitor`
10. Verify .NET API is up and can reach the hosted agent

## RBAC Requirements

The container's managed identity needs **Azure AI User** role on the CognitiveServices account:

```bash
az role assignment create \
  --assignee "<managed-identity-object-id>" \
  --role "Azure AI User" \
  --scope "/subscriptions/.../providers/Microsoft.CognitiveServices/accounts/agentic-hugo-cms"
```

## Container Sizing

Valid CPU/memory pairs (fixed 1:2 ratio):

| vCPU | Memory |
| --- | --- |
| 0.5 | 1.0Gi |
| 1.0 | 2.0Gi |
| 2.0 | 4.0Gi |
| 4.0 | 8.0Gi |

## Common Issues

| Symptom | Cause | Fix |
| --- | --- | --- |
| `No such file '/app/main.py'` | Wrong COPY context in Dockerfile | `COPY src/content-creator-team/ .` |
| `PermissionDenied` on agents/write | Missing RBAC | Assign Azure AI User role |
| Container OOM | Undersized resources | Bump to next CPU/memory pair |
| .NET can't reach agent | Config mismatch | Verify `FoundryAgents` AgentName matches `agent.yaml` |

## Spec Reference

Full deployment spec: [deployment.spec.md](../../../docs/spec/hugo-content-creators/deployment.spec.md)
