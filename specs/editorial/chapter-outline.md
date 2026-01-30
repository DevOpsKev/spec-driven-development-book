# Chapter Outline: Specification Driven Development

This document defines the book's structure. Each chapter builds on previous chapters unless noted otherwise.

---

## Part 1: Foundation

### Chapter 1: The Fifth Generation

**Purpose:** Establish historical context. Position SDD within the evolution of software abstraction.

**Covers:**

- The arc of abstraction: machine code → assembly → high-level languages → frameworks → natural language
- Each generation elevated what developers focus on (mechanism → intent)
- AI coding agents as the catalyst for the fifth generation
- Why this moment is different: tooling is shaping the paradigm, not just supporting it

**Key concept introduced:** Abstraction elevation

**Ends with:** The shift from "how to implement" to "what to specify."

---

### Chapter 2: The Problem with Prompting

**Purpose:** Establish the pain point. Validate the reader's frustrations. Set up why a methodology is needed.

**Covers:**

- The current state: developers using AI agents ad-hoc
- Common failure patterns (vague prompts, over-detailed prompts, context loss, unrepeatable success)
- Why "get better at prompting" is insufficient
- The cost of iteration without structure
- "Vibe coding" and its limits

**Ends with:** The promise of a systematic alternative.

---

### Chapter 3: The Core Insight

**Purpose:** Introduce the central thesis and the architectural inversion.

**Covers:**

- "The specification is the artifact. Code is a side effect."
- The traditional model: code defines truth, architecture is advisory
- The SDD model: specification defines truth, code is derived
- Ambient code: generated artifacts are regenerable, disposable, reconcilable
- The unresolved debate: is spec or code the ultimate source of truth?
  - Radical view: spec is sole truth, code is byproduct
  - Traditional view: specs drive generation, code remains truth to maintain
- Why this inversion changes everything (regardless of which view you hold)

**Key concept introduced:** Specification, Architectural Inversion, Ambient Code

**Ends with:** Overview of what SDD looks like in practice.

---

### Chapter 4: Specifications vs. Prompts

**Purpose:** Clarify the distinction that defines SDD. Prevent conflation with prompt engineering.

**Covers:**

- What a prompt is (tactical, conversational, ephemeral)
- What a specification is (structured, versioned, complete, executable)
- The spectrum from prompt to spec
- When each is appropriate
- Prompts are tactical; specifications are strategic
- Why SDD is not a return to waterfall:
  - Waterfall fails due to long feedback cycles and disconnect between design and implementation
  - Vibe coding fails due to no structure—too fast, spontaneous, haphazard
  - SDD provides shorter, effective feedback loops with human-in-the-loop governance

**Key concept introduced:** Spec-first workflow

**Ends with:** Criteria for recognizing a real specification.

---

### Chapter 5: The Five-Layer Model

**Purpose:** Provide the architectural mental model for SDD systems.

**Covers:**

- The five layers: Specification → Generation → Artifact → Validation → Runtime
- How each layer functions and what it produces
- The closed control loop: intent shapes execution, execution validates intent
- Walkthrough: an example flowing through all five layers

**Key concepts introduced:** Specification Layer, Generation Layer, Artifact Layer, Validation Layer, Runtime Layer

**Ends with:** This model as the reference architecture for the rest of the book.

---

## Part 2: Writing Specifications

### Chapter 6: Anatomy of a Specification

**Purpose:** Define the components of an effective specification.

**Covers:**

- Required elements: context, requirements, constraints, acceptance criteria
- Optional elements: examples, non-goals, references
- Format considerations (structured text, markdown, schema)
- How much detail is enough
- Specifications as executable artifacts, not documentation
- Lessons from BDD that transfer to SDD:
  - Domain-oriented ubiquitous language (business intent, not tech-bound implementation)
  - Clear structure with consistent style (Given/When/Then patterns)
  - Completeness yet conciseness—cover critical paths without enumerating all cases
  - Clarity and determinism to reduce hallucinations
- The continued importance of machine-readable, semi-structured specs

**Ends with:** A template the reader can adapt.

---

### Chapter 7: Defining Context

**Purpose:** Teach how to establish the information environment for the agent.

**Covers:**

- What the agent needs to know vs. what it can infer
- Project context: architecture, conventions, dependencies
- Task context: where this fits, what exists already
- The cost of missing context vs. excessive context

**Key concept introduced:** Bounded context

**Ends with:** Checklist for context completeness.

---

### Chapter 8: Context Engineering

**Purpose:** Teach how to curate and manage context for AI agents at scale.

**Covers:**

- Prompt engineering optimizes human-LLM interaction; context engineering optimizes agent-LLM interaction
- Coding tasks require large amounts of contextual information
- System prompts: Cursor rules, AGENTS.md, and tool configuration
- Spec-by-example as few-shot prompting
- Separating planning from implementation compresses context into specs
- MCP servers and real-time documentation integration
- Extracting structure from legacy codebases (knowledge graphs, vector databases)
- Token budgets and context window management

**Key concept introduced:** Context Engineering

**Ends with:** Context curation checklist.

---

### Chapter 9: Writing Requirements

**Purpose:** Teach how to express what the code should do.

**Covers:**

- Behavioral requirements vs. implementation requirements
- Specificity calibration: when to constrain, when to leave open
- Functional vs. non-functional requirements in specs
- Common requirement failures (ambiguity, contradiction, incompleteness)

**Ends with:** Examples of weak requirements rewritten as strong ones.

---

### Chapter 10: Constraints and Boundaries

**Purpose:** Teach how to bound what the agent should and shouldn't do.

**Covers:**

- Technical constraints (language, framework, patterns to use/avoid)
- Scope constraints (what's in/out of this task)
- Style constraints (naming, structure, conventions)
- Why constraints improve output quality

**Ends with:** Constraint categories checklist.

---

### Chapter 11: Acceptance Criteria

**Purpose:** Teach how to define "done" in a way that enables validation.

**Covers:**

- The role of acceptance criteria in the generate-validate loop
- Writing testable criteria
- Criteria granularity: too loose vs. too tight
- Connecting criteria to validation methods

**Key concept introduced:** Validation (preview)

**Ends with:** Pattern for acceptance criteria that work.

---

## Part 3: The Workflow

### Chapter 12: Project Structure for SDD

**Purpose:** Teach how to organize projects for effective agent collaboration.

**Covers:**

- Breaking work into agent-sized units
- Directory and file organization
- Where specs live in relation to code
- Managing multiple specs across a project

**Key concept introduced:** Bounded context (applied to project structure)

**Ends with:** Example project structure.

---

### Chapter 13: The Generation Cycle

**Purpose:** Walk through the end-to-end process of spec to code.

**Covers:**

- Preparing the spec and context
- Invoking the agent (tool-agnostic framing)
- Receiving and reviewing output
- The judgment moment: accept, iterate, or reject
- Deterministic generation: same spec should yield consistent results

**Key concept introduced:** Generation

**Ends with:** Flowchart of the cycle.

---

### Chapter 14: Validation and Drift Detection

**Purpose:** Teach systematic approaches to evaluating output and preventing architectural drift.

**Covers:**

- Validation against acceptance criteria
- Drift: any divergence between declared intent and observed behavior
- Types of drift: structural, behavioral, semantic, security, evolutionary
- Contract tests, schema validation, payload inspection
- Why drift detection makes architecture self-enforcing
- Without drift detection, SDD collapses into documentation-driven development

**Key concepts introduced:** Validation, Drift Detection

**Ends with:** Decision tree for validation outcomes.

---

### Chapter 15: Iteration as Spec Refinement

**Purpose:** Teach how to improve output by improving the specification, not tweaking prompts.

**Covers:**

- Common output failures and their causes
- When to fix code vs. fix the spec
- Iteration as spec refinement, not prompt adjustment
- The feedback loop: execution validates intent, intent corrects execution

**Key concept introduced:** Iteration (SDD definition)

**Ends with:** Diagnostic process for iteration decisions.

---

### Chapter 16: SpecOps — Treating Specs as Code

**Purpose:** Integrate SDD with standard development practices and operational discipline.

**Covers:**

- Specs as versioned artifacts (same rigor as source code)
- Version control: branching, review, merge strategies
- Co-locating specs with code
- Commit strategies: spec and code together or separately
- Specs in code review
- Regeneration and spec history
- The operational discipline of specification management

**Key concept introduced:** SpecOps (Specification Operations)

**Ends with:** Git workflow recommendations.

---

### Chapter 17: Deterministic CI/CD for Non-Deterministic Generation

**Purpose:** Address how traditional CI/CD practices safeguard against generation unpredictability.

**Covers:**

- The problem: code generation from specs isn't deterministic
- Spec drift and hallucination are inherently difficult to avoid
- CI/CD as the essential counterweight to non-deterministic generation
- Contract testing in pipelines
- Schema validation gates
- Architectural fitness functions
- Automated spec-to-code conformance checks
- When to regenerate vs. when to patch
- Rollback strategies for generated code

**Key concept introduced:** Deterministic Validation

**Ends with:** CI/CD pipeline template for SDD projects.

---

## Part 4: Practice

### Chapter 18: When to Use SDD

**Purpose:** Define appropriate scope. Prevent over-application.

**Covers:**

- Tasks where SDD excels (well-defined, bounded, generatable)
- Tasks where SDD is overkill (trivial changes, exploration)
- Tasks where SDD struggles (highly novel, requires deep context)
- Mixing SDD with other approaches

**Ends with:** Decision framework for choosing SDD.

---

### Chapter 19: Human-in-the-Loop

**Purpose:** Define where human judgment remains essential in an automated architecture.

**Covers:**

- SDD does not remove humans; it relocates human judgment upward
- Humans as custodians of: intent, policy, risk tolerance, ethics, meaning
- What machines own: enforcement, generation, conformance
- Bounded autonomy: explicit approval boundaries for breaking changes
- When to override, when to trust

**Key concept introduced:** Human-in-the-Loop, Bounded Autonomy

**Ends with:** Framework for approval gates and human checkpoints.

---

### Chapter 20: Failure Modes

**Purpose:** Catalog common SDD failures and their remedies.

**Covers:**

- Spec failures: ambiguity, incompleteness, contradiction
- Context failures: too little, too much, wrong scope
- Workflow failures: skipping validation, over-iterating
- Expectation failures: wrong task for SDD
- Generator trust failures: non-determinism, hallucination, drift

**Ends with:** Diagnostic checklist when things go wrong.

---

### Chapter 21: SDD in Teams

**Purpose:** Address multi-person workflows and organizational considerations.

**Covers:**

- Specs as communication artifacts
- Dividing spec-writing and code-validation responsibilities
- Reviewing specs vs. reviewing code
- Schema engineering as a team discipline
- Onboarding team members to SDD

**Key concept introduced:** Schema Engineering

**Ends with:** Team workflow patterns.

---

### Chapter 22: Beyond Code Generation

**Purpose:** Extend SDD principles to adjacent activities.

**Covers:**

- Specs for documentation generation
- Specs for test generation
- Specs for refactoring and migration
- The limits of the methodology

**Ends with:** Framework for applying SDD to new domains.

---

## Part 5: Governance and Evolution

### Chapter 23: Governed Evolution

**Purpose:** Teach how to evolve specifications without breaking systems.

**Covers:**

- Compatibility as an architectural concern (not just versioning)
- Classifying changes: additive, compatible, breaking, ambiguous
- Compatibility policies and enforcement
- Parallel version surfaces
- Controlled deprecation curves
- Migration strategies

**Key concept introduced:** Governed Evolution

**Ends with:** Compatibility policy template.

---

### Chapter 24: Generator Trust

**Purpose:** Address the supply-chain and trust implications of AI-powered generation.

**Covers:**

- Generators as critical infrastructure, not convenience tools
- Requirements: determinism, reproducibility, auditability
- Verifiable provenance: which spec produced this code?
- Sandboxed execution and safety boundaries
- Evaluating and selecting generators
- What to do when generators fail or drift

**Key concept introduced:** Generator Trust

**Ends with:** Generator evaluation checklist.

---

### Chapter 25: Tradeoffs and Costs

**Purpose:** Honest assessment of SDD's costs and limitations.

**Covers:**

- Specifications become a primary complexity surface
- Runtime enforcement has real computational cost
- The cognitive shift is non-trivial
- New failure modes introduced by SDD
- When SDD is not worth it

**Ends with:** Framework for evaluating SDD ROI.

---

## Closing

### Chapter 26: The Future of Specification

**Purpose:** Provide perspective without speculation. Close the book.

**Covers:**

- What will change as agents improve (and what won't)
- The enduring value of clear thinking about requirements
- SDD as a foundation, not a final answer
- Where to go from here

**Ends with:** Call to practice, not just read.

---

## Appendices

### Appendix A: Specification Templates

Reusable templates for common specification types:

- Feature specification
- Bug fix specification
- Refactoring specification
- API endpoint specification

### Appendix B: Glossary

Full definitions of all SDD terminology. (Reference: glossary.md)

### Appendix C: Quick Reference

One-page SDD workflow summary. Checklists for spec writing, validation, troubleshooting.

---

## Notes for Content Generation

**Dependencies:** Chapters are sequential. Do not reference concepts before they are introduced.

**Examples:** Each chapter in Parts 2-5 requires at least one worked example. Coordinate examples across chapters where possible (e.g., a running project that evolves).

**Length guidance:**

- Part 1 chapters: shorter (establishing concepts and mental models)
- Part 2 chapters: medium (teaching core spec-writing skills)
- Part 3 chapters: medium (workflow and operational practice)
- Part 4 chapters: medium to longer (applied practice, team dynamics)
- Part 5 chapters: medium (governance, trust, tradeoffs)

**Cross-references:** Note when a chapter refers back to or sets up another chapter. Track in continuity-tracker.md.

**Key sources:**

- InfoQ article "Spec Driven Development: When Architecture Becomes Executable" (Griffin & Carroll, Jan 2026) — foundational framing for the five-layer model, architectural inversion, and SpecOps concepts.
- Thoughtworks article "Spec-driven development: Unpacking one of 2025's key new AI-assisted engineering practices" (Liu Shangqi, Dec 2025) — practical perspective on context engineering, BDD lessons, and CI/CD integration.
