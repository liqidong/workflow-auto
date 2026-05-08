## Context

This repo already has a narrow multi-agent posture:

- main thread owns boundaries and final decisions
- one writer is the default for one coherent milestone
- parallel writers are exceptional

That posture is sound, but the repo does not yet encode a concrete "ask before
launch" rule for optional delegation or parallel dispatch. Without that rule,
adopting compatibility names such as `subagent-driven-development` or
`dispatching-parallel-agents` would be too easy to misread as automatic default
behavior.

The goal is to expose the ideas safely:

- allow the workflow to recommend optional modes when useful
- require explicit user confirmation before startup
- keep route selection in `goi-workflow`
- keep execution defaults unchanged

## Goals / Non-Goals

**Goals:**

- make delegation-heavy and parallel-dispatch patterns available as opt-in
  start modes
- force a user confirmation step before those modes start
- define exact launch gates that keep parallelism rare and auditable
- strengthen the subagent task packet so a delegated task is concretely bounded
- preserve the existing one-writer default

**Non-Goals:**

- turning delegation into the new default for non-trivial work
- allowing auto-spawned writer teams without confirmation
- importing Superpowers' mandatory subagent chain
- widening the repo's concurrency posture beyond the current disjoint-write-set
  rule

## Decisions

### 1. Optional launch is recommendation-first, not auto-start

When the repo detects that a task is a good fit for delegation-heavy execution
or parallel dispatch, the workflow may recommend that mode. It must ask the
user whether to start it before launching workers.

Why:

- This keeps the user in control of execution shape.
- It avoids surprise delegation on tasks where cost, latency, or context
  sensitivity matter.

Alternative considered:

- Automatically start delegation when the route and checklist match.
- Rejected because the user explicitly wants confirmation before launch.

### 2. Route selection still comes first

`goi-workflow` keeps route selection authority. Optional launch modes may only
be considered after the route, control surface, and acceptance source are
already clear.

Why:

- This preserves thin routing and avoids letting a compatibility skill invent
  its own control plane.

### 3. Parallel dispatch requires a short hard checklist

Parallel-writer dispatch is allowed only when all of the following are true:

- write sets are disjoint
- each writer has its own worktree
- main-thread integration ownership is explicit
- the main thread is not blocked on both results simultaneously

Why:

- This matches the repo's current quality-first default and keeps parallelism
  exceptional.

### 4. Delegated work packets need stronger acceptance metadata

The task packet will add:

- `Acceptance source`
- `Review mode`
- `Checkpoint trigger`
- `Parallel-safe`

Why:

- These fields make the packet more executable and reduce ambiguity before
  dispatch.

## Risks / Trade-offs

- [Extra ceremony] Asking before launch adds one more decision point. ->
  Mitigation: ask only when launch conditions are already satisfied and the mode
  is actually recommended.
- [Wrapper confusion] Compatibility names may still be mistaken for defaults. ->
  Mitigation: keep the wrappers thin and explicit about opt-in startup.
- [Parallel overuse] Users may over-request parallelism because the shim exists.
  -> Mitigation: encode the hard checklist in docs and tests.

## Migration Plan

1. Add the new capability and route-policy delta.
2. Update the canonical router, task packet, and multi-agent docs.
3. Add thin `.codex` compatibility shims for the two names.
4. Update adoption analysis and tests.
5. Validate OpenSpec and repo tests.

## Open Questions

- Whether the repo should later expose a short textual startup prompt template
  for delegation confirmation.
- Whether `.claude` compatibility shims are also needed, or if `.codex` is
  sufficient for current local usage.
