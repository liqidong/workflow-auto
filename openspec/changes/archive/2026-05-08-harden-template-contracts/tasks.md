## 1. Identity And Mainline Inventory

- [x] 1.1 Clarify that `workflow-auto` hosts the reusable `workflow-base`
  template across README, AGENTS, pyproject, and workflow docs.
- [x] 1.2 Fill `openspec/specs/project-mainline-routing/spec.md` with the live
  current-mainline inventory, shipped surfaces, planned surfaces, support
  lanes, and truth-source hierarchy.

## 2. Executable Template Surfaces

- [x] 2.1 Reconcile README promises with actual compatibility surfaces,
  including a thin `.claude` GOI shim.
- [x] 2.2 Add `scripts/check-host-workflow-deps.sh` and wire it into the
  checklist and verification chain.
- [x] 2.3 Split route reporting into default short trace and conditional full
  trace on the canonical workflow surfaces.
- [x] 2.4 Add recovery rules and learning-capture guidance without expanding
  the route model.

## 3. Contract Verification

- [x] 3.1 Strengthen `scripts/verify-workflow-template.sh` for repo identity,
  required files, and current-mainline headings.
- [x] 3.2 Add or update pytest contract tests for route consistency, shim
  thinness, README/file alignment, and current-mainline inventory.

## 4. Verification

- [x] 4.1 Run `scripts/check-host-workflow-deps.sh`.
- [x] 4.2 Run `scripts/verify-workflow-template.sh`.
- [x] 4.3 Run `./.venv/bin/pytest -q`.
- [x] 4.4 Run `openspec validate --specs`.

Verification notes:

```yaml
verification_evidence:
  completed:
    - command_or_check: "scripts/check-host-workflow-deps.sh"
      result: "host workflow dependency check passed"
      evidence_artifact: "local host dependency probe"
    - command_or_check: "scripts/verify-workflow-template.sh"
      result: "workflow-auto template verification passed"
      evidence_artifact: "shell verifier"
    - command_or_check: "./.venv/bin/pytest -q"
      result: "37 passed"
      evidence_artifact: "local pytest contract suite"
    - command_or_check: "openspec validate --specs"
      result: "2 passed, 0 failed"
      evidence_artifact: "OpenSpec spec validation output"
```
