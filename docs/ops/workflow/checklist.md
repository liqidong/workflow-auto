# Workflow Template Checklist

Use this checklist when copying `workflow-base` into a new repository.

## Files That Must Exist

- `AGENTS.md`
- `README.md`
- `.agents/skills/goi-workflow/SKILL.md`
- `.codex/skills/goi-workflow/SKILL.md`
- `docs/ops/workflow/README.md`
- `docs/ops/workflow/skill-routing.md`
- `docs/ops/workflow/routing-table.md`
- `docs/ops/workflow/evidence.md`
- `docs/ops/workflow/routing-checks.md`
- `docs/ops/workflow/multi-agent-execution.md`
- `openspec/specs/workflow-routing-policy/spec.md`
- `openspec/specs/project-mainline-routing/spec.md`

## Customization Checklist

- Replace generic repository positioning in `README.md`.
- Fill in `openspec/specs/project-mainline-routing/spec.md`.
- Confirm branch naming matches the real integration branch.
- Confirm `.agents` stays canonical and `.codex` stays compatibility-only.
- Confirm no domain-specific route names or absolute source-machine paths remain.

## Validation Commands

```text
scripts/verify-workflow-template.sh
./.venv/bin/pytest -q
openspec validate --specs
```
