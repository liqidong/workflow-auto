# external-skill-adoption Specification

## Purpose
TBD - created by archiving change add-thin-skill-adoption-layer. Update Purpose after archive.
## Requirements
### Requirement: Selective external skill adoption SHALL preserve repo-local routing authority

The repo SHALL support adopting capabilities inspired by external skill
libraries through selective mapping, wrapping, or vendoring. The repo SHALL NOT
require installing a full external methodology that automatically replaces
repo-local route selection, GOI reporting, or OpenSpec control surfaces.

#### Scenario: Direct install would impose a competing methodology

- **WHEN** an external skill package would automatically activate a mandatory
  end-to-end workflow chain
- **THEN** the repo SHALL reject direct adoption of that package as the default
  workflow surface
- **AND** the repo SHALL prefer selective mapping, wrapping, or vendoring of
  only the needed capabilities

### Requirement: The repo SHALL maintain an auditable capability matrix

The repo SHALL maintain an auditable inventory of targeted external skill
capabilities. Each capability entry SHALL identify its status as `adopted`,
`equivalent`, `excluded`, or `pending`, and SHALL record its provenance.

#### Scenario: A user asks whether a referenced external skill exists locally

- **WHEN** a user asks for a skill that is known from an external library
- **THEN** the repo SHALL be able to identify whether that capability is
  locally available, mapped to an equivalent, intentionally excluded, or still
  pending
- **AND** the repo SHALL be able to show where that conclusion came from

### Requirement: Descriptive skill analysis SHALL stay outside the workflow control surface

The repo SHALL keep expanded route-to-skill mapping, capability comparison, and
source-analysis documents outside `docs/ops/workflow/*` unless those documents
are changing normative workflow policy.

#### Scenario: Skill commentary is added for operator guidance

- **WHEN** the repo adds a document that compares local workflow behavior to an
  external skill library
- **THEN** that document SHALL be stored outside the normative workflow control
  surface by default
- **AND** it SHALL identify itself as descriptive analysis rather than workflow
  law

### Requirement: Thin compatibility wrappers SHALL preserve canonical entrypoints

Any repo-local wrapper or alias created for an adopted external skill name SHALL
redirect to the canonical local entrypoint or policy surface. The wrapper SHALL
NOT duplicate a full external workflow chain or replace the canonical
`goi-workflow` intake.

#### Scenario: A compatibility wrapper is created for a familiar external name

- **WHEN** the repo adds a wrapper for an external skill name
- **THEN** the wrapper SHALL remain thin enough to audit easily
- **AND** it SHALL point callers back to the repo's canonical routing and
  execution surfaces
- **AND** it SHALL NOT silently install or invoke a mandatory foreign workflow

