# workflow-auto

[![Verify](https://github.com/liqidong/workflow-auto/actions/workflows/verify.yml/badge.svg)](https://github.com/liqidong/workflow-auto/actions/workflows/verify.yml)

`workflow-auto` is the repository that hosts the reusable `workflow-base`
template.

The template is a thin-routing, heavy-evidence workflow scaffold for agentic
repository work. This host repo hardens and verifies that template so it can be
copied, audited, and adapted without guessing the mainline.

## Repository Identity

- Public repository name: `workflow-auto`
- Reusable template name: `workflow-base`
- Current mainline: the reusable thin-routing, heavy-evidence workflow template
  itself

## Daily Usage

- Question, review, research, or route recommendation -> `assess`
- Tiny docs typo or path fix -> `micro`
- Implementation inside accepted scope -> `light`
- New feature, architecture change, workflow rule, or contract change -> `full`
- Failing test, user correction, or repeated failure -> `blocker`
- PR, release, archive, deploy, or closeout -> `landing`

Examples:

- `"review this repo"` -> `assess`
- `"fix this failing test"` -> `blocker`
- `"implement this active OpenSpec change"` -> `light`
- `"add a new feature"` -> `full`
- `"prepare release/archive"` -> `landing`

## What This Repository Ships

- canonical repo-local routing under `.agents/skills/goi-workflow`
- compatibility shims under `.codex` and `.claude`
- OpenSpec wrappers for explore, propose, apply, and archive
- Claude-specific OpenSpec command entrypoints under `.claude/commands/opsx/`
- workflow operating docs under `docs/ops/workflow/`
- GitHub Actions verification under `.github/workflows/verify.yml`
- live OpenSpec specs for workflow routing and project mainline posture
- host dependency and shell verification scripts under `scripts/`
- pytest contract tests under `tests/`
- local learning logs under `.learnings/`

## Design Goal

This template keeps the repository workflow thin.

It does not replace:

- upstream `gstack` skills
- the OpenSpec lifecycle
- repo-specific engineering judgment

It only adds:

- route selection
- evidence expectations
- repo-local guardrails
- compatibility shims for local skill discovery
- machine-checkable contract tests for drift-prone workflow rules

This template may also adopt external skill capabilities selectively, but it
does not assume a foreign mandatory methodology should replace repo-local
routing.

## Bootstrap Exception

During initial template adoption, direct edits on the initial setup branch are
allowed until all of the following are true:

- README identity is set
- `openspec/specs/project-mainline-routing/spec.md` is filled with the real
  inventory
- the first verification pass succeeds

After bootstrap, switch to the normal `main -> feat/* -> main` worktree
policy.

## Expected Upstream Dependencies

This template assumes:

- `git`, `rg`, and `openspec` are available on `PATH`
- a local Python virtual environment exists at `.venv`
- `./.venv/bin/pytest` is available for contract verification
- upstream skills such as `investigate`, `review`, `qa`, `qa-only`, `ship`,
  `land-and-deploy`, `canary`, `document-release`, `browse`, `plan-*`,
  `context-save`, `context-restore`, and `browser-use` are already available in
  the host environment

This template does not assume a `gstack` shell command exists locally. Treat
`gstack` as a skill family and workflow posture, not as a mandatory executable.

CI currently pins `@fission-ai/openspec@1.3.1` as the known-good OpenSpec CLI
version for the verification workflow.

Current host naming guidance:

- use `context-save` / `context-restore` for repo-local save-and-resume flows
- use `browse` / `browser-use` / `setup-browser-cookies` for browser
  verification and authenticated browser setup
- use the event-driven `self-improving-agent*` suite plus repo-local
  `.learnings/` for durable learning capture

External skill adoption guidance:

- prefer mapping to existing local or host skills before vendoring new ones
- keep compatibility wrappers thin and auditable
- keep expanded skill comparison or source-analysis docs outside
  `docs/ops/workflow/*`
- do not install a foreign skill system as the repo's default workflow when it
  would impose a competing mandatory chain

## Start Here

When you copy the reusable `workflow-base` template into a new repository:

1. Update [AGENTS.md](./AGENTS.md) only where the new repository genuinely
   needs repo-specific policy.
2. Fill in
   [openspec/specs/project-mainline-routing/spec.md](./openspec/specs/project-mainline-routing/spec.md)
   so the repo states its current mainline, shipped surfaces, planned
   surfaces, evidence lanes, and truth-source hierarchy.
3. Replace the generic sections in `README.md` with your repository's actual
   product, platform, or library posture.
4. Replace the README badge URL when the adopted repository slug differs from
   `liqidong/workflow-auto`.
5. Keep `.agents/skills/goi-workflow/SKILL.md` canonical and keep `.codex` and
   `.claude` compatibility shims short.
6. Treat `.claude/commands/opsx/` as a Claude-specific command surface.
   `.codex` uses skill entrypoints only and does not mirror command files.
7. Run:

```text
scripts/check-host-workflow-deps.sh
scripts/verify-workflow-template.sh
./.venv/bin/pytest -q
openspec validate --specs
```

## Default Branching Posture

After bootstrap, the template defaults to:

- `main` as the integration branch
- feature work in `.worktrees/feat-*`
- one active branch per folder

If your repository uses a different integration branch name, update the wording
in `AGENTS.md` and `docs/ops/git-worktree-layout.md` together.

## Included Operating Surfaces

- [AGENTS.md](./AGENTS.md)
- [.agents/skills/goi-workflow/SKILL.md](./.agents/skills/goi-workflow/SKILL.md)
- [.codex/skills/goi-workflow/SKILL.md](./.codex/skills/goi-workflow/SKILL.md)
- [.claude/skills/goi-workflow/SKILL.md](./.claude/skills/goi-workflow/SKILL.md)
- [.claude/commands/opsx/](./.claude/commands/opsx)
- [docs/ops/workflow/README.md](./docs/ops/workflow/README.md)
- [docs/ops/workflow/skill-routing.md](./docs/ops/workflow/skill-routing.md)
- [docs/ops/workflow/routing-table.md](./docs/ops/workflow/routing-table.md)
- [docs/ops/workflow/evidence.md](./docs/ops/workflow/evidence.md)
- [docs/ops/workflow/routing-checks.md](./docs/ops/workflow/routing-checks.md)
- [docs/ops/workflow/execution-quality.md](./docs/ops/workflow/execution-quality.md)
- [docs/ops/workflow/multi-agent-execution.md](./docs/ops/workflow/multi-agent-execution.md)
- [docs/ops/workflow/checklist.md](./docs/ops/workflow/checklist.md)
- [CHANGELOG.md](./CHANGELOG.md)
- [docs/releases/v0.1.0.md](./docs/releases/v0.1.0.md)
- [docs/releases/v0.1.1.md](./docs/releases/v0.1.1.md)
- [.github/workflows/verify.yml](./.github/workflows/verify.yml)
- [scripts/check-host-workflow-deps.sh](./scripts/check-host-workflow-deps.sh)
- [scripts/verify-workflow-template.sh](./scripts/verify-workflow-template.sh)
- [openspec/specs/workflow-routing-policy/spec.md](./openspec/specs/workflow-routing-policy/spec.md)
- [openspec/specs/project-mainline-routing/spec.md](./openspec/specs/project-mainline-routing/spec.md)

## Template Verification

The Python test suite checks:

- canonical route names
- short and full route trace posture
- hard gates and evidence contract
- compatibility shim thinness
- README/file-surface consistency
- current-mainline inventory presence
- removal of domain-specific source residue
- OpenSpec wrapper freshness

The shell verifier checks:

- key files exist
- repo identity and mainline headings exist
- obvious stale source strings are gone

The GitHub Actions workflow runs the same verification chain on `push` and
`pull_request`.

Keep both.
