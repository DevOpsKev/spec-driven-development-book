# Spec: readme-update — Generated README from Repository State

## Purpose

Generate `README.md` as a repeatable, spec-driven artifact that reflects
the current state of the repository, overwriting the previous version on
each execution.

## Prerequisites

Before executing this spec, load the following:

```
get_spec("provenance")
```

No domain skill is required — this spec drives content generation, not
code generation.

## Context

The current `README.md` was hand-authored and has already drifted from
the repository's actual state. It lists specs statically, omits the
brand and provenance systems, references `CLAUDE.md` instead of
`AGENTS.md`, and contains a "Progress" section that rots immediately.

This spec makes `README.md` a generated artifact. Each execution
discovers the repository's current state through MCP tools and directory
scanning, overwrites `README.md`, and records provenance. The README
itself carries a generation notice directing contributors to update the
spec rather than hand-editing the file.

This is also a dogfooding proof: the repository that teaches
Specification Driven Development uses SDD to maintain its own
documentation. The README should make this explicit.

## Single Source of Truth

This spec is the canonical source for the structure and content of
`README.md`. No other file defines what the README contains or how it
is organised.

- To change the README's structure, section ordering, or stable template
  prose: edit this spec and re-execute.
- To change dynamically discovered content (e.g., a new spec or MCP
  server): the next execution will pick it up automatically.
- `README.md` is a generated output. Do not hand-edit it.

## Changes

### 1. Discovery phase

Run the following discovery steps in this order. Each step must return
non-empty results unless explicitly noted otherwise. If any MCP call
returns an empty list or a required file does not exist, **halt
execution immediately** and report the failure as a spec deficiency —
do not generate empty or placeholder sections.

#### 1a. Load MCP server registry

Read `.mcp.json` from the repository root. Extract the server names,
command paths, and arguments. This gives the list of registered MCP
servers.

**Sanity floor:** `.mcp.json` must contain at least 2 server entries.

#### 1b. Discover specs

Call `list_specs()`. Parse the result to extract every spec's name,
category, and title. Group by category for the specs table.

**Sanity floor:** The result must contain at least 5 specs. If fewer,
halt and flag as a discovery failure.

#### 1c. Discover skills

Call `list_skills()`. Parse the result to extract every skill's name
and description.

**Sanity floor:** The result must contain at least 2 skills.

#### 1d. Discover brand resources

Call `list_brand()`. Parse the result to extract every brand resource's
name and title.

**Sanity floor:** The result must contain at least 3 brand resources.

#### 1e. Discover provenance records

Call `list_provenance()`. Parse the result. This populates the
provenance section. An empty result is acceptable here (not all specs
have been executed), but record the count.

#### 1f. Scan repository structure

Scan the repository's top-level directory and key subdirectories to
produce an accurate directory tree. Include:

- All top-level files and directories (excluding `.git/`)
- One level of depth inside: `.specmcp/`, `.skillmcp/`, `.brandmcp/`,
  `assets/`, `build/`, `content/`, `scripts/`, `site/`, `.github/`,
  `infra/`, `notes/`
- Two levels of depth inside `.specmcp/specs/` to show categories

Use actual directory scanning (e.g., `ls` or filesystem traversal), not
hardcoded paths. The tree must reflect reality at execution time.

### 2. Assemble README.md

Write `README.md` with the following sections in this exact order. Each
section is either **dynamic** (populated from discovery) or **stable**
(template prose verified against repo but not dynamically generated).
Stable sections are structurally fixed — their content is defined in
this spec. They should be verified against the current repo state but
not rewritten from discovery.

British English throughout (colour, licence, behaviour, organised, etc.).

---

#### 2a. Generation notice (stable)

Place the following at the very top of the file, before the H1 heading:

```markdown
<!-- GENERATED FILE — DO NOT HAND-EDIT -->
<!-- Source: .specmcp/specs/devops/readme-update.md -->
<!-- Re-generate by executing the readme-update spec -->

> **Generated file** — do not edit directly. This README is produced by
> the [`readme-update`](.specmcp/specs/devops/readme-update.md) spec.
> To change it, update the spec and re-execute.
```

#### 2b. Title and overview (stable)

```markdown
# Specification Driven Development: The Book

A practical guide to Specification Driven Development (SDD) for
professional developers working with AI coding agents.

**Website:** [sddbook.com](https://sddbook.com)

This repository contains the specifications, content, and build pipeline
for a book about Specification Driven Development — a methodology where
specifications become the primary artifact and code becomes a generated
side effect.
```

#### 2c. Core thesis (stable)

```markdown
## Core Thesis

> The specification is the artifact. Code is a side effect.
```

#### 2d. Dogfooding (stable)

```markdown
## This Repository Proves the Methodology

This repository is itself specification-driven. The book about SDD is
written using SDD. Specifications in `.specmcp/specs/` drive content
generation, MCP servers provide structured access to project resources,
and even this README is a generated artifact produced by executing a
spec.

Every workflow in this repository follows the SDD two-loop process
described below. The provenance system records what happened during each
spec execution, creating an audit trail that complements the git history.

If you want to understand what Specification Driven Development looks
like in practice, explore this repository.
```

#### 2e. The SDD workflow (stable)

This is a prominent section. Use this exact content:

```markdown
## The SDD Workflow

The SDD workflow has eight steps across two loops. The spec loop is
where the creative work happens. The execution loop is mechanical.

### The Spec Loop

1. **Brief** — Capture intent as bullet points or a problem statement.
   The brief is the spec for the spec — fast, loose, and incomplete by
   design.
2. **Spec draft** — An agent expands the brief into a full
   specification. The agent asks clarifying questions if the brief has
   gaps.
3. **Iterate spec** — The human reviews the draft. This is where the
   real intellectual work happens: missing requirements, implicit
   assumptions, verification gaps, scope creep.
4. **Commit spec to main** — The spec is the artifact. Committing it
   marks it as approved and ready for execution.

### The Execution Loop

5. **Plan** — An agent reads the committed spec and produces an
   execution plan in plan mode only — no files created, no changes made.
6. **Validate plan against spec** — Does the plan reveal deficiencies
   in the spec? If yes, fix the spec and discard the plan. If no,
   approve.
7. **Execute** — The agent executes the approved plan. The prompt
   should be minimal — if it needs to explain the work, the spec is
   deficient.
8. **Validate results** — Run every verification check listed in the
   spec. Every check is mandatory.

**Key principle:** The spec loop is where you spend your cognitive
budget. The execution loop should be boring. If execution is surprising,
the spec has holes.

For the full workflow reference, see [`AGENTS.md`](AGENTS.md).
```

#### 2f. MCP servers and tools (dynamic)

Generate this section from the discovery results in steps 1a–1d. For
each server registered in `.mcp.json`, list its name, script path, and
all tools with their descriptions.

The tools for each server are discovered by observing the MCP tools
available during execution and confirming against the `list_*` calls.
Do NOT read Python source files to extract tool information — the MCP
tools themselves are the authoritative source.

Format:

```markdown
## MCP Servers

This repository includes local MCP servers that provide AI agents with
structured access to project resources. All servers are registered in
[`.mcp.json`](.mcp.json).

### <Server display name> (`<script path>`)

<One-sentence description>

- **<tool_name>** — <description>
- ...
```

Repeat for each server. Include all tools discovered on each server.

#### 2g. Specifications table (dynamic)

Generate from `list_specs()` results. Group specs by category and
present as a table. Link each spec name to its file path.

```markdown
## Specifications

| Spec | Category | Purpose |
|------|----------|---------|
| [`<name>`](<path>) | <category> | <title from list_specs> |
| ... | ... | ... |
```

#### 2h. Skills table (dynamic)

Generate from `list_skills()` results. Link each skill name to its
file path.

```markdown
## Skills

| Skill | Description |
|-------|-------------|
| [`<name>`](<path>) | <description from list_skills> |
| ... | ... |
```

#### 2i. Target audience (stable)

```markdown
## Target Audience

Professional developers (3+ years experience) who:

- Use AI coding tools but find ad-hoc prompting frustrating
- Want systematic methods, not hacks
- Value engineering discipline over "vibe coding"
```

#### 2j. Outputs (stable)

```markdown
## Outputs

The build pipeline produces three book formats from the same markdown
source:

| Format | File | Purpose |
|--------|------|---------|
| **EPUB** | `spec-driven-development.epub` | E-readers and digital distribution |
| **Screen PDF** | `spec-driven-development.pdf` | Digital download with cover, RGB colours, clickable links |
| **Print PDF** | `spec-driven-development-print.pdf` | Print-ready interior (no cover, CMYK-safe, black links) |

All outputs are deployed to Azure Blob Storage on merge to `main`.
Each build embeds the short git hash and build date on the copyright
page for traceability.
```

#### 2k. Repository structure (dynamic)

Generate the directory tree from the actual scan in step 1f. Annotate
directories with brief descriptions based on their contents.

```markdown
## Repository Structure

```
<actual tree from step 1f>
```
```

#### 2l. Provenance system (stable + dynamic count)

```markdown
## Provenance

Every spec execution leaves a trace. Provenance files record what was
done, why, and how — creating an audit trail that complements the git
history.

Provenance files are stored at
`.specmcp/specs/provenance/<category>/<spec-name>.provenance.md` and
are overwritten on each execution (git provides the history). See the
[provenance spec](.specmcp/specs/workflow/provenance.md) for the full
convention.

**Current provenance records:** <N> (discovered via `list_provenance`)
```

Replace `<N>` with the actual count from step 1e.

#### 2m. Build (stable)

```markdown
## Build

### Prerequisites

```bash
# Install system dependencies (pandoc, texlive, fonts)
chmod +x scripts/setup-deps.sh
./scripts/setup-deps.sh
```

### Building locally

```bash
# Build cover images from SVG sources
python3 scripts/build-cover.py

# Build EPUB
python3 scripts/build-epub.py

# Build both PDF variants (screen + print)
python3 scripts/build-pdf.py

# Build a single variant
python3 scripts/build-pdf.py --variant screen
python3 scripts/build-pdf.py --variant print

# Include git hash and build date
python3 scripts/build-pdf.py \
  --git-hash "$(git rev-parse --short HEAD)" \
  --build-date "$(date +%Y-%m-%d)"
```

Output goes to `output/` (gitignored).
```

#### 2n. PDF typography (stable)

```markdown
### PDF Typography

PDFs are typeset with XeLaTeX at 6 x 9 inch trim size using Google
Fonts:

- **Source Serif 4** — Body text (designed for long-form reading)
- **Alfa Slab One** — Part and chapter titles
- **Inter** — Section headings
- **JetBrains Mono** — Code blocks

All fonts are committed to `assets/fonts/` for reproducible builds.
```

#### 2o. CI/CD (stable)

```markdown
## CI/CD

| Workflow | Trigger | What it does |
|----------|---------|--------------|
| `build-book.yml` | Push/PR to `main` | Builds cover, EPUB, and both PDFs. Deploys to Azure Blob Storage on merge. |
| `deploy-site.yml` | Push to `main` (`site/` changes) | Deploys landing page to GitHub Pages |

The build pipeline captures the git short hash and build date, passing
them to all build scripts. These are embedded on the copyright page of
every output so any copy can be traced back to the exact commit that
produced it.
```

#### 2p. Development (stable)

```markdown
## Development

```bash
# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Install MCP server dependencies
pip install -r .specmcp/requirements.txt

# Run linting manually
pre-commit run --all-files
```

For agent workflow and project conventions, see
[`AGENTS.md`](AGENTS.md).
```

#### 2q. Licence (stable)

```markdown
## Licence

This repository uses split licensing:

| Content | Licence |
|---------|---------|
| Book content, specifications, prose (`.specmcp/specs/`, `content/`) | [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/) |
| Code, scripts, build tooling (`scripts/`, `build/`, config files) | [MIT](LICENSE-MIT) |

**Book content:** Free to share with attribution. No commercial use or
derivatives.

**Code:** Do whatever you want with attribution.
```

### 3. Write README.md

Overwrite the existing `README.md` at the repository root with the
assembled content from step 2. This is a complete replacement, not a
patch.

### 4. Write provenance

Create (or overwrite) the provenance file for this execution at:

```
.specmcp/specs/provenance/devops/readme-update.provenance.md
```

Overwrite (do not append). This file describes only this execution.

The provenance entry must include:

- The MCP calls made during discovery (in order)
- The spec and skill counts discovered
- The directory scan results summary
- Any decisions made or deviations from this spec

### 5. Verify

Every check below is mandatory. Do not skip any.

#### Existence and structure

- [ ] `README.md` exists at the repository root
- [ ] `README.md` begins with the HTML generation notice comment
- [ ] The visible generation notice block appears before the H1 heading
- [ ] The H1 heading is `Specification Driven Development: The Book`
- [ ] `sddbook.com` appears as a link in the overview section
- [ ] The file references `AGENTS.md` (not `CLAUDE.md`) for workflow

#### Dynamic content sanity floors

- [ ] The Specifications table contains at least 5 entries
- [ ] The MCP Servers section lists at least 2 servers
- [ ] The MCP Servers section lists at least 10 tools total across all
      servers
- [ ] The Skills table contains at least 2 entries
- [ ] The Repository Structure tree includes `.specmcp/`, `.skillmcp/`,
      `.brandmcp/`, `content/`, `scripts/`

#### Stable content

- [ ] The SDD Workflow section includes all eight numbered steps
- [ ] The Outputs table lists EPUB, Screen PDF, and Print PDF
- [ ] The CI/CD table lists `build-book.yml` and `deploy-site.yml`
- [ ] The Licence section lists both CC BY-NC-ND 4.0 and MIT

#### Omissions

- [ ] No "Progress" section exists (replaced by provenance reference)
- [ ] No hand-editable content remains — all content is either
      discovered or defined as stable template in this spec

#### Language

- [ ] British English spelling throughout (colour, licence, behaviour,
      organised)
- [ ] No American English spellings of British-preferred terms

#### Provenance

- [ ] Provenance file exists at
      `.specmcp/specs/provenance/devops/readme-update.provenance.md`
- [ ] Provenance entry includes the MCP calls made during discovery

## Out of Scope

- Updating `AGENTS.md` (separate task)
- Changes to any MCP server code (`.specmcp/`, `.skillmcp/`,
  `.brandmcp/`)
- Changes to any spec other than creating this spec's provenance file
- Changes to book content in `content/`
- Changes to build scripts or CI/CD workflows
- Validating README content against the brand voice (future enhancement)
- Adding a CI workflow to re-generate README on changes (future spec)

## Branch

```
spec/readme-update/generate
```
