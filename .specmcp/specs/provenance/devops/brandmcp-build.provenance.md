# Provenance: brandmcp-build

## 2026-02-19 — Build .brandmcp MCP server from scratch

**Prompt:** Execute spec brandmcp-build

**Branch:** claude/execute-brandmcp-build-bSpiD
**Commit(s):** (included in this commit)

### Actions taken

1. Read the brandmcp-build spec, provenance convention, and mcp-builder skill.
2. Read `.specmcp/server.py` and `.skillmcp/server.py` as reference implementations.
3. Created `.brandmcp/brand/` directory structure.
4. Created `brand/tokens.json` with all canonical brand values (colours, fonts,
   font scales, page dimensions, cover dimensions) exactly as specified.
5. Created four brand content markdown files (`palette.md`, `typography.md`,
   `layout.md`, `voice.md`) with narrative context and usage rules.
6. Created `.brandmcp/server.py` following the mcp-builder skill architecture
   pattern with four tools: `list_brand`, `get_brand`, `get_design_tokens`,
   and `validate_brand`.
7. Created `.brandmcp/requirements.txt` with `mcp` dependency.
8. Added `sdd-book-brand` entry to `.mcp.json` with stdio transport.
9. Ran `ruff check` and `ruff format` — both pass.
10. Ran `pre-commit run --all-files` — all hooks pass except mypy, which has
    a pre-existing duplicate module name error unrelated to this change.
11. Verified server starts without error.
12. Verified all four tools return correct results via inline tests.
13. Created this provenance file.

### Decisions

- **BrandInfo dataclass name.** Used `BrandInfo` rather than the generic
  `ResourceInfo` from the mcp-builder template, consistent with `SpecInfo`
  and `SkillInfo` in the other servers.
- **validate_brand font checking.** The spec says to "flag any font name that
  is not in tokens.json fonts values". Implemented this by scanning for common
  non-brand font names rather than trying to detect arbitrary font references
  in prose, which would produce too many false positives.
- **validate_brand code block exclusion.** Strips fenced code blocks and inline
  code spans before checking for off-brand colours, fonts, and spelling, since
  code examples legitimately contain non-brand values.
- **requirements.txt.** Used `mcp` as specified in the spec, not `mcp>=1.2.0`
  as found in the existing servers. The spec is explicit.

### MCP calls

1. `get_spec("brandmcp-build")`
2. `get_spec("provenance")`
3. `get_skill("SKILL")` (mcp-builder skill)

### Deviations

- **Branch name:** Used `claude/execute-brandmcp-build-bSpiD` instead of the
  spec-mandated `spec/brandmcp-build/initial`. The `claude/` prefix is a
  system-enforced requirement for push access in this environment.
- **mypy pre-existing failure.** The `pre-commit run --all-files` mypy hook
  fails due to duplicate module names across `.specmcp/server.py`,
  `.skillmcp/server.py`, and `.brandmcp/server.py`. This error existed before
  this change (confirmed by running mypy with changes stashed). Not addressed
  as `.specmcp`/`.skillmcp` changes are out of scope.
