# Specification Driven Development: The Book

A practical guide to Specification Driven Development (SDD) for professional developers working with AI coding agents.

## What is this?

This repository contains the specifications, content, and build pipeline for a book about Specification Driven Development—a methodology where specifications become the primary artifact and code becomes a generated side effect.

The book is being written using SDD. The specifications in this repo drive the content generation.

## Core Thesis

> The specification is the artifact. Code is a side effect.

## Repository Structure

```
.
├── specs/
│   ├── editorial/          # What to write
│   │   ├── book-brief.md
│   │   ├── chapter-outline.md
│   │   ├── writers-guide.md
│   │   ├── glossary.md
│   │   ├── prior-art.md
│   │   ├── diataxis-integration.md
│   │   └── continuity-tracker.md
│   └── workflow/           # How to write it
│       └── workflow.md
├── content/                # Generated book content (coming)
├── build/                  # EPUB and audio configuration (coming)
├── validation/             # Content validation scripts (coming)
└── output/                 # Generated artifacts (gitignored)
```

## Specifications

| Document | Purpose |
|----------|---------|
| `book-brief.md` | Scope, thesis, audience, boundaries |
| `chapter-outline.md` | 26 chapters across 5 parts |
| `writers-guide.md` | Voice, tone, style rules |
| `glossary.md` | 27 canonical term definitions |
| `prior-art.md` | Related practices and positioning |
| `diataxis-integration.md` | Content type framework (Tutorial/How-to/Reference/Explanation) |
| `continuity-tracker.md` | Cross-reference and consistency tracking |
| `workflow.md` | Authoring workflow and CI/CD pipeline |

## Target Audience

Professional developers (3+ years experience) who:

- Use AI coding tools but find ad-hoc prompting frustrating
- Want systematic methods, not hacks
- Value engineering discipline over "vibe coding"

## Outputs

- **EPUB** — Primary distribution format
- **Audiobook** — Generated from markdown via ElevenLabs

## Development

```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Run linting manually
pre-commit run --all-files
```

## License

This work is licensed under [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International](https://creativecommons.org/licenses/by-nc-nd/4.0/).

You are free to share this material with attribution. You may not use it commercially or create derivative works.
