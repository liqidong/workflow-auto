---
name: using-git-worktrees
description: Thin compatibility wrapper. Use this repo's branch and worktree policy instead of a foreign branch-management workflow.
---

# Git Worktree Compatibility Shim

Use this repo's canonical branch and worktree surfaces:

- [AGENTS.md](../../../AGENTS.md)
- [docs/ops/git-worktree-layout.md](../../../docs/ops/git-worktree-layout.md)

Current local policy:

- root workspace stays on `main`
- feature work belongs on `feat/*`
- active feature branches live under `.worktrees/`
- one active branch per folder

This shim does not create worktrees automatically or replace repo-local route
selection.
It also does not import a mandatory foreign branch-management workflow.
