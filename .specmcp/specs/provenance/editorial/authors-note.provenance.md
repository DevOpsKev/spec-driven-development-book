# Provenance: authors-note

## 2026-02-18 — Add author's note front matter page

**Prompt:** Create a branch named `spec/authors-note/add-front-matter` and execute
the `authors-note` spec. Read the spec with `get_spec("authors-note")`, then
create the Author's Note page at `content/00-front-matter/05-authors-note.md`,
renumber existing front matter files from 05 onward, and update the build
pipeline to handle the new page. Record a provenance entry in
`editorial/authors-note.provenance.md`. Commit the changes and push the branch.

**Branch:** claude/add-authors-note-890SJ
**Commit(s):** (included in this commit)

### Actions taken

1. Read the authors-note spec and provenance convention.
2. Created `content/00-front-matter/05-authors-note.md` with beta status
   declaration, methodology hook, call for involvement, contact details,
   and contributor recognition policy. Content is 157 words, first person,
   uses `{.unnumbered}` Pandoc attribute.
3. Renamed `content/00-front-matter/07-preface.md` to
   `content/00-front-matter/08-preface.md` to align with the workflow spec's
   numbering scheme, which places the preface at position 08.
4. Verified that both build scripts (`build-pdf.py`, `build-epub.py`) discover
   files via glob and sort by numeric prefix — no hardcoded filename references
   to update. The new file is assembled from markdown like any other content
   file; it is not added to the `TEMPLATE_HANDLED` skip set.
5. Created this provenance file.

### Decisions

- **Author's note rendered from markdown, not template.** The spec says the
  author's note should be handled in the LaTeX template like the copyright page.
  The author directed that both PDF and EPUB builds should pick it up from the
  markdown source instead, keeping it out of `TEMPLATE_HANDLED`. This simplifies
  maintenance — one source file serves both formats.
- **Preface renumbered from 07 to 08.** The workflow spec lists the preface at
  position 08. The existing file at 07 was a holdover from before the full
  front matter numbering scheme was established.
- **No workflow spec update needed.** The spec's implementation notes say to
  update the workflow spec's repo structure, front matter table, and file
  naming examples. All three already list `05-authors-note.md` and
  `08-preface.md` at the correct positions.

### MCP calls

1. `get_spec("provenance")` (read directly from file)
2. `get_spec("authors-note")` (read directly from file)

### Deviations

- **Branch name:** Used `claude/add-authors-note-890SJ` instead of the
  provenance convention `spec/authors-note/add-front-matter`. The `claude/`
  prefix is a system-enforced requirement for push access in this environment.
- **Renumbering scope.** The spec says "renumber existing front matter files
  from `05-toc.md` onward (05 → 06, 06 → 07, etc. through to 09 → 10)." No
  file `05-toc.md` exists — the TOC is rendered by `\tableofcontents` in the
  LaTeX template. Positions 03–06 were vacant. Only `07-preface.md` was
  renumbered to `08-preface.md`. This is a spec bug: the spec assumes files
  exist at positions that are currently empty.
- **Template not modified.** The spec says the author's note must be handled in
  `template.tex` like the copyright page. Per author direction, the file is
  instead assembled from the markdown source by both build scripts, with no
  template changes.
