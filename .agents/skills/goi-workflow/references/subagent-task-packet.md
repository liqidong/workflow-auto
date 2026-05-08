# Subagent Task Packet

Use this template whenever `goi-workflow` dispatches a coding, review, or verification subagent.

If you cannot fill these fields concretely, the task is not ready to delegate.

## Required Packet

```text
Goal:
<specific outcome only>

Owned files:
- path/to/file

Read context:
- path/to/doc-or-file

Do not touch:
- path/to/shared-file

Acceptance source:
- path/to/spec-or-task

Review mode:
- spec-compliance | code-quality | verification

Checkpoint trigger:
- what event hands control back to the main thread

Parallel-safe:
- yes | no

Assumptions / unknowns:
- ...

Stop and ask if:
- ...

Verification:
- <exact command or observable check>
- pass condition: <what counts as done>

Expected output:
- changed files
- commands run
- test results
- blockers
- residual risks
```

## Repo-Specific Defaults

### Main-thread-only by default

Unless explicitly delegated, keep these in the main thread:

- `openspec/changes/**`
- shared integration files such as orchestrators and report compilers
- top-level repo docs like `README.md`
- final commit and push decisions

### Allowed subagent types

- read-only explorer
- milestone-scoped bounded implementer
- fresh read-only reviewer
- focused tester or benchmark runner

### Lifecycle defaults

- keep the main thread long-lived
- reuse one writer only within one coherent milestone
- create a fresh reviewer for each checkpoint, then close it after findings are consumed
- create explorer/docs agents on demand, then close them
- do not keep reviewer threads alive as a standing approval loop

### Parallelism

At most two code-writing implementers at once, and only when:

- write sets are disjoint
- each writer has a separate worktree
- integration ownership is clear
- the main thread is not blocked on both results simultaneously

Otherwise use one implementer and only the read-only reviewers/explorers actually needed for the current checkpoint.

### Return format

```text
Status: done | blocked | needs-main-thread-decision

What changed:
- ...

Files touched:
- ...

Verification:
- `command or observable check` -> pass|fail
- pass condition satisfied: yes|no

Open risks:
- ...

Questions for main thread:
- ...
```

## Common Failure Modes To Guard Against

- wrong worktree or branch
- shared-file edits by a worker that only owned a private module
- OpenSpec task checkboxes updated by the wrong thread
- missing acceptance source or review mode in the packet
- parallel-safe marked implicitly instead of explicitly
- vague verification like "pytest" instead of the exact focused command
- claiming completion from local verification only
