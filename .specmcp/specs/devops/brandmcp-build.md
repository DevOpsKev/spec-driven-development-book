# Spec: brandmcp Build — Brand Guidelines Server

## Purpose

Create the `.brandmcp` MCP server from scratch, providing AI agents with
structured access to brand guidelines, design tokens, and brand validation
for the SDD book. This is the first server built entirely from spec by
an agent.

## Prerequisites

Before executing this spec, load the mcp-builder skill:

```
get_skill("SKILL")
```

Follow all conventions described in that skill throughout this execution.

## Context

The SDD book has an established visual identity defined across cover SVGs
(`assets/cover/`) and a LaTeX template (`build/pdf/template.tex`). These
brand elements are currently implicit — embedded in build files with no
single source of truth. This server extracts them into queryable brand
guidelines that any agent can consume, and provides validation to catch
brand violations before they ship.

## Single Source of Truth

`brand/tokens.json` is the canonical source for all concrete values —
hex codes, font names, dimensions, CMYK values. No other file may define
these values independently.

The markdown guideline files (`palette.md`, `typography.md`, `layout.md`,
`voice.md`) provide narrative context — *why* to use a colour, *when* to
use a font, usage rules and constraints. For any concrete value, they
must reference `tokens.json` rather than redefine it.

This means:

- To change a hex code, edit `tokens.json`. The markdown prose stays as-is.
- To change a usage rule, edit the markdown file. The token stays as-is.
- `get_design_tokens` reads `tokens.json` directly — no parsing markdown.
- `validate_brand` reads `tokens.json` to check content against canonical values.
- Markdown files may quote token values for readability, but `tokens.json`
  is authoritative if they ever diverge.

## Changes

### 1. Create directory structure

```
.brandmcp/
├── server.py
├── requirements.txt
└── brand/
    ├── tokens.json
    ├── palette.md
    ├── typography.md
    ├── layout.md
    └── voice.md
```

### 2. Create tokens.json

This is the canonical source for all concrete brand values:

```json
{
  "colours": {
    "background": "#F8F4ED",
    "text-primary": "#1a1a1a",
    "text-secondary": "#444444",
    "text-tertiary": "#555555",
    "accent-red": "#e63926",
    "accent-screen": "#2563EB",
    "code-bg": "#F8F9FA"
  },
  "colours-print": {
    "accent-print": "cmyk(0.85, 0.50, 0, 0.20)",
    "link-print": "cmyk(0, 0, 0, 1)"
  },
  "fonts": {
    "display": "Alfa Slab One",
    "body": "Source Serif 4",
    "sans": "Inter",
    "mono": "JetBrains Mono"
  },
  "font-scale": {
    "cover-title": "148px / 112px",
    "cover-subtitle": "52px",
    "cover-author": "48px",
    "cover-tagline": "30px",
    "cover-build-ref": "24px",
    "spine-title": "46px",
    "spine-author": "26px",
    "mono-scale": 0.85,
    "sans-scale": 0.95
  },
  "page": {
    "trim": "6x9in",
    "inner-margin": "0.85in",
    "outer-margin": "0.65in",
    "top-margin": "0.75in",
    "bottom-margin": "0.75in",
    "footskip": "0.35in"
  },
  "cover": {
    "front-width": 1050,
    "front-height": 1500,
    "back-width": 1050,
    "back-height": 1500,
    "spine-width": 150,
    "spine-height": 1500,
    "accent-stroke": 3
  }
}
```

### 3. Create brand content files

These files provide narrative context and usage rules. They reference
`tokens.json` values for readability but do not redefine them. If values
diverge, `tokens.json` is authoritative.

#### `brand/palette.md`

```markdown
# Colour Palette

All colour values are defined in `tokens.json`. This document describes
when and how to use them.

## Core Colours

- **background** (`#F8F4ED`) — Warm cream. The foundation of the visual
  identity. Do not substitute pure white.
- **text-primary** (`#1a1a1a`) — Near-black. Titles, headings, emphasis.
- **text-secondary** (`#444444`) — Dark grey. Body copy on covers.
- **text-tertiary** (`#555555`) — Medium grey. Author name, metadata.
- **accent-red** (`#e63926`) — Red. Cover accent lines, URLs, build refs.
  Use sparingly — accents and metadata only, never body text.
- **accent-screen** (`#2563EB`) — Blue. Hyperlinks in screen PDF only.
- **code-bg** (`#F8F9FA`) — Light grey. Code block background, distinct
  from page background.

## Print Colours

- **accent-print** — Dark blue (CMYK). Hyperlinks in print PDF.
- **link-print** — Black (CMYK). Link text in print.

## Rules

- Screen PDFs use `accent-screen` (blue) for links; print uses black.
- `accent-red` is for structural accents — lines, metadata, URLs.
- Code backgrounds use `code-bg` to distinguish from page background.
```

#### `brand/typography.md`

```markdown
# Typography

All font names and scales are defined in `tokens.json`. This document
describes the typographic hierarchy and usage rules.

## Font Stack

- **Display** (Alfa Slab One) — Cover title, part headings, chapter
  headings. Display only — never use for body text or UI.
- **Body** (Source Serif 4) — All sustained prose. The reading font.
  Available in ExtraLight through Black weights, plus italics.
- **Sans** (Inter) — Subtitles, author name, section headings, subsection
  headings, UI elements. The workhorse sans-serif.
- **Mono** (JetBrains Mono) — Code blocks, inline code, build metadata.
  Scaled to 0.85x of body size.

## Hierarchy

| Element | Font | Weight |
|---------|------|--------|
| Part heading | Alfa Slab One | 400 |
| Chapter heading | Alfa Slab One | 400 |
| Section heading | Inter | Bold |
| Subsection heading | Inter | Bold |
| Body text | Source Serif 4 | Regular |
| Emphasis | Source Serif 4 | Italic |
| Strong | Source Serif 4 | Bold |
| Code | JetBrains Mono | Regular |

## Rules

- British English spelling throughout (colour, behaviour, etc.)
- Font files are stored in `assets/fonts/` as TTF.
- Inter sans is scaled to 0.95x when used inline with body text.
```

#### `brand/layout.md`

```markdown
# Layout

All dimensions are defined in `tokens.json`. This document describes
the layout system and design elements.

## Page

- 6 × 9 inch trim size
- Asymmetric margins: wider inner (0.85in) for binding, narrower outer (0.65in)
- No paragraph indent — space between paragraphs instead (0.5 baseline skip)
- Widow/orphan prevention (penalty 10000)

## Cover

- Front and back covers: 1050 × 1500px
- Spine: 150 × 1500px
- Red accent lines: 3px stroke weight
- Front cover vertical accent at x=108, back cover at x=942
- Horizontal divider separating title block from subtitle/metadata
- Spine has horizontal red accent lines at top (y=50) and bottom (y=1450)

## Headers and Footers

- Even pages (verso): chapter title in left header, italic, small
- Odd pages (recto): section title in right header, italic, small
- Page number centred in footer
- Header rule: 0.4pt
- No footer rule
```

#### `brand/voice.md`

```markdown
# Voice and Tone

## Brand Voice

The SDD book speaks with authority grounded in practice, not theory.
The voice is direct, confident, and technically precise without being
academic or inaccessible.

## Key Characteristics

- **Direct** — state things plainly, avoid hedging
- **Practical** — every concept is tied to real usage
- **Confident** — the methodology works; say so without arrogance
- **Technical** — precise terminology, no dumbing down
- **Conversational** — accessible without being casual

## Cover Copy Style

- Opening line is personal and provocative ("I got tired of watching...")
- Bold statements set apart: "There's a better way." / "This book will teach you how."
- Conversational tone even in marketing copy
- No jargon in taglines — plain language that any developer understands

## Tagline

> Move beyond ad-hoc prompting to structured workflows where the spec
> is the source of truth and code follows.

## URL

sddbook.com — always lowercase, always in `accent-red`.
```

### 4. Create server.py

Follow the mcp-builder skill architecture pattern exactly. The server
must implement four tools:

#### `list_brand(category: str | None = None) -> str`

List available brand guideline documents. Returns name, category, path,
and title of each brand document. Optionally filter by category.

Auto-discovers `.md` files in `brand/`. Excludes `.provenance.md` files.

#### `get_brand(name: str) -> str`

Get the full content of a brand guideline document by name. Use
`list_brand` to discover available names. Returns error string on failure.

Excludes `.provenance.md` files from loading.

#### `get_design_tokens() -> str`

Read and return `brand/tokens.json` directly. No transformation, no
parsing markdown. Returns the raw JSON content.

If `tokens.json` is missing or unreadable, return an error string.

#### `validate_brand(content: str) -> str`

Validate content against the brand guidelines. Reads `tokens.json` to
check content against canonical values. Returns a JSON report.

Checks to implement:

1. **Colour references** — scan for hex colour codes in content. Flag any
   hex code that is not in `tokens.json` `colours` values. This catches
   off-brand colours being introduced.

2. **Font references** — scan for font-family references in content. Flag
   any font name that is not in `tokens.json` `fonts` values. This catches
   off-brand fonts being introduced.

3. **Spelling** — flag "color" (American) when found outside of code blocks
   or HTML/CSS attributes. The brand uses British English ("colour").

Return format:

```json
{
  "passed": true,
  "issue_count": 0,
  "issues": []
}
```

Issue format:

```json
{
  "type": "off_brand_colour",
  "found": "#FF0000",
  "line": 12,
  "suggestion": "Use a colour from tokens.json"
}
```

Issue types: `off_brand_colour`, `off_brand_font`, `spelling`.

### 5. Create requirements.txt

```
mcp
```

### 6. Apply standard conventions

- Filter `.provenance.md` files in discovery and loading functions
- All tools return error strings on failure — never raise
- Logging to stderr only
- `from __future__ import annotations`
- Server docstring with usage and transport info

### 7. Register in .mcp.json

Add `sdd-book-brand` server entry:

```json
"sdd-book-brand": {
  "type": "stdio",
  "command": "python",
  "args": [".brandmcp/server.py"]
}
```

### 8. Write provenance

Create the provenance file for this execution at:

```
.specmcp/specs/provenance/devops/brandmcp-build.provenance.md
```

Overwrite (do not append). This file describes only this execution.

### 9. Verify

Every check below is mandatory. Do not skip any.

- [ ] `ruff check .brandmcp/` passes
- [ ] `ruff format --check .brandmcp/` produces no changes
- [ ] `pre-commit run --all-files` passes
- [ ] `python .brandmcp/server.py` starts without error
- [ ] `list_brand` returns four entries: palette, typography, layout, voice
- [ ] `get_brand("palette")` returns colour palette content
- [ ] `get_brand("typography")` returns typography content
- [ ] `get_brand("nonexistent")` returns an error string, does not raise
- [ ] `get_design_tokens` returns valid JSON with `colours`, `fonts`, and `page` keys
- [ ] `tokens.json` is valid JSON and parseable
- [ ] `validate_brand` with clean content returns `{"passed": true, ...}`
- [ ] `validate_brand` with an off-brand hex code flags it as `off_brand_colour`
- [ ] `validate_brand` with "color" in prose flags it as `spelling`
- [ ] `.mcp.json` contains `sdd-book-brand` entry

## Out of Scope

- Updating AGENTS.md (separate task)
- Changes to `.specmcp` or `.skillmcp`
- Changes to cover SVGs or LaTeX template
- Migrating cover SVGs or LaTeX template to consume `tokens.json`
  (future spec — this is the natural next step)

## Branch

```
spec/brandmcp-build/initial
```
