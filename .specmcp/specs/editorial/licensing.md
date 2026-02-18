# Licensing

Canonical specification for the book's copyright page and licensing terms.

## Purpose

Define the exact licensing structure, human-readable summary, and copyright
page text for *Specification Driven Development: Code is a Side Effect*.

## Licensing Stack

This project uses a three-layer licensing model: a base license per content
type, extended by the Distributed Equity License (DEL) v1.0 for AI-specific
terms.

### Book Content

Covers all prose, diagrams, specifications, and examples in `.specmcp/specs/`
and `content/`.

**Base license:** CC BY-NC-ND 4.0
(<https://creativecommons.org/licenses/by-nc-nd/4.0/>)

**AI extension:** DEL v1.0
(<https://distributedequity.org/license>)

**DEL flags:**
`airetrieval attributable quotable notraining noderivatives noncommercial`

**Custom clause — AI training requires express permission:**

> No AI or machine learning system may use the book content as training data,
> fine-tuning data, or for model adaptation without express written permission
> from the author. This restriction applies regardless of whether the use is
> commercial or non-commercial. For licensing enquiries contact the author
> directly.

### Code and Tooling

Covers all scripts, build pipeline, templates, and configuration files in
`scripts/`, `build/`, and project-level config files.

**Base license:** MIT (<https://opensource.org/licenses/MIT>)

**AI extension:** DEL v1.0
(<https://distributedequity.org/license>)

**DEL flags:**
`aitraining airetrieval aituning attributable`

## Human-Readable Summary

The following summary must appear on the copyright page of every output format
(EPUB, screen PDF, print PDF). It replaces any existing licensing text.

---

### Licensing — What You Can and Can't Do

This project uses three licenses working together. Here's what that means in
practice.

**The Book Content** (text, diagrams, examples)

License: CC BY-NC-ND 4.0 + DEL v1.0

You are free to read, share, and reference the book, quote excerpts with
attribution, use it for personal learning and education, and link to it from
any context.

AI systems may retrieve and cite the content in responses (with attribution),
quote limited excerpts (≤250 words or 10%, whichever is smaller), and reference
it in RAG and search systems.

You may not modify the text or create derivative works, use it for commercial
purposes, train AI/ML models on the content without express written permission
from the author, or republish or redistribute modified versions.

**The Code and Tooling** (build pipeline, scripts, templates)

License: MIT + DEL v1.0

You are free to use, copy, modify, and distribute the code, use it
commercially, and build your own projects with it.

AI systems may train on the code, retrieve and reference it, and fine-tune
models using it.

The only requirement is attribution — keep the copyright notice and license
text intact.

**Getting Permission**

If you want to do something these licenses don't cover — including AI training
on the book content — contact the author directly.

---

## Copyright Page Text

The copyright page in `content/00-front-matter/02-copyright.md` must contain,
in order:

1. Copyright notice: `© [year] Kevin Ryan. All rights reserved.`
2. The human-readable licensing summary above.
3. DEL reference: a note that AI-specific terms are governed by the
   Distributed Equity License v1.0 with a link to
   <https://distributedequity.org/license>.
4. Build traceability line (injected by the build pipeline):
   `Build [git-hash] · [build-date]`

## Implementation Notes

- The README license table must be updated to reflect the three-layer model
  (CC BY-NC-ND 4.0, MIT, and DEL v1.0) rather than just the two base licenses.
- LICENSE-CC-BY-NC-ND and LICENSE-MIT files at the repo root should be kept as
  the full legal texts of the base licenses.
- A LICENSE-DEL file or prominent link to
  <https://distributedequity.org/license> should be added at the repo root.
- DEL inline tags in source files are out of scope for this spec. They may be
  addressed in a future spec if granular per-file tagging is needed.
