# Spec: author-spec Skill — How to Write Specifications

## Purpose

Create the `author-spec` skill that teaches AI agents how to write
effective specifications for SDD workflows, and fix the skill naming
convention to support multiple skills.

## Prerequisites

Before executing this spec, load the mcp-builder skill:

```
get_skill("SKILL")
```

Note: this prerequisite call will change after this spec executes.
Future specs will use `get_skill("mcp-builder")`.

## Context

The SDD book project has developed a mature specification authoring
workflow through iterative practice. The lessons learned are currently
distributed across conversation history, provenance files, and tacit
knowledge. This skill captures them as a reusable, teachable artifact.

This skill is distinct from the mcp-builder skill (which teaches how to
build MCP servers) and from the specs themselves (which describe specific
work). The author-spec skill teaches the *meta-practice* of writing
specifications that agents can execute reliably.

## Naming Convention Fix

The current mcp-builder skill uses the filename `SKILL.md`. This worked
with a single skill but breaks with multiple skills because
`load_skill()` matches on file stem — all skills named `SKILL.md` would
collide.

The fix: each skill file is named after the skill itself.

- `mcp-builder/SKILL.md` → `mcp-builder/mcp-builder.md`
- `author-spec/author-spec.md` (new)

This makes `get_skill("mcp-builder")` and `get_skill("author-spec")`
unambiguous. The `load_skill()` function in `.skillmcp/server.py`
requires no changes — it already matches on stem name.

## Changes

### 1. Rename mcp-builder skill file

Rename `.skillmcp/skills/mcp-builder/SKILL.md` to
`.skillmcp/skills/mcp-builder/mcp-builder.md` using `git mv`.

Content stays identical. Only the filename changes.

### 2. Update AGENTS.md references

Replace all references to `get_skill("SKILL")` in `AGENTS.md` with
`get_skill("mcp-builder")`.

If any other files in the repository reference `get_skill("SKILL")`,
update those too. Search the entire repo.

### 3. Create the author-spec skill file

Create `.skillmcp/skills/author-spec/author-spec.md` with the content
specified below.

### 4. Skill Content

The skill must cover the following sections in this order. Each section
includes the required content — the agent should use this as the source
material and write it as clear, direct prose in the skill's voice.

---

#### Section: SDD Level

This skill targets **spec-as-source** — the highest level of
Specification Driven Development. In this model:

- Specs are the primary artifact. Code is a generated side effect.
- Humans author and iterate specs. Humans never edit generated code.
- Specs are living documents that evolve with the system.
- The spec is kept after execution and remains the source of truth
  for future evolution and maintenance.

This is distinct from spec-first (write spec, use it, discard) and
spec-anchored (keep spec but humans also edit code). In spec-as-source,
the specification is the only thing the human maintains.

Reference: Birgitta Böckeler's taxonomy of SDD levels
(Fowler, "Exploring Gen AI" series, October 2025).

---

#### Section: The Workflow

The SDD workflow has eight steps across two loops. The spec loop
(steps 1–4) is where the creative work happens. The execution loop
(steps 5–8) is mechanical.

**The Spec Loop:**

1. **Brief** — The human captures intent as bullet points, rough
   requirements, or a problem statement. The brief is the spec for
   the spec. It is fast, loose, and incomplete by design.

2. **Spec draft** — An agent expands the brief into a full
   specification following the structure defined in this skill.
   The agent should ask clarifying questions if the brief has gaps.

3. **Iterate spec** — The human reviews the draft. This is where
   the real intellectual work happens. Look for: missing requirements,
   implicit assumptions, unstated conventions, verification gaps,
   scope creep, and single-source-of-truth violations.

4. **Commit spec to main** — The spec is the artifact. Committing
   it to main marks it as approved and ready for execution.

**The Execution Loop:**

5. **Plan** — An agent reads the committed spec and produces an
   execution plan. The plan must be generated in plan mode only —
   no files created, no changes made.

6. **Validate plan against spec** — The human (or another agent)
   reviews the plan. The critical question is: does the plan reveal
   deficiencies in the spec?
   - If yes → fix the spec (return to step 3), discard the plan.
   - If no → approve the plan.

7. **Execute** — The agent executes the approved plan. The prompt
   to execute should be minimal. If the prompt needs to explain the
   work, the spec is deficient.

8. **Validate results** — Run every verification check listed in the
   spec. Every check is mandatory. Do not skip any. Verification is
   not a suggestion.

**Key principle:** The spec loop is where you spend your cognitive
budget. The execution loop should be boring. If execution is
surprising, the spec has holes.

---

#### Section: Spec Structure

Every spec should follow this structure. Sections marked (required)
must be present. Sections marked (recommended) should be included
unless there is a good reason to omit them.

1. **Title and Purpose** (required) — One sentence stating what the
   spec achieves. Not how — what.

2. **Prerequisites** (required) — Skills, specs, or context that
   must be loaded before execution. Always include:
   `get_skill("<skill-name>")` for the relevant skill.

3. **Context** (recommended) — Why this work exists. What problem
   it solves. What the current state is. This section helps agents
   make good judgement calls when the spec is ambiguous.

4. **Single Source of Truth** (required if applicable) — If the spec
   introduces or modifies data that could exist in multiple places,
   explicitly state which file is canonical. Never defer unification
   to a future spec — if you know two sources of truth is wrong,
   fix it now.

5. **Changes** (required) — Numbered steps describing what must
   change. Each step should be:
   - Specific enough that an agent can execute it without asking
     questions.
   - Ordered logically (dependencies before dependents).
   - Explicit about file paths, function names, and expected
     behaviour.

6. **Out of Scope** (required) — What this spec deliberately does
   not cover. This is as important as what it does cover. Without
   this section, agents will gold-plate.

7. **Verification** (required) — An explicit, enumerated checklist
   of mandatory checks. Include both positive tests (thing works)
   and negative tests (thing fails gracefully). Every check is
   mandatory — state this explicitly. Plans that reduce verification
   to "check it works" are failing the spec.

8. **Branch** (required) — The expected branch name for the work.
   Agents may deviate due to environment constraints; this should
   be documented in provenance.

---

#### Section: Principles

These principles were discovered through practical application of
SDD. They are not theoretical — each one was learned by hitting the
problem it prevents.

**The spec is cheap, execution is expensive.**
Rewriting a spec and discarding a plan feels like rework. It is
iteration. The spec is a few hundred words. Execution is files,
tests, commits, reviews. Invest the time in the spec.

**If your prompt needs to explain the work, your spec is deficient.**
The execution prompt should be minimal: `Execute spec <n>`. If
you're adding context, caveats, or instructions to the prompt,
that's signal your spec has holes. Fix the spec, not the prompt.

**Always execute in plan mode first.**
The plan phase validates the spec against the current state of the
repository. Catch problems in the spec, not during execution.

**When the plan reveals a spec bug, fix the spec — not the plan.**
Do not patch the plan. Do not add a note. Go back to the spec,
fix the deficiency, commit the updated spec, and regenerate the
plan from scratch. The plan is disposable. The spec is the artifact.

**Don't burn cognitive budget on error recovery.**
If the agent encounters issues during execution, the solution is
to debug and improve the specification, not to manually fix outputs.

**The bug is always in the spec.**
When execution produces wrong results, the first place to look is
the spec. Ambiguity, missing requirements, and implicit assumptions
are spec bugs, not agent bugs.

**State conventions explicitly.**
Never assume an agent knows a convention. If provenance files should
be overwritten not appended, say so. If tools must return error
strings not raise exceptions, say so. Implicit conventions become
inconsistent execution.

**Single source of truth — always.**
If a value, definition, or convention exists in more than one place,
one of them is wrong (or will be soon). Designate the canonical
source and make everything else reference it. Never defer
unification.

**Out of scope prevents gold-plating.**
Without explicit boundaries, agents will expand scope. They will
update documentation you didn't ask for, refactor code that wasn't
in the spec, and add features that seemed related. State what the
spec does NOT cover.

**Mandatory means mandatory.**
Verification checks are not suggestions. Write "Every check below
is mandatory. Do not skip any." in the spec. Plans that summarise
verification as "check it works" are not following the spec.

**Provenance is a side effect, not extra work.**
Provenance files are generated as part of spec execution. They
document what happened, what decisions were made, and what deviated
from the spec. They cost almost nothing to produce and become
invaluable as audit trails and content source material. The best
documentation is a side effect of the process, not an additional
task.

---

#### Section: Memory Bank vs Specs

The project has two layers of context (following Böckeler's
taxonomy):

**Memory bank** — Project-wide context that applies to all work.
In this project: `AGENTS.md`, skills (`.skillmcp/`), and brand
guidelines (`.brandmcp/`). These are referenced by specs but never
duplicated into them.

**Specs** — Task-specific documents that describe a discrete unit
of work. They live in `.specmcp/specs/` organised by category.
Specs reference the memory bank (e.g., "load the mcp-builder skill")
but do not reproduce its content.

The skill should instruct: if you find yourself copying content from
AGENTS.md or a skill into a spec, you're doing it wrong. Reference
it. The spec should say "follow the conventions in the mcp-builder
skill" not restate those conventions.

---

#### Section: Anti-Patterns

**The novel spec.** A spec that reads like a design document —
pages of context, rationale, and discussion with the actual
requirements buried in prose. Specs are instructions, not essays.

**The implicit spec.** A spec that assumes the agent knows things
it hasn't been told. "Follow our usual conventions" is not a
requirement. "Filter `.provenance.md` files in discovery and
loading functions" is.

**The mega-spec.** A spec that tries to do too much. If a spec has
more than ~10 changes, it probably wants to be two specs. Keep
specs atomic enough that a single plan can cover them.

**The unverifiable spec.** A spec with no verification section, or
with vague checks like "ensure it works." If you can't write a
concrete check, you don't know what success looks like.

**The deferred debt spec.** A spec that knowingly creates a problem
and adds "future spec" to fix it. If you know it's wrong now,
fix it now. The spec is cheap.

**The prompt-dependent spec.** A spec that only works if the
execution prompt adds extra context. The spec must be
self-sufficient. Test this by imagining a fresh agent session
with no prior conversation — can the agent execute from the spec
alone?

---

#### Section: Spec Iteration Checklist

Before committing a spec to main, review against this checklist:

- [ ] Purpose is one sentence stating what, not how
- [ ] Prerequisites list all skills and specs to load
- [ ] Every concrete value has a single source of truth
- [ ] Changes are numbered and ordered by dependency
- [ ] Each change is specific enough to execute without questions
- [ ] File paths are explicit, not implied
- [ ] Out of scope is defined
- [ ] Verification has enumerated, mandatory checks
- [ ] Verification includes at least one negative test
- [ ] Conventions are stated, not assumed
- [ ] Provenance location and convention are specified
- [ ] Branch name is specified
- [ ] The spec is self-sufficient (no prompt context needed)

---

### 5. Verify

Every check below is mandatory. Do not skip any.

- [ ] `.skillmcp/skills/mcp-builder/SKILL.md` no longer exists
- [ ] `.skillmcp/skills/mcp-builder/mcp-builder.md` exists with identical content
- [ ] `AGENTS.md` contains no references to `get_skill("SKILL")`
- [ ] No file in the repo references `get_skill("SKILL")`
- [ ] `get_skill("mcp-builder")` returns the mcp-builder skill content
- [ ] `.skillmcp/skills/author-spec/author-spec.md` exists
- [ ] `list_skills` returns both mcp-builder and author-spec
- [ ] `get_skill("author-spec")` returns the author-spec skill content
- [ ] `get_skill("nonexistent")` returns an error string, does not raise
- [ ] Content covers all seven sections specified above
- [ ] No section duplicates content from the mcp-builder skill
- [ ] `pre-commit run --all-files` passes

### 6. Write provenance

Create the provenance file for this execution at:

```
.specmcp/specs/provenance/methodology/author-spec-skill.provenance.md
```

Overwrite (do not append).

## Out of Scope

- Changes to `.specmcp` or `.brandmcp` servers
- Changes to `.skillmcp/server.py` (load_skill already matches on stem)
- Spec templates or generators (future work)
- Tooling to automate the workflow (future work)
- Updating existing specs to use new `get_skill("mcp-builder")` syntax
  (they reference the skill at execution time; the rename handles it)

## Branch

```
spec/author-spec-skill/initial
```
