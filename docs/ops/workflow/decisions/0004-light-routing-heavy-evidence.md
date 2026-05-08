# 0004: Light Routing Heavy Evidence Workflow Adapter

Status: accepted
Date: 2026-04-27

## Context

The repo already uses thin GOI routing over upstream `gstack`, OpenSpec, and
self-improvement. The remaining drift is that route names, evidence rules,
skipped-verification handling, and Codex repo skill discovery are not
centralized.

Current Codex repository skill discovery uses `.agents/skills`. The repo's
existing GOI skill lived under `.codex/skills`, which preserved local history
but risked silent non-discovery or duplicate mutable instruction surfaces.

## Decision

The repo adopts `.agents/skills/goi-workflow/SKILL.md` as the canonical
repo-local Codex skill.

The repo keeps `.codex/skills/goi-workflow/SKILL.md` only as a short
compatibility shim for older local tooling and custom agents.

The repo exposes six route names:

- `assess`
- `micro`
- `light`
- `full`
- `blocker`
- `landing`

Detailed route precedence belongs in `routing-table.md`. Evidence requirements
belong in `evidence.md`. Snapshot drift checks belong in `routing-checks.md`.
`AGENTS.md` stays short and policy-level.

The route mode composes with the GOI tuple. It does not replace `gstack`
posture, OpenSpec posture, active control-surface reporting, or triggered
self-improvement handling.

## Consequences

Positive:

- Codex skill discovery follows the current repo-scoped `.agents/skills` path.
- Older local tooling can still find `.codex/skills/goi-workflow/SKILL.md`.
- Route selection is easier to audit.
- Completion claims require fresh evidence or explicit skipped-verification
  records.

Negative:

- There are more workflow files to keep coherent.
- Text-policy tests must avoid becoming brittle.
- The `.codex` shim must stay short; otherwise it becomes a second instruction
  source.

## Rules Implied By This Decision

1. `.agents/skills/goi-workflow/SKILL.md` is canonical.
2. `.codex/skills/goi-workflow/SKILL.md` is compatibility only.
3. Route predicates remain declarative Markdown, not executable code.
4. `AGENTS.md` should link and summarize, not carry the full route table.
5. High-risk, blocker, active OpenSpec, release, and unknown-state routes must
   be covered by routing snapshot checks.

## Review Trigger

Revisit this decision if:

- Codex changes repo-scoped skill discovery semantics
- `.codex` compatibility stops being used
- route ambiguity repeats despite the six-mode vocabulary
- routing docs begin duplicating upstream `gstack` or OpenSpec lifecycle logic
