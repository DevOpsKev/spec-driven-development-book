# Spec: skillmcp Refactor — Skill Convention Alignment

## Purpose

Validate and align `.skillmcp/server.py` against the conventions described
in the mcp-builder skill it hosts. This server was hand-built before the
skill existed — this refactor ensures it practices what it preaches.

## Prerequisites

Before executing this spec, load the mcp-builder skill:

```
get_skill("mcp-builder")
```

Follow all conventions described in that skill throughout this execution.

## Context

The `.skillmcp` server was created manually during the same session that
produced the mcp-builder skill. It was written to broadly follow the
intended pattern, but it has never been validated against the skill by
an agent. This spec closes that gap.

## Changes

### 1. Audit server.py against skill conventions

Read the full `server.py` and compare line-by-line against the mcp-builder
skill. Check every convention:

- `from __future__ import annotations` present
- Logging to stderr only (stdout reserved for stdio transport)
- `SkillInfo` dataclass follows the `ResourceInfo` pattern from the skill
- `_extract_title()` helper matches the skill template
- `discover_skills()` matches the discovery pattern from the skill
- `discover_skills()` filters out any `.provenance.md` files (future-proofing)
- `load_skill()` filters out any `.provenance.md` files (future-proofing)
- `load_skill()` returns error strings on failure — never raises unhandled exceptions to callers
- All tool functions catch exceptions and return error strings
- Tool descriptions are precise and unambiguous
- Server docstring includes usage instructions and transport info
- Entry point follows the `main()` pattern

Document every deviation found. Fix each one.

### 2. Verify tool naming

Confirm tool names follow the skill prefix convention:

| Tool | Expected Name |
|------|---------------|
| List skills | `list_skills` |
| Get skill | `get_skill` |

Do not rename tools unless they deviate from this table.

### 3. Verify requirements.txt

Confirm `.skillmcp/requirements.txt` contains `mcp` as a minimum
dependency. Add any missing dependencies.

### 4. Verify .mcp.json registration

Confirm `.mcp.json` contains the `sdd-book-skills` server entry pointing
to `.skillmcp/server.py` with stdio transport.

### 5. Write provenance

Create the provenance file for this execution at:

```
.specmcp/specs/provenance/devops/skillmcp-refactor.provenance.md
```

Overwrite (do not append). This file describes only this execution.

### 6. Verify

- [ ] `ruff check .skillmcp/` passes
- [ ] `ruff format --check .skillmcp/` produces no changes
- [ ] `pre-commit run --all-files` passes
- [ ] `python .skillmcp/server.py` starts without error
- [ ] `list_skills` returns available skills
- [ ] `get_skill("mcp-builder")` returns the mcp-builder skill content
- [ ] `get_skill("nonexistent")` returns an error string, does not raise

## Out of Scope

- Updating AGENTS.md (separate task)
- Changes to `.specmcp` or `.brandmcp`
- Adding new tools beyond `list_skills` and `get_skill`
- Changes to skill content

## Branch

```
spec/skillmcp-refactor/convention-alignment
```
