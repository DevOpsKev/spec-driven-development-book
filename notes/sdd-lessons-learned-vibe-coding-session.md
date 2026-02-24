---
title: "SDD Lessons Learned: Vibe Coding a Knowledge Base"
category: "projects"
date: "2026-02-24"
tags: ["sdd", "vibe-coding", "lessons-learned", "auth0", "astro"]
description: "Real-world evidence for Spec Driven Development methodology captured during a single-day vibe coding session building a searchable, authenticated knowledge base"
---

## Context

On 24 February 2026, a full development session was conducted using conversational prompting with AI coding agents (Claude and Claude Code) to build a private, searchable, authenticated knowledge base. The stack: Astro, Pagefind, Auth0 with GitHub login, GitHub Pages, GitHub Actions CI/CD, Husky pre-commit hooks.

The session was deliberately run as "vibe coding" — conversational, iterative, minimal upfront specification. The result was functional but the journey exposed exactly the patterns that Spec Driven Development exists to address.

This document captures the SDD-relevant lessons, not the technical outcomes.

## The Core Pattern: Every Gap Became a Guess

Every prompt issued during the session contained at least one ambiguity that the AI agent resolved by guessing. Some guesses were correct. Many were not. Each incorrect guess required a correction cycle — inspect the output, identify the deviation, write a new prompt, wait for execution, verify again.

In a low-stakes internal project with a single stakeholder, this is tolerable. In an enterprise engagement with multiple teams, production deadlines, and real budget exposure, these cycles are where cost and risk accumulate.

**SDD principle confirmed: "The bug is always a gap in the spec."**

## Lesson 1: Undefined Environment Boundaries

**What happened:** The GitHub Actions workflow used `vars.PUBLIC_AUTH0_*` to inject environment variables at build time. The variables were set as repository variables. The build job lacked `environment: github-pages`, meaning the variables were scoped to an environment the build job couldn't access. The Auth0 domain and client ID were empty in the deployed site, producing a redirect to a nonexistent `authorize` host.

**The spec gap:** The prompt said "use environment variables" and "deploy via GitHub Actions" but never specified the relationship between GitHub's environment scoping and the workflow job configuration. The agent guessed — incorrectly — that repository variables would be accessible without an environment declaration.

**SDD takeaway:** When a spec references configuration, it must define the configuration boundary: where values are stored, which execution contexts can access them, and how they flow from storage to consumption. "Use environment variables" is not a spec. "Store values as GitHub repository variables scoped to the github-pages environment, accessible to any job declaring that environment" is a spec.

## Lesson 2: Exact String Matching in External Systems

**What happened:** Auth0 returned a "Callback URL mismatch" error. The application was sending `https://devopskev.github.io/professional-hq/callback/` (with trailing slash). Auth0 had `https://devopskev.github.io/professional-hq/callback` configured (without trailing slash). Auth0 requires exact string matches.

**The spec gap:** The prompt specified a callback URL but did not specify whether it should include a trailing slash, nor did it mandate that the configured URL must exactly match what the application sends. The agent produced code that appended a slash; the human configured Auth0 without one.

**SDD takeaway:** When a spec involves string values consumed by external systems, the spec must define the exact string — not a description of the string. Trailing slashes, case sensitivity, URL encoding, and protocol prefixes are all specification-level concerns, not implementation details. External system contracts are zero-tolerance.

## Lesson 3: API Surface Assumptions

**What happened:** The Auth0 post-login Action used `event.user.identities[].profileData.nickname` to check the GitHub username. At the post-login execution stage, `profileData` is undefined. The correct property is `event.user.nickname`. Every login attempt failed with "Cannot read properties of undefined (reading 'nickname')".

**The spec gap:** The prompt said "check the GitHub username" but did not specify which Auth0 event property to use. The agent guessed the wrong property path based on general Auth0 documentation rather than the specific execution context of a post-login Action.

**SDD takeaway:** When a spec references an external API, it must specify the exact data path, not the intent. "Check the GitHub username" is a requirement. "Read `event.user.nickname` in the post-login Action context" is a spec. The distinction matters because APIs frequently expose the same conceptual data at different paths depending on execution context, version, and provider configuration.

## Lesson 4: Scope Creep Through Ambiguity

**What happened:** A prompt requesting "targeted changes" to the existing theme — search box fix, button colour change, footer link, typography update, background palette — resulted in 1,446 lines of added code. The agent interpreted "iterate on the existing theme" as license to refactor broadly, touching files well beyond the scope of the requested changes.

**The spec gap:** "Iterate on the existing theme — do not redo what's already been done" is a natural language instruction with no enforceable boundary. There was no file-level scope constraint, no line budget, and no explicit list of files that should and should not be modified.

**SDD takeaway:** A spec must define scope boundaries that are machine-verifiable, not just human-interpretable. "Only modify files in `src/styles/` and `src/components/`" is enforceable. "Make targeted changes" is not. For AI agents in particular, the absence of a constraint is interpreted as permission. The silence gets filled with guesses — and at scale, those guesses compound into uncontrolled output.

**SDD principle confirmed: "Filling silence with guesses."**

## Lesson 5: Configuration Drift Between Environments

**What happened:** The Astro config set `base: '/professional-hq/'` for GitHub Pages deployment. In local development (Codespace), this caused the dev server to serve from `/professional-hq/` instead of `/`. A conditional base path was needed: `process.env.CI ? '/professional-hq/' : '/'`.

**The spec gap:** The prompt specified GitHub Pages deployment with a base path but did not address the local development experience. The agent optimised for the deployment target and left the development environment broken.

**SDD takeaway:** A spec must define behaviour per environment. If a value differs between development and production, both values must be specified along with the selection mechanism. "Deploy to GitHub Pages with base path /professional-hq/" is a production spec. It is not a development spec.

## Lesson 6: Static Sites Cannot Authenticate

**What happened:** The initial plan assumed GitHub Pages (private repo, GitHub Pro) would restrict site access. Investigation revealed that private GitHub Pages is now an Enterprise-only feature. The site would be publicly accessible. Multiple alternative approaches were evaluated (Cloudflare Access, Azure Static Web Apps, Auth0 client-side auth) before settling on Auth0 SPA SDK with client-side authentication.

**The spec gap:** The original prompt stated "this is a PRIVATE repo — the GitHub Pages site should only be accessible to me" without verifying that this was technically possible on the current GitHub plan. The constraint was stated as a requirement but never validated against platform capabilities.

**SDD takeaway:** A spec must distinguish between requirements and assumptions. "Only I can access this site" is a requirement. "GitHub Pages on Pro supports private sites" is an assumption. Assumptions must be validated before they become spec. When an assumption fails late in the process, the remediation cost includes all the work built on top of it.

## Lesson 7: Search Only Works Post-Build

**What happened:** Pagefind search returned a 404 in development mode because Pagefind indexes the compiled HTML output at build time. It does not exist during `astro dev`. This was a known Pagefind behaviour but was not communicated in the original prompt or README.

**The spec gap:** The prompt specified "Pagefind search" and "dev server with hot reload" as parallel features but did not specify that search would be unavailable in dev mode. The implicit assumption was that all features work in all modes.

**SDD takeaway:** When a spec defines features, it must also define feature availability per mode. If a feature has a build-time dependency, the spec must state this and define the expected developer workflow for testing it.

## Meta-Lesson: The Economics of Guess-and-Correct

Across the full session, at least seven distinct guess-and-correct cycles occurred. Each cycle followed the same pattern:

1. Prompt issued with implicit assumptions
2. Agent produces output based on those assumptions
3. Output tested and found incorrect
4. Root cause identified (usually an assumption mismatch)
5. Corrective prompt issued
6. Agent produces corrected output
7. Retested and verified

Each cycle cost between 5 and 20 minutes of human attention plus agent compute time. On a low-stakes personal project, the total cost was acceptable — perhaps 90 minutes of overhead across a productive day.

Scale this to an enterprise engagement:

- Multiple agents working in parallel
- Multiple teams consuming the outputs
- Production systems depending on correctness
- Regulatory or contractual consequences for defects

At enterprise scale, the guess-and-correct pattern does not degrade linearly — it compounds. Agent A's guess becomes Agent B's input. Agent B's guess becomes the test fixture. The test fixture validates the wrong behaviour. The wrong behaviour ships to production.

**SDD exists to break this chain at the source: the spec.**

## Applicability to the SDD Book

This session provides concrete, first-person evidence for several core SDD arguments:

- **Chapter on spec quality and agent cost:** The direct relationship between prompt precision and iteration count is quantifiable from this session. Seven spec gaps produced seven correction cycles.
- **Chapter on "filling silence with guesses":** The 1,446-line theme commit is a textbook example. The agent had permission (silence) and produced volume. The spec needed constraints.
- **Chapter on external system contracts:** The Auth0 callback URL and API property path failures demonstrate that external integrations are the highest-risk area for underspecification.
- **Chapter on environment-aware specs:** The base path and env var scoping failures show that specs must be environment-explicit, not environment-implied.

## Summary

Vibe coding works when:

- The stakes are low
- The stakeholder is the developer
- Iteration is cheap
- The system is small enough to hold in one person's head

Vibe coding fails when:

- The stakes are high
- Multiple stakeholders depend on the output
- Iteration is expensive (time, compute, coordination)
- The system exceeds one person's cognitive span

SDD is the methodology that bridges the gap. Not by eliminating iteration — iteration is valuable — but by ensuring that iteration addresses genuine design questions rather than correcting preventable guesses.

**The bug is always a gap in the spec. Today we proved it seven times.**
