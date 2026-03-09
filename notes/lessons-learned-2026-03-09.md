# Lessons Learned — Dark Factory Collateral Build
**Date:** 2026-03-09
**Session type:** Collateral build + positioning strategy
**Scope:** Webinar deck, session page, LinkedIn posts, capabilities rewrite, contact copy

---

## Context

Two-day session building the full collateral set for *The Dark Factory* — a presentation/webinar on the gap between AI-native software teams and everyone else. Source material was Nate Jones' YouTube video covering StrongDM, Anthropic/Boris Cherny, Dan Shapiro's Five Levels of Vibe Coding, and the METR 2025 RCT. The session produced a 20-slide deck, a session brief page, LinkedIn post series, and repositioned the kevinryan.io site copy.

These notes are written primarily as research input for *Spec Driven Development*.

---

## 1. SVG/HTML over PowerPoint for AI-generated presentation decks

**What happened:** Started with a PPTX deck built with pptxgenjs. Font rendering was broken in LibreOffice PDF export. Layouts needed a polish pass. Decided mid-session to rebuild as a single self-contained HTML file with inline SVGs.

**What we learned:** For AI-assisted deck production, HTML/SVG is a fundamentally better medium than PPTX. The reasons:

- **Pixel-perfect rendering** — fonts, spacing, and layouts render identically in every browser. No LibreOffice font substitution, no layout drift.
- **Infinite scalability** — a CSS `scale()` transform on a fixed 1280×720 canvas produces perfect results at any screen size.
- **Single file** — one `.html` file contains the entire deck: all 20 slides, all styles, all navigation JavaScript, all fonts (via Google Fonts import). Trivially shareable, trivially deployable as a static route.
- **AI specifiability** — this is the SDD insight. HTML/SVG is dramatically easier to specify precisely than PPTX. You can describe exactly what you want ("position this element at left:64px, top:88px, font-size:178px") and the AI produces it correctly. PPTX via pptxgenjs requires translating spatial intent into an abstract API that doesn't map naturally to visual description. The prompt is cleaner, the output is more accurate.
- **Ease of iteration** — `str_replace` on an HTML file is surgical. Changing one label, one colour, one heading is a single targeted edit. With PPTX you're re-running the entire generation script.
- **Print to PDF** — Chrome's print-to-PDF from a browser produces pixel-perfect output from the HTML deck. No intermediate tool needed.

**SDD implication:** The choice of output format is part of the specification architecture. Formats that map cleanly to natural language description (HTML, SVG, Markdown) produce better AI-assisted outputs than formats that require API abstraction layers (PPTX, DOCX). *Ease of specification should be a first-class criterion when choosing output formats for AI-assisted content production.*

---

## 2. "Developer as PM" is ambiguous — precision in framework labels matters

**What happened:** Slide 7 used "Developer as PM" for Level 4 of Dan Shapiro's Five Levels. During review, the question arose: Product Manager or Project Manager?

**What we learned:** The answer is unambiguously Product Manager — the level describes a developer who writes a spec, leaves, and returns to evaluate outcomes rather than reading code. That is product ownership, not project coordination. Project management (timelines, dependencies, coordination) is precisely the work that gets *eliminated* as teams move up the levels.

The resolution was to rename Level 4 **"Developer as Product Owner"** — a more precise term that most engineering audiences already understand from Scrum, and that makes the role collapse explicit.

**SDD implication:** Framework labels are specifications. Ambiguous labels produce ambiguous mental models in readers, which produce ambiguous behaviour in teams. The discipline of naming — choosing the most precise, least ambiguous term — is part of spec quality. *A spec that uses "PM" when it means "Product Owner" will generate the wrong mental model in every AI agent and human reader downstream.*

---

## 3. Slide title "Where It Gets Spicy" conflicted with Level 0 "Spicy Autocomplete"

**What happened:** Slide 7 — covering Levels 4 and 5 — was titled "Where It Gets Spicy." The word "spicy" also appears in Level 0: "Spicy Autocomplete." This created cognitive interference — the title pulled the audience back to the bottom of the ladder at precisely the moment they should be focused on the top.

**Resolution:** Renamed to **"Beyond the Ceiling"** — a direct callback to the preceding slide's payoff line ("most developers hit the ceiling right here") that points forward rather than backwards.

**SDD implication:** Specifications exist in context. A term that is precise in isolation may be imprecise when the surrounding context introduces a collision. *Spec review should include a pass for cross-reference coherence — checking that terms used in one part of the spec don't collide with terms established elsewhere.*

---

## 4. The consulting funnel is Talk → Assess → Embed, not the reverse

**What happened:** Building slide 20 ("how I can help"), the initial instinct was to order the engagement model as Assess → Embed → Talk. During review, this was immediately identified as backwards.

**What we learned:** In consulting sales, you never lead with the work. Talk is always the entry point — a low-friction, low-commitment first step. Assess is the diagnostic that follows. Embed is the outcome of a successful assessment. The correct order is:

1. **Talk** — one conversation, no pitch, figure out whether there's a fit
2. **Assess** — structured diagnostic of where the org sits
3. **Embed** — we come in and make it work

The order is a funnel, not a menu. Each step qualifies for the next.

**SDD implication:** Sequence is a form of specification. The order in which steps are presented is not neutral — it implies a process model. *When specifying a workflow or user journey, the sequence of steps is itself a design decision that encodes assumptions about how users and clients actually move through a process.*

---

## 5. "We" vs "I" — deliberate positioning choice with real consequences

**What happened:** Multiple points in the session where copy defaulted to "we" — "where we operate", "we come in, we make it work." This was challenged during capabilities section review.

**What we learned:** Kevin Ryan & Associates is deliberately personal. The "Associates" signals room to grow and access to a network without pretending to be a large consultancy. "We" in the section header would be a false signal at this stage. "I" in the header, "we" in the card body (implying client + consultant collaboration) is the right balance.

**The deliberate choice:** Use "I" for first-person positioning (bio, capabilities header, contact copy). Use "we" in engagement language where it means "you and I together" or in the FDE card where "we come in" signals a professional practice rather than a solo contractor.

**SDD implication:** Pronoun choice is a specification. "I" and "we" encode different organisational models. *Consistency in voice and person is a form of spec coherence — inconsistencies create reader uncertainty about who they are dealing with.*

---

## 6. The session page and the event page are different assets for different audiences

**What happened:** The first version of the webinar landing page was built as a consumer event registration page — "Save Your Seat", email capture form, registration CTA. This was wrong for the intended use case: pitching the talk to organisers and partners (e.g. Efficode) before a date exists.

**What we learned:** Two distinct assets are needed:

- **Session brief** (`/dark-factory`) — a B2B pitch page for organisers. Who it's for, key learnings, session structure, format requirements, presenter credentials, "interested in hosting this?" CTA. The reader is an organiser evaluating the talk for their audience.
- **Event page** — built later, once a date and organiser are confirmed. Audience registration, date/time, specific venue or platform.

The session brief does the work of a speaker one-sheet. The distinction is: the session brief helps you *get* the gig. The event page helps you *fill* the gig.

**SDD implication:** The same content serves different purposes for different audiences. *Specs should identify the primary reader explicitly — the same information organised for an organiser and organised for an attendee produces two different documents. Conflating the audience produces a document that serves neither.*

---

## 7. HTML/SVG decks are deployable as static routes — closing the content-to-platform loop

**What happened:** The Dark Factory deck is a single HTML file. The natural deployment is as a static route in the Next.js monorepo: `sites/kevinryan-io/app/dark-factory/deck/page.tsx`. The session brief lives at `sites/kevinryan-io/app/dark-factory/page.tsx`. Both are self-contained HTML files rendered as Next.js pages.

**What we learned:** The content production workflow (Claude → HTML file) and the deployment workflow (Next.js static route) compose cleanly. The deck is:
- Produced in one session
- Deployable as a URL (`kevinryan.io/dark-factory/deck`)
- Linkable from the session brief
- Shareable as a credibility signal when pitching to organisers
- Printable to PDF from Chrome for leave-behind use

This closes a loop that usually requires multiple tools: deck design software → export → hosting platform → embed. The HTML approach collapses it to: specification → AI output → static route.

**SDD implication:** *The specification, the artefact, and the deployment target should be considered together. When the output format (HTML) is chosen with the deployment target (static web route) in mind, the entire production workflow simplifies. This is the practical expression of "ease of specification as architectural principle."*

---

## 8. The bottleneck is spec quality AND execution — not one or the other

**What happened:** Slide 17 and slide 20 both referenced "the bottleneck has moved to spec quality." During review of slide 20's headline, this was challenged as incomplete.

**What we learned:** At Level 5 (dark factory), execution is solved — spec goes in, software comes out. But for organisations in transition (which is everyone the Dark Factory talk is actually aimed at), the bottleneck is two things:

- **Spec quality** — the ability to describe what needs to exist with enough precision that AI agents can build it without humans filling gaps
- **AI-native execution** — running the pipelines, structuring CI/CD, managing agent workflows, validating outputs at scale

These map directly to the two core service offerings:
- **Assess** → diagnoses the spec quality gap
- **Embed** → resolves the AI-native execution gap

**SDD implication:** *The bottleneck analysis is a core tool in spec-driven development. Identifying that the bottleneck is not one thing but two — and that they require different interventions — is the kind of precision that distinguishes a specification from a description. Vague problem statements produce vague solutions.*

---

## 9. The Five Levels framework as a diagnostic instrument

**What happened:** Dan Shapiro's Five Levels of Vibe Coding (L0–L5) was the central framework for the talk. During the collateral build, it became clear the framework does more work than Shapiro's original framing suggests.

**Emergent insight:** The Five Levels are not just a description of how AI coding operates. They are a **diagnostic instrument** for organisations — a way to establish current state, identify the ceiling, and design a transition path. Most teams operate at L2 believing they are at L3 or L4. The gap between perceived level and actual level is itself diagnostic information.

The framework also maps to org structure implications:
- **L0–L2** — individual developer productivity tool; org structure unchanged
- **L3** — team workflow changes; psychological barrier is the bottleneck
- **L4** — spec quality becomes the constraint; PM/PO role collapses into developer
- **L5** — org structure, team size, and economics are all disrupted

**SDD implication:** *Maturity frameworks are specifications of a transition path. The most useful maturity frameworks do three things: establish current state, identify the next level, and describe what changes at each transition. The Five Levels do all three. This structure should inform how SDD presents its own maturity model for specification practice.*

---

## 10. Breaking news as live content — keeping decks current in a fast-moving field

**What happened:** Boris Cherny's March 7 2026 X post — "Can confirm Claude Code is 100% written by Claude Code" — broke during the build session. The deck at that point said "converging on 100%." This was updated immediately to reflect the confirmed state.

**What we learned:** In a field moving this fast, content has a shelf life measured in weeks. The Anthropic/Claude Code timeline went from "80%" (May 2025) to "90%+" (October 2025) to "70-90% company-wide" (January 2026) to "100% confirmed" (March 2026) in ten months. A deck built in January 2026 using "90%" is already out of date by March.

The HTML format helps here — updating a single number in a static file and redeploying is a two-minute operation. Updating a PPTX, re-exporting, and redistributing takes considerably longer.

**SDD implication:** *Specifications have a freshness dimension. In fast-moving domains, a spec that was accurate six months ago may now produce the wrong output. Spec-driven development in AI contexts requires a maintenance model — not just for code, but for the specifications themselves. Living documents, versioned, with a review cadence.*

---

## Summary for SDD book research

The session produced ten discrete lessons. The ones with the highest value for the SDD book:

| # | Lesson | SDD Chapter relevance |
|---|--------|----------------------|
| 1 | HTML/SVG > PPTX for AI-generated content | Ease of specification as architectural principle |
| 2 | Ambiguous framework labels | Precision in specification language |
| 3 | Cross-reference coherence in spec | Spec review methodology |
| 4 | Funnel sequence is a specification | Workflow and sequence design |
| 6 | Audience identification changes the document | Spec audience analysis |
| 7 | Format × deployment × spec compose cleanly | AI-native production workflow |
| 8 | Bottleneck analysis precision | Problem statement specification |
| 9 | Maturity frameworks as diagnostic specs | Specification maturity models |
| 10 | Spec freshness in fast-moving domains | Living specifications and maintenance |

---

*Document produced: 2026-03-09. Session with Claude (claude.ai). For SDD book research archive.*
