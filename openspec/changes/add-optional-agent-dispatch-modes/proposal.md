## Why

The repo already has a quality-first multi-agent posture, but it does not yet
define a clear opt-in launch model for delegation-heavy or parallel-dispatch
execution styles. We need a way to benefit from those patterns without letting
them become automatic defaults or bypassing repo-local route selection.

## What Changes

- Add an explicit optional-agent-dispatch capability for this repo.
- Require delegation-heavy and parallel-dispatch execution modes to remain
  off-by-default and ask the user before startup.
- Define a practical launch checklist for single-writer delegation and
  parallel-writer dispatch.
- Extend the subagent task packet with acceptance, review mode, checkpoint, and
  parallel-safety fields.
- Add thin compatibility shims for `subagent-driven-development` and
  `dispatching-parallel-agents` that redirect to canonical local workflow
  surfaces rather than importing a foreign mandatory chain.
- Update descriptive adoption docs and tests to reflect opt-in adoption of
  those two compatibility names.

## Capabilities

### New Capabilities

- `optional-agent-dispatch`: define opt-in startup rules and launch gates for
  delegation-heavy and parallel-dispatch execution inside the repo's thin
  workflow

### Modified Capabilities

- `workflow-routing-policy`: require route selection to happen before optional
  delegation modes and require explicit user confirmation before launch

## Impact

- `.agents/skills/goi-workflow/SKILL.md`
- `.agents/skills/goi-workflow/references/subagent-task-packet.md`
- `.codex/skills/subagent-driven-development/SKILL.md`
- `.codex/skills/dispatching-parallel-agents/SKILL.md`
- `docs/ops/workflow/multi-agent-execution.md`
- `docs/ops/workflow/routing-checks.md`
- `docs/ops/superpowers-capability-adoption.md`
- tests covering workflow docs and compatibility shims
