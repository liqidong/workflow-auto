## ADDED Requirements

### Requirement: The repo SHALL distinguish short-lived feature branches from long-lived lane branches

The repo SHALL distinguish bounded `feat/*` branches from long-lived `lane/*`
branches in its branch policy.

`feat/*` branches SHALL be treated as the default short-lived implementation
branch type.

`lane/*` branches SHALL be treated as long-lived support lanes that are not
subject to the short-lived `feat/*` cleanup rule by default.

#### Scenario: Reader checks branch roles

- **WHEN** a reader consults the branch policy
- **THEN** they SHALL be able to tell that `feat/*` is short-lived
- **AND** they SHALL be able to tell that `lane/*` is long-lived

### Requirement: Merged feature branches SHALL have an explicit cleanup policy

The repo SHALL direct maintainers to clean up a bounded `feat/*` branch after
it is verified, merged back to `main`, and no longer needed.

That cleanup SHALL cover:

- local feature branch deletion
- remote feature branch deletion when no longer needed
- removal of the corresponding worktree

#### Scenario: Finished feature branch is published

- **WHEN** a verified `feat/*` branch is merged into `main`
- **THEN** the branch policy SHALL instruct maintainers to delete the local
  feature branch when it is no longer needed
- **AND** it SHALL instruct maintainers to delete the remote feature branch
  when it is no longer needed
- **AND** it SHALL instruct maintainers to remove the corresponding worktree
