## Why

`workflow-auto` needs a documented and testable way to use a locally configured
Claude CLI + DeepSeek setup for bounded implementation and review work without
turning that setup into the repo's default workflow or secret-bearing config
surface.

## What Changes

- Add an optional model-diversity lane document for Claude CLI + DeepSeek.
- Add Claude agent role docs for bounded code writing, code review, debugging,
  and docs-consistency review.
- Add a safe placeholder example config and strengthen `.gitignore` so local
  secret-bearing files stay out of git.
- Update README, workflow indexes, checklist, and the shell verifier to include
  the optional lane surfaces.
- Add pytest contract tests and a secret-pattern scan for the new lane.

## Capabilities

### New Capabilities
- `optional-model-diversity`: optional Claude CLI + DeepSeek execution lane for
  bounded writer, reviewer, investigator, and docs-review work

### Modified Capabilities
- `project-mainline-routing`: current shipped-surface inventory now includes the
  optional model-diversity operating surfaces when present

## Impact

- `README.md`
- `.gitignore`
- `.claude/agents/**`
- optional example config under `.claude/`
- `docs/ops/workflow/*`
- `scripts/verify-workflow-template.sh`
- `tests/*`
- `openspec/specs/project-mainline-routing/spec.md`
