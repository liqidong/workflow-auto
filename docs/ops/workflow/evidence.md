# Evidence Contract

Status: current operating surface

Principle: no completion claim without fresh evidence.

## Verification Evidence Template

Use this for non-trivial work:

```yaml
verification_evidence:
  required:
    - check:
      expected_signal:
  completed:
    - command_or_check:
      result:
      evidence_artifact:
  skipped:
    - check:
      reason:
      residual_risk:
      follow_up:
```

## Minimum Evidence By Route

| Route | Minimum evidence |
|---|---|
| `assess` | files/sources inspected, key findings, uncertainty list |
| `micro docs` | markdown/path/link check where available |
| `micro code` | targeted test, typecheck, or smallest executable check |
| `light implementation` | targeted tests plus smoke proof when behavior is affected |
| `light OpenSpec implementation` | targeted tests plus `openspec validate <change> --strict` when available |
| `full planning` | proposal/design/tasks/spec delta or accepted equivalent plus validation/review |
| `blocker` | reproduction evidence plus root-cause note plus regression check |
| `landing` | final test/review result plus archive/release/deploy decision |

## Skipped Verification

Skipping a check is allowed only when visible:

```yaml
skipped_verification:
  check:
  reason:
  residual_risk:
  follow_up:
```

Bad:

```text
Tests not run.
```

Good:

```yaml
skipped_verification:
  check: "./.venv/bin/pytest -q"
  reason: "The required GPU fixture is unavailable on this host."
  residual_risk: "GPU-only execution path is not proven locally."
  follow_up: "Run the same command on the normal GPU validation host."
```

## Root-Cause Evidence

For `blocker` mode, include:

```text
Symptom:
Reproduction:
Suspected cause:
Actual cause:
Fix:
Regression evidence:
```

## OpenSpec Drift Closeout

When OpenSpec is involved, close with:

```text
Active change:
Implementation summary:
Tasks completed with evidence:
Spec delta updated:
Validation:
Archive ready: yes/no
Residual risk:
```

For workflow-only changes, explicitly decide whether archive should apply specs
or use `--skip-specs`.

## Final Report Format

```text
Summary:
Route:
Files changed:
Verification:
Skipped verification:
Residual risk:
Follow-up:
```
