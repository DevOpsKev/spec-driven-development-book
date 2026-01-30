# Diátaxis Framework Integration

This document defines how the Diátaxis framework applies to this book. Use it to ensure content balance, proper classification, and reader-appropriate structure.

---

## Diátaxis Overview

Diátaxis identifies four types of documentation based on user needs:

| Type | Orientation | User Mode | Purpose |
|------|-------------|-----------|---------|
| **Tutorial** | Learning | Study | Acquire competence through guided experience |
| **How-to** | Task | Work | Accomplish specific goals |
| **Reference** | Information | Work | Look up accurate facts |
| **Explanation** | Understanding | Study | Gain deeper comprehension |

**The Diátaxis map:**

```
                    PRACTICAL (doing)
                          │
         Tutorials        │        How-to Guides
         (learning)       │        (goals)
                          │
   STUDY ─────────────────┼───────────────────── WORK
   (acquisition)          │                (application)
                          │
         Explanation      │        Reference
         (understanding)  │        (information)
                          │
                   THEORETICAL (knowing)
```

---

## Content Classification Rules

**When writing content, identify its primary type:**

| If the content... | It is | Write it as |
|-------------------|-------|-------------|
| Guides the reader step-by-step through a learning experience | Tutorial | Lesson with exercises |
| Helps the reader accomplish a specific task | How-to | Goal-oriented directions |
| Provides technical facts for lookup | Reference | Structured, scannable information |
| Explains concepts, context, or "why" | Explanation | Discursive prose |

**Do not mix types within a section.** If content needs multiple types, separate them.

---

## Book-Level Diátaxis Mapping

### Parts and Primary Types

| Part | Primary Type | Secondary Type | Rationale |
|------|--------------|----------------|-----------|
| Front matter | — | — | Not classified |
| Part 1: Foundation | Explanation | — | Establishes understanding of concepts |
| Part 2: Writing Specifications | Tutorial | How-to | Teaches skills through practice |
| Part 3: The Workflow | How-to | Tutorial | Guides practical application |
| Part 4: Practice | How-to | Explanation | Task-oriented with context |
| Part 5: Governance | Explanation | How-to | Understanding with practical guidance |
| Closing | Explanation | — | Reflection and context |
| Appendices | Reference | How-to | Lookup material with templates |

---

### Chapter Classifications

| Ch | Title | Primary | Secondary | Notes |
|----|-------|---------|-----------|-------|
| 1 | The Fifth Generation | Explanation | — | Context and framing |
| 2 | The Problem with Prompting | Explanation | — | Problem statement |
| 3 | The Core Insight | Explanation | — | Core thesis |
| 4 | Specifications vs. Prompts | Explanation | — | Key distinction |
| 5 | The Five-Layer Model | Explanation | Reference | Mental model + lookup |
| 6 | Anatomy of a Specification | Tutorial | Reference | Learn by building + structure |
| 7 | Defining Context | Tutorial | How-to | Learn skill + apply it |
| 8 | Context Engineering | Explanation | How-to | Concept + application |
| 9 | Writing Requirements | Tutorial | How-to | Skill building |
| 10 | Constraints and Boundaries | Tutorial | How-to | Skill building |
| 11 | Acceptance Criteria | Tutorial | How-to | Skill building |
| 12 | Project Structure for SDD | How-to | Reference | Task + lookup |
| 13 | The Generation Cycle | How-to | Tutorial | Process + learning |
| 14 | Validation and Drift Detection | How-to | Explanation | Task + understanding |
| 15 | Iteration as Spec Refinement | How-to | — | Task-focused |
| 16 | SpecOps | How-to | Reference | Task + lookup |
| 17 | Deterministic CI/CD | How-to | Reference | Task + lookup |
| 18 | When to Use SDD | Explanation | How-to | Decision guidance |
| 19 | Human-in-the-Loop | Explanation | How-to | Concept + application |
| 20 | Failure Modes | Reference | How-to | Lookup + troubleshooting |
| 21 | SDD in Teams | How-to | Explanation | Task + context |
| 22 | Beyond Code Generation | Explanation | How-to | Concepts + application |
| 23 | Governed Evolution | How-to | Explanation | Task + understanding |
| 24 | Generator Trust | Explanation | How-to | Concept + evaluation |
| 25 | Tradeoffs and Costs | Explanation | — | Analysis and context |
| 26 | The Future of Specification | Explanation | — | Reflection |
| App A | Specification Templates | Reference | How-to | Templates + usage |
| App B | Glossary | Reference | — | Pure lookup |
| App C | Quick Reference | Reference | How-to | Cheat sheets |

---

## Writing Rules by Type

### Tutorial Content

**Purpose:** Help reader acquire competence through doing.

**Structure:**

1. State what the reader will learn/build
2. Provide step-by-step instructions
3. Each step produces visible progress
4. End with working result

**Rules:**

- Reader follows along and does things
- Instructor is responsible for success
- Minimize explanation—link to it instead
- Concrete, specific, reproducible
- No decision points—guide completely

**Voice:** "Let's build... First, create... Now add..."

**Do not:**

- Explain why (link to explanation instead)
- Offer choices (make decisions for the reader)
- Cover edge cases (save for how-to)

---

### How-to Content

**Purpose:** Help reader accomplish a specific goal.

**Structure:**

1. State the goal/problem clearly
2. List prerequisites (if any)
3. Provide directions (may branch)
4. Confirm success

**Rules:**

- Assume reader is competent
- Focus on the goal, not learning
- Can include decision points
- Address real-world variations
- Practical, not theoretical

**Voice:** "To achieve X, do Y. If Z, then..."

**Do not:**

- Teach fundamentals (that's tutorials)
- Explain background (link to explanation)
- Include every option (link to reference)

---

### Reference Content

**Purpose:** Provide accurate information for lookup.

**Structure:**

- Consistent format across entries
- Scannable (tables, lists, headings)
- Complete within scope
- No narrative

**Rules:**

- Accurate and precise
- Structured for lookup, not reading
- Describe, don't explain
- Austere—no interpretation

**Voice:** Neutral, factual. "X is Y. Z takes parameters A, B, C."

**Do not:**

- Explain why (that's explanation)
- Provide steps (that's tutorial/how-to)
- Editorialize

---

### Explanation Content

**Purpose:** Help reader understand concepts deeply.

**Structure:**

- Can be discursive/narrative
- Connects ideas
- Provides context and history
- Answers "why" questions

**Rules:**

- Serve understanding, not action
- Can be opinionated (author's perspective)
- Connect to broader context
- Illuminate, don't instruct

**Voice:** Reflective, analytical. "The reason for X is... This matters because..."

**Do not:**

- Provide steps (that's tutorial/how-to)
- Just list facts (that's reference)
- Assume reader will act immediately

---

## Content Balance Checklist

For each major concept, ensure coverage exists:

| Concept | Tutorial | How-to | Reference | Explanation |
|---------|----------|--------|-----------|-------------|
| Specification | Ch 6 | Ch 6 | App A | Ch 3, 4 |
| Bounded context | Ch 7 | Ch 12 | Glossary | Ch 7 |
| Five-layer model | — | — | Ch 5 | Ch 5 |
| Generation | Ch 13 | Ch 13 | Glossary | Ch 3 |
| Validation | Ch 14 | Ch 14, 17 | Ch 20 | Ch 14 |
| Drift detection | — | Ch 14 | Ch 20 | Ch 14 |
| SpecOps | — | Ch 16 | Ch 16 | — |
| Context engineering | — | Ch 8 | Glossary | Ch 8 |

**Gap check:** If a concept has no Tutorial, can the reader learn by doing? If no How-to, can they apply it? If no Reference, can they look it up? If no Explanation, do they understand why?

---

## Chapter Brief Integration

Add Diátaxis fields to chapter briefs:

```markdown
## Diátaxis Classification

**Primary type:** [Tutorial / How-to / Reference / Explanation]
**Secondary type:** [If applicable]

**Content balance:**
- Tutorial elements: [What reader will do/build]
- How-to elements: [What tasks are addressed]
- Reference elements: [What can be looked up]
- Explanation elements: [What is explained/contextualized]

**Links to other types:**
- For deeper explanation, see: [Chapter X]
- For step-by-step tutorial, see: [Chapter Y]
- For reference details, see: [Appendix Z]
```

---

## Section-Level Tagging

Within chapters, tag sections by type:

```markdown
## Understanding Bounded Contexts
<!-- type: explanation -->

A bounded context defines the scope within which...

## Creating Your First Bounded Context
<!-- type: tutorial -->

Let's create a bounded context for a user authentication feature...

## Bounded Context Checklist
<!-- type: reference -->

| Element | Required | Description |
|---------|----------|-------------|
```

This helps validation scripts check for type mixing.

---

## Validation Rules

| Rule | Check |
|------|-------|
| No type mixing | Sections tagged with single type |
| Tutorial completeness | Every tutorial has clear start/end, produces result |
| How-to goal clarity | Every how-to states goal in title or first line |
| Reference structure | Reference sections use consistent format |
| Explanation links | Explanations link to related tutorials/how-tos |
| Concept coverage | Major concepts have all four types somewhere |

---

## Anti-Patterns

**Do not:**

| Anti-pattern | Problem | Fix |
|--------------|---------|-----|
| Tutorial with explanations | Distracts learner | Move explanation to separate section, link |
| How-to that teaches | Patronizes competent user | Assume competence, link to tutorial |
| Reference with opinions | Confuses facts and interpretation | Move opinions to explanation |
| Explanation with steps | Reader expects to understand, not do | Move steps to tutorial/how-to |
| "See also" overload | Fragments attention | One link per need, contextual |

---

## Reader Journey

Diátaxis supports a natural progression:

```
New to SDD                              Experienced with SDD
    │                                           │
    ▼                                           ▼
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│Tutorial │ ──▶│ How-to  │ ──▶│Reference│ ──▶│Explain- │
│         │    │         │    │         │    │ation    │
│"I want  │    │"I want  │    │"I need  │    │"I want  │
│to learn"│    │to do X" │    │to check"│    │to under-│
│         │    │         │    │         │    │stand"   │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
```

**Book supports multiple entry points:**

- New reader: Start Part 1, follow through
- Experienced reader with problem: Jump to Part 3-4 how-tos
- Quick lookup: Appendices
- Deep understanding: Part 1, Part 5

---

## Summary

| When writing... | Ask yourself |
|-----------------|--------------|
| Tutorial | "Is the reader doing something at each step?" |
| How-to | "Does this help accomplish a specific goal?" |
| Reference | "Can someone look this up quickly?" |
| Explanation | "Does this help someone understand?" |

**Default rule:** If unsure, it's probably Explanation. Most writers over-explain. Check if it should actually be one of the other three.
