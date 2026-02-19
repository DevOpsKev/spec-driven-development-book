# Provenance: specmcp-refactor

## 2026-02-19 — Separate provenance files from specs in specmcp server

**Prompt:** Execute the `specmcp-refactor` spec. Read the spec with
`get_spec("specmcp-refactor")`, then refactor `.specmcp/server.py` to separate
provenance files from specification files and expose provenance through dedicated
MCP tools. Record a provenance entry in
`provenance/devops/specmcp-refactor.provenance.md`. Commit the changes and push
the branch.

**Branch:** claude/refactor-specmcp-XBSaG
**Commit(s):** (included in this commit)

### Actions taken

1. Read the specmcp-refactor spec, provenance convention, and mcp-builder skill.
2. Created `specs/provenance/editorial/` and `specs/provenance/devops/` directories.
3. Moved `specs/editorial/authors-note.provenance.md` to
   `specs/provenance/editorial/authors-note.provenance.md` using `git mv`.
4. Moved `specs/editorial/licensing.provenance.md` to
   `specs/provenance/editorial/licensing.provenance.md` using `git mv`.
5. Updated `discover_specs()` to skip files whose stem ends with `.provenance`.
6. Updated `load_spec()` to skip files whose stem ends with `.provenance`.
7. Added `discover_provenance()` function scanning for `*.provenance.md` files.
8. Added `load_provenance(spec_name)` function returning error string on failure.
9. Added `list_provenance` MCP tool.
10. Added `get_provenance` MCP tool.
11. Reviewed existing code against mcp-builder skill conventions; no additional
    alignment changes needed beyond the provenance filtering.
12. Created this provenance file.

### Decisions

- **Used `SpecInfo` for provenance metadata.** The mcp-builder skill template uses
  `ResourceInfo`, but the specmcp server already uses `SpecInfo` with identical
  fields. The spec says to reuse `SpecInfo`.
- **Provenance tool placement.** Added `list_provenance` and `get_provenance` after
  `get_spec` and before `get_chapter_context` to group provenance access near spec
  access in the tool listing.
- **No changes to `get_chapter_context` or `validate_content` error handling.** These
  tools call `load_spec` for core infrastructure specs. Raising on missing core specs
  is correct behavior — it surfaces configuration problems rather than masking them.
  The spec says "Do not rename existing tools or change their signatures."

### MCP calls

1. `get_spec("specmcp-refactor")`
2. `get_spec("provenance")`
3. `get_skill("SKILL")` (mcp-builder skill)

### Deviations

- **Branch name:** Used `claude/refactor-specmcp-XBSaG` instead of the spec-mandated
  `spec/specmcp-refactor/provenance-separation`. The `claude/` prefix is a
  system-enforced requirement for push access in this environment.
