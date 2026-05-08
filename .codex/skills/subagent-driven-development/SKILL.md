---
name: subagent-driven-development
description: Thin compatibility wrapper. Use this repo's optional delegation mode only after route selection and explicit user launch confirmation.
---

# Subagent-Driven Development Compatibility Shim

This repo does not treat subagent-driven development as a mandatory default
workflow.

Use the canonical local surfaces:

- [`.agents/skills/goi-workflow/SKILL.md`](../../../.agents/skills/goi-workflow/SKILL.md)
- [`.agents/skills/goi-workflow/references/subagent-task-packet.md`](../../../.agents/skills/goi-workflow/references/subagent-task-packet.md)
- [docs/ops/workflow/multi-agent-execution.md](../../../docs/ops/workflow/multi-agent-execution.md)

Local rule:

- route first
- lock acceptance first
- prepare the task packet first
- ask the user before launching this mode

Ask the user before launching this mode.

This shim does not import a mandatory foreign subagent workflow chain.
