---
title: "Lecture 06. Make the Agent Initialize Before Every Work Session"
source: "https://walkinglabs.github.io/learn-harness-engineering/en/lectures/lecture-06-why-initialization-needs-its-own-phase/"
author:
published:
created: 2026-05-24
description: "A project-based course on designing the environments, state, verification, and control systems that make Codex and Claude Code reliable."
tags:
  - "clippings"
---
[中文版 →](https://walkinglabs.github.io/learn-harness-engineering/zh/lectures/lecture-06-why-initialization-needs-its-own-phase/)

> Code examples: [code/](https://github.com/walkinglabs/learn-harness-engineering/blob/main/docs/en/lectures/lecture-06-why-initialization-needs-its-own-phase/code/) Practice project: [Project 03. Multi-session continuity](https://walkinglabs.github.io/learn-harness-engineering/en/projects/project-03-multi-session-continuity/)

You start a new agent session and tell it "add a search feature." It jumps straight into coding — admirable enthusiasm. After 20 minutes it discovers the test framework isn't configured properly, spends another 10 minutes fixing that, then finds the database migration script format is wrong, more fiddling. The search feature does get added in the end, but the whole session was inefficient. Most of the time went to "figuring out how this project works" rather than writing the search feature itself.

The better approach: before letting the agent start working, use a separate phase to get the base environment ready, run verification commands through, and understand the project structure. Initialization work should not be crammed together with feature implementation — they are two fundamentally different kinds of tasks.

This lecture discusses why initialization must be a separate phase, not mixed in with implementation.

## Two Fundamentally Different Kinds of Work

Initialization and implementation have completely different optimization targets. The implementation phase aims to maximize the quantity and quality of verified features. The initialization phase aims to maximize the reliability and efficiency of all subsequent implementation.

When you mix initialization and implementation, the agent faces a multi-objective optimization problem: it has to simultaneously build infrastructure and write feature code. Without explicit priority setting, the agent naturally gravitates toward writing code (because that's directly visible output) while sacrificing infrastructure (because its value only shows up in subsequent sessions). The result: infrastructure doesn't get built solidly, and the reliability of the feature code suffers as well.

## Initialization Lifecycle

<svg id="mermaid-32" width="100%" xmlns="http://www.w3.org/2000/svg" style="max-width: 2997.46875px;min-width: 0px; width: auto !important; max-width: 100% !important; max-height: min(56vh, 520px) !important;" viewBox="0 0 2997.46875 181" role="graphics-document document" aria-roledescription="flowchart-v2"><g><marker id="mermaid-32_flowchart-v2-pointEnd" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-32_flowchart-v2-pointStart" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" style="stroke-width: 1; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-32_flowchart-v2-pointEnd-margin" viewBox="0 0 11.5 14" refX="11.5" refY="7" markerUnits="userSpaceOnUse" markerWidth="10.5" markerHeight="14" orient="auto"><path d="M 0 0 L 11.5 7 L 0 14 z" style="stroke-width: 0; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-32_flowchart-v2-pointStart-margin" viewBox="0 0 11.5 14" refX="1" refY="7" markerUnits="userSpaceOnUse" markerWidth="11.5" markerHeight="14" orient="auto"><polygon points="0,7 11.5,14 11.5,0" style="stroke-width: 0; stroke-dasharray: 1, 0;"></polygon></marker><marker id="mermaid-32_flowchart-v2-circleEnd" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 1; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-32_flowchart-v2-circleStart" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 1; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-32_flowchart-v2-circleEnd-margin" viewBox="0 0 10 10" refY="5" refX="12.25" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="14" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 0; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-32_flowchart-v2-circleStart-margin" viewBox="0 0 10 10" refX="-2" refY="5" markerUnits="userSpaceOnUse" markerWidth="14" markerHeight="14" orient="auto"><circle cx="5" cy="5" r="5" style="stroke-width: 0; stroke-dasharray: 1, 0;"></circle></marker><marker id="mermaid-32_flowchart-v2-crossEnd" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" style="stroke-width: 2; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-32_flowchart-v2-crossStart" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" style="stroke-width: 2; stroke-dasharray: 1, 0;"></path></marker><marker id="mermaid-32_flowchart-v2-crossEnd-margin" viewBox="0 0 15 15" refX="17.7" refY="7.5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto"><path d="M 1,1 L 14,14 M 1,14 L 14,1" style="stroke-width: 2.5;"></path></marker><marker id="mermaid-32_flowchart-v2-crossStart-margin" viewBox="0 0 15 15" refX="-3.5" refY="7.5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto"><path d="M 1,1 L 14,14 M 1,14 L 14,1" style="stroke-width: 2.5; stroke-dasharray: 1, 0;"></path></marker><g><g></g><g></g><g></g><g><g transform="translate(0, 0)"><g><g id="mermaid-32-Right" data-look="classic"><rect style="" x="8" y="8" width="1625.46875" height="165"></rect><g transform="translate(667.84375, 8)"><foreignObject width="305.78125" height="27"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: nowrap; line-height: 1.5;"><span style="font-size: 14px !important;"><p>Dedicated initialization phase (right)</p></span></div></foreignObject></g></g></g><g><path d="M296.5,90.5L303.25,90.5C310,90.5,323.5,90.5,336.333,90.5C349.167,90.5,361.333,90.5,367.417,90.5L373.5,90.5" id="mermaid-32-L_R1_R2_0" style=";" data-edge="true" data-et="edge" data-id="L_R1_R2_0" data-points="W3sieCI6Mjk2LjUsInkiOjkwLjV9LHsieCI6MzM3LCJ5Ijo5MC41fSx7IngiOjM3Ny41LCJ5Ijo5MC41fV0=" data-look="classic" marker-end="url(#mermaid-32_flowchart-v2-pointEnd)" fill="none" stroke="currentColor"></path><path d="M605.969,90.5L612.719,90.5C619.469,90.5,632.969,90.5,645.802,90.5C658.635,90.5,670.802,90.5,676.885,90.5L682.969,90.5" id="mermaid-32-L_R2_R3_0" style=";" data-edge="true" data-et="edge" data-id="L_R2_R3_0" data-points="W3sieCI6NjA1Ljk2ODc1LCJ5Ijo5MC41fSx7IngiOjY0Ni40Njg3NSwieSI6OTAuNX0seyJ4Ijo2ODYuOTY4NzUsInkiOjkwLjV9XQ==" data-look="classic" marker-end="url(#mermaid-32_flowchart-v2-pointEnd)" fill="none" stroke="currentColor"></path><path d="M934.969,90.5L941.719,90.5C948.469,90.5,961.969,90.5,974.802,90.5C987.635,90.5,999.802,90.5,1005.885,90.5L1011.969,90.5" id="mermaid-32-L_R3_R4_0" style=";" data-edge="true" data-et="edge" data-id="L_R3_R4_0" data-points="W3sieCI6OTM0Ljk2ODc1LCJ5Ijo5MC41fSx7IngiOjk3NS40Njg3NSwieSI6OTAuNX0seyJ4IjoxMDE1Ljk2ODc1LCJ5Ijo5MC41fV0=" data-look="classic" marker-end="url(#mermaid-32_flowchart-v2-pointEnd)" fill="none" stroke="currentColor"></path><path d="M1263.969,90.5L1270.719,90.5C1277.469,90.5,1290.969,90.5,1303.802,90.5C1316.635,90.5,1328.802,90.5,1334.885,90.5L1340.969,90.5" id="mermaid-32-L_R4_R5_0" style=";" data-edge="true" data-et="edge" data-id="L_R4_R5_0" data-points="W3sieCI6MTI2My45Njg3NSwieSI6OTAuNX0seyJ4IjoxMzA0LjQ2ODc1LCJ5Ijo5MC41fSx7IngiOjEzNDQuOTY4NzUsInkiOjkwLjV9XQ==" data-look="classic" marker-end="url(#mermaid-32_flowchart-v2-pointEnd)" fill="none" stroke="currentColor"></path></g><g><g style="font-size: 14px !important;"><g data-id="L_R1_R2_0" transform="translate(0, 0)" style="font-size: 14px !important;"></g></g><g style="font-size: 14px !important;"><g data-id="L_R2_R3_0" transform="translate(0, 0)" style="font-size: 14px !important;"></g></g><g style="font-size: 14px !important;"><g data-id="L_R3_R4_0" transform="translate(0, 0)" style="font-size: 14px !important;"></g></g><g style="font-size: 14px !important;"><g data-id="L_R4_R5_0" transform="translate(0, 0)" style="font-size: 14px !important;"></g></g></g><g><g id="mermaid-32-flowchart-R1-6" data-look="classic" transform="translate(172.5, 90.5)"><rect style="" x="-124" y="-39" width="248" height="78" fill="none" stroke="currentColor"></rect><g style="font-size: 14px !important;" transform="translate(-100, -27)"><rect></rect><foreignObject width="200" height="54"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table; white-space: break-spaces; line-height: 1.5; max-width: 200px; text-align: center; width: 200px;"><span style="font-size: 14px !important;"><p>Session 1: environment runnable</p></span></div></foreignObject></g></g><g id="mermaid-32-flowchart-R2-7" data-look="classic" transform="translate(491.734375, 90.5)"><rect style="" x="-114.234375" y="-25.5" width="228.46875" height="51" fill="none" stroke="currentColor"></rect><g style="font-size: 14px !important;" transform="translate(-90.234375, -13.5)"><rect></rect><foreignObject width="180.46875" height="27"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: nowrap; line-height: 1.5; max-width: 200px; text-align: center;"><span style="font-size: 14px !important;"><p>Example test passing</p></span></div></foreignObject></g></g><g id="mermaid-32-flowchart-R3-9" data-look="classic" transform="translate(810.96875, 90.5)"><rect style="" x="-124" y="-52.5" width="248" height="105" fill="none" stroke="currentColor"></rect><g style="font-size: 14px !important;" transform="translate(-100, -40.5)"><rect></rect><foreignObject width="200" height="81"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table; white-space: break-spaces; line-height: 1.5; max-width: 200px; text-align: center; width: 200px;"><span style="font-size: 14px !important;"><p>Startup readiness checklist + task list written</p></span></div></foreignObject></g></g><g id="mermaid-32-flowchart-R4-11" data-look="classic" transform="translate(1139.96875, 90.5)"><rect style="" x="-124" y="-39" width="248" height="78" fill="none" stroke="currentColor"></rect><g style="font-size: 14px !important;" transform="translate(-100, -27)"><rect></rect><foreignObject width="200" height="54"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table; white-space: break-spaces; line-height: 1.5; max-width: 200px; text-align: center; width: 200px;"><span style="font-size: 14px !important;"><p>Clean checkpoint committed</p></span></div></foreignObject></g></g><g id="mermaid-32-flowchart-R5-13" data-look="classic" transform="translate(1468.96875, 90.5)"><rect style="" x="-124" y="-52.5" width="248" height="105" fill="none" stroke="currentColor"></rect><g style="font-size: 14px !important;" transform="translate(-100, -40.5)"><rect></rect><foreignObject width="200" height="81"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table; white-space: break-spaces; line-height: 1.5; max-width: 200px; text-align: center; width: 200px;"><span style="font-size: 14px !important;"><p>Later sessions start directly on verified tasks</p></span></div></foreignObject></g></g></g></g><g transform="translate(1665.46875, 0)"><g><g id="mermaid-32-Wrong" data-look="classic"><rect style="" x="8" y="8" width="1316" height="165"></rect><g transform="translate(532.5859375, 8)"><foreignObject width="266.828125" height="27"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table-cell; white-space: nowrap; line-height: 1.5;"><span style="font-size: 14px !important;"><p>Mixed into one session (wrong)</p></span></div></foreignObject></g></g></g><g><path d="M296.5,90.5L303.25,90.5C310,90.5,323.5,90.5,336.333,90.5C349.167,90.5,361.333,90.5,367.417,90.5L373.5,90.5" id="mermaid-32-L_W1_W2_0" style=";" data-edge="true" data-et="edge" data-id="L_W1_W2_0" data-points="W3sieCI6Mjk2LjUsInkiOjkwLjV9LHsieCI6MzM3LCJ5Ijo5MC41fSx7IngiOjM3Ny41LCJ5Ijo5MC41fV0=" data-look="classic" marker-end="url(#mermaid-32_flowchart-v2-pointEnd)" fill="none" stroke="currentColor"></path><path d="M625.5,90.5L632.25,90.5C639,90.5,652.5,90.5,665.333,90.5C678.167,90.5,690.333,90.5,696.417,90.5L702.5,90.5" id="mermaid-32-L_W2_W3_0" style=";" data-edge="true" data-et="edge" data-id="L_W2_W3_0" data-points="W3sieCI6NjI1LjUsInkiOjkwLjV9LHsieCI6NjY2LCJ5Ijo5MC41fSx7IngiOjcwNi41LCJ5Ijo5MC41fV0=" data-look="classic" marker-end="url(#mermaid-32_flowchart-v2-pointEnd)" fill="none" stroke="currentColor"></path><path d="M954.5,90.5L961.25,90.5C968,90.5,981.5,90.5,994.333,90.5C1007.167,90.5,1019.333,90.5,1025.417,90.5L1031.5,90.5" id="mermaid-32-L_W3_W4_0" style=";" data-edge="true" data-et="edge" data-id="L_W3_W4_0" data-points="W3sieCI6OTU0LjUsInkiOjkwLjV9LHsieCI6OTk1LCJ5Ijo5MC41fSx7IngiOjEwMzUuNSwieSI6OTAuNX1d" data-look="classic" marker-end="url(#mermaid-32_flowchart-v2-pointEnd)" fill="none" stroke="currentColor"></path></g><g><g style="font-size: 14px !important;"><g data-id="L_W1_W2_0" transform="translate(0, 0)" style="font-size: 14px !important;"></g></g><g style="font-size: 14px !important;"><g data-id="L_W2_W3_0" transform="translate(0, 0)" style="font-size: 14px !important;"></g></g><g style="font-size: 14px !important;"><g data-id="L_W3_W4_0" transform="translate(0, 0)" style="font-size: 14px !important;"></g></g></g><g><g id="mermaid-32-flowchart-W1-0" data-look="classic" transform="translate(172.5, 90.5)"><rect style="" x="-124" y="-39" width="248" height="78" fill="none" stroke="currentColor"></rect><g style="font-size: 14px !important;" transform="translate(-100, -27)"><rect></rect><foreignObject width="200" height="54"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table; white-space: break-spaces; line-height: 1.5; max-width: 200px; text-align: center; width: 200px;"><span style="font-size: 14px !important;"><p>Start feature work immediately</p></span></div></foreignObject></g></g><g id="mermaid-32-flowchart-W2-1" data-look="classic" transform="translate(501.5, 90.5)"><rect style="" x="-124" y="-39" width="248" height="78" fill="none" stroke="currentColor"></rect><g style="font-size: 14px !important;" transform="translate(-100, -27)"><rect></rect><foreignObject width="200" height="54"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table; white-space: break-spaces; line-height: 1.5; max-width: 200px; text-align: center; width: 200px;"><span style="font-size: 14px !important;"><p>Discover env and test gaps mid-task</p></span></div></foreignObject></g></g><g id="mermaid-32-flowchart-W3-3" data-look="classic" transform="translate(830.5, 90.5)"><rect style="" x="-124" y="-39" width="248" height="78" fill="none" stroke="currentColor"></rect><g style="font-size: 14px !important;" transform="translate(-100, -27)"><rect></rect><foreignObject width="200" height="54"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table; white-space: break-spaces; line-height: 1.5; max-width: 200px; text-align: center; width: 200px;"><span style="font-size: 14px !important;"><p>Accumulate unverified code</p></span></div></foreignObject></g></g><g id="mermaid-32-flowchart-W4-5" data-look="classic" transform="translate(1159.5, 90.5)"><rect style="" x="-124" y="-52.5" width="248" height="105" fill="none" stroke="currentColor"></rect><g style="font-size: 14px !important;" transform="translate(-100, -40.5)"><rect></rect><foreignObject width="200" height="81"><div xmlns="http://www.w3.org/1999/xhtml" style="display: table; white-space: break-spaces; line-height: 1.5; max-width: 200px; text-align: center; width: 200px;"><span style="font-size: 14px !important;"><p>Next session must rediscover project state</p></span></div></foreignObject></g></g></g></g></g></g></g><defs></defs><defs></defs><linearGradient id="mermaid-32-gradient" gradientUnits="objectBoundingBox" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#D1D1D1" stop-opacity="1"></stop><stop offset="100%" stop-color="hsl(-70, 0%, 84.5098039216%)" stop-opacity="1"></stop></linearGradient></svg>

## What Happens When You Mix Them

The most direct problem: infrastructure doesn't get built solidly. The agent spends 80% of its effort on feature code and the remaining 20% casually setting up some infrastructure. The test framework is configured but never verified, lint rules are set but too loose, no progress file created. These defects aren't obvious in the first session (because the agent still remembers what it did), but they surface in the second session: the new agent doesn't know how to run the project, how to test, or where things stand.

A more hidden cost is "unverified accumulation." Feature code written before the test framework is properly configured — when you finally go back to add tests, you might discover the design itself was flawed. Had you known earlier, you would have implemented it differently. The more code written up front, the more has to be torn down and redone later.

Context budget is being wasted too. Initialization work (configuring environments, setting up tests, understanding project structure) consumes a large chunk of the budget, leaving less for actual feature implementation. The result: the first session only completes half the features, and the second session still has to start from scratch understanding the project. Budget was spent on initialization, but initialization wasn't done well either — the worst of both worlds.

The most easily overlooked problem is implicit assumption landmines. Decisions the agent makes during initialization (which test framework, how to organize directories, dependency management) — if not explicitly recorded, subsequent sessions may make contradictory choices. The first session chose Vitest as the test framework, but the second session's agent doesn't know and introduces Jest. Two test frameworks coexist, and maintenance costs double.

Anthropic's long-running application development research explicitly recommends separating initialization from implementation. Their experimental data: projects using a dedicated initialization phase showed 31% higher feature completion rates in multi-session scenarios compared to mixed approaches. And the time invested in the initialization phase is fully recovered within the next 3-4 sessions.

OpenAI's Codex harness engineering guide also emphasizes the "repository as operational record" principle: establish clear operational structure from the very first run, or every new session has to re-infer project conventions.

## Core Concepts

- **Initialization Phase**: The first phase in the agent's lifecycle — it only establishes the prerequisites for subsequent implementation, with no feature development. Its output is infrastructure, not business code.
- **Startup Readiness Checklist**: The conditions under which a project can be unambiguously operated by a fresh agent session: can start, can test, can see progress, can pick up next steps. Four conditions, all required.
- **From Scratch vs From Template**: Starting from scratch means the agent must infer project structure on its own from an empty directory; starting from a template means infrastructure is already in place. Starting from a template far outperforms starting from scratch.
- **Always Ready to Hand Off**: The project is in a state at any given moment where a fresh agent can take over. No verbal explanation needed — just looking at the repo contents is enough to continue working.
- **Time from Start to First Passing Test**: The time from project start until the first feature point passes verification. This is the core metric for measuring initialization efficiency.
- **Success Rate of Subsequent Sessions**: The proportion of subsequent sessions that can successfully execute tasks without relying on implicit knowledge. This is the best measure of initialization quality.

## How to Do Initialization Right

**Treat initialization as a dedicated phase.** The first session does only initialization — no business feature code at all. Initialization produces:

**1\. Runnable environment.** The project starts, dependencies are installed, no environment issues.

**2\. Verifiable test framework.** At least one example test passes, proving the test framework itself is properly configured.

**3\. Startup readiness checklist document.** A clear document telling subsequent sessions:

```markdown
# Startup Readiness Checklist

## Start Commands
- Install dependencies: \`make setup\`
- Start dev server: \`make dev\`
- Run tests: \`make test\`
- Full verification: \`make check\`

## Current State
- All dependencies installed and locked
- Test framework configured (Vitest + React Testing Library)
- Example test passing (1/1)
- Lint rules configured (ESLint + Prettier)

## Project Structure
- src/ — Source code
- src/components/ — React components
- src/api/ — API client
- tests/ — Test files
```

**4\. Task breakdown.** Split the entire project into an ordered task list, each task with clear acceptance criteria:

```markdown
# Task Breakdown

## Task 1: User Authentication Basics
- Implement JWT auth middleware
- Add login/register endpoints
- Acceptance: pytest tests/test_auth.py all passing

## Task 2: User Profile Page
- Implement user profile CRUD
- Add profile edit form
- Acceptance: pytest tests/test_profile.py all passing

## Task 3: Search Feature
- ...
```

**5\. Git commit as checkpoint.** After initialization completes, commit a clean checkpoint. All subsequent work starts from this checkpoint.

**Starting from a template**: Don't start from an empty directory. Use a project template (create-react-app, fastapi-template, etc.) to preset standard directory structure, dependency configuration, and test framework. Bake common initialization steps into the template, leaving only project-specific initialization work.

**Initialization completion criteria**: Not "how much code was written," but whether the startup readiness checklist's four conditions are all met: can start, can test, can see progress, can pick up next steps. Use this checklist to validate initialization:

```markdown
## Initialization Acceptance Checklist
- [ ] \`make setup\` succeeds from scratch
- [ ] \`make test\` has at least one passing test
- [ ] A new agent session can answer "how to run" and "how to test" from repo contents alone
- [ ] Task breakdown file exists with at least 3 tasks
- [ ] Everything committed to git
```

## Real-World Example

Two initialization approaches for a React frontend project, compared:

**Mixed approach**: The agent simultaneously created project scaffolding and implemented the first feature in session 1. At session end, the repo had runnable code but no explicit start/test command documentation, no progress tracking file, no task breakdown. Session 2 spent about 20 minutes inferring project structure, test framework, and build process.

**Dedicated initialization**: Session 1 did only initialization — created directory structure from a template, configured the test framework (Vitest + React Testing Library), wrote and verified one example test, created the startup readiness checklist and task breakdown file, committed the initial checkpoint. Session 2's rebuild time was under 3 minutes, and it started working directly from the task list.

Full project cycle comparison: the mixed approach's total rebuild time (across all sessions) was about 60% more than the dedicated initialization approach. The extra 20 minutes spent on initialization was recovered many times over in subsequent sessions. Invest a bit more time up front to do initialization properly, and subsequent efficiency is actually higher.

## Key Takeaways

- Initialization and implementation have different optimization targets — mixing them only drags both down.
- Initialization's output isn't business code, it's infrastructure: runnable environment, verifiable tests, startup readiness checklist, task breakdown.
- Validate initialization with the startup readiness checklist's four conditions: can start, can test, can see progress, can pick up next steps.
- Starting from a template beats starting from scratch. Use project templates to preset standardized infrastructure.
- Time invested in initialization is fully recovered in the next 3-4 sessions. This isn't extra cost — it's upfront investment.

## Further Reading

- [Anthropic: Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [OpenAI: Harness Engineering](https://openai.com/index/harness-engineering/)
- [HumanLayer: Harness Engineering for Coding Agents](https://humanlayer.dev/articles/harness-engineering-for-coding-agents/)
- [Infrastructure as Code — Martin Fowler](https://martinfowler.com/bliki/InfrastructureAsCode.html)
- [SWE-agent: Agent-Computer Interfaces](https://github.com/princeton-nlp/SWE-agent)

## Exercises

1. **Startup readiness checklist design**: Write a complete startup readiness checklist for a project you're developing. Then open a completely fresh agent session, show it only repo contents (no verbal context at all), and have it try to start the project, run tests, and understand current progress. Record every problem it encounters — each one corresponds to a missing clause in your startup readiness checklist.
2. **Comparison experiment**: Pick a moderately complex new project. Approach A: let the agent initialize and do first implementation simultaneously. Approach B: spend one session on dedicated initialization, start implementation in session 2. After 4 sessions, compare time from start to first passing test, rebuild cost, and feature completion rate.
3. **Initialization acceptance checklist**: Design an initialization acceptance checklist for your project. Have a fresh agent session execute each checklist item and record which pass and which fail. The failing items are where your harness needs strengthening.