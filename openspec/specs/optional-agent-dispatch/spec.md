# optional-agent-dispatch Specification

## Purpose
TBD - created by archiving change add-optional-agent-dispatch-modes. Update Purpose after archive.
## Requirements
### Requirement: Optional delegation-heavy execution SHALL require explicit user launch confirmation

The repo SHALL allow delegation-heavy execution patterns only as optional start
modes. When the workflow recommends such a mode, it SHALL ask the user whether
to start it before launching a writer or reviewer topology that is not already
the current default.

#### Scenario: Delegation-heavy mode is a good fit

- **WHEN** the route, acceptance source, and task packet are concrete enough to
  support a bounded delegated implementation
- **THEN** the workflow MAY recommend starting a delegation-heavy execution mode
- **AND** it SHALL ask the user for confirmation before launching that mode

### Requirement: Parallel writer dispatch SHALL satisfy a hard launch checklist

The repo SHALL allow parallel writer dispatch only when the write sets are
disjoint, each writer has a separate worktree, main-thread integration
ownership is explicit, and the main thread is not blocked on both results
simultaneously.

#### Scenario: Parallel writer dispatch is requested

- **WHEN** a user or workflow suggests parallel writer dispatch
- **THEN** the repo SHALL check the hard launch checklist before startup
- **AND** it SHALL refuse parallel writer launch when any checklist condition is
  not satisfied

### Requirement: Delegated task packets SHALL carry acceptance and checkpoint metadata

Delegated task packets SHALL include acceptance source, review mode,
checkpoint trigger, and parallel-safety metadata before a worker is launched.

#### Scenario: A worker packet is prepared for launch

- **WHEN** the repo prepares a delegated coding or review task packet
- **THEN** the packet SHALL identify the acceptance source and review mode
- **AND** it SHALL identify whether the work is parallel-safe
- **AND** it SHALL identify what event triggers the next checkpoint

