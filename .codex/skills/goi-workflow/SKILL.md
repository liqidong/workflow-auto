---
name: goi-workflow
description: Compatibility entry for older or custom agents. Canonical repo-local GOI routing lives in .agents/skills/goi-workflow/SKILL.md.
---

# GOI Workflow Compatibility Shim

This `.codex` skill path is kept for compatibility with older local tooling and
repo history.

The canonical repo-local GOI workflow skill is:

- [.agents/skills/goi-workflow/SKILL.md](../../../.agents/skills/goi-workflow/SKILL.md)

Use the canonical skill for:

- light routing / heavy evidence mode selection
- GOI route traces
- hard gates
- evidence and skipped-verification requirements
- current repo mainline posture
- subagent task packet references

This compatibility shim does not replace, fork, or rewrite official skills. It
also does not duplicate the canonical route table, hard-gate list, or evidence
contract.

Related workflow docs:

- [docs/ops/workflow/skill-routing.md](../../../docs/ops/workflow/skill-routing.md)
- [docs/ops/workflow/routing-table.md](../../../docs/ops/workflow/routing-table.md)
- [docs/ops/workflow/evidence.md](../../../docs/ops/workflow/evidence.md)
- [docs/ops/workflow/routing-checks.md](../../../docs/ops/workflow/routing-checks.md)

