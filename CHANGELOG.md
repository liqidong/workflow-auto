# Changelog

## Unreleased

### Added

- execution-quality guardrails for implementation, debugging, hardening,
  review-finding fixes, and blocker fixes

## 0.1.0 - 2026-05-09

### Added

- reusable workflow-base template hosted in workflow-auto
- canonical `.agents/skills/goi-workflow`
- `.codex` and `.claude` compatibility shims
- OpenSpec wrappers
- local host dependency check
- shell verifier
- pytest contract tests
- GitHub Actions verification
- bootstrap contract coverage

### Changed

- clarified workflow-auto vs workflow-base identity
- split route trace into short trace and full trace
- archived harden-template-contracts OpenSpec change
- pinned CI OpenSpec installation to `@fission-ai/openspec@1.3.1`

### Verification

- `scripts/check-host-workflow-deps.sh`
- `scripts/verify-workflow-template.sh`
- `./.venv/bin/pytest -q`
- `openspec validate --specs`
