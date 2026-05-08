---
name: requesting-code-review
description: Thin compatibility wrapper. Use the repo's canonical review and landing surfaces for pre-merge risk review.
---

# Code Review Request Compatibility Shim

Use the repo's canonical review surfaces:

- `review` for pre-landing diff review
- `ship` when the work is ready to prepare a PR
- `land-and-deploy` when landing and deploy verification are the remaining work

Route selection still comes first through:

- [`.agents/skills/goi-workflow/SKILL.md`](../../../.agents/skills/goi-workflow/SKILL.md)

This shim does not insert a mandatory review chain into every task.
