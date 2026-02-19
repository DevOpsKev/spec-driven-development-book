# SDD Book Repository

This repository uses Specification Driven Development to author a book about SDD.

## MCP Servers

This repo includes local MCP servers that provide AI agents with structured
access to project resources. All servers are registered in `.mcp.json`.

### Spec Server (`.specmcp/server.py`)

Structured access to book specifications:

- **list_specs** — Discover available specifications
- **get_spec** — Read a specific specification by name
- **get_chapter_context** — Get bundled context for writing a chapter
- **validate_content** — Check content against spec rules

### Skills Server (`.skillmcp/server.py`)

Reusable skills that guide agent workflows:

- **list_skills** — Discover available skills
- **get_skill** — Read a skill by name

Before building or refactoring any MCP server, call `get_skill("mcp-builder")`
to load the mcp-builder skill and follow its conventions.

## Key Specifications

Start with `list_specs` to see all available specs. The most important are:

- **book-brief** — Scope, thesis, audience
- **writers-guide** — Voice, tone, style rules (read this before writing any content)
- **glossary** — Canonical term definitions (use terms exactly as defined)
- **chapter-outline** — 26 chapters across 5 parts
- **provenance** — Branch naming and execution audit trail (read before any spec execution)

## Writing Workflow

When writing a chapter:

1. Call `get_chapter_context` with the chapter number
2. Follow the writers guide strictly
3. Use glossary terms exactly as defined
4. After writing, call `validate_content` to check for issues

## Spec Execution Workflow

When executing any spec:

1. Call `get_spec("provenance")` to load the conventions
2. Call `get_spec("<spec-name>")` and review it in plan mode first
3. Validate that all file paths, references, and assumptions in the spec
   match the current state of the repository — specs have bugs too
4. Create a branch named `spec/<spec-name>/<action>`
5. Execute the work
6. Append a provenance entry to `<spec-name>.provenance.md`
7. Commit everything together and push the branch

## Code Quality

Python code uses ruff (linting + formatting) and mypy (type checking).
Run `pre-commit run --all-files` before committing.

## Environment Constraints

This environment supports git push but does not have GitHub API access.
Do not attempt to create PRs via `gh` CLI — push the branch and the
author will create the PR manually.
