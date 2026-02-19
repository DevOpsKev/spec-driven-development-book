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
