# Lessons Learned: The AI-Native Development Stack is a Composition, Not a Tool

**Date:** 2026-03-03
**Author:** Kevin Ryan
**Context:** SDD Book Research / AI-Native Software Engineering

---

## Key Insight

The AI-native development stack is not a single tool — it is a **composition of tools operating at different abstraction levels**, each owning a distinct concern. Choosing one over another is a false dichotomy. The real skill is understanding which layer each tool serves and composing them effectively.

## The Stack

| Layer | Concern | Tool | Interaction Pattern |
|-------|---------|------|-------------------|
| **Specification** | Defining intent and architectural decisions | SpecMCP / ADRs | Declarative, persistent |
| **Orchestration** | Multi-step, project-level transformations | Claude Code (CLI) | Agentic, asynchronous |
| **Interaction** | Moment-to-moment development flow | Cursor | Conversational, synchronous |
| **Environment** | Reproducible infrastructure definition | Codespaces / devcontainers | Infrastructure-as-Code |

## Observations

### Cursor as State of the Art

Cursor represents the current reference implementation for AI-native IDE tooling. It validates the "ease of specification" principle — the entire UX is about lowering friction between intent and implementation. Writing about SDD without hands-on Cursor experience would be a credibility gap.

### Cursor + Codespaces: Separation of Concerns

Cursor owns the **interaction layer** — how you communicate intent to the AI. Codespaces owns the **infrastructure layer** — what the environment looks like. These are orthogonal concerns that should not be coupled.

Practical approach: Use Cursor locally as the AI-native interface, with `devcontainer.json` specifications maintaining Infrastructure-as-Code rigour underneath. Cursor supports Remote SSH and dev containers natively, so the Codespaces hosting layer may be optional — the same devcontainer specs can run locally through Cursor.

### Claude Code is Complementary, Not Competing

Claude Code lives in the terminal, not the IDE. It operates at a different abstraction level:

- **Cursor** — tight feedback loop, inline editing, tab completion. Best for in-flow development work.
- **Claude Code** — agentic orchestration across the whole codebase. Best for larger transformations, spec-to-implementation workflows, and the kind of work SpecMCP would eventually orchestrate.

They serve different interaction patterns and can run simultaneously — Cursor in the editor, Claude Code in the integrated terminal or a separate shell.

### Comparative Analysis Opportunity

A chapter or section comparing the specification experience across AI-native tools (Cursor, Copilot, Claude Code, Windsurf) through an **architectural lens** — not just "which autocomplete is faster" — would be genuinely valuable content for the SDD book. Nobody is doing rigorous comparative analysis of these tools from a specification-driven perspective.

## Implications for SDD Book

1. The layered stack model provides a framework for evaluating AI-native tooling without picking tribes.
2. "Ease of specification" operates differently at each layer — inline (Cursor), conversational (Claude Code), declarative (SpecMCP).
3. The question of whether current tools are the endgame or a transitional form is central — will the IDE evolve beyond the text-editor paradigm entirely when specification becomes the primary artifact?
4. ADRs as "context engineering" for AI agents connects directly to how these tools manage context across large codebases.

## Action Items

- [ ] Install Cursor and begin daily use alongside existing Codespaces workflow
- [ ] Document the devcontainer interop experience (Cursor local vs Codespaces hosted)
- [ ] Run Claude Code within Cursor's terminal on an existing project to test the composition
- [ ] Draft comparative framework for AI-native tooling chapter in SDD book
- [ ] Investigate how Cursor handles context window management across large codebases

---

*Filed under: SDD Book Research / AI-Native Tooling / Career Pivot*
