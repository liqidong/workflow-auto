## Why

The repo already has a thin-routing, heavy-evidence workflow, but it does not
yet define how to adopt useful capabilities from external skill libraries such
as `obra/superpowers` without letting an external methodology take over the
repo's routing posture. We need a sanctioned way to reuse high-value skill
capabilities while keeping `goi-workflow` as the canonical intake and control
surface.

## What Changes

- Define a selective external-skill adoption layer for the repo.
- Require external skill capabilities to be mapped, wrapped, or vendored
  without replacing repo-local routing, GOI reporting, or OpenSpec control.
- Add an auditable skill capability matrix that classifies targeted external
  skills as adopted, equivalent, excluded, or pending.
- Add a descriptive route-to-skill analysis surface outside the
  supply-chain-sensitive workflow control docs.
- Allow only thin compatibility wrappers for high-friction names and prohibit
  copying a full mandatory workflow chain into repo-local control surfaces.
- Add verification that the repo remains thin even after skill adoption work.

## Capabilities

### New Capabilities

- `external-skill-adoption`: selectively adopt useful external skill
  capabilities while preserving repo-local routing authority and thin workflow
  control surfaces

### Modified Capabilities

- `workflow-routing-policy`: clarify that adopted external skills remain
  downstream execution aids and SHALL NOT replace repo-local route selection or
  impose a mandatory workflow chain

## Impact

- `docs/ops/` descriptive workflow-analysis artifacts
- `docs/ops/workflow/` thin control surfaces and routing references
- repo-local skill wrappers or compatibility shims under `.agents`, `.codex`,
  or `.claude` when justified
- `README.md`, `AGENTS.md`, and tests that verify thinness and provenance
