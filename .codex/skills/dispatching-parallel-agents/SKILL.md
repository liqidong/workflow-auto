---
name: dispatching-parallel-agents
description: Thin compatibility wrapper. Use this repo's optional parallel-dispatch checklist only after route selection and explicit user launch confirmation.
---

# Parallel Agent Dispatch Compatibility Shim

This repo does not treat parallel agent dispatch as a default execution mode.

Use the canonical local surfaces:

- [`.agents/skills/goi-workflow/SKILL.md`](../../../.agents/skills/goi-workflow/SKILL.md)
- [docs/ops/workflow/multi-agent-execution.md](../../../docs/ops/workflow/multi-agent-execution.md)
- [docs/ops/workflow/routing-checks.md](../../../docs/ops/workflow/routing-checks.md)

Parallel launch is allowed only when:

- write sets are disjoint
- each writer has a separate worktree
- integration ownership is explicit
- the main thread is not blocked on both results simultaneously

Ask the user before launching this mode.

This shim does not import a mandatory foreign parallel-agent workflow chain.
