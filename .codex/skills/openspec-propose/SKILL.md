---
name: openspec-propose
description: Propose a new change and generate the artifacts needed to become apply-ready.
license: MIT
compatibility: Requires openspec CLI.
metadata:
  author: openspec
  version: "1.0"
  generatedBy: "1.3.1"
---

Propose a new change and create the minimum OpenSpec artifacts needed to become
apply-ready.

Artifacts usually include:

- `proposal.md`
- `design.md`
- `tasks.md`

## Flow

1. Get a change name or a concrete build/fix description from the user.
2. Create the scaffold with `openspec new change "<name>"`.
3. Inspect the artifact graph with `openspec status --change "<name>" --json`.
4. For each ready artifact, read
   `openspec instructions <artifact> --change "<name>" --json`.
5. Use the instruction template and dependency files to write the artifact.
6. Re-run `openspec status --change "<name>" --json` until every
   apply-required artifact is complete.
7. End by showing `openspec status --change "<name>"`.

## Guardrails

- Ask the user when the change goal is genuinely unclear.
- Prefer the current host's question or progress-tracking tools when available,
  but do not hardcode host-specific tool names into the workflow.
- Read dependency artifacts before creating a later artifact.
- Do not copy instruction metadata blocks into the output files.
- Stop once the change is ready for `openspec-apply-change`.

