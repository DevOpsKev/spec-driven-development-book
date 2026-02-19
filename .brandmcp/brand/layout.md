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
