# workflow-routing-policy Specification

## Purpose
Define the repo-local light-routing/heavy-evidence workflow policy, including
the canonical `.agents` GOI skill path, six route modes, hard gates, evidence
contract, and routing snapshot checks.
## Requirements
### Requirement: The repo SHALL expose a canonical GOI workflow skill under `.agents`

The repo SHALL expose the canonical repo-local GOI workflow skill at
`.agents/skills/goi-workflow/SKILL.md`.

The legacy `.codex/skills/goi-workflow/SKILL.md` path SHALL remain only as a
short compatibility shim that points to the canonical `.agents` skill and SHALL
NOT duplicate the route table, evidence contract, or hard-gate definitions.

#### Scenario: Codex skill discovery uses the canonical path

- **WHEN** a Codex agent starts in this repo and needs the GOI workflow skill
- **THEN** the canonical skill SHALL be available at
  `.agents/skills/goi-workflow/SKILL.md`
- **AND** the `.codex` skill surface SHALL identify itself as compatibility
  only

### Requirement: The repo SHALL define six light-routing modes

The repo SHALL define these route modes for non-trivial work:

- `assess`
- `micro`
- `light`
- `full`
- `blocker`
- `landing`

The route mode SHALL compose with, not replace, the GOI tuple fields for
`gstack`, OpenSpec, and triggered self-improvement.

#### Scenario: Route trace includes route mode and GOI tuple

- **WHEN** a non-trivial task starts
- **THEN** the agent SHALL report the route mode
- **AND** the agent SHALL report `gstack` posture, OpenSpec posture, active
  OpenSpec control surface when applicable, and triggered self-improvement
  handling when applicable

### Requirement: The repo SHALL enforce workflow hard gates declaratively

The workflow routing policy SHALL document hard gates that prevent unsafe route
selection.

At minimum:

- high-risk work cannot route to `micro`
- blocker, correction, or repeated-failure work must investigate before
  implementation
- active OpenSpec implementation inherits the active change and uses `light`
  unless scope changed
- instruction files are supply-chain sensitive
- routing predicates remain declarative and are not executable code

#### Scenario: High-risk work cannot use micro

- **WHEN** the task changes workflow rules, architecture, contracts, security,
  deployment, or production behavior
- **THEN** the route SHALL NOT be `micro`

#### Scenario: Blocker work investigates before implementation

- **WHEN** a task starts from a failing smoke, failing test, user correction,
  repeated failure, unexplained regression, or drift
- **THEN** the route SHALL require investigation before implementation

### Requirement: The repo SHALL require fresh evidence or explicit skipped verification

The workflow policy SHALL require fresh verification evidence before completion
claims for non-trivial work.

When a required verification cannot run, the closeout SHALL include an explicit
skipped-verification record with:

- `check`
- `reason`
- `residual_risk`
- `follow_up`

#### Scenario: Completion includes evidence

- **WHEN** a non-trivial task closes
- **THEN** the final report SHALL include fresh verification evidence
- **OR** it SHALL include a skipped-verification record with reason, residual
  risk, and follow-up

### Requirement: The repo SHALL provide routing snapshot checks

The workflow docs SHALL include manual routing snapshot checks covering high-risk
workflow changes, active OpenSpec implementation, active OpenSpec scope
expansion, failing smoke, repeated failure, review-only requests, README typo,
architecture boundary changes, release/archive, unknown project state, spec/code
mismatch, and small local code cleanup.

#### Scenario: Snapshot checks prevent route drift

- **WHEN** routing policy changes
- **THEN** the reviewer SHALL be able to check representative route cases in
  `docs/ops/workflow/routing-checks.md`
