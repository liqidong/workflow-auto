---
name: systematic-debugging
description: Thin compatibility wrapper. Use the repo's blocker route and canonical investigate skill for root-cause work.
---

# Systematic Debugging Compatibility Shim

For debugging in this repo:

- route through [`.agents/skills/goi-workflow/SKILL.md`](../../../.agents/skills/goi-workflow/SKILL.md)
- when the work is a blocker, use the host `investigate` skill as the
  canonical execution surface
- close with regression evidence from
  [docs/ops/workflow/evidence.md](../../../docs/ops/workflow/evidence.md)

Local rules still apply:

- reproduce before fix when possible
- avoid stacking speculative fixes
- keep docs and archive work secondary while a blocker is live

This shim does not replace the canonical `blocker` route.
It also does not import a mandatory foreign debugging workflow.
