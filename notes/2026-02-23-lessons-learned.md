# Lessons Learned — 2026-02-23

## Session Focus

Architectural review of the MCP server structure. Started with "what specs should actually be skills?" and ended up rethinking the entire server topology, naming conventions, and alignment with MCP protocol primitives.

---

## The Four Types of Context

The key insight from this session. Every piece of context an agent loads falls into one of four categories:

| Type | Definition | Server | Example |
|------|-----------|--------|---------|
| **Intent** | What needs to happen | `.spec_mcp` | `book-brief`, `authors-note` |
| **Method** | How to do it well | `.skill_mcp` | `author-spec`, `mcp-builder` |
| **Brand** | What it must look and sound like | `.brand_mcp` | `voice`, `palette`, `typography` |
| **State** | What has already happened | `.memory_mcp` | `continuity-tracker`, `glossary` |

This maps to how anyone approaches work: what am I doing, how should I do it, what are the guardrails, and what's already been done. The SDD insight is that when the executor is an AI agent, you can't rely on tribal knowledge — you have to make all four types explicit, structured, and machine-readable.

---

## Specs That Should Be Skills

Several files currently in `.specmcp/specs/editorial/` are not tasks with a plan-execute-verify lifecycle. They are reference material that agents load for context. That makes them skills (method), not specs (intent).

**Move to `.skill_mcp`:**

- **writers-guide** — teaches agents how to write for this book. Loaded before every chapter. Pure method.
- **prior-art** — positioning knowledge. "When you encounter X, relate it to SDD like this."
- **diataxis-integration** — a framework for classifying content. Loaded and applied, never executed.

**Move to `.memory_mcp`:**

- **continuity-tracker** — accumulated state tracking what concepts have been introduced, where, and what cross-references exist. Updated as a side effect of chapter writing.
- **glossary** — canonical terms that accumulate as chapters are written. Not a skill (doesn't teach method), not brand (not identity). It's state.

**Keep as specs:**

- **book-brief** — on reflection this is intent. It defines the scope, thesis, and audience. Every spec references it.
- **chapter-outline** — living document that defines what chapters exist and their dependencies. Could go either way, but it's closer to intent than method.
- All the task specs (brandmcp-build, readme-update, refactors, authors-note, epigraph, licensing) — these have a lifecycle.

**The migration lesson:** The spec/skill/memory boundary isn't always obvious at project start. Things migrate between categories as you understand the domain. Recognising when something is miscategorised is part of spec hygiene. The taxonomy of your artifacts evolves through practice.

---

## Memory Server Design

`.memory_mcp` is a new server. Unlike the other servers, memory is structured data, not prose.

**Why not markdown:** The other servers serve markdown because their content is prose — specs are instructions, skills are teaching, brand is voice guidelines. Memory is different. "Concept X, introduced in chapter 2, cross-referenced in chapter 5" needs to be queried and updated at the field level, not appended as paragraphs. Markdown will become a nightmare to parse reliably as it grows.

**JSON is the right format.** Python reads and writes it natively, no extra dependencies, and the MCP tools become the interface — agents never touch the files directly.

**Write tools from day one.** We're about to get into real chapters, so the agent needs to update continuity tracking and glossary terms as a side effect of writing. This makes `.memory_mcp` the first server in the repo with write operations.

Example structure for concepts:

```json
{
  "concepts": {
    "spec-as-source": {
      "introduced": "chapter-1",
      "section": "The Three Levels",
      "referenced_in": ["chapter-2", "chapter-5"]
    }
  }
}
```

Example structure for glossary:

```json
{
  "terms": {
    "specification": {
      "definition": "A structured document...",
      "first_used": "chapter-1",
      "alternatives": ["spec"]
    }
  }
}
```

---

## The Agent Is the Orchestrator

Important correction made during the session. The original mental model was "specmcp orchestrates and calls skillmcp, brandmcp, memorymcp." That's wrong.

**The agent is the orchestrator.** All four servers are peers — passive resource providers. The agent reads a spec, sees "load the mcp-builder skill," and the agent calls skillmcp. The spec is just instructions. No server calls another server.

```
Agent (orchestrator)
  ├── .spec_mcp    (intent)
  ├── .skill_mcp   (method)
  ├── .brand_mcp   (brand)
  └── .memory_mcp  (state)
```

The servers are the filing cabinets. The agent is the person walking between them.

---

## Naming Convention Change

**Old:** `.specmcp`, `.skillmcp`, `.brandmcp` — compound words that are hard to parse at a glance, especially `memorymcp`.

**New:** `.spec_mcp`, `.skill_mcp`, `.brand_mcp`, `.memory_mcp`

Dot prefix for hidden (infrastructure, not content). Underscore for readability. Consistent with the existing `snake_case` tool naming (`list_specs`, `get_skill`). This requires a rename spec across all four directories, `.mcp.json`, `CLAUDE.md`, `AGENTS.md`, and any import paths.

---

## MCP Protocol Alignment — The Practical Compromise

We mapped every operation across all four servers against MCP's three primitives (resources, tools, prompts):

**Resources** (read-only, application/user-directed):
- `get_spec`, `get_skill`, `get_brand`, `get_memory`
- All `list_` operations
- Basically everything that reads without side effects

**Tools** (model-controlled, actions with side effects):
- `validate_content()` in spec_mcp
- `write_provenance()` in spec_mcp
- `add_concept()`, `add_term()`, `update_references()` in memory_mcp

**Prompts** (reusable templates that shape agent behaviour):
- `get_chapter_context()` is really a prompt — it bundles context to set up a task
- Skills themselves are arguably prompts — behavioural templates that shape how the agent works

**The problem:** The correct MCP mapping would make most reads into resources and only writes into tools. But Claude Code (and most MCP hosts) don't support model-invoked resource access. Resources are application-driven — the host decides when to fetch them. In an agentic workflow, the agent needs to autonomously pull context based on instructions in the spec. That requires tools.

**The deeper insight:** Our workflow is actually *more* aligned with MCP's intent than the implementation allows. When the human prompts "execute spec X," the agent calls `get_spec("X")` — that's user-directed context loading, exactly the resource pattern. When the spec says "load the mcp-builder skill," the agent loading it is still user-directed, one step removed. The human authored the spec that says to load it. The agent isn't discovering anything; it's following instructions at every step.

**The result:** Every `get_` and `list_` operation is a resource dressed up as a tool because that's what works in an agentic context today. This is a real architectural compromise every MCP builder will hit, and it's worth naming in the book.

---

## Decisions Made

1. Four server types: intent, method, brand, state
2. New naming: `.spec_mcp`, `.skill_mcp`, `.brand_mcp`, `.memory_mcp`
3. writers-guide, prior-art, diataxis-integration move to skill_mcp
4. continuity-tracker and glossary move to memory_mcp as JSON
5. memory_mcp gets write tools from day one
6. The agent is the orchestrator, servers are peers
7. "Constraints" rejected as a category name — brand is specific, constraints is a junk drawer
8. "State" rejected for server name — memory is less clinical, less overloaded in software context

---

## Open Questions

- What's the spec sequence? Rename first, then build memory_mcp, then migrate files?
- Does chapter-outline belong in spec_mcp or skill_mcp?
- Should book-brief stay as a spec or is it more like ambient context?
- What's the schema design for memory_mcp beyond concepts and glossary? Decisions log?
- How does `get_chapter_context()` evolve — does it pull from all four servers?
