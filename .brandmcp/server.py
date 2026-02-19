#!/usr/bin/env python3
"""Brand MCP Server.

Provides AI agents with structured access to brand guidelines, design tokens,
and brand validation for the SDD book. Brand documents in brand/ are
auto-discovered — adding a new guideline requires no code changes.

Usage:
    python .brandmcp/server.py

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

BRAND_DIR = Path(__file__).resolve().parent / "brand"
TOKENS_PATH = BRAND_DIR / "tokens.json"

mcp = FastMCP("sdd-book-brand")


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------


@dataclass
class BrandInfo:
    """Metadata for a discovered brand guideline file."""

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


def discover_brand(category: str | None = None) -> list[BrandInfo]:
    """Scan brand/ and return metadata for every .md file found."""
    resources: list[BrandInfo] = []
    for md_file in sorted(BRAND_DIR.rglob("*.md")):
        if md_file.stem.endswith(".provenance"):
            continue  # Skip provenance files — accessed via dedicated tools
        cat = md_file.parent.name
        if category and cat != category:
            continue
        resources.append(
            BrandInfo(
                name=md_file.stem,
                category=cat,
                path=str(md_file.relative_to(BRAND_DIR)),
                title=_extract_title(md_file),
                size_bytes=md_file.stat().st_size,
            )
        )
    return resources


def load_brand(name: str) -> str:
    """Load a brand guideline by name. Raises ValueError if not found."""
    for md_file in BRAND_DIR.rglob("*.md"):
        if md_file.stem.endswith(".provenance"):
            continue
        if md_file.stem == name:
            return md_file.read_text(encoding="utf-8")
    available = [r.name for r in discover_brand()]
    msg = f"Brand guideline '{name}' not found. Available: {', '.join(available)}"
    raise ValueError(msg)


def _load_tokens() -> dict:
    """Load and parse tokens.json. Raises FileNotFoundError or json.JSONDecodeError."""
    return json.loads(TOKENS_PATH.read_text(encoding="utf-8"))


# ---------------------------------------------------------------------------
# Validation helpers
# ---------------------------------------------------------------------------

_HEX_PATTERN = re.compile(r"#[0-9A-Fa-f]{6}\b")
_CODE_BLOCK_PATTERN = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_PATTERN = re.compile(r"`[^`]+`")
_CSS_ATTR_PATTERN = re.compile(
    r'(?:color|background-color|background|fill|stroke)\s*[:=]\s*["\']?#[0-9A-Fa-f]{6}',
    re.IGNORECASE,
)


def _strip_code_blocks(content: str) -> list[tuple[int, str]]:
    """Return (line_number, text) pairs for lines outside code blocks.

    Removes fenced code blocks and inline code spans so validation only
    checks prose.
    """
    # Remove fenced code blocks, replacing with empty lines to preserve numbering
    stripped = _CODE_BLOCK_PATTERN.sub(lambda m: "\n" * m.group().count("\n"), content)
    # Remove inline code spans
    stripped = _INLINE_CODE_PATTERN.sub("", stripped)
    return list(enumerate(stripped.splitlines(), 1))


def _check_colours(prose_lines: list[tuple[int, str]], tokens: dict) -> list[dict[str, str | int]]:
    """Flag hex colour codes not present in tokens.json colours."""
    allowed = {v.upper() for v in tokens.get("colours", {}).values()}
    issues: list[dict[str, str | int]] = []
    for line_num, line in prose_lines:
        for match in _HEX_PATTERN.finditer(line):
            hex_code = match.group().upper()
            if hex_code not in allowed:
                issues.append(
                    {
                        "type": "off_brand_colour",
                        "found": match.group(),
                        "line": line_num,
                        "suggestion": "Use a colour from tokens.json",
                    }
                )
    return issues


def _check_fonts(prose_lines: list[tuple[int, str]], tokens: dict) -> list[dict[str, str | int]]:
    """Flag font-family references not present in tokens.json fonts."""
    brand_fonts = set(tokens.get("fonts", {}).values())
    # Build patterns for each brand font to detect near-misses
    common_fonts = {
        "Arial",
        "Helvetica",
        "Times New Roman",
        "Times",
        "Courier New",
        "Courier",
        "Georgia",
        "Verdana",
        "Trebuchet MS",
        "Comic Sans MS",
        "Impact",
        "Palatino",
        "Garamond",
        "Bookman",
        "Roboto",
        "Open Sans",
        "Lato",
        "Montserrat",
        "Raleway",
        "Nunito",
        "Fira Code",
        "Source Code Pro",
        "Consolas",
        "Menlo",
        "Monaco",
    }
    # Only flag fonts that are NOT brand fonts
    off_brand = common_fonts - brand_fonts
    issues: list[dict[str, str | int]] = []
    for line_num, line in prose_lines:
        for font in off_brand:
            if font.lower() in line.lower():
                issues.append(
                    {
                        "type": "off_brand_font",
                        "found": font,
                        "line": line_num,
                        "suggestion": f"Use a font from tokens.json: {', '.join(sorted(brand_fonts))}",
                    }
                )
    return issues


def _check_spelling(
    prose_lines: list[tuple[int, str]],
) -> list[dict[str, str | int]]:
    """Flag American 'color' spelling outside code blocks and CSS attributes."""
    # Match 'color' as a standalone word (not part of 'colour')
    color_pattern = re.compile(r"\bcolor\b", re.IGNORECASE)
    issues: list[dict[str, str | int]] = []
    for line_num, line in prose_lines:
        # Skip lines that look like CSS/HTML attributes
        if _CSS_ATTR_PATTERN.search(line):
            continue
        for match in color_pattern.finditer(line):
            issues.append(
                {
                    "type": "spelling",
                    "found": match.group(),
                    "line": line_num,
                    "suggestion": "Use British English 'colour'",
                }
            )
    return issues


# ---------------------------------------------------------------------------
# MCP Tools
# ---------------------------------------------------------------------------


@mcp.tool()
def list_brand(category: str | None = None) -> str:
    """List available brand guideline documents.

    Returns name, category, path, and title of each brand document.
    Optionally filter by category.
    """
    resources = discover_brand(category)
    return json.dumps([asdict(r) for r in resources], indent=2)


@mcp.tool()
def get_brand(name: str) -> str:
    """Get the full content of a brand guideline document by name.

    Use list_brand to discover available names. Examples:
    'palette', 'typography', 'layout', 'voice'.
    """
    try:
        return load_brand(name)
    except ValueError as exc:
        return str(exc)


@mcp.tool()
def get_design_tokens() -> str:
    """Read and return the design tokens from brand/tokens.json.

    Returns the raw JSON content — hex codes, font names, dimensions,
    CMYK values. This is the single source of truth for all concrete
    brand values.
    """
    try:
        return TOKENS_PATH.read_text(encoding="utf-8")
    except (FileNotFoundError, OSError) as exc:
        return f"Error reading tokens.json: {exc}"


@mcp.tool()
def validate_brand(content: str) -> str:
    """Validate content against the brand guidelines.

    Checks for off-brand colours, off-brand fonts, and American spelling
    of 'color'. Reads tokens.json for canonical values. Returns a JSON
    report with pass/fail status and any issues found.
    """
    try:
        tokens = _load_tokens()
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        return json.dumps(
            {
                "passed": False,
                "issue_count": 1,
                "issues": [
                    {
                        "type": "error",
                        "found": str(exc),
                        "line": 0,
                        "suggestion": "Ensure brand/tokens.json exists and is valid JSON",
                    }
                ],
            },
            indent=2,
        )

    prose_lines = _strip_code_blocks(content)
    issues: list[dict[str, str | int]] = []
    issues.extend(_check_colours(prose_lines, tokens))
    issues.extend(_check_fonts(prose_lines, tokens))
    issues.extend(_check_spelling(prose_lines))

    passed = len(issues) == 0
    report: dict = {
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
