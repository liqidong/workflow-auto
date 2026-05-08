# 0001: Thin Routing Over Full Workflow

Status: accepted
Date: 2026-04-17

## Context

A repository using this template typically uses:

- `gstack`
- `OpenSpec`
- repo-local process rules

The practical problem is not absence of structure. The practical problem is that
repo-local corrections can accumulate into an always-on workflow shape that is
heavier than the work actually needs.

Two source-grounded constraints matter:

1. `gstack` already provides a linked skill graph, shared handoff semantics,
   shared review/report infrastructure, and generated skill docs.
2. `OpenSpec` already provides change creation, artifact graph ordering,
   implementation gating, `tasks.md` progress tracking, and archive/spec-apply.

If the repo restates those upstream capabilities in full, it creates drift,
duplicate truth surfaces, and avoidable process overhead.

## Decision

The repo workflow should be modeled as:

- upstream tool layer
- repo routing layer
- project state layer
- decision layer

### Upstream tool layer

Source of truth:

- official `gstack` skills
- official `OpenSpec` lifecycle

The repo must not mirror:

- the full `gstack` linked skill graph
- `gstack` internal handoff prose
- `gstack` internal report/log/dashboard mechanics
- `OpenSpec` change lifecycle or archive state machine

### Repo routing layer

Source of truth:

- `AGENTS.md`
- `goi-workflow/SKILL.md`
- `docs/ops/workflow/skill-routing.md`

This layer should answer only:

- the current GOI routing tuple:
  - `gstack stage`
  - `gstack status`: `required / inherited / skipped`
  - `OpenSpec` status: `required / inherited / skipped`
  - `self-improvement` status: `triggered / not-triggered`
- when `OpenSpec` status is not `skipped`, the active OpenSpec control surface (active change and relevant OpenSpec action)
- what repo-specific override or guardrail applies

### Project state layer

Source of truth:

- current program tracker
- current phase lock
- active change
- `.learnings/`

This layer should answer only:

- what is active now
- what is blocked now
- what the next bounded move is

### Decision layer

Source of truth:

- workflow ADRs in `docs/ops/workflow/decisions/`

This layer holds rationale and superseded decisions. It should not become the
day-to-day operating workflow.

## Consequences

Positive:

- less duplication of upstream process logic
- clearer separation between routing, state, and rationale
- lower risk that workflow docs become a second control plane
- easier to keep repo-local rules thin

Negative:

- readers may need one extra hop from operating docs to decision docs
- repo docs must be disciplined about not expanding the routing layer into a
  second workflow graph

## Rules Implied By This Decision

1. `workflow/README.md` and `workflow/skill-routing.md` are operating surfaces.
2. rationale-heavy documents belong under `workflow/decisions/`.
3. repo-local docs may name the current `gstack` stage and likely next
   `gstack` stage, but only inside an explicit GOI routing tuple and without rewriting the full upstream chain.
4. repo-local docs must continue to route the full GOI triad, not just `gstack`.
5. repo-local docs may summarize current program state, but must not re-create
   OpenSpec progress tracking or archive semantics.

## Review Trigger

Revisit this decision if:

- the same routing ambiguity repeats across multiple real rounds
- a second project state surface becomes necessary in practice
- upstream `gstack` or `OpenSpec` materially changes their lifecycle model
