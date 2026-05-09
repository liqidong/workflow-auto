# Git Worktree Layout

This template assumes one git repository with multiple worktrees.

The goal is simple:

- one active branch per folder
- no repeated `git checkout` in the same workspace
- keep `main` clean as the integration view
- keep feature work isolated and easy to publish back to `main`

## Suggested Layout

Suggested layout under the repo root:

```text
/path/to/repo                                -> root workspace, main
/path/to/repo/.worktrees/feat-example-task
/path/to/repo/.worktrees/feat-second-task
```

Current practical rule:

- root workspace stays on `main`
- active feature branches live under `.worktrees/`
- new feature branches should be created under `.worktrees/<branch-slug>`
- default development flow is `main -> feat/* -> main`
- merged `feat/*` branches should be cleaned up when no longer needed
- long-lived `lane/*` branches are explicit exceptions to the short-lived
  `feat/*` cleanup rule

## Branch Roles

- `main`
  - integration branch
  - use for clean inspection, release prep, and merge target validation
  - do not use for daily implementation work

- `feat/*`
  - bounded feature or workflow work
  - one worktree per feature branch
  - default branch type for new implementation work
  - merge back to `main` after verification, then clean up when no longer
    needed

- `lane/*`
  - long-lived support lane
  - may carry its own tags and independent evolution
  - do not auto-delete it under the bounded `feat/*` cleanup rule

## Naming Rules

- directory name should be a filesystem-safe branch slug
- examples:
  - `feat/example-task` -> `.worktrees/feat-example-task`
  - `feat/workflow-docs` -> `.worktrees/feat-workflow-docs`

## Safety Rules

- never use the same branch in two worktrees
- do not keep daily development on `main`
- prefer `feat/*` branches for normal work
- before creating a new worktree, make sure `.worktrees/` stays ignored
- verify a clean baseline in the new worktree before major edits
- after a merged `feat/*` branch is no longer needed, clean up the branch and
  remove its worktree
- do not apply that cleanup rule automatically to a long-lived `lane/*` branch

## Standard Operations

List worktrees:

```text
git worktree list
```

Create a new feature worktree:

```text
git worktree add .worktrees/feat-my-task -b feat/my-task
```

Publish a finished feature branch back to `main`:

```text
git checkout main
git merge --no-ff feat/my-task
git push origin main
```

Clean up a finished feature branch when it is no longer needed:

```text
git branch -d feat/my-task
git push origin --delete feat/my-task
git worktree remove .worktrees/feat-my-task
```
