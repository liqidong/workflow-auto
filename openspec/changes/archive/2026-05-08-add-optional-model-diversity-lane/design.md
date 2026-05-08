## Overview

This change adds a model-diversity lane for repositories that already run
Claude CLI against a DeepSeek-compatible Anthropic endpoint locally. The repo
will document that lane, index it in the shipped surfaces, and test its guard
rails, but it will not create a new route, new default executor, or committed
local settings file.

## Design Decisions

### Optional lane, not workflow replacement

The new lane lives under `docs/ops/workflow/model-diversity.md` and `.claude`
agent docs. It is downstream of GOI route selection and OpenSpec control
surfaces. The main thread still owns route selection, acceptance, final review,
merge, and release decisions.

### Bounded Claude agent roles

Four `.claude/agents/` role docs are added:

- `code-writer`
- `code-reviewer`
- `debug-investigator`
- `docs-reviewer`

These roles are intentionally scoped:

- writer work stays inside accepted scope and must verify its own changes
- reviewer/docs roles default to read-only behavior
- investigator work starts from reproduction and escalates repeated failure to
  `blocker`

### Secret-safe example only

The repo will not read, write, or commit `.claude/settings.local.json`.
Instead, it may ship `.claude/settings.deepseek.example.json` with placeholders
only, plus `.gitignore` rules for local settings and `.env` patterns.

### Testable contract

The lane is enforced by documentation, shell verification, pytest contracts,
and a simple secret-pattern scan. No external runtime dependency or host
configuration mutation is introduced.

## Affected Surfaces

- `README.md`
- `.gitignore`
- `.claude/agents/*.md`
- `.claude/settings.deepseek.example.json`
- `docs/ops/workflow/model-diversity.md`
- `docs/ops/workflow/README.md`
- `docs/ops/workflow/checklist.md`
- `scripts/verify-workflow-template.sh`
- `openspec/specs/project-mainline-routing/spec.md`
- `tests/test_model_diversity_lane.py`

## Non-Goals

- changing GOI route modes
- replacing OpenSpec, `gstack`, review, or QA
- making Claude CLI + DeepSeek the default main-thread executor
- committing real API keys or local settings
