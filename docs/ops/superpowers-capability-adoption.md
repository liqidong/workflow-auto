# Superpowers Capability Adoption

Status: descriptive analysis  
Date: 2026-05-08  
Scope: selective reuse of `obra/superpowers` skill capabilities inside this
repo's thin-routing, heavy-evidence workflow

## Purpose

This document explains how the repo can reuse useful capabilities from
`obra/superpowers` without installing or inheriting the full Superpowers
methodology as the repo's default workflow.

It is descriptive analysis, not workflow law.

## Source Surface

Primary local sources:

- `AGENTS.md`
- `README.md`
- `docs/ops/workflow/README.md`
- `docs/ops/workflow/skill-routing.md`
- `docs/ops/workflow/multi-agent-execution.md`
- `.agents/skills/goi-workflow/SKILL.md`
- `.codex/skills/openspec-*`

Primary external source:

- `obra/superpowers` README:
  `https://github.com/obra/superpowers`
- `obra/superpowers` skills index:
  `https://github.com/obra/superpowers/tree/main/skills`

## Adoption Posture

The repo adopts the following posture:

- keep `goi-workflow` as the canonical route selector
- keep OpenSpec as the planning and active-change control surface
- keep `gstack` skills as downstream execution and verification surfaces
- reuse external skill capabilities selectively through mapping, wrapping, or
  vendoring
- reject direct installation of a foreign methodology when it would impose a
  competing mandatory workflow chain

Why this matters:

- Superpowers explicitly describes itself as a complete methodology with
  automatic and mandatory workflow activation.
- This repo explicitly keeps routing thin and conditional.
- Directly importing the full methodology would compete with repo-local route
  selection and control surfaces.

## Capability Matrix

| Superpowers skill | Superpowers role | Status here | Local entrypoint or source | Provenance | Notes |
| --- | --- | --- | --- | --- | --- |
| `brainstorming` | pre-code design refinement | `adopted` | `.codex/skills/brainstorming`, `openspec-explore`, optional `plan-*` review skills | repo-local thin wrapper + existing skills | Preserved as a compatibility name, but it does not auto-trigger a mandatory design loop. |
| `using-git-worktrees` | isolated branch workspace creation | `adopted` | `.codex/skills/using-git-worktrees`, `AGENTS.md`, `docs/ops/git-worktree-layout.md` | repo-local thin wrapper + existing docs | Uses this repo's `main -> feat/* -> main` posture. |
| `writing-plans` | detailed implementation plan | `adopted` | `.codex/skills/writing-plans`, `openspec-propose` | repo-local thin wrapper + existing OpenSpec wrapper | Planning stays inside OpenSpec proposal/design/tasks artifacts. |
| `subagent-driven-development` | mandatory subagent execution loop | `adopted` | `.codex/skills/subagent-driven-development`, `goi-workflow`, subagent task packet | repo-local thin wrapper + existing docs | Supported only as an opt-in launch mode that asks before startup. |
| `executing-plans` | batch execution against plan | `equivalent` | `openspec-apply-change` | existing OpenSpec wrapper | Similar capability exists, but not as a separate mandatory stage name. |
| `test-driven-development` | mandatory TDD loop | `adopted` | `.codex/skills/test-driven-development`, `./.venv/bin/pytest -q` | repo-local thin wrapper + existing pytest suite | Supported as an optional discipline aid without importing a mandatory foreign TDD chain. |
| `requesting-code-review` | structured pre-review handoff | `adopted` | `.codex/skills/requesting-code-review`, `review` | repo-local thin wrapper + existing gstack skill | Review remains conditional and route-driven. |
| `receiving-code-review` | structured response to review feedback | `adopted` | `.codex/skills/receiving-code-review`, inherited `light` / `blocker` route | repo-local thin wrapper + existing routing rules | Fixes stay inside accepted scope unless control surface changes. |
| `finishing-a-development-branch` | merge/PR/cleanup closeout | `equivalent` | `ship`, `land-and-deploy`, branch policy docs | existing skills + docs | Similar capability exists without importing a foreign branch-closing ritual. |
| `systematic-debugging` | root-cause-first debugging | `adopted` | `.codex/skills/systematic-debugging`, `investigate` | repo-local thin wrapper + existing gstack skill | Maps to the repo's `blocker` posture. |
| `verification-before-completion` | verify before claiming success | `adopted` | `.codex/skills/verification-before-completion`, `docs/ops/workflow/evidence.md` | repo-local thin wrapper + existing evidence contract | Already native to this repo, but exposed under the familiar name. |
| `dispatching-parallel-agents` | concurrent agent teams | `adopted` | `.codex/skills/dispatching-parallel-agents`, multi-agent checklist docs | repo-local thin wrapper + existing docs | Supported only as an opt-in launch mode with a hard parallel checklist and pre-launch confirmation. |
| `writing-skills` | authoring new skills | `equivalent` | `skill-creator`, `extract` | existing host skills | Similar capability already exists in the host environment. |
| `using-superpowers` | introduction to the superpowers system | `excluded` | none | explicit exclusion | This repo is not adopting the full Superpowers methodology as its operating system. |

## Route Mapping

The repo's practical mapping with selective Superpowers compatibility is:

| Route | Canonical local control surface | Optional compatibility names |
| --- | --- | --- |
| `assess` | `goi-workflow` + `openspec-explore` | `brainstorming` |
| `micro` | `goi-workflow` + direct narrow verification | none by default |
| `light` | `goi-workflow` + `openspec-apply-change` | `writing-plans` as historical plan context only, `test-driven-development` when narrow test-first work is useful |
| `full` | `goi-workflow` + `openspec-propose` | `brainstorming`, `writing-plans` |
| `blocker` | `goi-workflow` + `investigate` | `systematic-debugging`, `verification-before-completion` |
| `landing` | `goi-workflow` + `review` / `ship` / `land-and-deploy` | `requesting-code-review`, `receiving-code-review`, `using-git-worktrees` |

## Wrapper Decisions

High-friction names selected for thin wrappers in this repo:

- `brainstorming`
- `using-git-worktrees`
- `writing-plans`
- `test-driven-development`
- `systematic-debugging`
- `requesting-code-review`
- `receiving-code-review`
- `verification-before-completion`
- `subagent-driven-development`
- `dispatching-parallel-agents`

Selection rule:

- choose names that are likely to be requested directly
- prefer wrappers when there is already a clear canonical local capability
- do not create wrappers for names that would smuggle in a mandatory foreign
  execution pattern

Wrappers intentionally not added in this round:

- `using-superpowers`

Reason:

- each would import a foreign top-level methodology instead of a thin local
  compatibility entrypoint

## Why This Lives Outside `docs/ops/workflow/`

This document lives in `docs/ops/`, not `docs/ops/workflow/`, because:

- `docs/ops/workflow/*` is the supply-chain-sensitive workflow control surface
- this file compares local behavior to an external skill library
- it is guidance and inventory, not normative route law
- keeping it separate reduces the chance of accidental workflow drift
