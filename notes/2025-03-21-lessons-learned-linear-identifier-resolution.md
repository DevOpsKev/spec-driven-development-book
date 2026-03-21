# Lessons Learned: Linear Identifier Resolution Fix

**Date:** 2025-03-21
**Participants:** Kevin Ryan, HQ
**Area:** HQ Linear Integration / System Prompt Engineering

## Context

HQ's Linear integration silently failed when using short identifiers (e.g. `KRA-5`) for write operations like `update_linear_issue`, `add_linear_comment`, and `list_linear_comments`. The underlying `resolveLinearIssueId()` function used a filter query that returned zero results without raising an error. Writes appeared to succeed but never persisted.

## Root Cause

The Linear API's `issues(filter: { identifier: { eq: "KRA-5" } })` query does not support filtering by the `identifier` field. It returned an empty result set with no error. The code treated "no error" as "success", and callers had no indication the resolution had failed.

## Fix Journey

1. **Diagnosed** — Tested assignment, comments, and reads. Mapped what worked (UUIDs) vs what didn't (short identifiers).
2. **Prompt-as-bandage** — Added a Known Limitations section to the system prompt instructing HQ to resolve short identifiers to UUIDs via search before write operations. Deployed immediately.
3. **Code fix attempt 1** — Replaced filter query with `issueSearch(query: "KRA-5")`. Didn't work — `issueSearch` only searches title/description text, not identifiers.
4. **Code fix attempt 2** — Parsed the short identifier into team key and number, then queried `issues(filter: { number: { eq: 5 }, team: { key: { eq: "KRA" } } })`. This worked.
5. **Prompt cleanup** — Removed the Known Limitations workaround from the system prompt now that the code fix was deployed and verified.

## Key Lessons

### 1. Silent failures are the worst kind

The Linear API returned success with zero results instead of an error. No exception, no warning. The code assumed "no results = not found" but the caller assumed "no error = success". Always validate that an API response contains the expected data — do not treat the absence of an error as confirmation of success.

### 2. System prompt and tooling must be in sync

The system prompt said short identifiers work. The tool descriptions said short identifiers work. The actual API call behind them silently failed. The system prompt is only as good as the reality it describes. When tooling behaviour changes or breaks, the prompt must reflect that immediately.

### 3. Prompt-as-bandage, code-as-fix, prompt-cleanup-after

When something doesn't work:

1. **Document the workaround in the prompt immediately** — this is the fastest deployment path and unblocks operations within minutes
2. **Fix the code** — address the root cause properly
3. **Clean up the prompt** — remove the workaround once the fix is verified

This pattern is quick to deploy, safe to iterate, and leaves no permanent hacks in the system.

### 4. Test the actual flow, not the assumption

We only discovered the bug by trying to use the feature end-to-end: assign a user, write a comment, read comments. Unit-level assumptions ("the API supports identifier filters") were wrong. Integration-level testing caught it.

### 5. Check the docs before guessing

The working fix — filtering by `number` + `team.key` — is a documented pattern used by multiple Linear integrations. The first attempt (`issueSearch`) was a guess. Ten minutes of research would have saved a failed deploy.

## Artefacts

- **System prompt:** `config/hq-system-prompt.md`
- **Code fix:** `src/app/api/chat/route.ts` — `resolveLinearIssueId()` function
- **Linear issue:** KRA-5 — Linear App registration (replace PAT)