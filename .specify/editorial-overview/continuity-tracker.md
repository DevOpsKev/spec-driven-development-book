# Continuity Tracker

This document tracks concepts, terms, examples, and cross-references across the book. Use it to prevent contradictions, ensure proper sequencing, and maintain consistency.

Update this document as content is generated.

---

## Usage Rules

1. **Check before writing.** Before generating chapter content, verify which concepts have been introduced.
2. **Do not use undefined terms.** If a term has not been introduced, either introduce it properly or do not use it.
3. **Update after writing.** After generating content, log new concepts, examples, and references here.
4. **Flag contradictions.** If new content conflicts with logged information, flag for resolution.

---

## Concepts Introduction Log

Track when each concept is first introduced and defined.

| Concept | Introduced In | Definition Status | Notes |
|---------|---------------|-------------------|-------|
| Specification (spec) | Chapter 3 | Defined in glossary | Core term |
| Architectural Inversion | Chapter 3 | Defined in glossary | Core thesis |
| Ambient Code | Chapter 3 | Defined in glossary | |
| Spec-first workflow | Chapter 4 | Defined in glossary | |
| Five-layer model | Chapter 5 | Defined in glossary | Full breakdown in chapter |
| Specification Layer | Chapter 5 | Defined in glossary | Part of five-layer model |
| Generation Layer | Chapter 5 | Defined in glossary | Part of five-layer model |
| Artifact Layer | Chapter 5 | Defined in glossary | Part of five-layer model |
| Validation Layer | Chapter 5 | Defined in glossary | Part of five-layer model |
| Runtime Layer | Chapter 5 | Defined in glossary | Part of five-layer model |
| Bounded context | Chapter 7 | Defined in glossary | Borrowed from DDD—acknowledge origin |
| Context engineering | Chapter 8 | Defined in glossary | Distinct from prompt engineering |
| Acceptance criteria | Chapter 11 | Defined in glossary | Preview; detailed in Ch 14 |
| Generation | Chapter 5, detailed Ch 13 | Defined in glossary | |
| Generation cycle | Chapter 13 | Defined in glossary | |
| Validation | Chapter 11 preview, Ch 14 detail | Defined in glossary | |
| Drift | Chapter 14 | Defined in glossary | |
| Drift detection | Chapter 14 | Defined in glossary | |
| Iteration (SDD definition) | Chapter 15 | Defined in glossary | Spec refinement, not prompt tweaking |
| SpecOps | Chapter 16 | Defined in glossary | |
| Deterministic validation | Chapter 17 | Defined in glossary | |
| Human-in-the-loop | Chapter 19 | Defined in glossary | |
| Bounded autonomy | Chapter 19 | Defined in glossary | |
| Schema engineering | Chapter 21 | Defined in glossary | |
| Governed evolution | Chapter 23 | Defined in glossary | |
| Generator trust | Chapter 24 | Defined in glossary | |
| Vibe coding | Chapter 2 | Defined in glossary | Contrast term |
| Prompt engineering | Chapter 4 | Defined in glossary | Contrast term—correct conflation |

---

## Chapter Dependencies

Track which chapters depend on concepts from prior chapters.

| Chapter | Requires Concepts From | Introduces |
|---------|------------------------|------------|
| Ch 1: The Fifth Generation | None | Abstraction elevation |
| Ch 2: The Problem with Prompting | None | Vibe coding (as problem) |
| Ch 3: The Core Insight | Ch 2 | Specification, Architectural Inversion, Ambient Code |
| Ch 4: Specifications vs. Prompts | Ch 3 | Spec-first workflow, Prompt engineering (contrast) |
| Ch 5: The Five-Layer Model | Ch 3, Ch 4 | Five-layer model, all layer terms |
| Ch 6: Anatomy of a Specification | Ch 3, Ch 4 | Spec-by-example |
| Ch 7: Defining Context | Ch 6 | Bounded context |
| Ch 8: Context Engineering | Ch 7 | Context engineering |
| Ch 9: Writing Requirements | Ch 6 | — |
| Ch 10: Constraints and Boundaries | Ch 6 | — |
| Ch 11: Acceptance Criteria | Ch 6 | Acceptance criteria, Validation (preview) |
| Ch 12: Project Structure for SDD | Ch 7 | — |
| Ch 13: The Generation Cycle | Ch 5, Ch 6 | Generation cycle |
| Ch 14: Validation and Drift Detection | Ch 5, Ch 11 | Drift, Drift detection, Validation (full) |
| Ch 15: Iteration as Spec Refinement | Ch 13, Ch 14 | Iteration |
| Ch 16: SpecOps | Ch 14, Ch 15 | SpecOps |
| Ch 17: Deterministic CI/CD | Ch 14, Ch 16 | Deterministic validation |
| Ch 18: When to Use SDD | Ch 1–17 | — |
| Ch 19: Human-in-the-Loop | Ch 5, Ch 14 | Human-in-the-loop, Bounded autonomy |
| Ch 20: Failure Modes | Ch 14, Ch 17 | — |
| Ch 21: SDD in Teams | Ch 16, Ch 19 | Schema engineering |
| Ch 22: Beyond Code Generation | Ch 5, Ch 13 | — |
| Ch 23: Governed Evolution | Ch 16, Ch 21 | Governed evolution |
| Ch 24: Generator Trust | Ch 13, Ch 17 | Generator trust |
| Ch 25: Tradeoffs and Costs | All prior | — |
| Ch 26: The Future of Specification | All prior | — |

---

## Examples Log

Track examples used to ensure consistency and avoid repetition.

| Example | Used In | Type | Notes |
|---------|---------|------|-------|
| (No examples logged yet) | | | |

**Example types:**
- Running example (evolves across chapters)
- Standalone (single chapter use)
- Code snippet
- Specification sample
- Workflow diagram
- Before/after comparison

---

## Forward References

Track when content references concepts not yet introduced.

| Reference | In Chapter | Points To | Resolution |
|-----------|------------|-----------|------------|
| (No forward references logged yet) | | | |

**Resolution options:**
- Add brief preview
- Reorder content
- Remove reference
- Accept (if minor)

---

## Backward References

Track when content explicitly references prior material.

| Reference | In Chapter | Points Back To | Type |
|-----------|------------|----------------|------|
| (No backward references logged yet) | | | |

**Reference types:**
- Concept recall
- Example continuation
- Contrast with earlier point
- Building on foundation

---

## Contradictions and Conflicts

Flag any inconsistencies discovered during content generation.

| Issue | Location | Conflicting Content | Status | Resolution |
|-------|----------|---------------------|--------|------------|
| (No contradictions logged) | | | | |

**Status options:** Open, Under review, Resolved

---

## Document Registry

Track all project documents and their relationships.

| Document | Purpose | Status | Last Updated |
|----------|---------|--------|--------------|
| writers-guide.md | Voice, tone, editorial rules | Complete (v1) | Current session |
| book-brief.md | Scope, thesis, audience, boundaries | Complete (v1) | Current session |
| chapter-outline.md | Book structure, 26 chapters | Complete (v1) | Current session |
| glossary.md | Terminology canon, 27 terms | Complete (v1) | Current session |
| prior-art.md | Related practices, positioning | Complete (v1) | Current session |
| continuity-tracker.md | Cross-reference state | Active | Current session |
| author-voice.md | Author perspective, opinions | Not started | — |
| examples-library.md | Reusable examples | Not started | — |
| anti-patterns.md | Common mistakes catalog | Not started | — |
| chapter-briefs/ | Per-chapter scope | Not started | — |

---

## Key Decisions Log

Track significant decisions about content, positioning, or structure.

| Decision | Context | Rationale | Date |
|----------|---------|-----------|------|
| Source of truth debate left open | Ch 3, book-brief | Both radical and traditional views benefit from same practices; book does not require commitment | Current session |
| 26 chapters + appendices structure | chapter-outline | Based on InfoQ and Thoughtworks article coverage | Current session |
| BDD as primary prior art reference | prior-art | Most readers know BDD; strongest transferable lessons | Current session |
| CI/CD chapter added (Ch 17) | chapter-outline | Non-deterministic generation requires deterministic validation (Thoughtworks insight) | Current session |
| Context engineering as separate chapter (Ch 8) | chapter-outline | Distinct from bounded context; important enough for dedicated coverage | Current session |

---

## Terminology Consistency Checks

Flag terms that need consistent usage across chapters.

| Term | Preferred | Avoid | Notes |
|------|-----------|-------|-------|
| Specification, spec | Both acceptable | "prompt document", "instruction set" | |
| AI coding agent, agent | Both acceptable | "AI assistant", "copilot" (unless specific product) | |
| Generated code, output | Both acceptable | "hallucination" (unless discussing failure modes) | |
| Context | — | — | Always qualify: "context window", "project context", "conversation context" |
| Drift | Drift | "deviation", "mismatch" (less precise) | |
| Iteration | Iteration | "prompt tweaking" (wrong concept) | SDD iteration = spec refinement |

---

## Open Items

Track items requiring author input or decisions.

| Item | Type | Blocking | Notes |
|------|------|----------|-------|
| Running example project | Example | Ch 6+ | Need realistic project that evolves across chapters |
| Author voice content | Document | author-voice.md | Only author can provide opinions, anecdotes |
| Case study inclusion | Decision | Ch 18–22 | Depth and length of case studies TBD |
| Companion repository | Decision | Appendices | Whether example specs repo exists |
| Final book title | Decision | Publication | Options in book-brief.md |
| Position on source of truth debate | Decision | Ch 3 | Currently neutral; author may want to take stance |