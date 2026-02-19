# Spec: epigraph — Create the Book's Epigraph Page

## Purpose

Create the epigraph front matter page and add the template and CSS
support needed to render it correctly in both PDF and EPUB builds.

## Prerequisites

Before executing this spec, load the following:

```
get_spec("provenance")
get_spec("writers-guide")
```

No domain skill is required — this spec drives content creation and
template modification, not code generation.

## Context

The book's front matter workflow spec (`workflow/workflow.md`) already
defines a slot at `content/00-front-matter/04-epigraph.md`. The file
does not yet exist. This spec creates it and ensures both output formats
render the epigraph correctly.

The epigraph is a short opening quotation that appears in the front
matter, after the copyright page and before the author's note. It is
unnumbered, has no running header, and carries no chapter designation.

Current state of the build pipeline relevant to this work:

- **PDF build** (`scripts/build-pdf.py`): Assembles front matter files
  into `$body$` via pandoc + XeLaTeX. Files in `00-front-matter/` are
  included unless listed in `TEMPLATE_HANDLED` (currently only
  `01-title-page.md` and `02-copyright.md`). The epigraph file will be
  assembled as regular markdown content in frontmatter mode (roman
  numerals, before `\mainmatter`).
- **PDF template** (`build/pdf/template.tex`): Defines `\frontmatter`,
  then hardcoded half-title, title page, copyright, and TOC, followed
  by `$body$`. No epigraph environment or styling exists.
- **EPUB build** (`scripts/build-epub.py`): Includes all markdown files
  in section order. References `CSS_FILE` at `build/epub/styles.css`
  and includes it if present. The CSS file does not yet exist.
- **EPUB metadata** (`build/epub/metadata.yaml`): Sets `lang: en-GB`.

Pandoc converts fenced divs (`::: {.classname}`) to
`\begin{classname}...\end{classname}` in LaTeX output and
`<div class="classname">...</div>` in HTML/EPUB output. This spec
relies on that behaviour for format-specific styling.

## Single Source of Truth

The epigraph text and attribution are defined in
`content/00-front-matter/04-epigraph.md`. That file is the single
source of truth. The template and CSS reference the `.epigraph` class
but do not contain the text.

## Changes

### 1. Create `content/00-front-matter/04-epigraph.md`

Create the file with this exact content:

```markdown
::: {.epigraph}
*It's turtles all the way down*

— Attributed to everyone, owned by no one.
:::
```

Notes on this structure:

- The fenced div `::: {.epigraph}` gives both LaTeX and HTML a styling
  hook without inline formatting.
- The quote text uses `*...*` (emphasis) — Pandoc renders this as
  `\emph{}` in LaTeX and `<em>` in HTML. The template and CSS control
  the final visual presentation.
- The attribution line starts with an em dash (`—`), not a hyphen.
- There is no H1 heading. The epigraph is a decorative page, not a
  chapter. This means the EPUB build will not create a separate XHTML
  section for this content — it will appear at the end of the preceding
  section's XHTML file (the copyright page). The CSS `page-break-before`
  rule in change 3 forces a visual page break in EPUB readers, which is
  sufficient for this use case.
- British English throughout.

### 2. Add epigraph environment to `build/pdf/template.tex`

Insert the following LaTeX block in the preamble, after the Pandoc
compatibility section (after the `$if(csl-refs)$...$endif$` block,
before `\begin{document}`). Add a blank line before and after the new
block.

```latex
% === EPIGRAPH ===
\newenvironment{epigraph}{%
  \cleardoublepage
  \thispagestyle{empty}%
  \null\vfill
  \begin{center}%
  \begin{minipage}{0.7\textwidth}%
  \centering\large
}{%
  \end{minipage}%
  \end{center}%
  \vfill\null
  \cleardoublepage
}
```

This environment:

- Starts on a new recto page (`\cleardoublepage`).
- Suppresses running headers and page numbers (`\thispagestyle{empty}`).
- Vertically centres the content (`\vfill` above and below).
- Horizontally centres the content in a 70% width minipage.
- Sets the base font size to `\large` (the emphasis markup in the
  markdown handles italic).
- Ends with `\cleardoublepage` so the next content starts on a fresh
  page.

### 3. Create `build/epub/styles.css`

Create the file at `build/epub/styles.css` with this exact content:

```css
/* Epigraph page styling */
.epigraph {
  margin: 20% auto 0;
  padding: 0 10%;
  text-align: center;
  page-break-before: always;
  page-break-after: always;
}

.epigraph p:first-child {
  font-size: 1.2em;
}

.epigraph p:last-child {
  font-size: 0.9em;
  margin-top: 1.5em;
}
```

Notes:

- `page-break-before: always` forces a visual page break in EPUB
  readers, separating the epigraph from the copyright page content even
  though they share an XHTML section (see change 1 notes).
- `page-break-after: always` separates the epigraph from whatever
  follows.
- `margin: 20% auto 0` pushes the content down from the top, creating
  a visually centred effect in reflowable EPUB layouts.
- `padding: 0 10%` constrains the text width for readability.
- The first paragraph (the quote) is slightly larger; the last paragraph
  (the attribution) is slightly smaller with a top margin for spacing.
- The emphasis (`<em>`) from the markdown already renders in italic —
  no additional `font-style` rule is needed.
- The CSS file is intentionally epigraph-only. Future front matter
  specs that need EPUB styling should add to this file rather than
  create new ones. The EPUB build script includes the file if it exists
  (line 133 of `scripts/build-epub.py`).

## Out of Scope

- Other front matter files (title page, copyright, author's note,
  preface, dedication, foreword, TOC).
- Chapter content.
- Changes to build scripts (`build-epub.py`, `build-pdf.py`).
- CI/CD workflows.
- Adding the epigraph file to the `TEMPLATE_HANDLED` set in the PDF
  build script — the epigraph is assembled as regular markdown content,
  not rendered from the LaTeX template.
- Restructuring front matter file numbering — the `04-` slot already
  exists in the workflow spec.
- EPUB TOC entries — the epigraph has no heading and should not appear
  in the table of contents. If EPUB testing reveals an unwanted TOC
  entry, that is a separate issue.

## Verification

Every check below is mandatory. Do not skip any.

### File existence

- [ ] `content/00-front-matter/04-epigraph.md` exists.
- [ ] `build/epub/styles.css` exists.
- [ ] `build/pdf/template.tex` exists and contains the `epigraph`
      environment definition.

### Markdown content

- [ ] `04-epigraph.md` contains exactly one fenced div with class
      `.epigraph`.
- [ ] The quote text is `*It's turtles all the way down*` (emphasis
      markers, no other formatting).
- [ ] The attribution is `— Attributed to everyone, owned by no one.`
      (em dash, not hyphen).
- [ ] The file contains no H1 or other heading.
- [ ] The file contains no inline styling, no raw LaTeX, and no raw
      HTML.
- [ ] The file uses British English (no American spellings).

### LaTeX template

- [ ] `template.tex` defines `\newenvironment{epigraph}` in the
      preamble (before `\begin{document}`).
- [ ] The environment uses `\thispagestyle{empty}` (no running headers
      or page numbers).
- [ ] The environment uses `\cleardoublepage` at start and end.
- [ ] The environment vertically centres the content with `\vfill`.
- [ ] The existing template content is otherwise unmodified — no
      deletions, no reordering, no changes to other environments.

### EPUB CSS

- [ ] `styles.css` contains a `.epigraph` rule block.
- [ ] The `.epigraph` rule includes `page-break-before: always`.
- [ ] The `.epigraph` rule includes `page-break-after: always`.
- [ ] The `.epigraph` rule includes `text-align: center`.
- [ ] The CSS file contains no rules unrelated to the epigraph.

### Negative checks

- [ ] `04-epigraph.md` does not appear in the `TEMPLATE_HANDLED` set
      in `scripts/build-pdf.py` (it should NOT be there).
- [ ] No changes have been made to `scripts/build-epub.py`.
- [ ] No changes have been made to `scripts/build-pdf.py`.
- [ ] No changes have been made to any file in `content/` other than
      creating `04-epigraph.md`.
- [ ] No changes have been made to `build/epub/metadata.yaml`.

## Branch

```
spec/epigraph/create
```
