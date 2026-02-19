---
name: author-spec
description: >
  Write effective specifications for Specification Driven Development (SDD)
  workflows. Use when creating new specs, iterating on draft specs, or
  reviewing specs before execution. Covers the full lifecycle: brief,
  draft, iterate, commit, plan, validate, execute, verify.
---

# Author Spec Skill

Write specifications that AI agents can execute reliably. This skill
captures the meta-practice of spec authoring — not what to build, but
how to describe what to build so that an agent produces correct results
on the first pass.

This skill is distinct from the mcp-builder skill (which teaches how to
build MCP servers). The mcp-builder skill is a *domain* skill. This skill
teaches you how to write the specs that invoke domain skills.

## SDD Level

This skill targets **spec-as-source** — the highest level of Specification
Driven Development. In this model:

- Specs are the primary artifact. Code is a generated side effect.
- Humans author and iterate specs. Humans never edit generated code.
- Specs are living documents that evolve with the system.
- The spec is kept after execution and remains the source of truth for
  future evolution and maintenance.

Spec-as-source is distinct from two lower levels:

- **Spec-first** — write a spec, use it to guide generation, then discard
  the spec. The code becomes the artifact. This is better than no spec,
  but the spec's value is lost after the first pass.
- **Spec-anchored** — keep the spec alongside the code, but humans also
  edit generated code directly. The spec drifts from reality because two
  sources of truth exist.

In spec-as-source, the specification is the only thing the human maintains.
When the system needs to change, you change the spec and regenerate. The
spec is always accurate because it is always authoritative.

Reference: Birgitta Boeckeler's taxonomy of SDD levels (Fowler, "Exploring
Gen AI" series, October 2025).

## The Workflow

The SDD workflow has eight steps across two loops. The spec loop
(steps 1-4) is where the creative work happens. The execution loop
(steps 5-8) is mechanical.

### The Spec Loop

1. **Brief** — The human captures intent as bullet points, rough
   requirements, or a problem statement. The brief is the spec for the
   spec. It is fast, loose, and incomplete by design.

2. **Spec draft** — An agent expands the brief into a full specification
   following the structure defined in this skill. The agent should ask
   clarifying questions if the brief has gaps.

3. **Iterate spec** — The human reviews the draft. This is where the real
   intellectual work happens. Look for: missing requirements, implicit
   assumptions, unstated conventions, verification gaps, scope creep, and
   single-source-of-truth violations.

4. **Commit spec to main** — The spec is the artifact. Committing it to
   main marks it as approved and ready for execution.

### The Execution Loop

5. **Plan** — An agent reads the committed spec and produces an execution
   plan. The plan must be generated in plan mode only — no files created,
   no changes made.

6. **Validate plan against spec** — The human (or another agent) reviews
   the plan. The critical question is: does the plan reveal deficiencies
   in the spec?
   - If yes: fix the spec (return to step 3), discard the plan.
   - If no: approve the plan.

7. **Execute** — The agent executes the approved plan. The prompt to
   execute should be minimal. If the prompt needs to explain the work,
   the spec is deficient.

8. **Validate results** — Run every verification check listed in the spec.
   Every check is mandatory. Do not skip any. Verification is not a
   suggestion.

**Key principle:** The spec loop is where you spend your cognitive budget.
The execution loop should be boring. If execution is surprising, the spec
has holes.

## Spec Structure

Every spec should follow this structure. Sections marked (required) must
be present. Sections marked (recommended) should be included unless there
is a good reason to omit them.

1. **Title and Purpose** (required) — One sentence stating what the spec
   achieves. Not how — what.

2. **Prerequisites** (required) — Skills, specs, or context that must be
   loaded before execution. Always include `get_skill("<skill-name>")` for
   the relevant skill.

3. **Context** (recommended) — Why this work exists. What problem it
   solves. What the current state is. This section helps agents make good
   judgement calls when the spec is ambiguous.

4. **Single Source of Truth** (required if applicable) — If the spec
   introduces or modifies data that could exist in multiple places,
   explicitly state which file is canonical. Never defer unification to a
   future spec — if you know two sources of truth is wrong, fix it now.

5. **Changes** (required) — Numbered steps describing what must change.
   Each step should be:
   - Specific enough that an agent can execute it without asking questions.
   - Ordered logically (dependencies before dependents).
   - Explicit about file paths, function names, and expected behaviour.

6. **Out of Scope** (required) — What this spec deliberately does not
   cover. This is as important as what it does cover. Without this
   section, agents will gold-plate.

7. **Verification** (required) — An explicit, enumerated checklist of
   mandatory checks. Include both positive tests (thing works) and
   negative tests (thing fails gracefully). Every check is mandatory —
   state this explicitly. Plans that reduce verification to "check it
   works" are failing the spec.

8. **Branch** (required) — The expected branch name for the work. Agents
   may deviate due to environment constraints; this should be documented
   in provenance.

## Principles

These principles were discovered through practical application of SDD.
They are not theoretical — each one was learned by hitting the problem
it prevents.

**The spec is cheap, execution is expensive.** Rewriting a spec and
discarding a plan feels like rework. It is iteration. The spec is a few
hundred words. Execution is files, tests, commits, reviews. Invest the
time in the spec.

**If your prompt needs to explain the work, your spec is deficient.** The
execution prompt should be minimal: "Execute spec X." If you are adding
context, caveats, or instructions to the prompt, that is signal your spec
has holes. Fix the spec, not the prompt.

**Always execute in plan mode first.** The plan phase validates the spec
against the current state of the repository. Catch problems in the spec,
not during execution.

**When the plan reveals a spec bug, fix the spec — not the plan.** Do not
patch the plan. Do not add a note. Go back to the spec, fix the
deficiency, commit the updated spec, and regenerate the plan from scratch.
The plan is disposable. The spec is the artifact.

**Don't burn cognitive budget on error recovery.** If the agent encounters
issues during execution, the solution is to debug and improve the
specification, not to manually fix outputs.

**The bug is always in the spec.** When execution produces wrong results,
the first place to look is the spec. Ambiguity, missing requirements, and
implicit assumptions are spec bugs, not agent bugs.

**State conventions explicitly.** Never assume an agent knows a convention.
If provenance files should be overwritten not appended, say so. If tools
must return error strings not raise exceptions, say so. Implicit
conventions become inconsistent execution.

**Single source of truth — always.** If a value, definition, or convention
exists in more than one place, one of them is wrong (or will be soon).
Designate the canonical source and make everything else reference it.
Never defer unification.

**Out of scope prevents gold-plating.** Without explicit boundaries,
agents will expand scope. They will update documentation you did not ask
for, refactor code that was not in the spec, and add features that seemed
related. State what the spec does NOT cover.

**Mandatory means mandatory.** Verification checks are not suggestions.
Write "Every check below is mandatory. Do not skip any." in the spec.
Plans that summarise verification as "check it works" are not following
the spec.

**Provenance is a side effect, not extra work.** Provenance files are
generated as part of spec execution. They document what happened, what
decisions were made, and what deviated from the spec. They cost almost
nothing to produce and become invaluable as audit trails and content
source material. The best documentation is a side effect of the process,
not an additional task.

## Memory Bank vs Specs

The project has two layers of context:

**Memory bank** — Project-wide context that applies to all work. In this
project: `AGENTS.md`, skills (`.skillmcp/`), and brand guidelines
(`.brandmcp/`). These are referenced by specs but never duplicated into
them.

**Specs** — Task-specific documents that describe a discrete unit of work.
They live in `.specmcp/specs/` organised by category. Specs reference the
memory bank (e.g., "load the mcp-builder skill") but do not reproduce its
content.

If you find yourself copying content from `AGENTS.md` or a skill into a
spec, you are doing it wrong. Reference it. The spec should say "follow
the conventions in the mcp-builder skill" not restate those conventions.

This separation follows Boeckeler's taxonomy of context layers: memory
bank provides ambient knowledge; specs provide task-specific instructions.

## Anti-Patterns

**The novel spec.** A spec that reads like a design document — pages of
context, rationale, and discussion with the actual requirements buried in
prose. Specs are instructions, not essays.

**The implicit spec.** A spec that assumes the agent knows things it has
not been told. "Follow our usual conventions" is not a requirement.
"Filter `.provenance.md` files in discovery and loading functions" is.

**The mega-spec.** A spec that tries to do too much. If a spec has more
than approximately ten changes, it probably wants to be two specs. Keep
specs atomic enough that a single plan can cover them.

**The unverifiable spec.** A spec with no verification section, or with
vague checks like "ensure it works." If you cannot write a concrete check,
you do not know what success looks like.

**The deferred debt spec.** A spec that knowingly creates a problem and
adds "future spec" to fix it. If you know it is wrong now, fix it now.
The spec is cheap.

**The prompt-dependent spec.** A spec that only works if the execution
prompt adds extra context. The spec must be self-sufficient. Test this by
imagining a fresh agent session with no prior conversation — can the agent
execute from the spec alone?

## Spec Iteration Checklist

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
