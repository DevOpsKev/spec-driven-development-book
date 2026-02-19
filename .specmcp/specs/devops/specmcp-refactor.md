# Spec: specmcp Refactor — Provenance Separation

## Purpose

Refactor `.specmcp/server.py` to cleanly separate provenance files from
specification files and expose provenance through dedicated MCP tools.

## Prerequisites

Before executing this spec, load the mcp-builder skill:

```
get_skill("SKILL")
```

Follow all conventions described in that skill throughout this execution.

## Context

Provenance files currently live alongside specs in `specs/editorial/` with a
`.provenance.md` suffix. This causes two problems:

1. `discover_specs()` returns provenance files mixed in with specs
2. There are no tools to query provenance directly

## Changes

### 1. Move provenance files

Move all `*.provenance.md` files from their current locations into a new
`specs/provenance/` directory, mirroring the category structure of the
specs they track:

```
.specmcp/specs/provenance/
├── editorial/
│   ├── authors-note.provenance.md
│   └── licensing.provenance.md
└── devops/
    └── (future provenance files)
```

Preserve filenames and mirror the source category directory. For example,
`specs/editorial/authors-note.provenance.md` moves to
`specs/provenance/editorial/authors-note.provenance.md`.

### 2. Update discover_specs()

Add a filter to `discover_specs()` so it skips any file whose stem ends
with `.provenance`:

```python
if md_file.stem.endswith(".provenance"):
    continue
```

### 3. Add provenance discovery

Add a `discover_provenance()` function that scans `specs/` recursively
for `*.provenance.md` files. Reuse the existing `SpecInfo` dataclass for
the return type.

### 4. Add list_provenance tool

```python
@mcp.tool()
def list_provenance() -> str:
    """List all provenance records across specs.

    Returns metadata for each provenance file found.
    """
```

### 5. Add get_provenance tool

```python
@mcp.tool()
def get_provenance(spec_name: str) -> str:
    """Get the provenance (execution history) for a specific spec.

    Pass the spec name without the .provenance suffix.
    Example: get_provenance("authors-note")
    """
```

Follow the existing error handling pattern — return an error string on
failure, never raise unhandled exceptions.

### 6. Align existing code with skill conventions

Review the full `server.py` against the mcp-builder skill (`get_skill("SKILL")`)
and align where needed:

- Ensure `discover_specs()` filters out `.provenance.md` files
- Ensure all tools return error strings on failure — never raise unhandled exceptions
- Ensure tool descriptions are precise and unambiguous
- Ensure logging goes to stderr only (stdout reserved for stdio transport)
- Ensure the `SpecInfo` dataclass follows the `ResourceInfo` pattern from the skill
- Ensure the server docstring includes usage instructions and transport info
- Ensure imports follow `from __future__ import annotations` pattern

Do not rename existing tools or change their signatures — only align
internal implementation and documentation with the skill conventions.

### 7. Verify

- [ ] `ruff check .specmcp/` passes
- [ ] `ruff format --check .specmcp/` produces no changes
- [ ] `pre-commit run --all-files` passes
- [ ] `python .specmcp/server.py` starts without error
- [ ] `list_specs` no longer returns provenance files
- [ ] `list_provenance` returns the moved provenance files
- [ ] `get_provenance("authors-note")` returns content

## Out of Scope

- Updating AGENTS.md (separate task)
- Changes to `.skillmcp` or `.brandmcp`
- Changes to any spec content

## Branch

```
spec/specmcp-refactor/provenance-separation
```
