# workflow-auto AGENTS

## Project Mode

This repository, `workflow-auto`, hosts the reusable `workflow-base`
thin-routing, heavy-evidence template.

The repo should optimize for:

- clear ownership of workflow rules
- explicit evidence before completion claims
- compatibility with upstream skills instead of duplication
- reusable repo-local instructions that can be audited and tested
- machine-verifiable consistency across docs, skills, scripts, and specs

## Branch Policy

Do not develop directly on `main`.

Default rule:

- `main` stays as the integration branch
- start new implementation work from the latest `main`
- use a bounded `feat/*` branch for each task or feature
- merge the finished feature branch back to `main` only after verification
- use repo-local git worktrees under `.worktrees/` for concurrent branch work
- keep one active branch per folder

Bootstrap exception:

- during initial template adoption, direct edits on the initial setup branch
  are allowed until README identity is set, the project-mainline inventory is
  filled, and the first verification pass succeeds
- after bootstrap, switch to the normal `main -> feat/* -> main` worktree
  policy

Canonical reference:

- [docs/ops/git-worktree-layout.md](./docs/ops/git-worktree-layout.md)

## Default Workflow

For non-trivial work, use:

- `gstack`
- `OpenSpec`
- `self-improvement` as an event-driven recording rail, typically satisfied by
  the current `self-improving-agent*` skill family plus repo-local
  `.learnings/`
- route the GOI contract explicitly: `gstack stage`, `gstack status`
  (`required / inherited / skipped`), `OpenSpec` status
  (`required / inherited / skipped`), and active OpenSpec control surface when
  applicable
- surface `self-improvement` only when a real failure, correction, durable
  rule, explicit workflow audit, or user request triggers recording

## Workflow Posture

This repo uses a light routing / heavy evidence workflow adapter.

For non-trivial work, choose the smallest safe route:

- `assess`: read-only review, research, status, route recommendation, or risk
  assessment
- `micro`: tiny low-risk edit with the smallest useful verification
- `light`: implementation or debugging inside accepted scope or an active
  OpenSpec change
- `full`: new feature, architecture, contract, security, deployment, workflow,
  or production-impacting change
- `blocker`: failing test, failing smoke, user correction, repeated failure,
  unexplained regression, or drift
- `landing`: review, PR, release, deploy, archive, or closeout

Default short trace:

```text
Route:
Why:
Evidence:
```

Use the full trace only when:

- workflow / instruction files change
- architecture, security, deployment, or data-contract work is in scope
- the task starts from blocker, correction, or repeated failure conditions
- a writer, reviewer, or parallel-dispatch launch is being used
- the task is landing, release, deploy, archive, or closeout work
- the user explicitly asks for the complete route trace

Full trace:

```text
Route:
gstack stage:
gstack status:
gstack reason:
OpenSpec:
OpenSpec reason:
OpenSpec control surface:
self-improvement:
self-improvement reason:
Project state:
Task kind:
Risk level:
Problem kind:
Control surface:
Entry:
Reason:
Verification required:
```

Completion requires fresh verification evidence or an explicit
skipped-verification record:

```yaml
skipped_verification:
  check:
  reason:
  residual_risk:
  follow_up:
```

Hard gates:

- High-risk work cannot route to `micro`.
- Blocker, correction, or repeated-failure work must investigate before
  implementation.
- Active OpenSpec changes should be inherited rather than replanned unless
  scope changed.
- Repo-local instruction files are supply-chain sensitive, including
  `AGENTS.md`, `.agents/skills/**`, `.codex/skills/**`, `.claude/skills/**`,
  `.cursor/rules/**`, `.clinerules/**`, and `docs/ops/workflow/**`.
- Routing predicates must stay declarative; do not execute generated
  predicates.

Learning capture rule:

- repo-specific learnings and errors must be written to `.learnings/`
- `gstack /learn` is a retrieval and session-memory layer, not the only source
  of truth
- when a learning proves stable, promote it from `.learnings/` into
  `AGENTS.md` or durable docs

Learning capture guidance:

| Case | Capture? |
| --- | --- |
| one-off typo | no |
| same check fails twice | yes |
| user correction reveals wrong assumption | yes |
| repo-specific command, path, or environment pitfall | yes |
| general programming fact | no |
| workflow decision that should affect future routing | yes |

External skill adoption rule:

- external skill libraries may be used as capability sources
- repo-local route selection remains canonical
- direct installation of a foreign mandatory methodology is not the default
- thin compatibility wrappers are allowed when they redirect to canonical local
  entrypoints without duplicating the foreign workflow

## Process Gating

Use the full workflow for:

- new features
- architecture changes
- data-contract changes
- trust-boundary or security changes
- deployment changes
- workflow, wiki, or CLI changes

You may skip the heavyweight flow for:

- small, local, low-risk edits
- one-file documentation fixes
- narrow mechanical cleanup
- obvious typo or path fixes

When skipping, still keep the work explicit and verified.

## Implementation Light Mode

For implementation, debugging, hardening, and deployed proof on an already
locked active change:

- the active OpenSpec change is canonical
- primary execution surfaces are code/tests, real smoke or deployed proof, and
  review findings classified as `blocking / important / low`
- during live blockers, tracker/docs/archive work is secondary and must not
  interrupt root-cause execution

## Current Program Focus

The current mainline of this repository is the reusable workflow template
itself, not a product or application domain.

The active repository must define its current mainline in:

- [openspec/specs/project-mainline-routing/spec.md](./openspec/specs/project-mainline-routing/spec.md)
- the repository `README.md`

If those two surfaces are stale or disagree, fix them before treating any
domain route, API surface, or roadmap item as canonical.

## Multi-Agent Orchestration v0

Current orchestration source of truth stays in repo artifacts:

- OpenSpec changes and tasks
- workflow operating docs
- `.learnings/`

For avoidance of drift:

- `.learnings/` is the canonical repo-local learning log
- `gstack /learn` may mirror or surface learnings, but should not replace
  repo-local capture
- record stable orchestration issues and improvements in
  `docs/ops/agent-orchestration-feedback.md`

Current canonical starting pattern for execution shape:

- [docs/ops/workflow/multi-agent-execution.md](./docs/ops/workflow/multi-agent-execution.md)

Do not build a separate control-plane runtime, schema system, ledger, or lock
service unless repeated real usage proves the need.

Quality-first default for write-heavy implementation slices:

- keep the main thread long-lived for requirements, boundaries, acceptance, and
  final decisions
- default to one writer for one coherent milestone
- reuse that writer only while the milestone stays coherent
- use a fresh read-only reviewer for each checkpoint, then close it
- use explorer/docs agents on demand, then close them
- allow parallel writers only with separate worktrees, disjoint write sets, and
  explicit ownership
- ask before starting a delegation-heavy or parallel-dispatch mode that is not
  already the default local execution shape

Preferred model routing when multiple agent/model choices are available:

- `GPT-5.5 xhigh`: total control, architecture judgment, final review, and hard
  tradeoff decisions
- `GPT-5.5 high`: high-risk core implementation, difficult bugs, and complex
  refactors
- `GPT-5.4 high`: everyday implementation, multi-file changes, and toolchain
  work
- `GPT-5.3-Codex high`: local code edits, tests, lint fixes, small bugs, and
  documentation support

This routing is a default preference, not a hard lock. The main thread may
choose differently when context, cost, tool availability, or task risk makes a
different split more appropriate.

## Knowledge Capture

Execution outputs should accumulate into:

- repo docs
- wiki-ready markdown when the repo actually uses that surface
- verification artifacts
- reusable skills extracted from validated repeated workflows

Do not prebuild a platform just to feel organized.
Extract reusable skills only after the workflow has been exercised in real
runs.
