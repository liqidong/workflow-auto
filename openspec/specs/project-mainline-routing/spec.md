# project-mainline-routing Specification

## Purpose

Define how this repository states its current mainline, shipped surfaces,
planned surfaces, evidence lanes, and truth-source hierarchy.

## Current Repository Identity

- Public repository name: `workflow-auto`
- Reusable template name: `workflow-base`
- Current repo role: host, verify, and harden the reusable template itself

## Current Mainline

This repository hosts a reusable thin-routing, heavy-evidence workflow
template for agentic repository work.

The current mainline is the template's own auditable operating surface:
canonical routing skill, compatibility shims, OpenSpec wrappers, workflow
docs, verification scripts, and contract tests.

## Shipped Surfaces

- `.agents/skills/goi-workflow/SKILL.md`
- `.codex/skills/goi-workflow/SKILL.md`
- `.claude/skills/goi-workflow/SKILL.md`
- OpenSpec wrapper skills under `.codex/skills/openspec-*`
- OpenSpec wrapper skills under `.claude/skills/openspec-*`
- workflow docs under `docs/ops/workflow/`
- `scripts/check-host-workflow-deps.sh`
- `scripts/verify-workflow-template.sh`
- pytest contract tests under `tests/`
- live OpenSpec specs under `openspec/specs/`

## Planned Surfaces

- CI validation for the same local verification chain
- broader contract tests for future compatibility shims and adoption edges
- a copy/bootstrap checklist that can be reused outside this host repo without
  manual pruning

## Evidence-only / Support Lanes

- `.learnings/`
- `docs/ops/superpowers-capability-adoption.md`
- `docs/ops/workflow/multi-agent-execution.md`
- `docs/ops/agent-orchestration-feedback.md`

## Truth Source Hierarchy

1. `README.md` for repository identity and current mainline summary
2. `openspec/specs/project-mainline-routing/spec.md` for current inventory and
   truth-source hierarchy
3. `.agents/skills/goi-workflow/SKILL.md` for canonical route selection and
   evidence posture
4. `openspec/specs/workflow-routing-policy/spec.md` for normative routing
   requirements
5. `docs/ops/workflow/routing-table.md` and `docs/ops/workflow/evidence.md`
   for auditable operating detail
6. `AGENTS.md` for repo-default posture and operator reminders
7. compatibility shims under `.codex` and `.claude` for discovery only

## Requirements

### Requirement: The repo SHALL define a current mainline explicitly

The repo SHALL define what is currently considered the mainline.

That mainline MAY be a product surface, platform surface, library surface, or
internal workflow surface, but it SHALL be stated explicitly in:

- the repository `README.md`
- this specification

#### Scenario: New reader finds the mainline

- **WHEN** a reader starts from the repository entry documentation
- **THEN** they SHALL be able to identify the current mainline quickly
- **AND** they SHALL not have to infer it from scattered historical docs

### Requirement: The repo SHALL distinguish shipped, planned, and evidence-only work

The repo SHALL distinguish:

- shipped or currently supported surfaces
- planned but not yet shipped surfaces
- optimization, research, or evidence lanes that are not the current mainline

#### Scenario: Scope is read correctly

- **WHEN** a new implementation round starts
- **THEN** the implementer SHALL be able to tell which surfaces are already
  supported
- **AND** which surfaces are still planned
- **AND** which work streams are support lanes rather than mainline gates

### Requirement: The repo SHALL preserve public surface names

The repo SHALL preserve public route names, commands, APIs, or package names in
mainline documentation when those surfaces are already exposed publicly.

The repo SHALL NOT silently replace a shipped public name with internal
shorthand when documenting the active posture.

#### Scenario: Public naming stays stable

- **WHEN** mainline documentation is updated
- **THEN** it SHALL use the public names that callers actually see
- **AND** it SHALL mark planned names as planned until implementation lands

### Requirement: The repo SHALL identify authoritative truth sources

The repo SHALL define its truth-source hierarchy.

Machine-readable records SHOULD be preferred where they exist. Narrative docs,
screenshots, or proof notes MAY support review but SHALL NOT silently override a
more authoritative source.

#### Scenario: Evidence conflicts

- **WHEN** display evidence conflicts with a stronger machine-readable source
- **THEN** the stronger source SHALL be treated as authoritative
- **AND** the weaker evidence SHALL be treated as stale, incomplete, or support
  evidence until reconciled

### Requirement: The repo SHALL keep a current-state inventory

The repo SHALL maintain a current-state inventory that maps:

- shipped surfaces
- planned surfaces
- authoritative specs or contracts
- primary truth sources
- known gaps or follow-up surfaces

#### Scenario: Future work starts from the inventory

- **WHEN** a later change starts
- **THEN** the implementer SHALL be able to identify current support, planned
  work, and authoritative evidence without reading archive history first
