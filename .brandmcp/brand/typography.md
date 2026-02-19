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
