---
name: goi-workflow
description: Use before non-trivial repository work to choose the smallest safe route, compose it with the GOI tuple, and bind required evidence. Triggers on workflow routing, OpenSpec/gstack handoff, blockers, implementation, review, landing, and route recommendation.
---

# GOI Workflow Router

This is the canonical repo-local GOI workflow skill.

It implements the repo's light routing / heavy evidence adapter. It chooses the
smallest correct route, composes that route with the GOI tuple, and binds the
minimum evidence required before completion.

It does not replace, fork, or rewrite official skills.

## Core Rule

```text
project state + task kind + risk level + problem kind + control surface
=> smallest safe route
=> GOI tuple
=> required evidence
=> traceable reason
```

Use official `gstack`, OpenSpec, review, QA, ship, and self-improvement skills
for their own workflows. This skill only decides how to enter them and what
repo-local evidence is required.

## Step 1: Inspect Current State

Before choosing a route, inspect only what is necessary:

- user request and explicit constraints
- `git status --short`
- relevant `AGENTS.md` and local instructions
- active OpenSpec changes, if present
- relevant tasks, docs, source files, tests, logs, or PR context

Do not edit files in `assess` mode. Do not overwrite unrelated user changes.

## Step 2: Classify

Project state:

- `unknown`: not enough context read yet
- `clean`: no active change or blocker known
- `active_change`: OpenSpec change or accepted plan exists
- `implementation`: implementation is underway inside accepted scope
- `blocked`: failing check, smoke, runtime behavior, user correction, or drift
  blocks progress
- `review_ready`: implementation is ready for review
- `landing`: PR, release, deploy, archive, or closeout is the main remaining
  work

Task kind:

- `question`
- `research`
- `documentation`
- `feature`
- `architecture`
- `implementation`
- `debug`
- `review`
- `release`
- `workflow`

Risk level:

- `low`: local, reversible, no contract/runtime impact
- `medium`: behavior, agent docs, or more than one module affected
- `high`: architecture, data contract, security/trust boundary, deployment,
  workflow rules, or production behavior affected

Problem kind:

- `none`
- `ambiguity`
- `blocker`
- `regression`
- `correction`
- `drift`

Useful facts:

- `has_active_openspec`
- `has_reproduction`
- `has_verification`
- `dirty_worktree`
- `user_requested_no_write`
- `repeated_failure`
- `scope_changed`

## Step 3: Apply Hard Gates

These override normal preferences:

1. High-risk work cannot route to `micro`.
2. Blocker, correction, or repeated-failure work must investigate before
   implementation.
3. `problem_kind in [blocker, regression, correction]` routes to `blocker`
   unless the user explicitly asked for read-only assessment.
4. `repeated_failure == true` routes to `blocker`.
5. `user_requested_no_write == true` routes to `assess`.
6. Security, trust-boundary, workflow, deployment, production behavior, or
   data-contract changes require `full` unless an exact active control surface
   already covers the scope.
7. Active OpenSpec implementation should inherit the active change and use
   `light`, unless `scope_changed == true`.
8. Instruction files are supply-chain sensitive, including `AGENTS.md`,
   `.agents/skills/**`, `.codex/skills/**`, `.claude/skills/**`,
   `.cursor/rules/**`, `.clinerules/**`, and `docs/ops/workflow/**`.
9. Routing predicates must stay declarative; do not execute generated
   predicates.

## Step 4: Choose Mode

- `assess`: read-only research, review, status, route recommendation, or risk
  assessment
- `micro`: tiny low-risk edit with the smallest useful verification
- `light`: implementation, debugging, hardening, or review-finding fix inside
  accepted scope or active OpenSpec
- `full`: new feature, architecture, contract, security, deployment, workflow,
  or production-impacting change
- `blocker`: root-cause route for failing checks, failing smoke, user
  correction, repeated failure, unexplained regression, or drift
- `landing`: review, PR, release, deploy, archive, or closeout

Use [docs/ops/workflow/routing-table.md](../../../docs/ops/workflow/routing-table.md)
for detailed precedence and
[docs/ops/workflow/routing-checks.md](../../../docs/ops/workflow/routing-checks.md)
for snapshot cases.

## Step 5: Emit Route Trace

For routine non-high-risk work, default to a short trace:

```text
Route:
Why:
Evidence:
```

Use the full trace when any of the following are true:

- workflow / instruction files change
- architecture, security, deployment, or data-contract work is in scope
- the task starts from blocker, correction, or repeated failure conditions
- a writer, reviewer, or parallel-dispatch launch is being used
- the task is landing, release, deploy, archive, or closeout work
- the user explicitly asks for the complete route trace

Full trace:

```text
Route:
gstack stage:
gstack status:
gstack reason:
OpenSpec:
OpenSpec reason:
OpenSpec control surface:
self-improvement:
self-improvement reason:
Project state:
Task kind:
Risk level:
Problem kind:
Control surface:
Entry:
Reason:
Verification required:
```

Keep it short. The route trace is for observability, not ceremony. Routine
updates do not need a visible `self-improvement: not-triggered` line; triggered
self-improvement events must not be silently omitted.

## Step 6: Evidence Contract

Before claiming completion, provide fresh evidence:

```yaml
verification_evidence:
  required:
    - check:
      expected_signal:
  completed:
    - command_or_check:
      result:
      evidence_artifact:
  skipped:
    - check:
      reason:
      residual_risk:
      follow_up:
```

If a check cannot run, record:

```yaml
skipped_verification:
  check:
  reason:
  residual_risk:
  follow_up:
```

Use [docs/ops/workflow/evidence.md](../../../docs/ops/workflow/evidence.md)
for route-specific minimum evidence.

## Step 7: Thin Handoff Rule

Choose the smallest correct current `gstack` gate. Explain why the path
continues, stops, inherits, or skips. Do not expand the full downstream chain
unless the current task reaches it.

Before dispatch or non-trivial coding:

- name the assumptions or unknowns that matter now
- if multiple viable routes exist, choose the simpler viable route and say why
- phrase each non-trivial step as `action -> verification`
- if those assumptions are too weak for safe execution, stop and ask rather
  than guessing

## Step 7A: Optional Launch Modes

Delegation-heavy and parallel-dispatch patterns are available in this repo only
as optional launch modes.

Rules:

- route first
- lock the active OpenSpec control surface first when applicable
- prepare a concrete subagent task packet first
- if a delegation-heavy mode looks useful, recommend it explicitly instead of
  starting it silently
- ask the user before launching a writer or parallel-writer topology that is
  not already the default local execution shape

Parallel-writer launch requires all of the following:

- write sets are disjoint
- each writer has a separate worktree
- integration ownership is explicit
- the main thread is not blocked on both results simultaneously

If any checklist item is false, keep the work in the main thread or use one
writer plus read-only support only.

## Step 8: Implementation-Light Rule

When work is already inside an active planned change and in
implementation/debug/hardening/smoke:

- keep the active OpenSpec change as the contract source of truth
- keep the current implementation gate or inherited `gstack` status explicit
- use active change, code/tests, real smoke/deployed proof, and review findings
  classified as `blocking / important / low`
- keep docs/tracker/archive secondary while an unresolved blocker exists
- keep agenting narrow by default: main thread, one writer for one coherent
  milestone, one fresh reviewer per checkpoint, explorer/docs agents on demand
- allow parallel writers only with separate worktrees, disjoint write sets, and
  explicit ownership
- ask the user before starting a delegation-heavy or parallel-dispatch mode
- keep `agents.max_depth = 1`

## Current Program Focus

This template intentionally does not hardcode a product domain mainline.

Use these surfaces as the active mainline contract:

- `README.md`
- `openspec/specs/project-mainline-routing/spec.md`

If those surfaces are missing, stale, or disagree:

- pause route assumptions
- repair the mainline description first
- then continue with implementation, blocker, or landing work

If this template is copied into another repository, that repository must
replace any inherited host-specific identity and current-mainline inventory in
those two surfaces before treating them as canonical.

## Closeout

For implementation, blocker, or landing work, close with:

```text
Summary:
Route:
Files changed:
Evidence:
Skipped verification:
Residual risk:
Follow-up:
```

Do not claim completion without fresh evidence or an explicit skipped
verification record.
