# project-mainline-routing Specification

## Purpose

Define how this repository states its current mainline, shipped surfaces,
planned surfaces, evidence lanes, and truth-source hierarchy.

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
