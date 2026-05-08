## MODIFIED Requirements

### Requirement: The repo SHALL keep a current-state inventory

The repo SHALL maintain a current-state inventory that maps:

- shipped surfaces
- planned surfaces
- authoritative specs or contracts
- primary truth sources
- known gaps or follow-up surfaces

For the live host repo, the current-state inventory SHALL include the repo's
public identity, the current mainline it is actually hosting, and any shipped
optional lane surfaces that readers are expected to discover locally.

#### Scenario: Host repo inventory stays concrete after optional lane additions

- **WHEN** the host repo ships an optional execution or review lane surface
- **THEN** `openspec/specs/project-mainline-routing/spec.md` SHALL list that
  surface in the current shipped inventory when it is part of the repo
- **AND** the inventory SHALL still distinguish optional lanes from default
  routing or ownership surfaces
