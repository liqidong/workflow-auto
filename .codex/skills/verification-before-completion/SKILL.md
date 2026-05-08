---
name: verification-before-completion
description: Thin compatibility wrapper. Use the repo's fresh-evidence contract before claiming completion.
---

# Verification Compatibility Shim

This repo already has a native verification contract.

Use:

- [docs/ops/workflow/evidence.md](../../../docs/ops/workflow/evidence.md)
- [`.agents/skills/goi-workflow/SKILL.md`](../../../.agents/skills/goi-workflow/SKILL.md)

Minimum local rule:

- no completion claim without fresh evidence
- if a required check cannot run, record explicit `skipped_verification`

Use route-appropriate execution aids such as `review`, `qa`, `ship`, or
targeted tests as needed.

This shim does not create a second verification policy.
It also does not import a mandatory foreign completion workflow.
