## 1. OpenSpec And Lane Contract

- [x] 1.1 Add the `optional-model-diversity` capability spec and the
  `project-mainline-routing` delta for shipped-surface inventory updates.
- [x] 1.2 Keep the lane explicitly optional and downstream of GOI routing,
  OpenSpec, `gstack`, review, and QA.

## 2. Optional Lane Surfaces

- [x] 2.1 Add `docs/ops/workflow/model-diversity.md` for the optional Claude
  CLI + DeepSeek lane.
- [x] 2.2 Add bounded `.claude/agents/` role docs for writer, reviewer,
  investigator, and docs review.
- [x] 2.3 Add a placeholder-only `.claude/settings.deepseek.example.json` and
  ignore local secret-bearing config files.

## 3. Indexes And Verification

- [x] 3.1 Update README, workflow indexes, checklist, and shipped-surface
  inventory to include the optional lane surfaces.
- [x] 3.2 Update `scripts/verify-workflow-template.sh` and add pytest contract
  tests for the optional lane and secret-safety rules.

## 4. Verification

- [x] 4.1 Run the required verification chain and the requested secret-pattern
  scan.
- [x] 4.2 Record verification evidence or explicit skipped verification.

Verification notes:

```yaml
verification_evidence:
  completed:
    - command_or_check: "rg -n \"sk-|DEEPSEEK_API_KEY|ANTHROPIC_AUTH_TOKEN|api.deepseek.com|deepseek-v4|settings.local\" ."
      result: "Only placeholder values, variable names, example endpoints/models, verifier/test references, and existing non-secret local-settings path references were found"
      evidence_artifact: "secret-pattern scan output"
    - command_or_check: "scripts/check-host-workflow-deps.sh"
      result: "host workflow dependency check passed"
      evidence_artifact: "local shell output"
    - command_or_check: "scripts/verify-workflow-template.sh"
      result: "workflow-auto template verification passed"
      evidence_artifact: "shell verifier"
    - command_or_check: "./.venv/bin/pytest -q"
      result: "68 passed"
      evidence_artifact: "local pytest run in repo venv"
    - command_or_check: "openspec validate --specs"
      result: "4 passed, 0 failed"
      evidence_artifact: "OpenSpec live spec validation output"
    - command_or_check: "openspec validate add-optional-model-diversity-lane"
      result: "Change is valid"
      evidence_artifact: "OpenSpec change validation output"
```
