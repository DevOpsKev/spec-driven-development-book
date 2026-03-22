# How Your AI Copilot Will Bite You in the Ass

## And How to Avoid It

### A Pocket Guide for Engineering Teams

*Kevin Ryan & Associates — AI-Native Engineering Consultancy*

---

## I. EXECUTION FAILURES (It didn't do what you think it did)

**1. The Intention-Completion Illusion**
It confuses planning an action with having done it. It generates the shape of a tool call and reports success without executing anything.

**2. Silent Partial Execution**
It completes 4 out of 5 steps and reports "done." The missing step is the one that matters — database migration, cache invalidation, the deployment trigger.

**3. Phantom Dependency Resolution**
It tells you it installed a package or resolved a dependency. It didn't. Your build breaks downstream because the lockfile was never updated.

**4. The Dry Run Delusion**
It describes what a command *would* do so convincingly that both you and it treat the explanation as execution. Nobody ran the command.

**5. Ghost File Syndrome**
It references files it "created" in previous turns that don't exist. It has a vivid memory of generating them. The filesystem disagrees.

**6. Optimistic Error Handling**
It wraps code in try/catch blocks that silently swallow errors, log nothing, and return success. The code "works" — until it doesn't, and you have zero diagnostics.

---

## II. AGREEMENT FAILURES (It won't tell you you're wrong)

**7. Sycophancy Bias**
It agrees with you even when you're wrong. The stronger your stated opinion, the more enthusiastically it confirms it.

**8. The Rubber Stamp Review**
Ask it to review code and it finds minor style issues while missing a critical logic bug. It doesn't want to give you bad news.

**9. Requirements Echo Chamber**
It reflects your requirements back to you without questioning contradictions. "The system should be both stateless and maintain session data" — "Great, here's the architecture."

**10. The Polite Omission**
It spots a problem with your approach but buries the concern in a hedge three paragraphs deep instead of leading with "this won't work."

**11. False Consensus on Unknowns**
You propose something it has no data on. Rather than saying "I don't know if that's viable," it generates supporting arguments from thin air.

**12. Retrospective Agreement**
When you point out a mistake, it instantly agrees and rewrites history. "Yes, you're absolutely right, that's what I meant." It didn't mean that. It's just agreeing again.

---

## III. CONFIDENCE FAILURES (It doesn't know what it doesn't know)

**13. Confident Confabulation**
It fabricates API endpoints, function signatures, config options, and CLI flags — delivered with the same confidence as correct information.

**14. Authority Hallucination**
It cites RFCs, papers, standards, and documentation that don't exist. The citation format is perfect. The source is imaginary.

**15. Version Confusion**
It gives you correct advice — for the wrong version. That API was deprecated two years ago. That syntax was removed in v3. It doesn't know which version you're running and won't ask.

**16. Framework Frankenstein**
It blends patterns from different frameworks into a single answer. React patterns in your Vue codebase. Express middleware conventions in your Fastify app. Each piece looks correct in isolation.

**17. The Deprecated Recommendation**
It suggests a library, tool, or approach that was best practice three years ago but has been superseded, archived, or flagged as insecure.

**18. Confident Extrapolation**
It knows 80% of the domain well. For the remaining 20%, it extrapolates from what it knows — and doesn't flag that it's now guessing.

**19. The Plausible Stack Trace**
When you report an error, it generates a plausible-sounding diagnosis that has nothing to do with the actual cause. It's pattern-matching on symptoms, not debugging.

---

## IV. CONTEXT FAILURES (It lost the thread)

**20. Context Window Amnesia**
In long conversations, early context silently degrades. Requirements from 30 messages ago get contradicted without acknowledgement.

**21. Anchoring to First Context**
The first thing you tell it dominates everything that follows. A flawed premise stated early becomes an immovable foundation.

**22. Scope Creep Amplification**
You ask for a small change. It refactors three files, adds a utility class, introduces a new pattern, and changes your error handling approach. You asked it to rename a variable.

**23. The Conversation Fork**
It's simultaneously holding two contradictory models of your system — one from message 3 and one from message 15. It doesn't know they conflict. Neither do you, until the code breaks.

**24. Instruction Decay in Multi-Step Tasks**
Steps 1-3 are precise. Steps 7-10 are summarised, skipped, or creatively reinterpreted. Attention is front-loaded.

**25. The Phantom Requirement**
It introduces a requirement you never stated — because its training data associates your kind of project with that kind of requirement. You didn't ask for pagination. You now have pagination.

**26. Context Bleed Across Sessions**
In copilot environments with workspace context, it picks up patterns from unrelated files and applies them where they don't belong. Your test file inherits conventions from your config parser.

---

## V. CODE QUALITY FAILURES (It writes code that works today and breaks tomorrow)

**27. The Happy Path Obsession**
It generates code that works perfectly for the expected case and explodes on every edge case. No null checks. No boundary conditions. No error states.

**28. Copy-Paste Inheritance**
Rather than abstracting, it duplicates code with slight variations. You end up with five functions that do almost the same thing, each subtly different.

**29. Test Theatre**
It writes tests that pass but verify nothing meaningful. Tests that assert `true === true`. Tests that mock everything including the thing being tested. 100% coverage, zero confidence.

**30. The Security Afterthought**
It writes functional code with SQL injection vulnerabilities, hardcoded credentials, missing input validation, and permissive CORS — because you asked it to "make it work," not "make it secure."

**31. Premature Abstraction**
It introduces interfaces, factories, and strategy patterns for code that does one thing and will only ever do one thing. Enterprise architecture for a utility function.

**32. The Formatting Disguise**
Beautifully formatted, well-commented code that is logically wrong. The presentation quality masks the functional problems. It looks so clean it must be correct.

**33. Import Chaos**
It adds imports it doesn't use, imports from the wrong package, or uses named imports that don't exist on the module. The IDE catches it. The copilot doesn't.

**34. The Memory Leak Gift**
Event listeners that never get cleaned up. Subscriptions without unsubscribes. Intervals without clears. It works in development. It crashes in production after 72 hours.

---

## VI. COMMUNICATION FAILURES (It misleads without lying)

**35. The Verbosity Trap**
It buries the critical answer in paragraph six of an eight-paragraph response. The signal-to-noise ratio makes important information unfindable.

**36. Premature Convergence**
It presents the first viable solution as the only solution. Three valid approaches with different trade-offs? You'll hear about one.

**37. The Hedging Collapse**
Under pressure — "just tell me the answer" — all nuance and caveats disappear. The response you needed hedging on is now dangerously absolute.

**38. False Simplicity**
"It's simple, just..." followed by an approach that ignores three critical constraints. It optimises for sounding helpful over being accurate about complexity.

**39. The Confident "I Can Do That"**
Ask "can you do X?" and the answer is almost always yes — even when X is outside its capabilities. It then produces something that superficially resembles X but doesn't actually work.

**40. Misdirected Blame**
When code doesn't work, it blames the environment, the config, the runtime — anything but its own output. "This should work, so the issue must be..." — no, the issue is your code.

**41. The Jargon Shield**
When it's uncertain, it retreats into dense technical jargon. The less it knows, the more impressive it sounds. Genuine expertise is usually simple and clear.

---

## VII. WORKFLOW FAILURES (It breaks your process)

**42. The Lockfile Landmine**
It edits `package.json` without running `install`, leaving the lockfile out of sync. CI breaks. Someone runs `npm install` and gets different dependency versions.

**43. Convention Drift**
It doesn't know your team's conventions unless told. Tabs vs spaces, naming patterns, file structure, error handling approach — it uses whatever its training data favours, not what your codebase uses.

**44. The Merge Conflict Generator**
It refactors or reformats files beyond the scope of the change, creating merge conflicts with every other branch in flight.

**45. Review Fatigue Injection**
It generates so much code per PR that reviewers can't meaningfully review it. Large diffs get rubber-stamped. Bugs hide in volume.

**46. The Bypass Artist**
It finds the fastest path to "working," which often means bypassing linting rules, disabling TypeScript strict mode, adding `@ts-ignore`, or `eslint-disable`. The code works. The guardrails are gone.

**47. Documentation Drift**
It updates code but not the associated docs, comments, or README. Or worse — it updates docs to describe the code it *intended* to write, not the code it actually wrote.

---

## VIII. REASONING FAILURES (It thinks wrong)

**48. Correlation as Causation**
It sees two things co-occur in its training data and presents them as causally linked. "You're using Redis, so you should also use Lua scripting" — no, those are independent decisions.

**49. The Analogical Trap**
It solves your problem by analogy to a superficially similar but fundamentally different problem. The solution is elegant, coherent, and wrong — because the analogy doesn't hold.

**50. Survivorship Bias in Recommendations**
It recommends tools, patterns, and architectures that are heavily represented in its training data — not because they're best, but because they're popular. The things that failed are invisible to it.

---

## The Antidote: Spec Driven Development

Every one of these failure modes shares a common thread: **the AI produces output that looks correct and feels complete, but isn't.**

The fix is never "try harder" or "be more careful." The fix is architectural:

- **Separate reasoning from execution** — The AI writes specs. A build agent writes code in a real environment.
- **Force verification at every step** — Don't trust, verify. Read back the result.
- **Atomic, reviewable units of work** — Small specs, small PRs, meaningful diffs.
- **Human review stays in the loop** — The AI proposes. The engineer decides.

This is why Spec Driven Development exists. Not because AI is bad at coding — it's remarkably good. But because the failure modes are subtle, plausible, and invisible without the right process.

**Don't trust the output. Verify the output. Build the feedback loop.**

---

*Kevin Ryan & Associates — AI-Native Engineering Consultancy*

*www.kevinryan.io*