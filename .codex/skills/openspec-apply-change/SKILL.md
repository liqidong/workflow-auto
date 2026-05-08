---
name: openspec-apply-change
description: Implement tasks from an OpenSpec change.
license: MIT
compatibility: Requires openspec CLI.
metadata:
  author: openspec
  version: "1.0"
  generatedBy: "1.3.1"
---

Implement tasks from an OpenSpec change.

## Flow

1. Select the change explicitly or infer it only when unambiguous.
2. Run `openspec status --change "<name>" --json`.
3. Run `openspec instructions apply --change "<name>" --json`.
4. Read every file listed in `contextFiles`.
5. Implement pending tasks in order, keeping changes scoped and minimal.
6. Mark each finished task in `tasks.md`.
7. Stop only when all tasks are done, the user interrupts, or a real blocker
   appears.

## Blocked States

If `openspec instructions apply` reports that the change is blocked by missing
artifacts:

- do not guess
- explain which artifacts are missing
- suggest returning to `openspec-propose` or updating the missing artifact
  directly

## Guardrails

- Always read the apply context files before coding.
- Pause if a task is unclear or implementation reveals a design mismatch.
- Suggest artifact updates when the spec and implementation stop matching.
- If all tasks are complete, suggest using `openspec-archive-change`.

