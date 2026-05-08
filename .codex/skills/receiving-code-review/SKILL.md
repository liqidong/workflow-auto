---
name: receiving-code-review
description: Thin compatibility wrapper. Handle review findings through the repo's inherited light or blocker routes.
---

# Code Review Response Compatibility Shim

Use the repo's canonical response posture:

- bounded review findings inside accepted scope usually stay on `light`
- regressions, corrections, or repeated failure escalate to `blocker`
- active OpenSpec changes should be inherited unless scope changes

Primary local references:

- [`.agents/skills/goi-workflow/SKILL.md`](../../../.agents/skills/goi-workflow/SKILL.md)
- [docs/ops/workflow/routing-table.md](../../../docs/ops/workflow/routing-table.md)
- [docs/ops/workflow/evidence.md](../../../docs/ops/workflow/evidence.md)

This shim does not replace canonical routing or OpenSpec control.
It also does not import a mandatory foreign review-response workflow.
