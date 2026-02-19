#!/usr/bin/env python3
"""SDD Book MCP Server.

Provides AI agents with structured access to the book's specification layer.
Specifications in specs/ drive the server's behavior — adding a new spec file
requires no code changes.

Usage:
    python .specmcp/server.py

Configured for Claude Code via .mcp.json (stdio transport).
"""

from __future__ import annotations

import json
import logging
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

from mcp.server.fastmcp import FastMCP

# Logging must go to stderr — stdout is reserved for stdio transport.
logging.basicConfig(stream=sys.stderr, level=logging.INFO)
logger = logging.getLogger(__name__)

SPECS_DIR = Path(__file__).resolve().parent / "specs"

mcp = FastMCP("sdd-book-specs")


# ---------------------------------------------------------------------------
# Spec discovery
# ---------------------------------------------------------------------------


@dataclass
class SpecInfo:
    """Metadata for a discovered spec file."""

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


def discover_specs(category: str | None = None) -> list[SpecInfo]:
    """Scan specs/ and return metadata for every .md file found."""
    specs: list[SpecInfo] = []
    for md_file in sorted(SPECS_DIR.rglob("*.md")):
        if md_file.stem.endswith(".provenance"):
            continue  # Skip provenance files — accessed via dedicated tools
        cat = md_file.parent.name
        if category and cat != category:
            continue
        specs.append(
            SpecInfo(
                name=md_file.stem,
                category=cat,
                path=str(md_file.relative_to(SPECS_DIR)),
                title=_extract_title(md_file),
                size_bytes=md_file.stat().st_size,
            )
        )
    return specs


def load_spec(name: str) -> str:
    """Load a spec by name. Raises ValueError if not found."""
    for md_file in SPECS_DIR.rglob("*.md"):
        if md_file.stem.endswith(".provenance"):
            continue
        if md_file.stem == name:
            return md_file.read_text(encoding="utf-8")
    available = [s.name for s in discover_specs()]
    msg = f"Spec '{name}' not found. Available: {', '.join(available)}"
    raise ValueError(msg)


# ---------------------------------------------------------------------------
# Provenance discovery
# ---------------------------------------------------------------------------


def discover_provenance() -> list[SpecInfo]:
    """Scan specs/ for provenance files and return metadata for each."""
    provenance: list[SpecInfo] = []
    for md_file in sorted(SPECS_DIR.rglob("*.provenance.md")):
        provenance.append(
            SpecInfo(
                name=md_file.stem,
                category=md_file.parent.name,
                path=str(md_file.relative_to(SPECS_DIR)),
                title=_extract_title(md_file),
                size_bytes=md_file.stat().st_size,
            )
        )
    return provenance


def load_provenance(spec_name: str) -> str:
    """Load provenance for a spec by name. Returns error string if not found."""
    target = f"{spec_name}.provenance"
    for md_file in SPECS_DIR.rglob("*.provenance.md"):
        if md_file.stem == target:
            return md_file.read_text(encoding="utf-8")
    return f"No provenance found for spec '{spec_name}'."


# ---------------------------------------------------------------------------
# Parsing helpers
# ---------------------------------------------------------------------------


def extract_chapter_section(chapter_number: int) -> str:
    """Extract a single chapter's section from chapter-outline.md."""
    content = load_spec("chapter-outline")
    pattern = rf"^### Chapter {chapter_number}:"
    lines = content.splitlines()
    start = None
    for i, line in enumerate(lines):
        if re.match(pattern, line):
            start = i
        elif start is not None and re.match(r"^###? ", line) and i > start:
            return "\n".join(lines[start:i]).strip()
    if start is not None:
        return "\n".join(lines[start:]).strip()
    return f"No outline found for chapter {chapter_number}."


def extract_chapter_diataxis(chapter_number: int) -> str:
    """Extract the diataxis classification row for a chapter."""
    content = load_spec("diataxis-integration")
    for line in content.splitlines():
        if re.match(rf"^\|\s*{chapter_number}\s*\|", line):
            return line.strip()
    return f"No diataxis classification found for chapter {chapter_number}."


def get_banned_words() -> list[tuple[str, str]]:
    """Parse banned words from writers-guide.md.

    Returns (banned_word, suggestion) pairs.
    """
    content = load_spec("writers-guide")
    banned: list[tuple[str, str]] = []
    in_banned = False
    for line in content.splitlines():
        if "Banned words and phrases" in line:
            in_banned = True
            continue
        if in_banned and line.startswith("---"):
            break
        if in_banned and line.startswith("- "):
            match = re.match(r'^- "(.+?)"(?: \(use "(.+?)"\))?', line)
            if match:
                word = match.group(1)
                suggestion = match.group(2) or ""
                banned.append((word, suggestion))
    return banned


def get_terminology_map() -> dict[str, str]:
    """Parse preferred terminology from writers-guide.md.

    Returns {wrong_term: preferred_term}.
    """
    content = load_spec("writers-guide")
    terms: dict[str, str] = {}
    in_table = False
    for line in content.splitlines():
        if "| Preferred Term" in line:
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            continue
        if in_table and line.startswith("|"):
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 2:
                preferred = cols[0]
                wrong_terms = [t.strip() for t in cols[1].split(",")]
                for wrong in wrong_terms:
                    # Strip parenthetical notes
                    clean = re.sub(r"\(.*?\)", "", wrong).strip()
                    if clean:
                        terms[clean.lower()] = preferred
        elif in_table and not line.strip():
            break
    return terms


# ---------------------------------------------------------------------------
# MCP Tools
# ---------------------------------------------------------------------------


@mcp.tool()
def list_specs(category: str | None = None) -> str:
    """List available specifications in the SDD book repository.

    Returns the name, category, path, and title of each spec document.
    Optionally filter by category (e.g., 'editorial', 'workflow').
    """
    specs = discover_specs(category)
    return json.dumps([asdict(s) for s in specs], indent=2)


@mcp.tool()
def get_spec(name: str) -> str:
    """Get the full content of a specification document by name.

    Use list_specs to discover available names. Examples:
    'book-brief', 'glossary', 'writers-guide', 'workflow'.
    """
    try:
        return load_spec(name)
    except ValueError as exc:
        return str(exc)


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
    return load_provenance(spec_name)


@mcp.tool()
def get_chapter_context(chapter_number: int) -> str:
    """Get bundled specification context for generating a specific chapter.

    Assembles the full context an agent needs to write a chapter, following
    the SDD workflow: book brief, writers guide, glossary, chapter outline
    excerpt, prior-art, continuity state, diataxis classification, and the
    chapter brief (if one exists).
    """
    if chapter_number < 1 or chapter_number > 26:
        return "Chapter number must be between 1 and 26."

    sections: list[str] = []

    def _add(heading: str, content: str) -> None:
        sections.append(f"=== {heading} ===\n\n{content}")

    _add("BOOK BRIEF", load_spec("book-brief"))
    _add("WRITERS GUIDE", load_spec("writers-guide"))
    _add("GLOSSARY", load_spec("glossary"))
    _add(f"CHAPTER OUTLINE (Chapter {chapter_number})", extract_chapter_section(chapter_number))
    _add("PRIOR ART", load_spec("prior-art"))
    _add("CONTINUITY STATE", load_spec("continuity-tracker"))
    _add(
        f"DIATAXIS CLASSIFICATION (Chapter {chapter_number})",
        extract_chapter_diataxis(chapter_number),
    )

    # Chapter brief — may not exist yet
    brief_name = f"ch{chapter_number:02d}-brief"
    try:
        _add("CHAPTER BRIEF", load_spec(brief_name))
    except ValueError:
        _add(
            "CHAPTER BRIEF",
            f"No chapter brief found ({brief_name}.md). Create one in specs/editorial/chapter-briefs/.",
        )

    return "\n\n".join(sections)


@mcp.tool()
def validate_content(content: str, chapter_number: int | None = None) -> str:
    """Validate content against SDD book specifications.

    Checks for banned words from the writers guide, terminology consistency,
    and basic structural requirements. Returns a JSON report.
    """
    issues: list[dict[str, str | int]] = []
    lines = content.splitlines()

    # 1. Banned words
    banned = get_banned_words()
    for i, line in enumerate(lines, 1):
        lower = line.lower()
        for word, suggestion in banned:
            if word.lower() in lower:
                issue: dict[str, str | int] = {
                    "type": "banned_word",
                    "word": word,
                    "line": i,
                }
                if suggestion:
                    issue["suggestion"] = suggestion
                issues.append(issue)

    # 2. Terminology
    term_map = get_terminology_map()
    for i, line in enumerate(lines, 1):
        lower = line.lower()
        for wrong, preferred in term_map.items():
            if wrong in lower:
                issues.append(
                    {
                        "type": "terminology",
                        "found": wrong,
                        "preferred": preferred,
                        "line": i,
                    }
                )

    # 3. Structure
    if lines and not lines[0].startswith("#"):
        issues.append(
            {"type": "structure", "issue": "Content should start with a heading", "line": 1}
        )

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.endswith("?") and (
            stripped.startswith("Have you") or stripped.startswith("What if")
        ):
            issues.append(
                {
                    "type": "structure",
                    "issue": "Avoid rhetorical questions as transitions",
                    "line": i,
                }
            )

    passed = len(issues) == 0
    report = {
        "passed": passed,
        "issue_count": len(issues),
        "issues": issues,
    }
    if not passed:
        by_type: dict[str, int] = {}
        for issue in issues:
            t = str(issue["type"])
            by_type[t] = by_type.get(t, 0) + 1
        report["summary"] = ", ".join(f"{v} {k}" for k, v in by_type.items())

    return json.dumps(report, indent=2)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Run the MCP server with stdio transport."""
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
