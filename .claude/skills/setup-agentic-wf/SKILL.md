---
name: setup-agentic-wf
description: Set up GitHub Agentic Workflows for SuperLeague.TV site monitoring. Guides installation of gh-aw CLI, authentication with repo scope, repository initialization, Copilot token creation, and workflow compilation. Use when deploying automated workflows like web-performance-monitor for Core Web Vitals tracking.
---

# Set Up GitHub Agentic Workflows

Complete setup guide for GitHub Agentic Workflows in the SuperLeague.TV repository, including CLI installation, authentication, token creation, and workflow compilation.

## Prerequisites

- GitHub CLI installed ([download](https://github.com/cli/cli/releases))
- GitHub account with access to the target repository
- Administrator or maintainer permissions for the repository

## Step-by-Step Setup

### 1. Install the gh-aw extension

```bash
gh auth login
gh extension install github/gh-aw
```

### 2. Check and update your gh CLI authentication scopes

The automated token creation step requires `repo` scope. Check your current scopes:

```bash
gh auth status
```

Expected output shows your scopes. Look for `repo` in the list.

**If `repo` is not listed**, re-authenticate:

```bash
gh auth logout
gh auth login
```

Follow the prompts:

- Choose your GitHub host (`github.com`)
- Choose protocol (`HTTPS` or `SSH`)
- When asked "How would you like to authenticate?", select **"Login with a web browser"**
- Authorize in the browser (it will automatically request `repo` scope among others)

Verify the scope is now present:

```bash
gh auth status
```

### 3. Initialize the repository (one-time)

From the repository root, set up agentic workflows:

```bash
gh aw init
```

This creates:

- `.github/aw/` folder
- `actions-lock.json` — dependency lock file for agentic workflows (similar to `package-lock.json`)

Commit these files to your repository.

### 4. Create and set the Copilot token

Choose one option:

**Option A: Manual (recommended for first-time setup)**

1. Visit [github.com/settings/tokens](https://github.com/settings/tokens)
2. Click "Generate new token" → "Generate new fine-grained personal access token"
3. Configure scopes:
   - **Repository access**: Select your target repository
   - **Permissions**:
     - `Actions` (read)
     - `Contents` (read)
4. Generate and copy the token
5. Add it as a repository secret:

```bash
gh secret set COPILOT_GITHUB_TOKEN --body "<your-token>" --repo <owner>/<repo>
```

**Option B: Semi-automated (using GitHub API)**

If your gh CLI is authenticated with `repo` scope (from step 2), create and set in one command:

```bash
TOKEN=$(gh api POST /user/personal-access-tokens \
  -f name="COPILOT_GITHUB_TOKEN_$(date +%s)" \
  -f owner="<owner>" \
  -f repositories="[\"<repo>\"]" \
  -f permissions='{"actions":"read","contents":"read"}' \
  --jq '.token')

gh secret set COPILOT_GITHUB_TOKEN --body "$TOKEN" --repo <owner>/<repo>
```

### 5. Compile workflows

After any edit to a `.md` workflow file, regenerate the executable `.lock.yml`:

```bash
gh aw compile
```

> **Important**: Always run `gh aw` commands from the **repository root**. The CLI looks for `.github/workflows/` relative to your current working directory.

## Verify Setup

Check that workflows are compiled and ready:

```bash
gh aw status
```

Expected output shows compiled workflows with their status.

## Running a Workflow

Once setup is complete, manually trigger a workflow:

```bash
cd <repository-root>
gh aw run <workflow-name>
```

Example: `gh aw run web-performance-monitor`

## Common Workflows

| Workflow                  | Purpose                                              | Command                             |
| ------------------------- | ---------------------------------------------------- | ----------------------------------- |
| `web-performance-monitor` | Daily Core Web Vitals audit on superleague.tv pages | `gh aw run web-performance-monitor` |

## Troubleshooting

| Issue                             | Solution                                                          |
| --------------------------------- | ----------------------------------------------------------------- |
| `workflow not found`              | Ensure you're running from the repo root, not a subdirectory      |
| `permission denied`               | Your gh CLI token lacks `repo` scope; re-authenticate with step 2 |
| `Compiled: N/A` in `gh aw status` | Run `gh aw compile` after editing any `.md` workflow file         |
| `COPILOT_GITHUB_TOKEN not found`  | Verify the secret was created: `gh secret list`                   |

## Related Documentation

- [seo-vitals.md](../../docs/seo-vitals.md) — Core Web Vitals monitoring workflow details
- [GitHub Agentic Workflows Documentation](https://github.github.com/gh-aw/introduction/overview/)
- [GitHub CLI Manual](https://cli.github.com/manual/)
