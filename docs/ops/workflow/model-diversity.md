# Model Diversity Lane

Claude CLI + DeepSeek is an optional model-diversity lane.

This document defines execution-quality guardrails for using that lane after route
selection. It does not create a new route and does not replace GOI routing,
OpenSpec, `gstack`, review, or QA. It is not the repo's default workflow.

## Positioning

Use this lane only as an optional execution aid when the main thread has
already selected the route and locked the active control surface.

DeepSeek Claude CLI may be a primary writer, but not the final owner.

The Codex or GPT main thread still owns:

- route selection
- acceptance
- final review
- merge decision
- tag or release decision

## Good Fits

Claude CLI + DeepSeek may be used for:

- primary bounded code writer
- outside reviewer
- debug investigator
- docs consistency reviewer
- low-risk implementation candidate inside accepted scope

The bounded writer path should still follow
[execution-quality.md](./execution-quality.md).

## Not For

Claude CLI + DeepSeek must not be used to:

- bypass GOI routing
- bypass OpenSpec
- bypass verification
- become the default parallel writer
- become the final merge or release owner
- write shared files without explicit ownership
- commit local secrets

## Role Boundaries

- `code-writer`: may write code only inside accepted scope and must verify
  or report skipped verification
- `code-reviewer`: read-only outside reviewer for bounded findings
- `debug-investigator`: reproduce first, then isolate the cause, then propose
  or implement the minimal fix
- `docs-reviewer`: read-only consistency reviewer for docs and verification
  surfaces

## Local Config Posture

This repo does not commit a real `.claude/settings.local.json`.

If a local setup uses Claude CLI + DeepSeek, keep the actual settings file
local-only and use `.claude/settings.deepseek.example.json` for placeholders
only.

## When Not To Expand This Lane

- trivial typo or one-line path fix
- read-only `assess` work
- any task where the active scope is unclear
- any task that has already crossed into repeated-failure or `blocker`
  conditions without a fresh main-thread decision
