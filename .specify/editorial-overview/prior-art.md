# Prior Art: Related Concepts and How SDD Relates

Reference this document when positioning SDD relative to established practices. Use it to draw correct analogies, avoid conflation, and connect to reader knowledge.

---

## Quick Reference

| Practice | Relationship to SDD | Use When | Avoid |
|----------|--------------------|-----------| ------|
| TDD | Parallel philosophy | Explaining "spec before code" mindset | Implying SDD replaces TDD |
| BDD | Direct ancestor | Discussing spec structure, language, examples | Treating as identical |
| DDD | Concept source | Explaining bounded contexts, domain language | Over-complicating with full DDD theory |
| Contract-First | Partial precedent | Explaining "contract as truth" for API-familiar readers | Limiting scope to interfaces |
| Prompt Engineering | Predecessor skill | Acknowledging reader background | Conflating with SDD |
| Vibe Coding | Problem SDD solves | Validating reader frustrations | Being dismissive |
| MDD | Cautionary parallel | Warning about failure modes | Suggesting equivalence |
| Literate Programming | Philosophical connection | Historical context (optional) | Over-emphasizing |
| Context Engineering | Component of SDD | Discussing context management | Treating as separate practice |

---

## Test-Driven Development (TDD)

**Definition:** Write tests before code. Red → green → refactor cycle.

| Aspect | TDD | SDD |
|--------|-----|-----|
| Drives development | Tests | Specifications |
| Primary artifact | Test suite + code | Specification + generated code |
| Validation | Automated test execution | Spec conformance + drift detection |
| Iteration target | Code | Specification |
| Implementation | Human | AI agent |

**Borrow from TDD:**
- Define expectations before implementation
- Fast feedback loops
- Executable specifications concept

**Do not say:**
- "SDD replaces TDD"
- "You don't need tests with SDD"

**Do say:**
- "Like TDD, SDD defines expectations before implementation"
- "Generated code still benefits from tests"
- "SDD and TDD can coexist"

---

## Behavior-Driven Development (BDD)

**Definition:** Natural language specifications (Given/When/Then) describing behavior. Specs execute as tests.

| Aspect | BDD | SDD |
|--------|-----|-----|
| Spec format | Gherkin (Given/When/Then) | Structured markdown/text |
| Primary audience | Business + developers | AI agents + developers |
| Spec execution | Becomes automated tests | Becomes generation input |
| Maintenance | Living documentation | System source of truth |

**Borrow from BDD:**
- Ubiquitous language (domain terms, not implementation terms)
- Consistent structure (Given/When/Then patterns useful)
- Spec-by-example (concrete examples = few-shot prompting)
- Completeness yet conciseness
- Clarity and determinism

**Do not say:**
- "SDD is just BDD for AI"
- "Use Cucumber for SDD"

**Do say:**
- "BDD's lessons about spec structure transfer directly"
- "Spec-by-example in BDD is equivalent to few-shot prompting"
- "SDD extends BDD's insights to the generation era"

**Reference frequency:** High. Most readers know BDD.

---

## Domain-Driven Design (DDD)

**Definition:** Software design centered on business domain. Key concepts: ubiquitous language, bounded contexts, aggregates.

| Aspect | DDD | SDD |
|--------|-----|-----|
| Central concern | Domain model accuracy | Specification completeness |
| Structuring concept | Bounded context | Bounded context (adopted) |
| Language emphasis | Ubiquitous language | Domain-oriented specs |
| Implementation | Human developers | AI agents |

**Borrow from DDD:**
- Bounded context (term borrowed directly—acknowledge this)
- Ubiquitous language
- Model before code

**Key distinction:**
- DDD bounded contexts = semantic (team/domain boundaries)
- SDD bounded contexts = also pragmatic (context window limits)

**Do not say:**
- "You need to understand DDD to use SDD"
- Deep DDD concepts (aggregates, entities, repositories) unless specifically relevant

**Do say:**
- "The term 'bounded context' comes from DDD"
- "Like DDD, SDD emphasizes domain language over technical jargon"

**Reference frequency:** Medium. Use for bounded context explanation.

---

## Contract-First / API-First Development

**Definition:** Define API contracts (OpenAPI, protobuf) before implementation. Generate code from contracts.

| Aspect | Contract-First | SDD |
|--------|----------------|-----|
| Source of truth | API schema | Specification |
| Code generation | Stubs, clients, validators | Full implementation |
| Scope | Interface boundaries | Entire system behavior |
| Generation type | Deterministic templates | Non-deterministic LLM |

**Borrow from Contract-First:**
- Contract/schema as truth (established precedent)
- Multi-target generation
- Versioning and compatibility practices

**Do not say:**
- "SDD is just OpenAPI for everything"

**Do say:**
- "Contract-first for interfaces; SDD extends this to full implementation"
- "If you've used OpenAPI workflows, SDD will feel familiar"

**Reference frequency:** Medium. Useful for API-familiar readers.

---

## Prompt Engineering

**Definition:** Crafting LLM inputs to get desired outputs. Techniques: chain-of-thought, few-shot, role assignment.

| Aspect | Prompt Engineering | SDD |
|--------|-------------------|-----|
| Scope | Individual interactions | Development methodology |
| Artifact | Prompts (ephemeral) | Specifications (versioned) |
| Focus | Model output optimization | Workflow structure |
| Persistence | Ad-hoc | Systematic |

**Borrow from Prompt Engineering:**
- Structure improves output
- Few-shot examples help
- Context matters

**Critical distinction:**
- Prompt engineering = tactical (single requests)
- SDD = strategic (entire methodology)

**Do not say:**
- "SDD is advanced prompt engineering"
- "Better prompts = SDD"

**Do say:**
- "Prompt engineering optimizes individual interactions; SDD structures entire workflows"
- "SDD is what comes after you've mastered prompting"
- "Prompts are tactical; specifications are strategic"

**Reference frequency:** High. Correct the conflation explicitly.

---

## Vibe Coding

**Definition:** Ad-hoc, conversational coding with AI. Loose prompts, iterative chat, accept whatever works, minimal structure.

| Aspect | Vibe Coding | SDD |
|--------|-------------|-----|
| Structure | Minimal | High |
| Planning | Ad-hoc | Deliberate |
| Artifacts | Conversation history | Versioned specifications |
| Reproducibility | Low | High |
| Feedback loops | Chaotic or none | Structured validation |

**Vibe coding works for:**
- Quick prototypes
- Exploration
- Throwaway scripts
- Low-stakes automation

**Vibe coding fails for:**
- Production systems
- Maintainable code
- Team collaboration
- Consistency requirements

**SDD relationship:** SDD is the structured alternative to vibe coding.

**Do not say:**
- "Vibe coding is wrong/bad/stupid"
- Dismissive language about readers' current practices

**Do say:**
- "Vibe coding is fast and fun, but insufficient for serious work"
- "If you've felt frustrated by inconsistent results from ad-hoc prompting, SDD provides structure"
- "SDD is what you adopt when vibe coding stops scaling"

**Reference frequency:** High. This is the "before" state for most readers.

---

## Model-Driven Development (MDD)

**Definition:** Abstract models (UML, DSLs) as primary artifacts. Code generated from models. Enterprise tooling (IBM Rational, etc.).

| Aspect | MDD | SDD |
|--------|-----|-----|
| Model format | Visual diagrams, formal DSLs | Natural language specs |
| Generation | Deterministic templates | Non-deterministic LLM |
| Flexibility | Rigid, tool-dependent | Flexible, tool-agnostic |
| Adoption | Failed mainstream | Emerging |

**Borrow from MDD:**
- Model/spec as truth (shared ambition)
- Generation pipeline concept

**MDD failed because:**
- Steep learning curves
- Proprietary tool lock-in
- Rigidity
- Model-code sync problems (drift)

**SDD must avoid these failures:**
- Keep specs in natural language (no proprietary DSL)
- Maintain tool-agnosticism
- Prioritize drift detection

**Do not say:**
- "SDD is like MDD but better"
- Imply equivalence

**Do say:**
- "MDD had similar ambitions but different approach"
- "SDD addresses MDD's drift problem with continuous validation"
- "Unlike MDD, SDD uses natural language—no specialized modeling skills required"

**Reference frequency:** Low. Cautionary reference only.

---

## Literate Programming

**Definition:** Programs as documents for human reading. Code embedded in explanatory prose. Document is primary; code extracted.

| Aspect | Literate Programming | SDD |
|--------|---------------------|-----|
| Primary artifact | Document with embedded code | Specification |
| Code relationship | Extracted from document | Generated from spec |
| Audience | Human readers | AI agents + humans |

**Borrow from Literate Programming:**
- Inversion of primacy (document over code)
- Explanation-first forces clarity

**Do not say:**
- Extended comparisons (connection is philosophical, not practical)

**Reference frequency:** Very low. Optional historical note.

---

## Context Engineering

**Definition:** Curating and managing contextual information for AI agents at scale. Distinct from prompt engineering.

| Aspect | Prompt Engineering | Context Engineering |
|--------|-------------------|---------------------|
| Optimizes | Human-LLM interaction | Agent-LLM interaction |
| Scale | Single requests | System-wide |
| Concerns | Prompt wording | Information curation, context windows, knowledge bases |

**Relationship to SDD:** Context engineering is a component of SDD, not a separate practice.

**Context engineering in SDD includes:**
- Specs compress context into structured form
- Bounded contexts manage agent information
- System prompts (AGENTS.md, Cursor rules)
- MCP servers and knowledge bases

**Do not say:**
- "Context engineering vs. SDD"
- Treat as competing approaches

**Do say:**
- "SDD incorporates context engineering practices"
- "Specifications are a form of context compression"

**Reference frequency:** Medium. Part of SDD methodology.

---

## Comparison Rules

**When drawing comparisons:**

| If comparing to... | Emphasize | De-emphasize |
|-------------------|-----------|--------------|
| TDD | Shared "define first" philosophy | Implementation differences |
| BDD | Transferable spec-writing lessons | Execution mechanism differences |
| DDD | Bounded context concept | Full DDD complexity |
| Contract-First | Extended scope (interfaces → full implementation) | Tool-specific details |
| Prompt Engineering | Strategic vs. tactical distinction | Technique overlap |
| Vibe Coding | Structure as solution | Reader's current competence |
| MDD | Why SDD avoids MDD's failures | Shared ambition |

**Default stance:** SDD builds on established practices, extends them for the AI generation era, and addresses new challenges they couldn't anticipate.

---

## Forbidden Comparisons

Do not say:

- "SDD replaces [any practice]"
- "You don't need [TDD/testing/code review] with SDD"
- "SDD is just [X] for AI"
- "Unlike [practice], SDD actually works"
- Dismissive statements about any methodology

---

## Reader Knowledge Assumptions

| Practice | Assume Reader Knows | Action |
|----------|---------------------|--------|
| TDD | Yes | Reference freely |
| BDD | Likely | Reference freely |
| Git workflows | Yes | Reference freely |
| Prompt engineering | Yes | Reference freely |
| Vibe coding | Yes (experience) | Reference freely |
| DDD | Maybe not | Explain bounded context when used |
| Contract-first | Maybe not | Explain if referenced |
| MDD | Probably not | Explain if referenced |
| Literate programming | No | Do not assume |