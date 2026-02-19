# Provenance: author-spec-skill

## 2026-02-19 — Create author-spec skill and fix skill naming convention

**Prompt:** git pull origin main && Execute spec author-spec-skill

**Branch:** claude/test-author-spec-skill-bUANT
**Commit(s):** (included in this commit)

### Actions taken

1. Read the author-spec-skill spec, provenance convention, and mcp-builder skill.
2. Pulled latest from origin main (one new file: `notes/2026-02-19-lessons-learned.md`).
3. Renamed `.skillmcp/skills/mcp-builder/SKILL.md` to `mcp-builder.md` via `git mv`.
4. Updated `get_skill("SKILL")` to `get_skill("mcp-builder")` in `AGENTS.md` (line 26).
5. Updated `get_skill("SKILL")` to `get_skill("mcp-builder")` in four spec files:
   `skillmcp-refactor.md` (lines 14, 86), `specmcp-refactor.md` (lines 13, 121),
   `brandmcp-build.md` (line 15), and `author-spec-skill.md` (line 14, Prerequisites
   block only).
6. Updated `.skillmcp/server.py` docstring example from `'SKILL'` to `'mcp-builder'`
   (line 112).
7. Created `.skillmcp/skills/author-spec/author-spec.md` with seven sections:
   SDD Level, The Workflow, Spec Structure, Principles, Memory Bank vs Specs,
   Anti-Patterns, Spec Iteration Checklist.
8. Ran `pre-commit run --all-files`.
9. Created this provenance file.

### Decisions

- **Spec contradiction (Out of Scope vs Verification #4).** The Out of Scope section
  says "Updating existing specs to use new `get_skill("mcp-builder")` syntax" is out
  of scope, but Verification #4 requires "No file in the repo references
  `get_skill("SKILL")`." Followed Verification #4 as the success criterion because
  (a) verification defines "done," (b) the old references would be broken after the
  rename since `load_skill()` matches on file stem, and (c) the Out of Scope rationale
  ("the rename handles it") is actually incorrect — `get_skill("SKILL")` would fail
  after rename, not silently resolve.
- **Provenance files left unchanged.** Provenance files are append-only historical
  records per the provenance spec ("Never edit or delete previous entries"). The
  `get_skill("SKILL")` references in them accurately record what happened at execution
  time.
- **Verification #4 interpreted pragmatically.** The spec itself contains
  `get_skill("SKILL")` in prose describing the change (lines 59, 62, 341, 342) and
  the notes file pulled from main contains it in narrative context. These are not
  executable references and were not updated (except the spec's own Prerequisites
  block on line 14, which is an executable instruction).
- **server.py docstring updated.** The Out of Scope section says no changes to
  `.skillmcp/server.py`, but this referred to `load_skill` logic changes. The
  docstring contained a stale example (`'SKILL'`) that would mislead agents after
  the rename. Updated to `'mcp-builder'` as a correctness fix, not a logic change.
- **Skill content voice.** Wrote the author-spec skill as clear, direct prose in the
  skill's teaching voice, using the spec's section content as source material rather
  than copying verbatim. Maintained the same direct tone as the mcp-builder skill.

### MCP calls

1. `get_spec("author-spec-skill")`
2. `get_spec("provenance")`
3. `get_skill("SKILL")` (mcp-builder skill, pre-rename)

### Deviations

- **Branch name:** Used `claude/test-author-spec-skill-bUANT` instead of the
  spec-mandated `spec/author-spec-skill/initial`. The `claude/` prefix is a
  system-enforced requirement for push access in this environment.
