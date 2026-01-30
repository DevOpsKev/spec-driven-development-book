# Glossary: SDD Terminology

This is the authoritative source for all SDD terminology. Reference this document when using or defining terms. Do not invent definitions. Use terms exactly as defined here.

---

## Usage Rules

1. **Use preferred terms.** If a term has alternatives listed, use the preferred term.
2. **Define on first use.** When a term first appears in a chapter, provide its definition.
3. **Do not redefine.** After first use, use the term without re-explaining.
4. **Maintain consistency.** Never alternate between a term and its alternatives.
5. **Link related terms.** When terms are connected, reference the relationship.

---

## Core Concepts

### Specification (spec)

**Definition:** A structured document defining what to build, serving as input for an AI coding agent and criteria for validating output.

**Is:** Versioned, maintained, executable, the source of truth (in SDD model)

**Is not:** A prompt, a PRD, documentation, disposable

**Related terms:** Spec-first workflow, Validation, Drift

**First introduced:** Chapter 3

---

### Spec-First Workflow

**Definition:** Writing the specification before engaging the agent, rather than iterating through conversation.

**Contrast with:** Vibe coding, prompt-driven development

**Related terms:** Specification, Generation cycle

**First introduced:** Chapter 4

---

### Architectural Inversion

**Definition:** The shift from code-as-truth to specification-as-truth. Implementations are derived from specs, not vice versa.

**Traditional model:** Code defines behavior; architecture is advisory

**SDD model:** Specification defines behavior; code is derived

**Related terms:** Ambient code, Specification

**First introduced:** Chapter 3

---

### Ambient Code

**Definition:** Generated code that is regenerable, disposable, and continuously reconcilable. Not the primary artifact.

**Implication:** Code can be deleted and regenerated from spec without loss

**Related terms:** Architectural inversion, Generation

**First introduced:** Chapter 3

---

### Five-Layer Model

**Definition:** The SDD architectural model consisting of five layers that form a closed control loop.

**Layers:**
| Layer | Function | Output |
|-------|----------|--------|
| Specification | Declares intent | Spec documents |
| Generation | Transforms spec to code | Generated artifacts |
| Artifact | Contains generated outputs | Services, components, clients |
| Validation | Enforces conformance | Pass/fail, drift reports |
| Runtime | Executes the system | Running software |

**Flow:** Specification → Generation → Artifact → Validation → Runtime (loops back to Specification)

**Related terms:** All layer-specific terms

**First introduced:** Chapter 5

---

### Bounded Context

**Definition:** A scoped portion of a project small enough for an agent to hold in working memory.

**Origin:** Borrowed from Domain-Driven Design (DDD)

**DDD meaning:** Semantic boundary around a coherent domain area

**SDD meaning:** Also pragmatic—constrained by agent context window limits

**Related terms:** Context engineering, Project structure

**First introduced:** Chapter 7

---

### Context Engineering

**Definition:** Curating and managing contextual information for AI agents at scale.

**Distinction:** Prompt engineering optimizes human-LLM interaction; context engineering optimizes agent-LLM interaction.

**Includes:**
- Spec structure (context compression)
- System prompts (AGENTS.md, Cursor rules)
- MCP servers and knowledge bases
- Token budget management

**Related terms:** Bounded context, Specification

**First introduced:** Chapter 8

---

### Generation

**Definition:** The code output produced by an agent from a specification.

**Properties:**
- Non-deterministic (same spec may yield different code)
- Should be validated against spec
- Regenerable from spec

**Related terms:** Ambient code, Generation cycle, Validation

**First introduced:** Chapter 5, detailed in Chapter 13

---

### Generation Cycle

**Definition:** The end-to-end process from specification to validated code.

**Steps:**
1. Prepare spec and context
2. Invoke agent
3. Receive output
4. Validate against spec
5. Accept, iterate, or reject

**Related terms:** Specification, Generation, Validation, Iteration

**First introduced:** Chapter 13

---

### Validation

**Definition:** Systematic verification that generated code meets the specification.

**Methods:**
- Acceptance criteria checking
- Contract tests
- Schema validation
- Drift detection

**Related terms:** Drift detection, Acceptance criteria, Deterministic validation

**First introduced:** Chapter 11 (preview), detailed in Chapter 14

---

### Drift

**Definition:** Any divergence between declared specification intent and observed system behavior.

**Types:**
| Type | Description |
|------|-------------|
| Structural | Schema/interface mismatches |
| Behavioral | Logic deviates from spec |
| Semantic | Meaning shifts from intent |
| Security | Policy violations |
| Evolutionary | Uncontrolled version divergence |

**Related terms:** Drift detection, Validation

**First introduced:** Chapter 14

---

### Drift Detection

**Definition:** Mechanisms for identifying divergence between specification and implementation.

**Methods:**
- Schema validation
- Contract testing
- Payload inspection
- Spec diffing
- Architectural fitness functions

**Importance:** Without drift detection, SDD collapses into documentation-driven development.

**Related terms:** Drift, Validation, Deterministic validation

**First introduced:** Chapter 14

---

### Iteration

**Definition:** Refining the specification (not the prompt) to improve generation output.

**SDD iteration:** Spec refinement → regeneration → validation

**Contrast with:** Prompt tweaking, code patching

**Related terms:** Generation cycle, Validation

**First introduced:** Chapter 15

---

### SpecOps (Specification Operations)

**Definition:** Treating specifications with the same operational rigor as source code.

**Practices:**
- Version control
- Branching strategies
- Code review for specs
- CI/CD integration
- Controlled merges

**Related terms:** Specification, Governed evolution

**First introduced:** Chapter 16

---

### Deterministic Validation

**Definition:** Using CI/CD practices to safeguard against non-deterministic generation.

**Rationale:** Code generation is non-deterministic; validation must be deterministic to ensure quality.

**Includes:**
- Contract tests in pipelines
- Schema validation gates
- Architectural fitness functions
- Automated conformance checks

**Related terms:** Validation, Drift detection, SpecOps

**First introduced:** Chapter 17

---

### Human-in-the-Loop

**Definition:** Preserving human authority over intent, policy, and meaning while delegating enforcement to machines.

**Humans own:** Intent, policy, risk tolerance, ethics, meaning, approval decisions

**Machines own:** Enforcement, generation, conformance checking

**Related terms:** Bounded autonomy

**First introduced:** Chapter 19

---

### Bounded Autonomy

**Definition:** Explicit approval boundaries within which machines can act; breaking changes require human authorization.

**Examples of approval gates:**
- Breaking schema changes
- Policy shifts
- Compatibility downgrades
- Security boundary changes

**Related terms:** Human-in-the-loop, Governed evolution

**First introduced:** Chapter 19

---

### Governed Evolution

**Definition:** Systematic approach to evolving specifications without breaking dependent systems.

**Includes:**
- Change classification (additive, compatible, breaking, ambiguous)
- Compatibility policies
- Parallel version surfaces
- Controlled deprecation
- Migration strategies

**Related terms:** SpecOps, Bounded autonomy

**First introduced:** Chapter 23

---

### Generator Trust

**Definition:** Treating AI generators as critical infrastructure requiring determinism, reproducibility, and auditability.

**Requirements:**
| Requirement | Description |
|-------------|-------------|
| Determinism | Same input should yield consistent output patterns |
| Reproducibility | Generation can be repeated reliably |
| Auditability | Can trace which spec produced which code |
| Provenance | Verifiable origin of generated artifacts |

**Related terms:** Generation, Validation

**First introduced:** Chapter 24

---

### Schema Engineering

**Definition:** The discipline of designing and maintaining specifications as long-lived executable infrastructure.

**Treats specs as:** Technical debt surface, architectural artifact, team discipline

**Related terms:** Specification, SpecOps, Governed evolution

**First introduced:** Chapter 21

---

## Workflow Terms

### Acceptance Criteria

**Definition:** Testable conditions that define when generated code meets the specification.

**Properties:** Specific, measurable, tied to validation methods

**Related terms:** Validation, Specification

**First introduced:** Chapter 11

---

### Spec-by-Example

**Definition:** Using concrete examples within specifications to illustrate expected behavior.

**Origin:** BDD practice

**SDD application:** Functions as few-shot prompting for agents

**Related terms:** Specification, BDD (see Prior Art)

**First introduced:** Chapter 6

---

## Contrast Terms

These terms describe approaches SDD differs from. Use when positioning SDD.

### Vibe Coding

**Definition:** Ad-hoc, conversational coding with AI. Minimal structure, loose prompts, accept whatever works.

**Characteristics:** Fast, spontaneous, haphazard, low reproducibility

**SDD relationship:** SDD is the structured alternative

**Use in text:** Validate reader experience, do not dismiss

**First introduced:** Chapter 2

---

### Prompt Engineering

**Definition:** Crafting LLM inputs to optimize individual outputs.

**Scope:** Tactical (single interactions)

**SDD relationship:** SDD is strategic (methodology); prompt engineering is a component skill

**Common conflation:** "SDD is just better prompting" — correct this explicitly

**First introduced:** Chapter 4

---

## Architectural Terms

### Specification Layer

**Definition:** The layer in the five-layer model that contains authoritative definitions of system behavior.

**Contains:** API models, contracts, schemas, constraints, policies

**Related terms:** Five-layer model

**First introduced:** Chapter 5

---

### Generation Layer

**Definition:** The layer that transforms specifications into executable artifacts.

**Function:** Multi-target compilation (specs → code, docs, tests)

**Related terms:** Five-layer model, Generation

**First introduced:** Chapter 5

---

### Artifact Layer

**Definition:** The layer containing generated outputs (services, components, clients).

**Key property:** Artifacts are not primary—they are regenerable from specs

**Related terms:** Five-layer model, Ambient code

**First introduced:** Chapter 5

---

### Validation Layer

**Definition:** The layer that enforces continuous alignment between intent and execution.

**Function:** Contract tests, schema validation, drift detection

**Related terms:** Five-layer model, Validation, Drift detection

**First introduced:** Chapter 5

---

### Runtime Layer

**Definition:** The operational system composed of deployed artifacts.

**Key property:** Runtime behavior is constrained by upstream specification and validation layers

**Related terms:** Five-layer model

**First introduced:** Chapter 5

---

## Term Relationships

```
Specification
├── drives → Generation
├── validated by → Validation
├── managed via → SpecOps
└── evolves via → Governed Evolution

Generation
├── produces → Artifacts (Ambient Code)
├── is non-deterministic → requires Deterministic Validation
└── depends on → Generator Trust

Validation
├── detects → Drift
├── uses → Acceptance Criteria
└── enforced by → CI/CD (Deterministic Validation)

Human-in-the-Loop
├── owns → Intent, Policy, Meaning
├── delegates → Enforcement, Generation
└── defines → Bounded Autonomy

Bounded Context
├── borrowed from → DDD
├── enables → Context Engineering
└── constrains → Agent working memory
```

---

## Adding New Terms

When the glossary needs expansion:

1. Add term in appropriate section
2. Include: Definition, Related terms, First introduced (chapter)
3. Add to Term Relationships if connected to existing terms
4. Update chapter-outline.md to note where term is introduced