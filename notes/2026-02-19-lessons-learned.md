# 2026-02-19 — Lessons Learned

Session covering specmcp refactor, skillmcp build and refactor, brandmcp
build, audiobook cover proof-of-concept, and author-spec skill creation.
Three MCP servers built, one skill created, one skill spec authored, five
external SDD sources reviewed, and a methodology codified.

## The Workflow Discovery

The biggest outcome of the day was making the SDD workflow explicit. We'd
been doing it all session without naming it. Once named, it became
teachable.

**Two loops, eight steps:**

The Spec Loop (creative work — this is where you spend cognitive budget):

1. Brief — human intent as bullet points, rough shape
2. Spec draft — agent expands brief into a full specification
3. Iterate spec — review, refine, catch gaps
4. Commit spec to main — the spec is the artifact

The Execution Loop (mechanical — should be boring):

5. Plan — agent reads spec, produces execution plan
6. Validate plan against spec — does the plan reveal spec bugs?
7. Execute — the prompt should be minimal
8. Validate results — mandatory checks from the spec

The critical decision gate is step 6. If the plan reveals a spec
deficiency: fix the spec (return to step 3), discard the plan. Do not
patch the plan. The plan is disposable. The spec is the artifact.

We hit this gate three times today — each time, the correct move was to
update the spec, bin the plan, and regenerate.

## Principles Discovered

Every one of these was learned by hitting the problem it prevents.

**The spec is cheap, execution is expensive.**
Rewriting a spec and discarding a plan feels like rework. It is
iteration. The spec is a few hundred words. Execution is files, tests,
commits, reviews. We rewrote the brandmcp spec twice before execution.
Each rewrite was minutes. Execution would have been hours of rework if
done wrong.

**If your prompt needs to explain the work, your spec is deficient.**
The execution prompt should be: `Execute spec <name>`. If you're adding
context, caveats, or instructions, your spec has holes. Fix the spec,
not the prompt.

**Always execute in plan mode first.**
The plan phase validates the spec against the current state of the repo.
Catch problems in the spec, not during execution. The specmcp agent
skipped plan approval and went straight to execution — "the
implementation was done during the planning phase since the plan was
approved implicitly." That's a spec bug, not an agent bug. We added
explicit plan approval to the workflow.

**When the plan reveals a spec bug, fix the spec — not the plan.**
The SKILL.md naming collision was caught at plan time. The plan correctly
identified that `get_skill("SKILL")` would be ambiguous with two skills.
The fix was in the spec (rename files to `<skill-name>.md`), not in the
plan.

**Don't burn cognitive budget on error recovery.**
If the agent encounters issues during execution, the solution is to
debug and improve the specification, not manually fix outputs.

**The bug is always in the spec.**
When execution produces wrong results, look at the spec first. Ambiguity,
missing requirements, and implicit assumptions are spec bugs, not agent
bugs.

**State conventions explicitly.**
Never assume an agent knows a convention. The skillmcp refactor found
missing provenance file filtering — a convention that existed in specmcp
but wasn't stated in any skill or spec. If provenance files should be
overwritten not appended, say so. If tools must return error strings not
raise exceptions, say so.

**Single source of truth — always. Never defer unification.**
The brandmcp spec initially had design tokens defined both in a JSON
file and hardcoded in markdown. Plan review caught this. We unified to
`tokens.json` as the single canonical source before execution — didn't
defer to a "future spec." If you know two sources of truth is wrong, fix
it now.

**Out of scope prevents gold-plating.**
Without explicit boundaries, agents expand scope. They update
documentation you didn't ask for, refactor code that wasn't in the spec,
and add features that seemed related. Every spec needs an explicit "Out
of Scope" section.

**Mandatory means mandatory.**
The brandmcp plan reduced the spec's 14 verification checks to "ruff,
format, pre-commit, server starts." That's the plan failing the spec.
Write: "Every check below is mandatory. Do not skip any." Include
positive and negative tests.

**Provenance is a side effect, not extra work.**
Provenance files are generated as part of spec execution. They cost
almost nothing and become invaluable as audit trails, case studies, and
primary source material for the book. The best documentation is a side
effect of the process, not an additional task.

**The brief is the spec for the spec.**
New layer discovered: brief → spec → plan → execution. The brief
captures human intent as bullet points. The spec is the precise,
complete document an agent can execute without further context. This
distinction matters because the brief is where you think, the spec is
where you hand off.

## New IP Created This Session

We reviewed five external SDD sources before authoring the skill:

- Birgitta Böckeler (Fowler) — SDD levels taxonomy, Oct 2025
- InfoQ — architecture as executable, drift detection, Jan 2026
- Microsoft — spec-kit, constitution concept, Sep 2025
- GitHub spec-kit — Specify → Plan → Tasks workflow
- Thoughtworks — SDD as fifth-generation abstraction

**What none of them cover that we developed today:**

**Brief-to-spec expansion as a first-class step.** None of the reviewed
tools explicitly model the human intent capture step. Kiro goes straight
to "Requirements." Spec-kit starts at "Specify." Nobody treats the
brief — the messy, incomplete, bullet-point version of intent — as a
distinct, valuable phase that precedes the spec.

**Spec iteration as the primary creative act.** Spec-kit treats specs as
something you write once and execute. We proved that spec revision *is*
the work. Rewriting the brandmcp spec twice before execution wasn't
rework — it was the creative process. The execution was mechanical.

**The two-loop workflow with a decision gate.** No tool models the
explicit separation between the spec loop (creative) and the execution
loop (mechanical), with the plan-as-spec-validator decision gate at step
6. Kiro has Requirements → Design → Tasks. Spec-kit has Specify → Plan
→ Tasks. Neither has the explicit "does the plan reveal a spec bug?"
gate that sends you back to the spec.

**Provenance as reusable content pipeline.** Nobody else is capturing
execution records as primary source material. The provenance files are
not just audit trails — they're case studies, chapter content, and
masterclass training material. Every spec execution generates a
provenance record documenting how the book was built using SDD. The book
teaches SDD. The provenance files prove SDD works. The masterclass
teaches people how to do SDD using the same artifacts. Turtles all the
way down.

**Git history as narrative arc.** Because provenance files are
overwritten (not appended), `git log --follow <file>.provenance.md`
gives the full evolution — spec changes, execution changes, what broke,
what got fixed. A narrative arc built into version control. Not designed,
discovered.

## Bugs Caught by the Workflow

**Missing `validate_brand` tool.**
The original brandmcp spec had three tools. During plan review, we
realised there was no validation tool — the server could serve brand
data but couldn't check content against it. Spec updated, plan binned,
re-executed.

**Shallow verification in plans.**
The brandmcp plan reduced 14 mandatory checks to "ruff, format,
pre-commit, starts." The spec was reinforced with explicit language:
"Every check below is mandatory. Do not skip any."

**Two sources of truth for design tokens.**
The brandmcp spec initially had design values in both `tokens.json` and
hardcoded in markdown files. Plan review caught the duplication. Spec
updated: `tokens.json` is canonical, markdown provides narrative context
only.

**SKILL.md naming collision.**
The author-spec plan revealed that all skills sharing the filename
`SKILL.md` would collide in `load_skill()`, which matches on file stem.
`get_skill("SKILL")` would return the alphabetically-first match —
`author-spec`, not `mcp-builder`. Fix: each skill file named after the
skill itself (`mcp-builder.md`, `author-spec.md`). Spec updated to
include the rename.

**Agent skipping plan approval.**
The specmcp refactor agent executed during the planning phase, treating
"no objection" as "go ahead." This was a spec bug — AGENTS.md didn't
explicitly require plan approval before execution. Added: "Do not
execute until the plan is explicitly approved by the author."

**Missing provenance file filtering in skillmcp.**
The skillmcp server didn't filter `.provenance.md` files from discovery
or loading — a convention that existed in specmcp but wasn't applied
when skillmcp was built before the mcp-builder skill existed. The skill
now documents this convention explicitly.

## The Ouroboros

The recursive self-reference continued all session:

- Used SDD to write the first spec for a spec about SDD
- Used a skill to build the skill server that serves skills
- The mcp-builder skill lives inside the server it describes how to build
- Used a spec to create a skill about writing specs
- The book about SDD is built using SDD
- The provenance files generated by SDD become book content about SDD
- A future masterclass will teach SDD using the provenance, specs, and
  skills generated while building the book that describes SDD

"It's turtles all the way down."

## Proof Runs

**Brand server as proof of concept.** An agent with no prior knowledge
of the book's visual identity called three tools (`get_design_tokens`,
`get_brand("palette")`, `get_brand("typography")`), got structured data
back, and produced a brand-compliant audiobook cover on the first
attempt. No iterations, no corrections, no "actually the red is
#e63926." Every colour, font, and proportion sourced from `tokens.json`.

This validates the full chain:
- specmcp — specs drive the work
- skillmcp — skills teach agents how to build
- brandmcp — brand data is queryable and consumable

## Spec Categories Established

- `devops/` — infrastructure specs (specmcp, skillmcp, brandmcp)
- `editorial/` — book content specs
- `methodology/` — process and practice specs (author-spec)

The author-spec was initially placed in `devops/`. Corrected to
`methodology/` — it's a process spec, not an infrastructure spec.

## Anti-Patterns Identified

**The novel spec.** Reads like a design document — pages of context and
rationale with requirements buried in prose. Specs are instructions, not
essays.

**The implicit spec.** Assumes the agent knows things it hasn't been
told. "Follow our usual conventions" is not a requirement.

**The mega-spec.** Tries to do too much. If a spec has more than ~10
changes, it probably wants to be two specs.

**The unverifiable spec.** No verification section, or vague checks like
"ensure it works." If you can't write a concrete check, you don't know
what success looks like.

**The deferred debt spec.** Knowingly creates a problem and adds "future
spec" to fix it. If you know it's wrong now, fix it now.

**The prompt-dependent spec.** Only works if the execution prompt adds
extra context. Test: can a fresh agent with no prior conversation
execute from the spec alone?

## External Sources — Key Takeaways

**Böckeler's taxonomy (Fowler, Oct 2025):**
Three SDD levels: spec-first (write, use, discard), spec-anchored (keep
as living doc), spec-as-source (humans only edit specs, never code). Our
project is spec-as-source. Useful framing to position the book.

**Böckeler's spec vs memory bank distinction:**
Memory bank = project-wide context (AGENTS.md, skills, brand). Specs =
task-specific documents. Don't duplicate — reference.

**Böckeler's verification critique:**
"Your role isn't just to steer. It's to verify." Specs must have
explicit, enumerated checks. Maps directly to our "mandatory means
mandatory" principle.

**InfoQ — architecture as executable:**
SDD as "fifth-generation abstraction." Drift detection — the spec
remains the source of truth, the system detects when code has drifted.
Our `validate_brand` and `validate_content` are exactly this.

**Microsoft/spec-kit — the constitution concept:**
Immutable project-wide principles separate from individual specs. Our
AGENTS.md + skills serve this role. Specs reference but don't duplicate
constitutional knowledge.

**Spec-kit — workflow phases:**
Specify → Plan → Tasks, with checklists as "definition of done" for
each phase. Maps to our Brief → Spec → Plan → Execute → Validate.

## Files Created This Session

**MCP Servers:**
- `.brandmcp/server.py` (4 tools: list_brand, get_brand,
  get_design_tokens, validate_brand)
- `.brandmcp/brand/tokens.json` (canonical design token source)
- `.brandmcp/brand/palette.md`, `typography.md`, `layout.md`, `voice.md`

**Skills:**
- `.skillmcp/skills/mcp-builder/SKILL.md` (created, later marked for
  rename to `mcp-builder.md`)

**Specs:**
- `.specmcp/specs/devops/brandmcp-build.md`
- `.specmcp/specs/methodology/author-spec-skill.md`

**Provenance:**
- `.specmcp/specs/provenance/devops/specmcp-refactor.provenance.md`
- `.specmcp/specs/provenance/devops/skillmcp-refactor.provenance.md`
- `.specmcp/specs/provenance/devops/brandmcp-build.provenance.md`

**Other:**
- `audiobook-cover-preview.svg` / `.png` (brand server proof of concept)
- `AGENTS.md` (updated with all three MCP servers)

## Quotes Worth Keeping

"The best documentation is a side effect of the process, not an
additional task."

"If your prompt needs to explain the work, your spec is deficient."

"The spec is cheap, execution is expensive."

"When the plan reveals a spec bug, fix the spec — not the plan."

"`git log --follow` on overwritten provenance files gives the full
evolution — spec changes, execution changes, what broke, what got fixed.
A narrative arc built into version control."

"The agent skipped plan approval and went straight to execution. That's
a spec bug, not an agent bug."

"It's turtles all the way down."

## What's Next

1. Execute author-spec skill (spec updated with SKILL.md rename fix,
   plan stale — needs fresh session and new plan)
2. Merge all PRs (specmcp, skillmcp, brandmcp)
3. Continue book chapters (the book supports the job search, the job
   search does not wait for the book)
4. Future: create SDD masterclass from provenance files, specs, and
   skills — after a few chapters are down
