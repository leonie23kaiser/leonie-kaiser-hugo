---
name: agent-learning-loop
description: Analyze GitHub Copilot conversation artifacts and existing `.conversation/analysis` outputs to identify routing mistakes, incomplete skill output, repeated retries, and follow-up actions. Use when reviewing a Copilot session, generating learnings from `.conversation/data`, or updating the session learning docs without relying on Claude-specific hook files.
---

# Agent Learning Loop

Use this skill for GitHub Copilot session review and learning extraction.

## When to Use This Skill

- A Copilot session finished and you want to review what happened
- You have `.conversation/data` session files and want structured learnings
- You want to update `.conversation/analysis/patterns.json` from existing Copilot artifacts
- You need to inspect whether a skill choice or follow-up edit pattern should become a docs or skill update

## Supported Inputs

- `.conversation/data/history-*.json`
- `.conversation/data/tools-*.json`
- `.conversation/data/agents-*-*.json`
- Existing `.conversation/analysis/patterns.json`
- Existing `.conversation/analysis/*-learnings.md`

## Workflow

1. Check whether `.conversation/data` exists.
2. If it exists, read the relevant session files and reconstruct the session timeline.
3. Identify repeated edits, tool retries, wrong routing, or manual cleanup after a skill-like action.
4. Update or create the learnings output under `.conversation/analysis/` only when the user asks for the results to be persisted.
5. If the findings imply a documentation or skill change, update the corresponding `.github/skills/` or `docs/` file directly.

## Constraints

- Do not rely on `.claude/settings.json` or `.claude/hooks/` for GitHub Copilot session capture.
- Prefer GitHub Copilot repo customizations under `.github/agents/`, `.github/skills/`, `.github/copilot-instructions.md`, and MCP tools.
- If `.conversation/data` is missing, report that there is no Copilot session artifact to analyze instead of inventing one.
