# The Dark Factory

Two things happened in 2025.

StrongDM shipped production software with three engineers. No standups. No sprints. No Jira. No humans writing code. No humans reviewing code. Agents built the software, tested it, and shipped it. The engineers specified what needed to exist and evaluated whether the output met the specification. Their AI compute bill was a thousand dollars per engineer per day. They considered it a bargain.

Meanwhile, researchers at METR ran a randomised controlled trial. Sixteen experienced developers. Two hundred and forty-six tasks. Their own codebases — repositories with a million lines or more. Frontier AI tools. The result: developers were 19% slower with AI than without. They believed they were 24% faster. Wrong on direction and magnitude.

Same industry. Same year. Same underlying technology.

The gap between those two realities is not a technology gap. Both had access to frontier models. The gap is in how the work was specified and how the execution was structured. One team built the infrastructure to tell machines exactly what to build and exactly how to evaluate the result. The other gave smart people smart tools and told them to go faster.

"The future is already here," William Gibson wrote. "It's just not evenly distributed."

The Dark Factory is the future. Almost nobody operates there yet. Most companies that exist today never will. But the companies that do are the bellwether of a disruption that reshapes the economics of the entire industry. This chapter is about understanding what they see that others don't. The rest of the book is about moving you toward it — not to Level 5, which requires infrastructure most organisations cannot justify, but to Level 3 or 4, where the leverage is real and the path is practical.

## The Five Levels

Dan Shapiro, CEO of Glowforge, published a framework in January 2026 that I have found more diagnostically useful than anything else in the discourse. He calls it the Five Levels of Vibe Coding, modelled on the NHTSA's five levels of driving automation.

**Level 0 — Spicy Autocomplete.** Not a character hits the disk without your approval. You might use AI as a search engine on steroids, but the code is unmistakably yours.

**Level 1 — Coding Intern.** You offload discrete tasks — "write a unit test for this," "add a docstring" — but your job is unchanged. You are still moving at the rate you type.

**Level 2 — Autopilot on the Highway.** You are pairing with the AI. You get into a flow state. You are more productive than you have ever been. Shapiro estimates 90% of self-described "AI-native" developers are here. And here is the danger: Level 2, and every level after it, feels like you are done. You are not done.

**Level 3 — The Manager.** You are the human in the loop. Your coding agent is always running. You spend your days reviewing code. So much code. Your life is diffs. For many people, this feels like things got worse. Almost everyone tops out here.

**Level 4 — The PM.** You write a spec. You argue with the AI about the spec. You plan schedules. You review plans. Then you leave for twelve hours and check to see if the tests pass. Shapiro puts himself here.

**Level 5 — The Dark Factory.** A black box that turns specs into software. Named after the Fanuc robot factory — dark because humans are neither needed nor welcome. A handful of people on the planet operate here.

The diagnostic value is not in the levels themselves. It is in the gap between where teams believe they are and where they actually are. In every engagement I have run in the past year, teams self-assess at least one level higher than their practice. They think Level 3. They are Level 2. That gap is itself diagnostic: if you cannot accurately measure your own AI maturity, you cannot plan where you are going.

The ceiling at Level 3 is not technical. The models are capable of more. The ceiling is psychological. At Level 3, your life is code review — reading diffs all day. To reach Level 4, you have to stop reading the code entirely and trust the specification and the evaluation instead. If you have spent two decades building your career on your ability to read a function and spot the bug, that shift feels like negligence. It is not. But it feels like it, and that feeling is where most teams stall.

## Proof the Future Exists

StrongDM's Dark Factory has been running since July 2024. Three engineers. Fully autonomous. But the interesting part is not the automation — it is two architectural innovations that matter for anyone trying to move up the stack.

First, external scenarios. Traditional tests live inside the codebase. The AI can see them, and — whether by design or optimisation pressure — can build code that passes the tests without exhibiting the intended behaviour. Same problem as teaching to the test. StrongDM moved evaluation outside the codebase entirely. The agent never sees the success criteria. It cannot game them. Same principle as a holdout set in machine learning.

Second, digital twins. StrongDM integrates with dozens of external services — Okta, Jira, Slack, Google Drive. You cannot let an autonomous agent make authenticated calls to production APIs during development. So they built behavioural clones of every service. The agents develop against simulated environments that behave like reality but touch no real data. Safe autonomous execution at speed.

Both innovations — external evaluation and simulated environments — are directly relevant to the methodology in this book and will recur throughout it.

The hyperscaler evidence confirms the trajectory. Boris Cherny, who leads Claude Code at Anthropic, reported in May 2025 that roughly 80% of Claude Code was written by Claude Code. By October, Dario Amodei told Marc Benioff the number was above 90%. On March 7, 2026, Cherny posted publicly: "Can confirm Claude Code is 100% written by Claude Code." Eighty to one hundred percent in ten months. OpenAI's Codex 5.3 was reportedly built by Codex itself. The recursive loop is closed.

If the people who build the models are running their own development this way, the question is not whether this way of working is viable. The question is what is stopping you. In most cases the answer is the same: specification quality and execution infrastructure.

## Why Most Organisations Are Stuck

DORA — the largest annual study of software delivery performance, surveying over 39,000 professionals — found in 2024 that every 25% increase in AI adoption correlated with a 1.5% drop in delivery throughput and a 7.2% drop in stability. The DORA team called this a J-curve.

The dip is real. Evaluating AI suggestions takes time. Correcting "almost right" code — the output that compiles, passes obvious tests, but hides a subtle defect — can take longer than writing it from scratch. And 39% of developers reported low or zero trust in AI-generated code, creating a cycle: you don't trust the AI, so you review everything manually, which makes AI-assisted work slower, which confirms the distrust.

The METR study puts the sharpest point on it. Experienced developers. Their own codebases. Frontier tools. Nineteen percent slower. And they could not feel the slowdown — their subjective experience was the opposite of the measured reality. If you cannot trust your own perception of whether a tool is helping, you need external measurement. Which is to say, you need the evaluation infrastructure most organisations have not built.

Most leadership teams interpret the J-curve dip as evidence that AI does not work. They cut investment or slow adoption precisely when they should push through. The J-curve is the mechanism by which a specification gap becomes a competitive gap. By the time the first group realises what happened, the distance will be very hard to close.

## Where the Bottleneck Has Moved

For fifty years, the bottleneck in software production was implementation. We did not have enough developers. They were expensive. Development took too long. Every methodology in the history of software engineering — waterfall, agile, DevOps, SAFe — was fundamentally an attempt to make implementation faster, cheaper, or more predictable.

That bottleneck has moved. Implementation is becoming cheap. The models can write code. They can write a lot of it. They can write it fast. And they are improving at a pace that means whatever limits you hit today will be less limiting in six months.

The new bottleneck is in two places. First, specification quality — the ability to describe what needs to exist precisely enough that a machine can build it without a human filling gaps. A specification that works for a human developer, who can ask questions and use judgment to resolve ambiguity, does not work for an AI agent. The agent will do what you say. If what you said was imprecise, the output will be precisely wrong.

Second, AI-native execution — the pipelines, the agent workflows, the evaluation systems, the deployment gates. The machinery that turns a specification into running software and validates the result. This is the engineering discipline that sits between the spec and the ship. It is emerging now and has no established playbook.

The structural consequences are already visible. Junior developer job postings in the US have fallen 67%. The entry-level work — boilerplate, simple bugs, small features — got automated first. The ramp that turned juniors into seniors is disappearing. AI-native startups are generating $2–3 million in revenue per employee, four times the SaaS benchmark. The economics have shifted. The org charts have flattened. The companies that understand specification and evaluation are pulling away.

## What This Book Is For

Here is what I want to be direct about. You do not need to be StrongDM. You do not need a Dark Factory. Level 5 requires infrastructure, investment, and architectural commitment that most organisations cannot and should not attempt today.

But Level 3 is achievable. Level 4 is achievable for teams willing to invest in specification discipline and evaluation infrastructure. And the difference between Level 2 — where most teams are stuck — and Level 3 or 4 is not a technology upgrade. It is a change in how you think about the work. What you specify. How you evaluate. Where you place your trust.

The first part of this book introduces the ideas and concepts that define Specification Driven Development. This is an emerging discipline, still in flux — the field is moving fast and the practices are evolving in real time. What you will find here is not a finished canon but a working framework: the clearest articulation of where the thinking is now, grounded in practice rather than theory.

The second part addresses the harder problem — the organisational one. The mindset shift required to migrate to an AI-native way of working. The structural changes: flattened hierarchies, the collapse of siloed roles, the emergence of multidisciplinary practitioners who combine product thinking with engineering judgment. The evolution of roles like "Product Owner as Engineer" — people who specify and evaluate rather than manage and delegate. Technology is the easier part of this transition. Culture is where it gets difficult.

The methodology that runs through both parts holds them together. The Five Artefact taxonomy — spec, code, provenance, scenarios, and tests — gives you a structure for specification quality. The builder-tester agent separation gives you a model for execution. The provenance chain gives you traceability. These are not abstractions. They are the operating system for the organisational changes the second part describes — the concrete practices that make flatter teams and autonomous agents work in reality, not just on a slide.

The cost of building software is dropping by an order of magnitude. Every time that has happened before — mainframes to PCs, PCs to the web, the web to cloud — the total volume of software in the world exploded. Cloud did not make existing software cheaper. It created SaaS, mobile, streaming, and industries that could not exist before. We are at the start of the same dynamic, applied to software production itself.

The question is no longer "can we build it." For an expanding range of problems, the answer is yes. The question is "can we specify it well enough to get it right." That has always been the harder question. We just could not see it when implementation was in the way.

Let's begin.
