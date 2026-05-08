## MODIFIED Requirements

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

When external or vendored skills are adopted, they SHALL enter only after the
repo-local route is chosen and SHALL NOT replace repo-local route selection or
the GOI tuple.

#### Scenario: Route trace includes route mode and GOI tuple

- **WHEN** a non-trivial task starts
- **THEN** the agent SHALL report the route mode
- **AND** the agent SHALL report `gstack` posture, OpenSpec posture, active
  OpenSpec control surface when applicable, and triggered self-improvement
  handling when applicable

#### Scenario: External skill use stays downstream of routing

- **WHEN** an adopted external skill is relevant to the current task
- **THEN** the agent SHALL choose a repo-local route before invoking that skill
- **AND** the external skill SHALL be treated as an optional downstream
  execution aid or compatibility layer
- **AND** the external skill SHALL NOT silently impose a mandatory end-to-end
  workflow chain
