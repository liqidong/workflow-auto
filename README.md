# workflow-base

`workflow-base` is a reusable repository template for a thin-routing,
heavy-evidence workflow.

It is meant to be copied into a new repository and customized, not treated as a
finished product or domain-specific starter kit.

## What This Template Includes

- repo-local routing under `.agents/skills/goi-workflow`
- compatibility shims under `.codex` and `.claude`
- OpenSpec wrappers for explore, propose, apply, and archive
- workflow operating docs under `docs/ops/workflow/`
- live OpenSpec specs for workflow routing and project mainline posture
- text-based drift tests under `tests/`
- lightweight non-Python verification via `scripts/verify-workflow-template.sh`
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

This template may also adopt external skill capabilities selectively, but it
does not assume a foreign mandatory methodology should replace repo-local
routing.

## Expected Upstream Dependencies

This template assumes:

- `openspec` CLI is installed and available on `PATH`
- upstream skills such as `investigate`, `review`, `qa`, `qa-only`, `ship`,
  `land-and-deploy`, `canary`, `document-release`, `browse`, `plan-*`,
  `context-save`, `context-restore`, and `browser-use` are already available in
  the host environment

This template does not assume a `gstack` shell command exists locally. Treat
`gstack` as a skill family and workflow posture, not as a mandatory executable.

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

When you copy this template into a new repository:

1. Update [AGENTS.md](./AGENTS.md) only where the new repository genuinely
   needs repo-specific policy.
2. Fill in [openspec/specs/project-mainline-routing/spec.md](./openspec/specs/project-mainline-routing/spec.md)
   so the repo states its current mainline, shipped surfaces, planned surfaces,
   evidence lanes, and truth-source hierarchy.
3. Replace the generic sections in `README.md` with your repository's actual
   product, platform, or library posture.
4. Keep `.agents/skills/goi-workflow/SKILL.md` canonical and keep `.codex`
   compatibility shims short.
5. Run:

```text
scripts/verify-workflow-template.sh
./.venv/bin/pytest -q
openspec validate --specs
```

## Default Branching Posture

The template defaults to:

- `main` as the integration branch
- feature work in `.worktrees/feat-*`
- one active branch per folder

If your repository uses a different integration branch name, update the wording
in `AGENTS.md` and `docs/ops/git-worktree-layout.md` together.

## Included Operating Surfaces

- [AGENTS.md](./AGENTS.md)
- [.agents/skills/goi-workflow/SKILL.md](./.agents/skills/goi-workflow/SKILL.md)
- [docs/ops/workflow/README.md](./docs/ops/workflow/README.md)
- [docs/ops/workflow/skill-routing.md](./docs/ops/workflow/skill-routing.md)
- [docs/ops/workflow/routing-table.md](./docs/ops/workflow/routing-table.md)
- [docs/ops/workflow/evidence.md](./docs/ops/workflow/evidence.md)
- [docs/ops/workflow/routing-checks.md](./docs/ops/workflow/routing-checks.md)
- [docs/ops/workflow/multi-agent-execution.md](./docs/ops/workflow/multi-agent-execution.md)
- [docs/ops/workflow/checklist.md](./docs/ops/workflow/checklist.md)
- [openspec/specs/workflow-routing-policy/spec.md](./openspec/specs/workflow-routing-policy/spec.md)
- [openspec/specs/project-mainline-routing/spec.md](./openspec/specs/project-mainline-routing/spec.md)

## Template Verification

The Python test suite checks:

- canonical route names
- route trace fields
- hard gates and evidence contract
- compatibility shim thinness
- removal of domain-specific source residue
- OpenSpec wrapper freshness

The shell verifier checks:

- key files exist
- key headings exist
- obvious stale source strings are gone

Keep both.
