# 0003: Event-Driven Self-Improvement Rail

Status: accepted
Date: 2026-04-24

## Context

This workflow template already keeps repo workflow thin and preserves a
quality-first multi-agent default.

The remaining ambiguity is how `self-improvement` should appear in routine GOI
updates. Recent repo-local routing examples often required a visible
`self-improvement: not-triggered` line even when nothing meaningful happened.
That created three problems:

- routine updates became noisier without adding decision value
- `self-improvement` looked like an always-on parallel control plane
- repo docs risked implying workflow semantics that belong to the upstream
  `self-improvement` skill itself

At the same time, the repo still needs a durable way to surface real failures,
corrections, stable new rules, and explicit workflow-audit outcomes.

## Decision

The repo keeps `self-improvement` in the GOI model, but treats it as an
event-driven recording rail rather than a routine status line.

Routine non-trivial routing updates must explicitly report:

- `gstack` stage and status
- `OpenSpec` status
- the active OpenSpec control surface when `OpenSpec` is not `skipped`

Routine updates do not need a visible `self-improvement: not-triggered` line.

`self-improvement` must be surfaced when one of the following occurs:

- a real failure was reproduced or corrected
- a durable new rule or guardrail was learned
- the task explicitly audits workflow hygiene
- the user explicitly asks for `self-improvement` capture

When surfaced, the update should state:

- the triggering event
- whether durable recording was written
- where the durable recording lives if one was created

This decision changes repo-local routing posture only. It does not modify the
underlying capabilities or official semantics of `gstack`, `OpenSpec`, or
`self-improvement`.

## Consequences

Positive:

- routine workflow updates stay thinner and easier to scan
- real learning events become more salient
- repo-local docs stay aligned with the thin-routing model

Negative:

- readers must understand that an omitted `self-improvement` line usually means
  "no triggered event", not "the rail no longer exists"
- workflow audits now need to be explicit when they want `self-improvement`
  surfaced

## Rules Implied By This Decision

1. Repo-local routing docs should describe `self-improvement` as conditional and
   event-driven.
2. Triggered `self-improvement` events must not be silently omitted.
3. Repo docs must not present this change as an upstream skill rewrite.
4. `.learnings/` remains the repo-local durable capture surface when a learning
   is worth recording.

## Relationship To Earlier Decisions

This decision clarifies and supersedes the routine `self-improvement` status
examples from [0001-thin-routing-over-full-workflow.md](0001-thin-routing-over-full-workflow.md)
without changing the thin-layer model itself.

## Review Trigger

Revisit this decision if:

- repeated real rounds show that hidden non-events create operator confusion
- the upstream `self-improvement` skill changes its expected reporting posture
- the repo adopts a different durable learning surface than `.learnings/`
