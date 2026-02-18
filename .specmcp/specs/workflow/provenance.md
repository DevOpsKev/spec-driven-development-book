# Provenance

Convention for recording how specifications are executed by agents.

## Purpose

Every spec execution should leave a trace. A provenance file captures what
was done, why, and how — creating an audit trail that complements the git
history. The spec defines intent; the provenance records realisation.

## File Convention

Provenance files live alongside their parent spec using the naming pattern:

```
<spec-name>.provenance.md
```

Examples:

- `editorial/licensing.md` → `editorial/licensing.provenance.md`
- `editorial/glossary.md` → `editorial/glossary.provenance.md`
- `workflow/workflow.md` → `workflow/workflow.provenance.md`

A provenance file is created on first execution and appended to on subsequent
executions. Never replace or edit previous entries.

## Branch Convention

Spec-driven branches follow the naming pattern:

```
spec/<spec-name>/<action>
```

Examples:

- `spec/licensing/update-copyright`
- `spec/glossary/add-terms`
- `spec/chapter-outline/revise-part-3`

The `spec/` prefix identifies the branch as spec-driven rather than ad-hoc.

## Entry Structure

Each execution appends a new dated entry to the provenance file using the
following template:

```markdown
## YYYY-MM-DD — Short description of what was done

**Prompt:** The exact prompt or instruction that triggered execution.

**Branch:** spec/<spec-name>/<action>
**Commit(s):** <short hash(es)>

### Actions taken

Describe each concrete action in the order it was performed. Be specific
about which files were created, modified, or deleted.

### Decisions

Record any judgment calls, ambiguities resolved, or trade-offs made during
execution. If the spec left room for interpretation, explain the choice and
the reasoning.

### MCP calls

List tool calls made during execution, in order:

1. `get_spec("licensing")`
2. `validate_content("content/front-matter/copyright.md")`

### Deviations

Note anything that diverged from the spec and why. If none, omit this
section.
```

## Rules

1. **Append-only.** Never edit or delete previous entries. Each execution
   adds a new dated section at the bottom of the file.
2. **One entry per execution.** A single prompt that triggers a single
   branch of work produces one entry, regardless of how many commits it
   takes.
3. **Honest reporting.** Provenance is self-reported by the executing agent.
   It is complementary to the git diff, not a replacement. Do not omit
   decisions or deviations.
4. **Create on first use.** If no provenance file exists for a spec, create
   it with a top-level heading `# Provenance: <spec-name>` followed by the
   first entry.
5. **Commit together.** The provenance entry should be included in the same
   PR as the spec execution work, not added after the fact.

## Prompt Template

When executing a spec, use a prompt of this form:

```
Create a branch named `spec/<spec-name>/<action>` and execute the
`<spec-name>` spec. Read the spec with `get_spec("<spec-name>")`, then
<describe the work>. Record a provenance entry in
`<spec-name>.provenance.md`. Commit the changes and push the branch.
```
