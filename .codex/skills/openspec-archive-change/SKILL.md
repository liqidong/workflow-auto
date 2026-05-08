---
name: openspec-archive-change
description: Archive a completed change with the official OpenSpec CLI.
license: MIT
compatibility: Requires openspec CLI.
metadata:
  author: openspec
  version: "1.0"
  generatedBy: "1.3.1"
---

Archive a completed change with the official OpenSpec CLI.

## Flow

1. Select the change explicitly unless only one active change exists.
2. Inspect `openspec status --change "<name>" --json`.
3. Check for incomplete artifacts or unchecked tasks and warn before
   continuing.
4. Decide whether the change should archive normally or use `--skip-specs` for
   workflow-only, documentation-only, or infrastructure-only changes.
5. Run:

```text
openspec archive "<name>"
```

or:

```text
openspec archive "<name>" --skip-specs
```

Use `--no-validate` only as an explicit fallback when the user accepts the
risk.

## Guardrails

- Prefer the official `openspec archive` flow over manual file moves.
- Do not assume spec syncing needs a separate helper skill.
- Make the `--skip-specs` decision explicit in the final summary.

