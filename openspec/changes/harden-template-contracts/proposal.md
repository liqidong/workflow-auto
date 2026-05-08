## Why

The repository already documents a thin-routing, heavy-evidence template, but
its host identity, current-mainline inventory, verification entrypoints, and
machine-checkable contracts are still loose enough that a new reader or agent
can misread what is actually shipped. We need to harden the template so it is
not only descriptive, but also verifiable, copyable, and portable.

## What Changes

- Clarify that `workflow-auto` is the repository that hosts the reusable
  `workflow-base` template.
- Fill `project-mainline-routing` with the real current inventory for this host
  repo instead of leaving it abstract-only.
- Align README promises with actual repo surfaces, including a thin `.claude`
  GOI shim.
- Add a host dependency checker and strengthen the shell verifier.
- Split route reporting into default short trace and required full trace.
- Add recovery rules and learning-capture guidance without expanding the core
  workflow model.
- Add stronger pytest contract tests that check consistency across docs, skill
  surfaces, scripts, and specs.

## Capabilities

### Modified Capabilities

- `workflow-routing-policy`: distinguish short and full trace posture and keep
  contract verification machine-checkable
- `project-mainline-routing`: require current repo identity and concrete
  inventory, not abstract requirements only

## Impact

- `README.md`
- `AGENTS.md`
- `openspec/specs/project-mainline-routing/spec.md`
- `openspec/specs/workflow-routing-policy/spec.md`
- `docs/ops/workflow/*`
- `.claude/skills/goi-workflow/SKILL.md`
- `scripts/check-host-workflow-deps.sh`
- `scripts/verify-workflow-template.sh`
- `tests/*`
