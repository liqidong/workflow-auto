# Routing Snapshot Checks

Status: current operating surface

Purpose: prevent light routing from drifting into loose routing.

Run these checks mentally or in review whenever routing rules change.

| Case | Input | Expected route |
|---|---|---|
| High-risk workflow rule change | `task_kind=workflow`, `risk_level=high` | `full`; owner/review expected |
| Active OpenSpec implementation | `has_active_openspec=true`, `task_kind=implementation` | `light`; inherit OpenSpec |
| Active OpenSpec scope expansion | `has_active_openspec=true`, `scope_changed=true` | `full`; update control surface |
| Failing smoke | `problem_kind=blocker`, `has_reproduction=true` | `blocker`; investigate before fix |
| Same test fails twice | `repeated_failure=true` | `blocker` |
| User asks "review only" | `user_requested_no_write=true` | `assess` |
| README typo | `task_kind=documentation`, `risk_level=low` | `micro` |
| Architecture boundary change | `task_kind=architecture`, `risk_level=high` | `full` plus ADR/OpenSpec consideration |
| Release/archive | `task_kind=release` | `landing` |
| Unknown project state | `project_state=unknown` | `assess` first |
| Spec/code mismatch | `problem_kind=drift` | `blocker` or `full` before more implementation |
| Small local code cleanup | `risk_level=low`, no contract impact | `micro` or `light` with targeted check |
| Delegation-heavy launch candidate | accepted scope, concrete task packet, user not yet asked | keep route; ask before launch |
| Parallel writer suggestion with shared files | overlapping write set or shared integration file | refuse parallel dispatch |

## Table Change Checklist

- [ ] No high-risk case can route only to `micro`.
- [ ] No blocker/correction/repeated-failure case can skip investigation.
- [ ] Active OpenSpec implementation inherits rather than replans.
- [ ] Scope changes update the control surface before implementation.
- [ ] Release/archive remains `landing`.
- [ ] Unknown state starts read-only.
- [ ] Every route has minimum evidence.
- [ ] Optional delegation or parallel launch asks the user before startup.
- [ ] Parallel dispatch refuses shared-file or overlapping-write-set cases.
- [ ] Routing predicates stay declarative and are not executable code.
