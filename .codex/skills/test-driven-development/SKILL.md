---
name: test-driven-development
description: Thin compatibility wrapper. Use repo-local tests and pytest as a discipline aid without importing a mandatory foreign TDD chain.
---

# Test-Driven Development Compatibility Shim

For this repo, test-driven development is an optional discipline aid and is not mandatory as a foreign workflow.

Canonical local posture:

- route first with [`.agents/skills/goi-workflow/SKILL.md`](../../../.agents/skills/goi-workflow/SKILL.md)
- keep implementation inside the active OpenSpec change when one exists
- use repo-local tests as executable evidence
- use `./.venv/bin/pytest -q` as the stable local pytest entrypoint on this host

When using this shim:

- prefer writing or updating the narrowest failing test that captures the
  intended behavior
- make the minimal code change needed to satisfy that test
- finish with fresh verification evidence rather than a claim

This shim does not import a mandatory foreign TDD chain or delete code
automatically.
