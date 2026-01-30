# SDD Workflow: Authoring This Book

This document defines the specification-driven workflow for writing, validating, and delivering this book. The book is authored using the methodology it describes.

---

## System Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        SPECIFICATION LAYER                          │
│  book-brief.md │ writers-guide.md │ chapter-outline.md │ glossary.md │
│  prior-art.md │ continuity-tracker.md │ chapter-briefs/              │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        GENERATION LAYER                             │
│                   AI Agent + Chapter Brief → Draft                  │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         ARTIFACT LAYER                              │
│                 chapters/*.md │ examples/ │ diagrams/               │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                        VALIDATION LAYER                             │
│    Continuity checks │ Glossary compliance │ Style validation       │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                         RUNTIME LAYER                               │
│              CI/CD Pipeline → EPUB → Audiobook (ElevenLabs)         │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Repository Structure

```
sdd-book/
├── specs/                              # Specification layer
│   ├── book-brief.md
│   ├── writers-guide.md
│   ├── chapter-outline.md
│   ├── glossary.md
│   ├── prior-art.md
│   ├── continuity-tracker.md
│   ├── author-voice.md
│   ├── examples-library.md
│   ├── anti-patterns.md
│   └── chapter-briefs/
│       ├── ch01-brief.md
│       ├── ch02-brief.md
│       └── ...
│
├── content/                            # Artifact layer (generated)
│   │
│   ├── 00-front-matter/                # Front matter (ordered first)
│   │   ├── 00-cover.md                 # Title, subtitle, author
│   │   ├── 01-title-page.md            # Full title page
│   │   ├── 02-copyright.md             # Copyright, edition, ISBN
│   │   ├── 03-dedication.md            # Optional
│   │   ├── 04-epigraph.md              # Optional opening quote
│   │   ├── 05-toc.md                   # Table of contents (auto-generated)
│   │   ├── 06-foreword.md              # Optional (by someone else)
│   │   ├── 07-preface.md               # Author's context, why this book
│   │   ├── 08-acknowledgments.md       # Optional (can also be back matter)
│   │   └── 09-introduction.md          # Setup for the reader
│   │
│   ├── 01-part-1-foundation/           # Part 1: Foundation
│   │   ├── 00-part-intro.md            # Part 1 intro (optional)
│   │   ├── 01-the-fifth-generation.md
│   │   ├── 02-the-problem-with-prompting.md
│   │   ├── 03-the-core-insight.md
│   │   ├── 04-specifications-vs-prompts.md
│   │   └── 05-the-five-layer-model.md
│   │
│   ├── 02-part-2-writing-specifications/ # Part 2: Writing Specifications
│   │   ├── 00-part-intro.md
│   │   ├── 06-anatomy-of-a-specification.md
│   │   ├── 07-defining-context.md
│   │   ├── 08-context-engineering.md
│   │   ├── 09-writing-requirements.md
│   │   ├── 10-constraints-and-boundaries.md
│   │   └── 11-acceptance-criteria.md
│   │
│   ├── 03-part-3-the-workflow/         # Part 3: The Workflow
│   │   ├── 00-part-intro.md
│   │   ├── 12-project-structure-for-sdd.md
│   │   ├── 13-the-generation-cycle.md
│   │   ├── 14-validation-and-drift-detection.md
│   │   ├── 15-iteration-as-spec-refinement.md
│   │   ├── 16-specops.md
│   │   └── 17-deterministic-cicd.md
│   │
│   ├── 04-part-4-practice/             # Part 4: Practice
│   │   ├── 00-part-intro.md
│   │   ├── 18-when-to-use-sdd.md
│   │   ├── 19-human-in-the-loop.md
│   │   ├── 20-failure-modes.md
│   │   ├── 21-sdd-in-teams.md
│   │   └── 22-beyond-code-generation.md
│   │
│   ├── 05-part-5-governance-and-evolution/ # Part 5: Governance and Evolution
│   │   ├── 00-part-intro.md
│   │   ├── 23-governed-evolution.md
│   │   ├── 24-generator-trust.md
│   │   └── 25-tradeoffs-and-costs.md
│   │
│   ├── 06-closing/                     # Closing
│   │   └── 26-the-future-of-specification.md
│   │
│   ├── 07-back-matter/                 # Back matter (ordered last)
│   │   ├── 01-appendix-a-specification-templates.md
│   │   ├── 02-appendix-b-glossary.md
│   │   ├── 03-appendix-c-quick-reference.md
│   │   ├── 04-bibliography.md          # References and further reading
│   │   ├── 05-index.md                 # Index (auto-generated or manual)
│   │   ├── 06-about-author.md          # Author bio
│   │   └── 07-colophon.md              # Optional: how book was made (meta!)
│   │
│   └── assets/                         # Shared assets
│       ├── diagrams/
│       │   ├── five-layer-model.svg
│       │   ├── generation-cycle.svg
│       │   └── ...
│       ├── examples/
│       │   ├── sample-spec-feature.md
│       │   ├── sample-spec-bugfix.md
│       │   └── ...
│       └── images/
│
├── build/                              # Build configuration
│   ├── epub/
│   │   ├── metadata.yaml               # EPUB metadata
│   │   ├── styles.css                  # EPUB styling
│   │   ├── cover.png                   # Cover image
│   │   └── epub-order.txt              # Explicit file ordering
│   ├── audio/
│   │   ├── elevenlabs-config.yaml      # Voice, model settings
│   │   ├── chapter-settings.yaml       # Per-chapter overrides
│   │   └── preprocessing-rules.yaml    # Markdown-to-speech rules
│   └── print/                          # Future: print PDF
│       └── print-styles.css
│
├── output/                             # Generated artifacts (gitignored)
│   ├── sdd-book.epub
│   ├── sdd-book.pdf
│   └── audio/
│       ├── 00-00-cover.mp3
│       ├── 00-07-preface.mp3
│       ├── 01-01-the-fifth-generation.mp3
│       └── ...
│
├── validation/                         # Validation scripts
│   ├── check-glossary.py
│   ├── check-continuity.py
│   ├── check-style.py
│   ├── check-structure.py
│   ├── check-links.py                  # Internal cross-references
│   ├── check-reading-order.py          # File ordering validation
│   └── requirements.txt
│
├── scripts/                            # Build and utility scripts
│   ├── generate-audio.py
│   ├── generate-toc.py                 # Auto-generate TOC
│   ├── generate-index.py               # Auto-generate index
│   ├── assemble-epub.py                # Combine files in order
│   └── validate-all.sh
│
├── .github/
│   └── workflows/
│       ├── validate.yml
│       ├── build-epub.yml
│       └── build-audio.yml
│
└── README.md
```

---

## Book Assembly Order

The book assembles in this sequence:

### Front Matter
| Order | File | Required | Notes |
|-------|------|----------|-------|
| 1 | cover.md | Yes | Title, subtitle, author name |
| 2 | title-page.md | Yes | Full title, author, publisher |
| 3 | copyright.md | Yes | © notice, edition, ISBN, rights |
| 4 | dedication.md | No | Short dedication |
| 5 | epigraph.md | No | Opening quote |
| 6 | toc.md | Yes | Auto-generated from chapters |
| 7 | foreword.md | No | Written by someone else |
| 8 | preface.md | Yes | Author's "why I wrote this" |
| 9 | acknowledgments.md | No | Can be front or back matter |
| 10 | introduction.md | Yes | Reader setup, how to use book |

### Body
| Order | Section | Chapters |
|-------|---------|----------|
| 11 | Part 1: Foundation | Ch 1–5 |
| 12 | Part 2: Writing Specifications | Ch 6–11 |
| 13 | Part 3: The Workflow | Ch 12–17 |
| 14 | Part 4: Practice | Ch 18–22 |
| 15 | Part 5: Governance and Evolution | Ch 23–25 |
| 16 | Closing | Ch 26 |

### Back Matter
| Order | File | Required | Notes |
|-------|------|----------|-------|
| 17 | appendix-a-specification-templates.md | Yes | Practical templates |
| 18 | appendix-b-glossary.md | Yes | Generated from glossary.md |
| 19 | appendix-c-quick-reference.md | Yes | Cheat sheet |
| 20 | bibliography.md | Yes | References, further reading |
| 21 | index.md | No | Auto-generated or manual |
| 22 | about-author.md | Yes | Author bio |
| 23 | colophon.md | No | How the book was made |

---

## File Naming Convention

```
[section]-[order]-[slug].md

Examples:
00-07-preface.md          # Front matter, 7th item, preface
01-03-the-core-insight.md # Part 1, chapter 3, slug
07-04-bibliography.md     # Back matter, 4th item, bibliography
```

**Section prefixes:**
| Prefix | Section |
|--------|---------|
| 00 | Front matter |
| 01 | Part 1 |
| 02 | Part 2 |
| 03 | Part 3 |
| 04 | Part 4 |
| 05 | Part 5 |
| 06 | Closing |
| 07 | Back matter |

This ensures correct alphabetical sorting matches reading order.

---

## Workflow Phases

### Phase 1: Specification

**Already complete:**
- [x] book-brief.md
- [x] writers-guide.md
- [x] chapter-outline.md
- [x] glossary.md
- [x] prior-art.md
- [x] continuity-tracker.md

**Remaining:**
- [ ] chapter-briefs/ (one per chapter)
- [ ] author-voice.md
- [ ] examples-library.md
- [ ] anti-patterns.md

---

### Phase 2: Chapter Brief Creation

Create one brief per chapter before generation.

**Chapter brief template:**

```markdown
# Chapter Brief: [Chapter Number] - [Chapter Title]

## Purpose
[One sentence: why this chapter exists]

## Reader State
- **Entering:** [What reader knows/feels coming in]
- **Exiting:** [What reader knows/feels leaving]

## Key Concepts
| Concept | Action |
|---------|--------|
| [Term] | Introduce / Reinforce / Reference |

## Required Content
- [ ] [Specific point that must be covered]
- [ ] [Specific point that must be covered]

## Required Examples
| Example | Type | Description |
|---------|------|-------------|
| [Name] | [Code/Spec/Workflow/Diagram] | [What it shows] |

## Constraints
- Word count: [Target range]
- Dependencies: [Chapters that must be read first]
- Forbidden: [Topics/terms to avoid in this chapter]

## Acceptance Criteria
- [ ] [Testable criterion]
- [ ] [Testable criterion]
- [ ] All terms from glossary used correctly
- [ ] No undefined terms introduced
- [ ] Continuity tracker updated

## Notes
[Any specific guidance for this chapter]
```

---

### Phase 3: Generation

**Input to agent:**
1. Full specification layer (all spec docs)
2. Chapter brief for target chapter
3. Any prior chapters (for continuity)

**Agent prompt structure:**

```
You are writing Chapter [N] of a book on Specification Driven Development.

## Specification Context
[Include: book-brief.md, writers-guide.md, glossary.md, prior-art.md]

## Chapter Brief
[Include: chapter-briefs/chNN-brief.md]

## Prior Content
[Include: any previously written chapters this chapter depends on]

## Continuity State
[Include: relevant sections of continuity-tracker.md]

## Task
Write the complete chapter following the brief and specifications.
```

**Output:** Draft markdown file in `content/chapters/`

---

### Phase 4: Validation

Run validation checks before accepting generated content.

| Check | Script | Validates Against |
|-------|--------|-------------------|
| Glossary compliance | `check-glossary.py` | glossary.md |
| Continuity | `check-continuity.py` | continuity-tracker.md, prior chapters |
| Style | `check-style.py` | writers-guide.md |
| Structure | `check-structure.py` | chapter-briefs/chNN-brief.md |

**Validation sequence:**

```
1. Generate chapter draft
2. Run validation suite
3. If PASS → Accept, update continuity-tracker.md
4. If FAIL → Identify failure type:
   a. Spec failure → Revise chapter brief, regenerate
   b. Generation failure → Regenerate with same brief
   c. Validation bug → Fix validation, re-run
```

---

### Phase 5: Iteration

**Iteration targets by failure type:**

| Failure | Symptom | Iteration Target |
|---------|---------|------------------|
| Wrong content | Missing/incorrect concepts | Chapter brief |
| Wrong tone | Style violations | writers-guide.md (if systemic) or regenerate |
| Wrong terms | Glossary violations | glossary.md (if term missing) or regenerate |
| Continuity error | Contradicts prior content | Chapter brief constraints |
| Structural issue | Missing sections | Chapter brief required content |

**Do not:** Tweak prompts. Refine specifications.

---

### Phase 6: Build (CI/CD)

#### EPUB Build Pipeline

**Trigger:** Push to `main` with changes in `content/`

```yaml
# .github/workflows/build-epub.yml
name: Build EPUB

on:
  push:
    branches: [main]
    paths:
      - 'content/**'
      - 'build/epub/**'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Install Pandoc
        run: sudo apt-get install -y pandoc
      
      - name: Build EPUB
        run: |
          pandoc \
            --metadata-file=build/epub/metadata.yaml \
            --css=build/epub/styles.css \
            --epub-cover-image=build/epub/cover.png \
            --toc \
            --toc-depth=2 \
            -o output/sdd-book.epub \
            content/chapters/*.md \
            content/appendices/*.md
      
      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: sdd-book-epub
          path: output/sdd-book.epub
```

#### Audiobook Build Pipeline

**Trigger:** Manual or on EPUB build success

```yaml
# .github/workflows/build-audio.yml
name: Build Audiobook

on:
  workflow_dispatch:
  workflow_run:
    workflows: ["Build EPUB"]
    types: [completed]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install elevenlabs markdown-it-py
      
      - name: Generate audio
        env:
          ELEVENLABS_API_KEY: ${{ secrets.ELEVENLABS_API_KEY }}
        run: python scripts/generate-audio.py
      
      - name: Upload artifacts
        uses: actions/upload-artifact@v4
        with:
          name: sdd-book-audio
          path: output/audio/
```

#### Audio Generation Script

```python
# scripts/generate-audio.py
import os
from pathlib import Path
from elevenlabs import generate, save, set_api_key
from markdown_it import MarkdownIt

set_api_key(os.environ['ELEVENLABS_API_KEY'])

# Configuration
VOICE_ID = "voice-id-here"  # Configure in build/audio/elevenlabs-config.yaml
MODEL = "eleven_multilingual_v2"
OUTPUT_DIR = Path("output/audio")
CHAPTERS_DIR = Path("content/chapters")

def markdown_to_text(md_content: str) -> str:
    """Strip markdown formatting for audio narration."""
    md = MarkdownIt()
    # Custom processing for:
    # - Remove code blocks or describe them
    # - Convert tables to readable format
    # - Handle emphasis appropriately
    # Implementation details...
    return plain_text

def generate_chapter_audio(chapter_path: Path):
    """Generate audio for a single chapter."""
    md_content = chapter_path.read_text()
    text = markdown_to_text(md_content)
    
    audio = generate(
        text=text,
        voice=VOICE_ID,
        model=MODEL
    )
    
    output_path = OUTPUT_DIR / f"{chapter_path.stem}.mp3"
    save(audio, str(output_path))
    print(f"Generated: {output_path}")

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    for chapter_file in sorted(CHAPTERS_DIR.glob("*.md")):
        generate_chapter_audio(chapter_file)

if __name__ == "__main__":
    main()
```

---

### Phase 7: Validation Pipeline

**Trigger:** Pull request to `main`

```yaml
# .github/workflows/validate.yml
name: Validate Content

on:
  pull_request:
    paths:
      - 'content/**'
      - 'specs/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: pip install -r validation/requirements.txt
      
      - name: Check glossary compliance
        run: python validation/check-glossary.py
      
      - name: Check continuity
        run: python validation/check-continuity.py
      
      - name: Check style
        run: python validation/check-style.py
      
      - name: Check structure
        run: python validation/check-structure.py
```

---

## Workflow Summary

| Step | Input | Output | Validation |
|------|-------|--------|------------|
| 1. Create chapter brief | chapter-outline.md, glossary.md | chapter-briefs/chNN-brief.md | Brief completeness |
| 2. Generate chapter | All specs + brief | content/chapters/NN-title.md | Automated checks |
| 3. Validate | Draft + specs | Pass/Fail + report | CI pipeline |
| 4. Iterate (if needed) | Failure report | Revised brief or regenerate | Re-run validation |
| 5. Accept | Validated draft | Merged to main | PR approval |
| 6. Build EPUB | All chapters | output/sdd-book.epub | Build success |
| 7. Build Audio | EPUB chapters | output/audio/*.mp3 | Build success |

---

## Iteration Decision Tree

```
Content fails validation
         │
         ▼
┌─────────────────────┐
│ What type of failure?│
└─────────────────────┘
         │
    ┌────┴────┬─────────────┬──────────────┐
    ▼         ▼             ▼              ▼
 Content    Style      Terminology    Continuity
  wrong     wrong        wrong          error
    │         │             │              │
    ▼         ▼             ▼              ▼
 Revise    Regenerate   Check if       Revise
 chapter   (style is    term should    chapter
 brief     in spec)     exist          brief
    │         │             │          constraints
    │         │        ┌────┴────┐         │
    │         │        ▼         ▼         │
    │         │     Add to    Regenerate   │
    │         │    glossary   (term error) │
    │         │        │         │         │
    └────┬────┴────────┴─────────┴─────────┘
         │
         ▼
    Regenerate chapter
         │
         ▼
    Re-run validation
```

---

## Audio-Specific Considerations

### Markdown to Audio Preprocessing

| Element | Audio Treatment |
|---------|-----------------|
| Headers | Pause before, announce as section |
| Code blocks | "The following code example shows..." or skip |
| Inline code | Speak naturally or spell out |
| Tables | Convert to list format or summarize |
| Links | Omit URL, keep link text |
| Emphasis (bold/italic) | Vocal emphasis (ElevenLabs handles) |
| Block quotes | "Quote:" prefix, pause after |
| Lists | Number items, pause between |

### Chapter Settings

```yaml
# build/audio/chapter-settings.yaml
defaults:
  voice: "voice-id"
  model: "eleven_multilingual_v2"
  stability: 0.5
  similarity_boost: 0.75

chapter_overrides:
  # Slower pace for foundational chapters
  01-the-fifth-generation:
    stability: 0.6
  
  # Technical chapters may need different handling
  05-the-five-layer-model:
    # Consider splitting by section
    split_by_heading: true
```

---

## Metrics to Track

| Metric | Purpose | Target |
|--------|---------|--------|
| Chapters complete | Progress | 26/26 |
| Validation pass rate | Quality | >90% first attempt |
| Iterations per chapter | Efficiency | <3 average |
| Brief revision rate | Spec quality | <20% of chapters |
| Build success rate | Pipeline health | 100% |
| Audio generation errors | Audio quality | 0 |

---

## Open Configuration Items

| Item | Decision Needed | Blocking |
|------|-----------------|----------|
| ElevenLabs voice selection | Which voice/model | Audio pipeline |
| EPUB styling | CSS design | EPUB build |
| Cover image | Design/create | EPUB build |
| Chapter word count targets | Length per chapter | Chapter briefs |
| Code block audio handling | Skip/describe/read | Audio preprocessing |
| Hosting/distribution | Where to publish | Post-build |