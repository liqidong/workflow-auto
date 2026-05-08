## ADDED Requirements

### Requirement: The repo SHALL support an optional model-diversity lane

The repo SHALL document Claude CLI + DeepSeek as an optional model-diversity
lane only.

That lane SHALL be downstream of repo-local GOI route selection and SHALL NOT
replace OpenSpec, `gstack`, review, or QA.

It MAY be used for bounded code writing, outside review, debugging
investigation, docs-consistency review, and low-risk implementation work inside
accepted scope.

It SHALL NOT be described as a mandatory or default workflow.

#### Scenario: Optional lane is invoked

- **WHEN** a reader or agent consults the model-diversity operating doc
- **THEN** they SHALL see that the lane is optional
- **AND** they SHALL see that route selection and final ownership remain with
  the main thread

### Requirement: DeepSeek Claude CLI SHALL remain non-final-owner even when used as a primary writer

The optional lane SHALL keep final ownership with the main thread even when it
uses Claude CLI + DeepSeek as a primary bounded code writer.

The main Codex or GPT thread SHALL remain responsible for:

- route selection
- acceptance
- final review
- merge decision
- tag or release decision

#### Scenario: Writer role is used

- **WHEN** the code-writer role is selected
- **THEN** it SHALL stay within accepted scope
- **AND** it SHALL run or report verification
- **AND** it SHALL stop and hand back to the main thread if scope changes

### Requirement: The optional lane SHALL preserve verification and secret safety

The optional lane SHALL NOT bypass verification, OpenSpec scope, or repo-local
secret handling.

The repo SHALL ignore local secret-bearing settings and `.env` files, and any
example settings file SHALL use placeholders only.

#### Scenario: Example settings are shipped

- **WHEN** the repo ships an example DeepSeek settings file
- **THEN** it SHALL contain placeholders only
- **AND** it SHALL NOT contain a real API key or committed local settings
