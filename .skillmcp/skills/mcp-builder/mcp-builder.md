---
name: mcp-builder
description: >
  Build, refactor, and maintain MCP (Model Context Protocol) servers for the
  SDD book repository. Use when creating new MCP servers, adding tools to
  existing servers, or refactoring server code. Covers the full lifecycle:
  design, implement, register, document, and verify.
---

# MCP Builder Skill

Build high-quality MCP servers that give AI agents structured access to
project resources. Every server in this repository follows the same
conventions — this skill captures those conventions so new servers are
consistent and existing servers can be refactored safely.

## Stack

All MCP servers in this project use:

- **Python 3.12+** with **FastMCP** (`mcp.server.fastmcp`)
- **stdio transport** (configured via `.mcp.json` at repo root)
- **ruff** for linting/formatting, **mypy** for type checking
- **pre-commit** hooks enforced on all commits

Do not use the deprecated `server.tool()` or `server.setRequestHandler()`
patterns. Use FastMCP's `@mcp.tool()` decorator exclusively.

## Directory Convention

Each MCP server lives in a dot-prefixed directory at the repo root:

```
.{name}mcp/
├── server.py          # Server entry point
├── requirements.txt   # Python dependencies
└── {domain}/          # Domain-specific resources (specs/, skills/, brand/, etc.)
    └── *.md           # Markdown files auto-discovered by the server
```

The dot prefix keeps MCP infrastructure out of the visible project tree
while remaining accessible to tooling.

Current servers:

| Directory | Domain | Purpose |
|-----------|--------|---------|
| `.specmcp` | specs | Book specifications and editorial standards |
| `.skillmcp` | skills | Reusable skills for AI agent workflows |
| `.brandmcp` | brand | Brand guidelines, voice, and visual identity |

## Server Architecture Pattern

Every server follows this architecture:

```python
#!/usr/bin/env python3
"""<n> MCP Server.

<Purpose description>.

Usage:
    python .<n>mcp/server.py

Configured for Claude Code via .mcp.json (stdio transport).
"""

from __future__ import annotations

import json
import logging
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Logging must go to stderr — stdout is reserved for stdio transport.
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger(__name__)

# Resource directory — sibling to server.py
RESOURCE_DIR = Path(__file__).resolve().parent / "<domain>"

mcp = FastMCP("<server-name>")


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

@dataclass
class ResourceInfo:
    """Metadata for a discovered resource file."""
    name: str
    category: str
    path: str
    title: str
    size_bytes: int


def _extract_title(path: Path) -> str:
    """Extract the first markdown heading from a file."""
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line.removeprefix("# ").strip()
    return path.stem


def discover_resources(category: str | None = None) -> list[ResourceInfo]:
    """Scan resource directory and return metadata for every .md file."""
    resources: list[ResourceInfo] = []
    for md_file in sorted(RESOURCE_DIR.rglob("*.md")):
        cat = md_file.parent.name
        if category and cat != category:
            continue
        resources.append(
            ResourceInfo(
                name=md_file.stem,
                category=cat,
                path=str(md_file.relative_to(RESOURCE_DIR)),
                title=_extract_title(md_file),
                size_bytes=md_file.stat().st_size,
            )
        )
    return resources


def load_resource(name: str) -> str:
    """Load a resource by stem name. Raises ValueError if not found."""
    for md_file in RESOURCE_DIR.rglob("*.md"):
        if md_file.stem == name:
            return md_file.read_text(encoding="utf-8")
    available = [r.name for r in discover_resources()]
    msg = f"Resource '{name}' not found. Available: {', '.join(available)}"
    raise ValueError(msg)


# ---------------------------------------------------------------------------
# MCP Tools
# ---------------------------------------------------------------------------

@mcp.tool()
def list_<domain>(category: str | None = None) -> str:
    """List available <domain> resources.

    Returns name, category, path, and title of each resource.
    Optionally filter by category.
    """
    resources = discover_resources(category)
    return json.dumps([asdict(r) for r in resources], indent=2)


@mcp.tool()
def get_<domain>(name: str) -> str:
    """Get the full content of a <domain> resource by name.

    Use list_<domain> to discover available names.
    """
    try:
        return load_resource(name)
    except ValueError as exc:
        return str(exc)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    """Run the MCP server with stdio transport."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
```

Replace `<n>`, `<server-name>`, and `<domain>` with the actual values.

## Tool Naming

Use `snake_case` for all tool names. Prefix tool names with the server's
domain to avoid collisions when multiple servers run simultaneously:

| Server | Prefix | Examples |
|--------|--------|----------|
| `.specmcp` | `spec_` or bare | `list_specs`, `get_spec`, `validate_content` |
| `.skillmcp` | `skill_` | `list_skills`, `get_skill` |
| `.brandmcp` | `brand_` | `list_brand`, `get_brand` |

Use action-oriented verbs: `list_`, `get_`, `validate_`, `search_`.

**Tool descriptions** must be precise and unambiguous. The description is
what the AI agent reads to decide whether to call the tool. Write it as
if explaining to a colleague what the function does and when to use it.

## Registering a Server

Add the server to `.mcp.json` at the repo root:

```json
{
  "mcpServers": {
    "<server-name>": {
      "type": "stdio",
      "command": "python",
      "args": [".<n>mcp/server.py"]
    }
  }
}
```

All servers use stdio transport. No HTTP, no SSE.

## Documenting a Server

After creating or modifying a server, update `CLAUDE.md` at the repo root:

1. Add the server to the MCP Server section
2. List its tools with one-line descriptions
3. Add any workflow guidance (e.g. "call list_skills before get_skill")

## Resource Auto-Discovery

Servers auto-discover `.md` files by scanning their resource directory
recursively. This means:

- Adding a new resource requires **no code changes** — just drop a `.md`
  file in the right directory
- Subdirectories become categories (e.g. `specs/editorial/book-brief.md`
  has category `editorial`)
- Files are identified by stem name (e.g. `book-brief` from `book-brief.md`)

## Provenance Files

Provenance files track the execution history of specs by AI agents.
They follow the naming pattern `<spec-name>.provenance.md` and live
in a dedicated `provenance/` directory within the server's resource tree.

Provenance files should be **excluded from resource discovery** by
filtering on the `.provenance.md` suffix in `discover_resources()`:

```python
def discover_resources(category: str | None = None) -> list[ResourceInfo]:
    resources: list[ResourceInfo] = []
    for md_file in sorted(RESOURCE_DIR.rglob("*.md")):
        if md_file.stem.endswith(".provenance"):
            continue  # Skip provenance files — accessed via dedicated tools
        # ... rest of discovery
```

Provide dedicated `list_provenance` and `get_provenance` tools instead:

```python
def discover_provenance() -> list[ResourceInfo]:
    """Scan for provenance files specifically."""
    provenance: list[ResourceInfo] = []
    for md_file in sorted(RESOURCE_DIR.rglob("*.provenance.md")):
        provenance.append(
            ResourceInfo(
                name=md_file.stem,  # e.g. "authors-note.provenance"
                category=md_file.parent.name,
                path=str(md_file.relative_to(RESOURCE_DIR)),
                title=_extract_title(md_file),
                size_bytes=md_file.stat().st_size,
            )
        )
    return provenance


@mcp.tool()
def list_provenance() -> str:
    """List all provenance records across specs.

    Returns metadata for each provenance file found.
    """
    records = discover_provenance()
    return json.dumps([asdict(r) for r in records], indent=2)


@mcp.tool()
def get_provenance(spec_name: str) -> str:
    """Get the provenance (execution history) for a specific spec.

    Pass the spec name without the .provenance suffix.
    Example: get_provenance("authors-note")
    """
    target = f"{spec_name}.provenance"
    for md_file in RESOURCE_DIR.rglob("*.provenance.md"):
        if md_file.stem == target:
            return md_file.read_text(encoding="utf-8")
    return f"No provenance found for spec '{spec_name}'."
```

## Dependencies

Every server directory includes a `requirements.txt`. At minimum:

```
mcp
```

Add additional dependencies only when needed. The `setup-deps.sh` script
handles system-level dependencies; `requirements.txt` is for Python
packages specific to the server.

## Code Quality Checklist

Before committing any MCP server code:

- [ ] `ruff check .` passes with no errors
- [ ] `ruff format .` produces no changes
- [ ] `pre-commit run --all-files` passes
- [ ] Server starts without error: `python .<n>mcp/server.py` (Ctrl+C to exit)
- [ ] All tools return valid JSON or plain text (never raise unhandled exceptions)
- [ ] Tool descriptions are precise and unambiguous
- [ ] `CLAUDE.md` updated with new/changed tools
- [ ] `.mcp.json` updated if server is new

## Error Handling

Tools should never raise unhandled exceptions. Wrap failures in
human-readable error strings:

```python
@mcp.tool()
def get_thing(name: str) -> str:
    try:
        return load_resource(name)
    except ValueError as exc:
        return str(exc)
```

This ensures the AI agent always gets a usable response, even on failure.

## Testing a Server

After creating or modifying a server, verify it works:

```bash
# 1. Check syntax and style
ruff check .<n>mcp/
ruff format --check .<n>mcp/

# 2. Start the server (should launch without error)
python .<n>mcp/server.py
# Ctrl+C to stop

# 3. Run pre-commit
pre-commit run --all-files
```

For Claude Code integration, the server is automatically available once
registered in `.mcp.json` — restart the Claude Code session to pick up
changes.
