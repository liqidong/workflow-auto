# Routing Decision Table

Status: current operating surface

Format: Markdown first. Do not convert this table to executable predicates
without explicit review.

## Precedence

```text
system/developer/tool constraints
> upstream skill safety rules once selected
> explicit user scope and intent
> repo routing hard gates
> decision table
> default preference
```

## Hard Gates

| Gate | Condition | Required route |
|---|---|---|
| G1 | `risk_level == high` | cannot be `micro`; usually `full` unless exact active control surface exists |
| G2 | `problem_kind in [blocker, regression, correction]` | `blocker` unless user explicitly requested read-only `assess` |
| G3 | `repeated_failure == true` | `blocker` |
| G4 | `user_requested_no_write == true` | `assess` |
| G5 | active OpenSpec covers exact implementation scope | `light`; inherit OpenSpec |
| G6 | active scope changed | `full`; update proposal/spec/plan first |
| G7 | release/deploy/archive requested | `landing` |
| G8 | instruction/workflow/routing files changed | at least `full` or explicit owner-reviewed route |

## Decision Table

| Priority | ID | When | Mode | Entry | OpenSpec posture | Minimum evidence | Reason |
|---:|---|---|---|---|---|---|---|
| 100 | repeated-failure | same check fails twice, unexplained regression, or user correction | `blocker` | investigate/root-cause | inherited if active, else skipped | reproduction, root-cause note, regression check | Stop guessing; establish cause before more edits. |
| 95 | explicit-readonly | user asks for analysis, review, research, or no-write work only | `assess` | read-only review/research | context only | inspected files/sources, uncertainty list | Respect no-write intent. |
| 90 | high-risk-new-scope | architecture, data contract, security/trust boundary, deployment, workflow rules, or production behavior changes | `full` | planning/review + OpenSpec or accepted equivalent | required unless already covered | proposal/design/tasks/spec delta, validation/review | High-risk work needs explicit control surface. |
| 85 | active-change-implementation | active OpenSpec or accepted plan covers requested implementation/debugging | `light` | apply active change / targeted implementation | inherited | targeted tests, smoke proof, OpenSpec validation if available | Contract already exists; avoid replanning. |
| 80 | scope-drift | implementation no longer matches spec/docs/tasks | `blocker` or `full` | drift check then update control surface | inherited, then update if needed | drift note, updated spec/tasks or rollback plan | Do not let code/spec silently diverge. |
| 75 | review-finding-fix | reviewer found bounded issue inside accepted scope | `light` | targeted fix | inherited if active | failing/review evidence, targeted check | Fix the finding without reopening full planning. |
| 70 | docs-low-risk | docs-only typo, path, formatting, or small clarification | `micro` | direct edit | skipped | markdown/path/link check where available | Keep small tasks small. |
| 65 | question-or-research | explanation, comparison, assessment, evidence gathering | `assess` | read-only research/review | context only | sources/files inspected, uncertainty list | No write needed. |
| 60 | release-closeout | PR, release, ship, deploy, archive, or final review | `landing` | review/ship/archive | inherited until archive | final checks, review result, archive/deploy decision | Landing is distinct from implementation. |
| 55 | unknown-state | insufficient repo context | `assess` | inspect first | unknown | project facts note | Inspect before choosing a write route. |
| 50 | low-risk-local-code | small reversible code change with no contract/security/runtime-wide effect | `micro` or `light` | direct edit or targeted implementation | skipped unless active | targeted unit/check | Avoid over-processing local changes. |
| 45 | fallback | none of the above match | `assess` | route recommendation | context only | findings + recommended next route | Safer to inspect than to invent a workflow. |

## Anti-Shadowing Checks

Before changing this table, verify:

- high-risk cannot match only `micro`
- blocker/correction/repeated failure cannot proceed straight to implementation
- active OpenSpec implementation chooses `light`, not `full`, unless scope changed
- docs-only low-risk edits can stay `micro`
- release/archive routes to `landing`
- unknown state starts with `assess`
- route predicates remain declarative Markdown and are not executable code
