## 1. OpenSpec And Launch Rules

- [x] 1.1 Add the `optional-agent-dispatch` capability spec and the workflow-routing-policy delta for explicit launch confirmation.
- [x] 1.2 Update `goi-workflow` so optional delegation and parallel dispatch are recommendation-first and require user confirmation before startup.

## 2. Task Packet And Workflow Docs

- [x] 2.1 Extend the subagent task packet with `Acceptance source`, `Review mode`, `Checkpoint trigger`, and `Parallel-safe`.
- [x] 2.2 Update `docs/ops/workflow/multi-agent-execution.md` with optional launch gates for single-writer delegation and parallel dispatch.
- [x] 2.3 Update `docs/ops/workflow/routing-checks.md` with snapshot cases for optional delegation and parallel-dispatch refusal.

## 3. Compatibility Shims And Adoption Docs

- [x] 3.1 Add thin `.codex` compatibility shims for `subagent-driven-development` and `dispatching-parallel-agents`.
- [x] 3.2 Update the Superpowers capability-adoption analysis to mark those names as opt-in adopted rather than excluded.

## 4. Verification

- [x] 4.1 Add or update tests to verify the opt-in launch rule, hard parallel checklist, and thin compatibility shims.
- [x] 4.2 Run `./.venv/bin/pytest -q`, `scripts/verify-workflow-template.sh`, and `openspec validate add-optional-agent-dispatch-modes`.

Verification notes:

```yaml
verification_evidence:
  completed:
    - command_or_check: "./.venv/bin/pytest -q"
      result: "29 passed"
      evidence_artifact: "local pytest run in repo venv"
    - command_or_check: "scripts/verify-workflow-template.sh"
      result: "workflow template verification passed"
      evidence_artifact: "shell verifier"
    - command_or_check: "openspec validate add-optional-agent-dispatch-modes"
      result: "Change is valid"
      evidence_artifact: "OpenSpec validation output"
```
