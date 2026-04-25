# hugo-release-feature

Release a completed feature into permanent documentation.

## When to Use
- A feature is fully implemented and should move from spec state into permanent docs
- Consolidates `docs/spec/<name>/` into `docs/<name>.md`
- Or syncs an existing `docs/<name>.md` and registers it in `docs/readme.md`
- Triggers `hugo-learn` to distribute the updated reference to all agents

## Release Modes

| Mode | Source | Result |
| --- | --- | --- |
| Spec-folder release | `docs/spec/<name>/` | Integrate multiple `*.spec.md` files into `docs/<name>.md` |
| Existing-doc sync | `docs/<name>.md` | Verify, refresh, and register the existing permanent doc |

## Workflow

### 1. Read the Source Material

Read the input for the selected mode.

| Mode | Read |
| --- | --- |
| Spec-folder release | Every `*.spec.md` in `docs/spec/<name>/` |
| Existing-doc sync | `docs/<name>.md` |

Capture the referenced files, selectors, data attributes, front matter fields, and any open implementation claims that must be checked.

### 2. Verify Against the Codebase

Verify every important claim against the actual implementation before writing the released doc.

| Claim type | Where to verify in this repo |
| --- | --- |
| Hugo layouts and partials | `src/integrations.at/layouts/` |
| CSS classes and variables | `src/integrations.at/assets/css/` |
| JavaScript runtime | `src/integrations.at/assets/js/` and inline scripts in layouts |
| Content schema and front matter | `src/integrations.at/content/` |
| Site config and params | `src/integrations.at/hugo.toml` |
| Static assets | `src/integrations.at/static/` |

Update stale paths, class names, data attributes, field names, and examples to match the code.

### 3. Write or Refresh `docs/<name>.md`

For spec-folder release mode, integrate the spec files into one permanent doc.

Recommended structure:

```markdown
# {Feature Name}

Short intro.

| Section | Description |
| --- | --- |
| ... | ... |

## Overview
...

## Implementation
...

## How to use hugo-* skills
...
```

For existing-doc sync, use the current permanent doc as the base and refresh it so it matches the code.

### 4. Update `docs/readme.md`

Register the released doc in the main table of contents and remove stale draft entries when applicable.

| Action | When |
| --- | --- |
| Add or refresh the row for `docs/<name>.md` | All modes |
| Remove the matching row from `## Planned Features` | When the feature was tracked as planned |
| Replace references to `docs/spec/<name>/` | When older links still exist |

### 5. Verify Cross-References

Search for links to the old source path and update them.

| Old path pattern | New target |
| --- | --- |
| `docs/spec/<name>/...` | `docs/<name>.md` when the specific spec file is no longer the canonical reference |

### 6. Call `hugo-learn`

After the permanent doc is written and registered, call `hugo-learn` with:

- The released doc path: `docs/<name>.md`
- A short summary of what the feature introduces or changes
- The agents, skills, or docs likely affected

## Completion Checklist

- [ ] Source docs or spec files read
- [ ] Important claims verified against the current codebase
- [ ] `docs/<name>.md` written or refreshed
- [ ] `docs/readme.md` updated
- [ ] Old links updated
- [ ] `hugo-learn` invoked
