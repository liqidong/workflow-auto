---
name: openspec-explore
description: Enter explore mode to investigate requirements, tradeoffs, and codebase context before or during a change.
license: MIT
compatibility: Requires openspec CLI.
metadata:
  author: openspec
  version: "1.0"
  generatedBy: "1.3.1"
---

Enter explore mode.

Explore mode is for thinking, not implementing.

You may:

- read files
- search code
- inspect OpenSpec changes and specs
- draw diagrams
- compare approaches
- suggest capture points for requirements, design, or tasks

You must not write application code or silently implement features in this
mode.

## Basic Flow

1. Run `openspec list --json` to check current context.
2. If a relevant change exists, read its artifacts for grounding.
3. Explore the codebase and problem space in parallel.
4. Surface tradeoffs, unknowns, and likely next steps.
5. Offer to capture decisions in OpenSpec artifacts when they become stable.

## Guardrails

- Stay read-only for implementation code.
- Ground your exploration in the real repository, not pure theory.
- If there is no active change and the work is clearly non-trivial, suggest
  moving to `openspec-propose`.
- If the user asks to implement, transition out of explore mode first.

