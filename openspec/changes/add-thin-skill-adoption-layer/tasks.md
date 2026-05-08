## 1. Capability Inventory

- [x] 1.1 Inventory the target superpowers skills and classify each one as `adopted`, `equivalent`, `excluded`, or `pending`.
- [x] 1.2 Record provenance for each targeted capability, including whether it comes from an existing host skill, a repo-local wrapper, or a vendored external source.

## 2. Descriptive Surfaces

- [x] 2.1 Add a descriptive analysis document under `docs/ops/` that explains the thin-skill adoption posture, route-to-skill mapping, and capability matrix.
- [x] 2.2 Keep the descriptive document outside `docs/ops/workflow/*` and state clearly that it is analysis, not workflow law.

## 3. Normative Workflow Updates

- [x] 3.1 Update the minimum workflow control surfaces needed to state that external skills remain downstream of repo-local route selection.
- [x] 3.2 Update `README.md` and `AGENTS.md` only where needed to describe the selective-adoption posture and expected dependencies.

## 4. Thin Compatibility Layer

- [x] 4.1 Identify high-friction external skill names that justify a local wrapper or alias.
- [x] 4.2 Implement only thin wrappers that redirect to canonical local entrypoints without copying a mandatory workflow chain.

## 5. Verification

- [x] 5.1 Add or update tests/checks that verify workflow control surfaces remain thin and do not embed a full superpowers methodology.
- [x] 5.2 Run OpenSpec validation and repo verification commands, and record any explicit skipped verification if a check cannot run.

Verification notes:

```yaml
verification_evidence:
  completed:
    - command_or_check: "./.venv/bin/pytest -q"
      result: "25 passed"
      evidence_artifact: "local pytest run in repo venv"
    - command_or_check: "scripts/verify-workflow-template.sh"
      result: "workflow template verification passed"
      evidence_artifact: "shell verifier"
    - command_or_check: "openspec validate add-thin-skill-adoption-layer"
      result: "Change is valid"
      evidence_artifact: "OpenSpec validation output"
```
