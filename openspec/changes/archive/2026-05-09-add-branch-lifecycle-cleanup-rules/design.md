## Overview

This change closes a narrow policy gap in the template's branch workflow: it
already requires `main -> feat/* -> main`, but it does not make post-merge
cleanup explicit. The design adds a small lifecycle policy without changing
route selection, OpenSpec lifecycle, or execution modes.

## Design Decisions

### Short-lived `feat/*` branches

Bounded `feat/*` branches remain the default unit of implementation work.
After verification and merge back to `main`, they should be cleaned up:

- delete the local branch
- delete the remote feature branch when it is no longer needed
- remove the corresponding `.worktrees/...` directory

This is phrased as a default policy, not an irreversible command mandate. If a
branch still carries unfinished work or pending review, it should stay alive.

### Long-lived `lane/*` branches

Long-lived `lane/*` branches are explicitly exempt from the short-lived
`feat/*` cleanup rule. They are allowed to persist, carry their own tags, and
evolve without merging into `main`.

### Keep the rule local to branch/worktree posture

This policy belongs in branch/worktree docs, README branching posture, and a
small dedicated OpenSpec capability. It does not belong in route tables or
execution-quality guidance.

## Affected Surfaces

- `AGENTS.md`
- `README.md`
- `docs/ops/git-worktree-layout.md`
- `docs/ops/workflow/checklist.md`
- `scripts/verify-workflow-template.sh`
- `tests/test_branch_lifecycle_policy.py`

## Non-Goals

- introducing new route modes
- changing `main` merge requirements
- forcing deletion of long-lived support lanes
- changing release tagging strategy
