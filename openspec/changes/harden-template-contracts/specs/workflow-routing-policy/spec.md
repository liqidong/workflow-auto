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

Routine non-high-risk work MAY use a short visible trace of:

- `Route`
- `Why`
- `Evidence`

The full GOI trace SHALL be used for workflow or instruction changes,
architecture, security, deployment, data-contract work, blocker or correction
work, repeated failure, multi-agent launch, landing work, or when the user
explicitly asks for it.

#### Scenario: Routine work uses a short visible trace

- **WHEN** a task is low or medium risk and does not involve workflow-sensitive
  or landing conditions
- **THEN** the agent MAY report the route using the short trace
- **AND** the short trace SHALL still state route, reason, and evidence

#### Scenario: Full trace is used for high-risk or workflow-sensitive work

- **WHEN** the task changes workflow or instruction files, enters blocker
  conditions, launches multi-agent execution, or reaches landing
- **THEN** the agent SHALL report the full GOI trace
- **AND** that trace SHALL keep `gstack`, OpenSpec, and verification posture
  explicit
