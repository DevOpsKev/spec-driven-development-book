# Book Brief: Specification Driven Development

This document defines the book's scope, thesis, audience, and boundaries. Reference it to ensure all content stays aligned with the book's purpose.

---

## Core Thesis

**"The specification is the artifact. Code is a side effect."**

Specification Driven Development (SDD) inverts traditional software development when working with AI coding agents:

- Traditional: think → code → document
- SDD: specify → generate → validate

The specification is the primary work product. Generated code is a derived output that can be regenerated, revised, or discarded.

**The unresolved debate:** There are competing views on how far this inversion goes:

| View | Position |
|------|----------|
| Radical | Spec is the sole source of truth. Code is a byproduct—an intermediate artifact between requirements and execution. |
| Traditional | Specs drive generation, but executable code remains the source of truth that must be maintained. |

This book does not require you to adopt either position fully. Both views benefit from the same practices: well-crafted specifications, systematic validation, and disciplined workflows.

---

## What This Book Teaches

The book teaches a methodology for working with AI coding agents effectively. After reading, the audience will be able to:

1. Write specifications that produce consistent, high-quality agent output
2. Structure projects so agents can work within bounded contexts
3. Apply context engineering to curate information for agents at scale
4. Validate and iterate on generated code systematically
5. Detect and prevent architectural drift between specs and implementation
6. Integrate SDD into existing workflows, version control, and CI/CD pipelines
7. Use deterministic CI/CD practices to safeguard against non-deterministic generation
8. Govern specification evolution without breaking systems
9. Identify when SDD is appropriate and when it is not

---

## Target Audience

**Primary:** Professional software developers already using AI coding tools.

Assume the reader:

- Has 3+ years of development experience
- Has used AI coding tools (Cursor, Copilot, Claude, etc.)
- Can evaluate generated code critically
- Is frustrated by inconsistent results from ad-hoc prompting
- Wants a repeatable system, not tips and tricks
- Is skeptical of AI hype

**Secondary:** Tech leads and engineering managers evaluating how AI agents affect team workflows.

---

## Audience Mental State

The reader arrives with these experiences:

- Vague prompts producing mediocre code
- Over-detailed prompts still producing wrong code
- Context getting lost across sessions
- Occasional successes they cannot replicate
- Suspicion that there's a better way

Meet this by: validating their frustrations, then providing the systematic approach they're looking for.

---

## Scope Boundaries

**This book is:**

- A methodology for specification-first development with AI agents
- An architectural pattern that repositions specification as the system's primary executable artifact
- Grounded in current practice, not speculation
- Tool-agnostic—principles transfer across agents
- Practical—every concept includes actionable application
- Connected to existing practices (BDD, TDD, contract-first development) while addressing new challenges

**This book is not:**

- A prompt engineering guide (prompts are one small component)
- A tutorial for specific tools (tools are examples, not the subject)
- A prediction about AI's future
- An argument for replacing developers with AI
- A return to waterfall (SDD provides shorter feedback loops, not longer ones)

---

## Content Boundaries

**Include:**

- Frameworks and mental models for SDD (including the five-layer model)
- Concrete specification formats and templates
- Real workflow examples
- Context engineering practices for agent-scale information curation
- Failure modes, drift detection, and how to address them
- Integration with existing development practices (git, code review, testing)
- CI/CD practices that safeguard against non-deterministic generation
- Lessons from BDD that transfer to SDD (ubiquitous language, spec-by-example)
- Governance, evolution, and compatibility strategies

**Exclude:**

- AI/ML theory or how language models work
- Comparisons or reviews of specific tools
- Speculation about future AI capabilities
- Arguments about AI ethics or job displacement
- Content that requires specific tool versions or features

---

## Positioning

**SDD is not:**

- "Prompt engineering" — prompts are tactical; SDD is strategic
- "Vibe coding" — SDD is structured and intentional; vibe coding is too fast, spontaneous, haphazard
- "No-code/low-code" — SDD assumes professional developers writing real software
- "Waterfall" — Waterfall fails due to long feedback cycles and disconnect between design and implementation; SDD provides shorter, effective feedback loops with human-in-the-loop governance

**SDD is:**

- A professional methodology for a new category of tooling
- An architectural pattern that makes specifications executable and enforceable
- Complementary to existing software engineering practices (BDD, TDD, contract-first)
- A response to the ad-hoc experimentation most developers are currently doing
- Part of the fifth generation of programming abstraction (natural language as interface)

---

## Tone Calibration

| Attribute | Setting |
|-----------|---------|
| Confidence | High—you are defining this practice |
| Formality | Professional but not academic |
| Enthusiasm | Low—grounded, not hypey |
| Humor | Minimal—dry observations only, no jokes |
| Directness | High—state claims plainly |
| Hedging | Avoid unless genuinely uncertain |

---

## Key Concepts to Establish

These concepts are central to SDD. Define them clearly and use them consistently:

| Concept | Brief Definition |
|---------|------------------|
| Specification | A structured document defining what to build, serving as input for an AI coding agent and criteria for validating output |
| Spec-first workflow | Writing the specification before engaging the agent, not iterating through conversation |
| Architectural inversion | The shift from code-as-truth to specification-as-truth; implementations derived from specs, not vice versa |
| Ambient code | Generated code that is regenerable, disposable, and continuously reconcilable—not the primary artifact |
| Five-layer model | Specification → Generation → Artifact → Validation → Runtime; the closed control loop of SDD |
| Bounded context | A scoped portion of a project small enough for an agent to hold in working memory |
| Context engineering | Curating and managing contextual information for AI agents at scale (distinct from prompt engineering) |
| Generation | The code output produced by an agent from a specification |
| Validation | Systematic verification that generated code meets the specification |
| Drift detection | Identifying divergence between declared spec intent and observed system behavior |
| Iteration | Refining the specification (not the prompt) to improve output |
| SpecOps | Treating specifications with operational rigor: version control, review, branching, CI/CD integration |
| Deterministic validation | Using CI/CD practices to safeguard against non-deterministic generation |
| Human-in-the-loop | Preserving human authority over intent, policy, and meaning while delegating enforcement to machines |
| Bounded autonomy | Explicit approval boundaries for breaking changes; machines act within human-defined constraints |
| Governed evolution | Systematic approach to evolving specifications without breaking compatibility |
| Generator trust | Treating AI generators as critical infrastructure requiring determinism, reproducibility, and auditability |
| Schema engineering | The discipline of designing and maintaining specifications as long-lived executable infrastructure |

---

## What Success Looks Like

A reader who has absorbed this book:

- Writes specs before opening an AI tool
- Structures projects into agent-sized bounded contexts
- Applies context engineering to curate information effectively
- Evaluates generated code against spec criteria, not gut feel
- Refines specs when output is wrong, rather than tweaking prompts
- Detects and prevents drift between specs and implementation
- Maintains specs as living documentation alongside code
- Uses CI/CD pipelines to validate non-deterministic generation
- Knows when to use SDD and when simpler approaches suffice
- Understands where human judgment is essential and where machines can be trusted
- Can evolve specifications without breaking dependent systems

---

## Open Questions

These decisions are not yet resolved. Flag if content depends on them:

- Depth of coverage for failure modes and anti-patterns
- Inclusion and length of case studies
- Extent of tooling setup guidance vs. pure methodology
- Whether a companion repository with example specs exists
- Final book title
- Position on the "source of truth" debate (or remain neutral)

---

## Key Sources

These articles inform the book's framing and should be referenced for foundational concepts:

- **InfoQ:** "Spec Driven Development: When Architecture Becomes Executable" (Griffin & Carroll, Jan 2026) — five-layer model, architectural inversion, SpecOps, drift detection, governed evolution
- **Thoughtworks:** "Spec-driven development: Unpacking one of 2025's key new AI-assisted engineering practices" (Liu Shangqi, Dec 2025) — context engineering, BDD lessons, CI/CD integration, "not waterfall" argument

---

## Reference

For voice, formatting, and editorial rules, see `writers-guide.md`.
For chapter structure, see `chapter-outline.md`.