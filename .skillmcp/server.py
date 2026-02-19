#!/usr/bin/env python3
"""Skill MCP Server.

Provides AI agents with structured access to reusable skills that guide
workflow execution. Skills in skills/ are auto-discovered — adding a new
skill requires no code changes.

Usage:
    python .skillmcp/server.py

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

SKILLS_DIR = Path(__file__).resolve().parent / "skills"

mcp = FastMCP("sdd-book-skills")


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------


@dataclass
class SkillInfo:
    """Metadata for a discovered skill file."""

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


def discover_skills(category: str | None = None) -> list[SkillInfo]:
    """Scan skills/ and return metadata for every .md file found."""
    skills: list[SkillInfo] = []
    for md_file in sorted(SKILLS_DIR.rglob("*.md")):
        cat = md_file.parent.name
        if category and cat != category:
            continue
        skills.append(
            SkillInfo(
                name=md_file.stem,
                category=cat,
                path=str(md_file.relative_to(SKILLS_DIR)),
                title=_extract_title(md_file),
                size_bytes=md_file.stat().st_size,
            )
        )
    return skills


def load_skill(name: str) -> str:
    """Load a skill by name. Raises ValueError if not found."""
    for md_file in SKILLS_DIR.rglob("*.md"):
        if md_file.stem == name:
            return md_file.read_text(encoding="utf-8")
    available = [s.name for s in discover_skills()]
    msg = f"Skill '{name}' not found. Available: {', '.join(available)}"
    raise ValueError(msg)


# ---------------------------------------------------------------------------
# MCP Tools
# ---------------------------------------------------------------------------


@mcp.tool()
def list_skills(category: str | None = None) -> str:
    """List available skills in the SDD book repository.

    Returns the name, category, path, and title of each skill document.
    Optionally filter by category (e.g., 'mcp-builder').
    """
    skills = discover_skills(category)
    return json.dumps([asdict(s) for s in skills], indent=2)


@mcp.tool()
def get_skill(name: str) -> str:
    """Get the full content of a skill document by name.

    Use list_skills to discover available names. Examples:
    'SKILL' (for the mcp-builder skill).
    """
    try:
        return load_skill(name)
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
