# Execution Quality Guardrails

Status: current operating surface

This document defines execution-quality guardrails for work that is already
inside a chosen route.

It is not a new workflow.

It does not replace:

- GOI routing
- OpenSpec
- `gstack`
- review
- QA

These guardrails constrain how implementation work is executed after route
selection and control-surface choice.

They do not create a new route.
They do not replace GOI routing, OpenSpec, `gstack`, review, or QA.

## Applies To

Use these guardrails during:

- implementation
- debugging
- hardening
- review-finding fixes
- blocker fixes

## Does Not Apply To

- trivial typo or path fixes do not need the full guardrail expansion
- read-only `assess` work should not pretend it is executing coding guardrails
- routing, planning, review, and QA still use their own canonical surfaces

## Think Before Coding

- do not hide assumptions
- state meaningful ambiguity before editing
- propose a simpler path when it would still satisfy the request
- if the critical facts are still unclear, stop and ask rather than guessing

## Simplicity First

- choose the smallest implementation that satisfies the goal
- do not add abstraction that was not requested
- do not add speculative flexibility
- avoid over-engineering when a direct change is sufficient

## Surgical Changes

- change only what the task actually requires
- do not bundle unrelated refactors
- do not opportunistically rewrite nearby formatting, comments, or adjacent code
- every changed line should be traceable to the user request, the active task,
  or a failed verification signal

## Goal-Driven Execution

- translate the task into a verifiable target
- phrase multi-step work as `action -> verification`
- for bug fixes, prefer reproduce -> fix -> regression verification
- completion still requires fresh evidence or explicit skipped verification
