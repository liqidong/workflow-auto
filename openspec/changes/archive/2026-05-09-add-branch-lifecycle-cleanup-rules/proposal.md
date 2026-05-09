## Why

The current template states that finished `feat/*` branches merge back to
`main`, but it does not explicitly say whether those branches and their
worktrees should be deleted afterward or how long-lived `lane/*` branches
should be handled.

## What Changes

- Add an explicit branch-lifecycle policy for bounded `feat/*` branches versus
  long-lived `lane/*` branches.
- Update branch-policy docs to say merged `feat/*` branches should be deleted
  locally and remotely and their worktrees removed when no longer needed.
- Document that `lane/*` branches are long-lived support lanes and should not
  be auto-deleted under the `feat/*` cleanup rule.
- Add verifier and pytest contract coverage for the new lifecycle wording.

## Capabilities

### New Capabilities
- `branch-lifecycle-policy`: normative cleanup rules for short-lived feature
  branches and long-lived lane branches

### Modified Capabilities
- none

## Impact

- `AGENTS.md`
- `README.md`
- `docs/ops/git-worktree-layout.md`
- `docs/ops/workflow/checklist.md`
- `scripts/verify-workflow-template.sh`
- `tests/*`
- `openspec/specs/branch-lifecycle-policy/spec.md`
