## MODIFIED Requirements

### Requirement: The repo SHALL keep a current-state inventory

The repo SHALL maintain a current-state inventory that maps:

- shipped surfaces
- planned surfaces
- authoritative specs or contracts
- primary truth sources
- known gaps or follow-up surfaces

For the live host repo, the current-state inventory SHALL include the repo's
public identity and the current mainline it is actually hosting.

#### Scenario: Host repo inventory is concrete

- **WHEN** a reader opens `openspec/specs/project-mainline-routing/spec.md`
- **THEN** they SHALL be able to identify the public repo name, reusable
  template name, current mainline, shipped surfaces, planned surfaces, support
  lanes, and truth-source hierarchy
- **AND** they SHALL not see only abstract adopter guidance
