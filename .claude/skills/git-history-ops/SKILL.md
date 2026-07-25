---
name: git-history-ops
description: >-
  Recover from messy git situations: a push rejected for a too-large file (rewrite history with
  git filter-repo), conflicts caused by squash-merge divergence, moving uncommitted WIP onto a clean
  branch, isolating work in a worktree so you don't entangle someone's WIP, and safely completing an
  incomplete refactor. Project-agnostic. Triggers on: "push rejected", "GH001 large files",
  "file too large for github", "remove file from git history", "filter-repo", "rewrite git history",
  "squash merge conflict", "merge conflict but my changes are additive", "branch is behind/diverged",
  "move my WIP to a branch", "isolate changes in a worktree", "shrink .git".
---

# Git history & branch surgery

Practical recoveries for the git messes that block a push or a merge. **History rewrites change every
commit hash** — safe when the remote is empty or the branch is yours; coordinate first if others pulled.

## Push rejected: a file is over GitHub's 100 MB limit (`GH001 ... pre-receive hook declined`)

The blob is **in history**, so gitignoring it now isn't enough — you must remove it from every commit.

```bash
# 1) find the big blobs
git rev-list --objects --all | git cat-file --batch-check='%(objecttype) %(objectsize) %(rest)' \
  | awk '/^blob/{print $2, $3}' | sort -rn | head

# 2) PRESERVE the file out-of-band first (filter-repo also drops it from the working tree)
mv path/to/huge.bin ../_archive/        # instant rename if same volume

# 3) strip it from all history (git-filter-repo; falls back to BFG if unavailable)
git filter-repo --path path/to --invert-paths --force
#    NOTE: filter-repo REMOVES the 'origin' remote afterward (safety). Re-add it:
git remote add origin <url>

# 4) gitignore it going forward, commit, push
printf 'path/to/\n*.bin\n' >> .gitignore && git add .gitignore && git commit -m 'gitignore large artifacts'
git push -u origin master
```

Real case: a 3.6 GB Hyper-V VM export bloated `.git` to 1.9 GB and blocked the push; filter-repo took
it to 23 MB. Keep big binaries (VM disks, DB dumps, media) out of git entirely.

## Squash-merge divergence: conflicts even though your changes are purely additive

If you branched off a commit that **later landed on the default branch as a *squash*** (different
hash, same content), git's 3-way merge sees both sides "modifying" the squashed files → conflicts,
and `gh pr merge` reports "merge conflicts". Don't fight it — **rebase your additive work onto the
current default branch and re-apply only your files**:

```bash
git fetch origin master
git reset --hard origin/master            # on your feature branch; loses the divergent base
git checkout <old-branch-tip> -- <your file1> <your dir2> ...   # bring back ONLY your changes
git commit -m '...'
git push --force-with-lease
```

`git branch --merged` is unreliable for squash-merged branches (they look "unmerged"); judge
staleness by **PR state** instead: `gh pr list --state all --json headRefName,state,mergedAt`.

## Move uncommitted WIP onto a clean branch (when local default branch has diverged)

```bash
git stash push -m wip
git checkout -B feature origin/master     # clean base
git stash apply                           # 3-way applies your WIP; resolve any conflict
# ... commit, push, PR ...
git stash drop                            # once it's safely committed
```

## Isolate work so you don't commit someone else's WIP

If the repo has uncommitted local changes that aren't yours, do **additive** work in a linked worktree
off the committed HEAD and commit only your files — never `git add -A` over a dirty index:

```bash
git config core.longpaths true            # Windows: committed bin/ paths blow past MAX_PATH
git worktree add /short/path -b mybranch HEAD   # use a SHORT path on Windows
```

## Completing an incomplete refactor safely

A half-done WIP can delete a symbol but leave references that break the build (e.g. `SeedData.cs`
deleted, but two test files still call it). Before committing such a change, **grep for the removed
symbol** and remove/fix the orphans too; let the CI/Docker build be the backstop. Also drop incidental
churn (regenerated `bin/`/`obj/` artifacts) from the commit — `git checkout origin/master -- <those>`.
