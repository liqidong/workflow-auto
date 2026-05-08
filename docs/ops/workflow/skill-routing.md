# Skill Routing

Status: current operating surface

This file defines only the repo-local GOI routing layer.

It does not restate the full `gstack` skill graph or the full `OpenSpec`
lifecycle. It chooses the smallest safe route, composes that route with the GOI
tuple, and points to the evidence surface required for completion.

## Purpose

This repo uses a light routing / heavy evidence workflow adapter.

The adapter does not replace OpenSpec, `gstack`, review, QA, ship, or
self-improvement. It only decides how to enter them and what evidence is
required.

Adopted external skills remain downstream execution aids or compatibility
entrypoints. They do not replace repo-local route selection or impose a
mandatory foreign workflow chain.

Delegation-heavy and parallel-dispatch modes are opt-in launch shapes in this
repo. They may be recommended after routing, but they should not start until
the user confirms the launch.

## Route Modes

### `assess`

Use for read-only review, research, explanation, status, route recommendation,
or risk assessment.

Rules:

- no file edits
- no dependency installation
- no deploy/archive/repair actions
- output findings, options, uncertainty, and recommended route

Minimum evidence:

- files inspected, commands run, source links where applicable, explicit uncertainty list

### `micro`

Use for typo fixes, tiny docs edits, mechanical local cleanup, and obvious
low-risk corrections.

Rules:

- one small scope
- no architecture, contract, runtime, security, workflow, or production impact
- may skip full route trace only if clearly trivial

Minimum evidence:

- markdown/path check, targeted `rg`, or smallest relevant test

### `light`

Use for implementation, debugging, hardening, or review-finding fixes inside an
already accepted scope.

Rules:

- inherit active OpenSpec or accepted plan
- do not reopen planning unless scope changes
- prefer source, tests, smoke, and review evidence over new process docs

Minimum evidence:

- targeted tests or smoke proof
- OpenSpec validation if OpenSpec is the control surface

### `full`

Use for new features, architecture changes, data contracts, security/trust
boundaries, deployment behavior, workflow rules, or production-impacting
changes.

Rules:

- plan before implementation
- create or update OpenSpec when behavior or contract must be locked
- record a durable decision when the workflow or architecture decision should
  outlive one change

Minimum evidence:

- proposal/design/tasks/spec delta or accepted equivalent
- review of scope and acceptance
- validation command where available

### `blocker`

Use for failing tests, failing smoke, broken runtime behavior, repeated
failures, user correction, unexplained regression, or spec/code drift that
blocks safe progress.

Rules:

- reproduce before fix when possible
- identify plausible root cause before implementation
- do not stack speculative fixes
- trigger self-improvement only when a durable lesson or repeated mistake exists

Minimum evidence:

- reproduction evidence
- root-cause note
- targeted regression check

### `landing`

Use for review, PR, release, deploy, archive, or closeout.

Rules:

- do not recreate the upstream landing workflow
- report current control surface, verification status, and residual risks
- archive OpenSpec only when implementation and spec agree, or explicitly choose
  skip-spec behavior for workflow-only changes

Minimum evidence:

- final checks, review outcome, archive/deploy decision, changelog/version proof when relevant

## GOI Tuple

For routine non-high-risk work, default to a short trace:

```text
Route:
Why:
Evidence:
```

Use the full GOI trace when any of the following are true:

- workflow / instruction files change
- architecture, security, deployment, or data-contract work is in scope
- the task starts from blocker, correction, or repeated failure conditions
- a writer, reviewer, or parallel-dispatch launch is being used
- the task is landing, release, deploy, archive, or closeout work
- the user explicitly asks for the complete route trace

Full GOI trace:

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

Routine updates do not need a visible `self-improvement: not-triggered` line.
Triggered self-improvement events must not be silently omitted.

## Hard Gates

- High-risk work cannot route to `micro`.
- Blocker, correction, or repeated-failure work must investigate before implementation.
- Active OpenSpec work should be inherited, not replanned, unless scope changed.
- Instruction files are supply-chain sensitive and require careful review.
- Routing predicates must be declarative; do not execute generated predicates.
- Skipped verification must be explicit and temporary.

## Current Program Focus

This template intentionally does not fix a product-domain mainline.

The active repository must define current program focus in:

- the top-level `README.md`
- `openspec/specs/project-mainline-routing/spec.md`

Those surfaces should answer:

- what is currently shipped
- what is planned but not yet shipped
- which work streams are optimization, research, or evidence lanes
- which machine-readable artifacts are authoritative

Copied repositories must replace inherited host-specific identity and inventory
in those two surfaces before treating them as canonical.

Keep the multi-agent quality default: one writer for one coherent milestone and
one fresh reviewer per checkpoint.


## Detailed Surfaces

- [routing-table.md](routing-table.md):
  precedence, hard gates, and route decision table
- [evidence.md](evidence.md):
  minimum evidence and skipped-verification contract
- [routing-checks.md](routing-checks.md):
  manual snapshot checks for routing drift

## Skills That Should Stay Conditional

Do not make these part of the always-on backbone.

Use them only when the work type actually calls for them:

- `browse`
- `qa`
- `qa-only`
- `plan-design-review`
- `design-review`
- `devex-review`
- `benchmark`
- `ship`
- `land-and-deploy`
- `canary`
- `setup-deploy`
- `careful`
- `freeze`

## Anti-Duplication Rule

If an official skill already explains what comes next, what came before, or how
it hands off to another skill, repo-local routing should not rewrite that
explanation in full.

The repo should only add:

- the route mode
- the current GOI routing tuple
- the active OpenSpec control surface when applicable
- the repo-specific override
- the current product program focus or active change context
- a thin note when an adopted external skill maps to an existing local surface
