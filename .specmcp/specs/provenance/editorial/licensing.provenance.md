# Provenance: licensing

## 2026-02-18 — Update copyright page to match licensing spec

**Prompt:** Create a branch named `spec/licensing/update-copyright` and execute
the `licensing` spec. Read the spec with `get_spec("licensing")`, then update
the copyright page in `content/00-front-matter/02-copyright.md` to match the
specified content and ordering. Record a provenance entry in
`editorial/licensing.provenance.md`. Commit the changes and open a PR against
`main`.

**Branch:** claude/update-copyright-page-9YW3M
**Commit(s):** (included in this commit)

### Actions taken

1. Read the licensing spec and provenance convention.
2. Replaced the contents of `content/00-front-matter/02-copyright.md` with the
   spec-mandated copyright notice (`© 2026 Kevin Ryan. All rights reserved.`),
   the verbatim human-readable licensing summary covering the three-layer model
   (CC BY-NC-ND 4.0, MIT, DEL v1.0), a DEL reference note with link, and
   retained book title/edition metadata.
3. Updated `build/pdf/template.tex` (lines 157–184) to mirror the new copyright
   page content for PDF output, since the PDF build renders the copyright page
   from the LaTeX template rather than the markdown source.
4. Created this provenance file.

### Decisions

- **Retained `{.unnumbered}` heading attribute.** The spec does not prescribe a
  heading format. The existing Pandoc attribute is required for correct EPUB
  rendering and matches the convention used by other front-matter files.
- **Retained book title and edition line.** The spec lists four required
  elements but does not say the page must contain only those elements. The
  title and edition are standard copyright-page metadata, present in the LaTeX
  template, and were kept after the DEL reference.
- **Omitted build traceability line from source.** The spec says it is "injected
  by the build pipeline." Both build scripts (EPUB via `build-epub.py` and PDF
  via `template.tex` conditional) handle this dynamically.
- **Adjusted heading level from `###` to `##`.** The spec's summary uses `###`
  because it is nested under `## Human-Readable Summary` in the spec document.
  In the copyright page (which starts at `#`), `##` is the correct next level.
  This also resolves a markdownlint MD001 violation.
- **Deferred README and LICENSE-DEL updates.** The spec's Implementation Notes
  mention updating the README license table and adding a LICENSE-DEL file. These
  are separate deliverables outside the "update copyright page" scope and can be
  addressed in a follow-up execution of the licensing spec.

### MCP calls

1. `get_spec("licensing")`
2. `get_spec("provenance")`

### Deviations

- **Branch name:** Used `claude/update-copyright-page-9YW3M` instead of the
  provenance convention `spec/licensing/update-copyright`. The `claude/` prefix
  is a system-enforced requirement for push access in this environment.
