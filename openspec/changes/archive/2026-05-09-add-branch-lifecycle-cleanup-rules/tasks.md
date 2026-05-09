## 1. Branch Lifecycle Policy

- [x] 1.1 Add the `branch-lifecycle-policy` capability spec.
- [x] 1.2 Document the cleanup rule for merged `feat/*` branches and the
  exemption for long-lived `lane/*` branches.

## 2. Branching Surfaces

- [x] 2.1 Update `AGENTS.md`, `README.md`, and
  `docs/ops/git-worktree-layout.md` with explicit post-merge cleanup guidance.
- [x] 2.2 Update the workflow checklist so adopters know to preserve the
  `feat/*` versus `lane/*` lifecycle distinction.

## 3. Verification

- [x] 3.1 Update `scripts/verify-workflow-template.sh` and add pytest contract
  coverage for the branch lifecycle policy.
- [x] 3.2 Run the normal verification chain and record evidence.

Verification notes:

```yaml
verification_evidence:
  completed:
    - command_or_check: "openspec validate add-branch-lifecycle-cleanup-rules"
      result: "Change is valid"
      evidence_artifact: "OpenSpec change validation output"
    - command_or_check: "scripts/check-host-workflow-deps.sh"
      result: "host workflow dependency check passed"
      evidence_artifact: "local shell output"
    - command_or_check: "scripts/verify-workflow-template.sh"
      result: "workflow-auto template verification passed"
      evidence_artifact: "shell verifier"
    - command_or_check: "./.venv/bin/pytest -q"
      result: "62 passed"
      evidence_artifact: "local pytest run in repo venv"
    - command_or_check: "openspec validate --specs"
      result: "4 passed, 0 failed"
      evidence_artifact: "OpenSpec live spec validation output"
```
