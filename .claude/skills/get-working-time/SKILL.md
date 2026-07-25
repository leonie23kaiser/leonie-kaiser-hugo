---
name: get-working-time
description: Calculate actual working time for the current git repo from commit history plus working-tree file mtimes, sessionized with idle-gap splitting (default 2h threshold) and a per-user breakdown. Generates a chronological markdown table with sessions, contributors, and cumulative times. Use when asked how much time was spent, working hours, effort, or time tracking on a repository.
---

# get-working-time

Analyze git commit history to calculate actual working time, accounting for idle periods (sleep, breaks). Generates chronological markdown table with sessions, contributors, and cumulative times.

## Usage

```bash
# Analyze current project (always outputs markdown table)
get-working-time

# With custom idle threshold (default 2 hours)
get-working-time --threshold 3h

# Show summary-only (no table)
get-working-time --summary-only
```

## Output

**Chronological Markdown Table (always included):**

| Timestamp | Author | Hash | Message | Session | Cumulative |
|-----------|--------|------|---------|---------|------------|
| Jun 4 19:59 | Alexander Kastil | `3895c7b` | initial | 1 | 0m |
| Jun 4 20:20 | Alexander Kastil | `4132096` | feat: implement family tree with CRUD... | 1 | 21m |
| Jun 4 21:00 | Alexander Kastil | `9537da8` | feat(login): add login component with... | 1 | 1h 0m |
| Jun 5 00:36 | Alexander Kastil | `569fc9a` | Feat/family tree ui (#1) | 1 | 5h 37m |
| Jun 5 08:46 | Alexander Kastil | `ad16e91` | feat(family-tree): merge force-layout... | 2 | 0m |
| Jun 5 13:09 | Alexander Kastil | `7b6d857` | feat: add user system, AI credits, an... | 2 | 4h 23m |

**Session Summary:**

| Session | Duration | Time Range |
|---------|----------|-----------|
| 1 | 5h 37m | Jun 4 19:59 → 00:36 |
| 2 | 4h 23m | Jun 5 08:46 → 13:09 |

**Stats:**
- Total working time: 9h 0m
- Contributors: 1 (Alexander Kastil)
- Total commits: 18

## How it works

1. Extracts all commits with timestamps, committer, hash, and message
2. Calculates time between consecutive commits
3. Identifies "idle" periods (gaps > threshold, default 2 hours)
4. Splits work into sessions separated by idle periods
5. Outputs markdown table with chronological entries and cumulative session time per contributor
