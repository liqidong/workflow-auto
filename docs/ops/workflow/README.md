# Workflow Layers

Status: current operating surface

This directory keeps repo-local workflow guidance thin.

It should not become a second workflow system parallel to `gstack` and
`OpenSpec`.

Use this directory by layer:

- `README.md`: entry and reading order
- `skill-routing.md`: operating routing surface
- `routing-table.md`: auditable route decision table
- `evidence.md`: route evidence and skipped-verification contract
- `routing-checks.md`: manual snapshot checks for routing drift
- `execution-quality.md`: execution-quality guardrails for coding and blocker
  work after route selection
- `model-diversity.md`: optional Claude CLI + DeepSeek lane for bounded writer,
  reviewer, investigator, and docs-consistency work after route selection
- `multi-agent-execution.md`: canonical starting pattern for repo-local
  multi-agent execution
- `checklist.md`: lightweight non-Python template verification
- `rule-reduction-checklist.md`: anti-duplication review reference
- `decisions/*.md`: rationale and durable workflow decisions

Host-specific repository identity belongs in the top-level `README.md` and
`openspec/specs/project-mainline-routing/spec.md`, not in the generic routing
surfaces in this directory.

## Layer Model

### Layer 1: Upstream Tool Layer

Source of truth:

- official `gstack` skills
- official `OpenSpec` lifecycle

Meaning:

- `gstack` already contains linked skill recommendations and next-step hints
- `OpenSpec` already contains change/action lifecycle behavior
- `self-improvement` already owns its own capture behavior
- repo docs should not duplicate either surface in full
- adopted external skills stay downstream of repo-local route selection

### Layer 2: Repo Routing Layer

Source of truth:

- [AGENTS.md](../../../AGENTS.md)
- [goi-workflow/SKILL.md](../../../.agents/skills/goi-workflow/SKILL.md)
- [skill-routing.md](skill-routing.md)
- [routing-table.md](routing-table.md)
- [evidence.md](evidence.md)
- [routing-checks.md](routing-checks.md)

Meaning:

- choose one route mode: `assess`, `micro`, `light`, `full`, `blocker`, or
  `landing`
- route the GOI triad together for the current task:
  - `gstack stage`
  - `gstack status`: `required / inherited / skipped`
  - `OpenSpec` status: `required / inherited / skipped`
  - `OpenSpec control surface` when `OpenSpec` is not `skipped`
- treat OpenSpec actions such as `openspec-propose`, `openspec-apply-change`,
  and `openspec-archive-change` as the active change control surface, separate
  from `gstack stage`
- treat `self-improvement` as an event-driven recording rail surfaced only when
  triggered
- add repo-local guardrails only when necessary

The older `.codex/skills/goi-workflow/SKILL.md` and
`.claude/skills/goi-workflow/SKILL.md` paths are compatibility surfaces for
local history and custom agents. `.agents/skills/goi-workflow/SKILL.md` is
canonical for current repo skill discovery.

### Layer 3: Project State

Source of truth:

- the repository `README.md`
- [openspec/specs/project-mainline-routing/spec.md](../../../openspec/specs/project-mainline-routing/spec.md)
- active OpenSpec change
- `.learnings/`

Meaning:

- what is active now
- what is blocked now
- what the next bounded move is

This template host repo defines the template itself as the current mainline.
Each adopting repository must replace the inherited inventory with its own
shipped surfaces, planned surfaces, evidence lanes, and truth-source
hierarchy before treating those surfaces as canonical.

### Layer 4: Decision Layer

Source of truth:

- [decisions/*.md](decisions/)

Meaning:

- keep rationale and durable workflow decisions separate from day-to-day
  routing

## Current Recommendation

Use the repo workflow as:

1. choose the smallest safe route mode
2. default to the short trace `Route / Why / Evidence`, and expand to the full
   GOI trace only for high-risk, workflow-sensitive, blocker, multi-agent, or
   landing work
3. state one GOI routing tuple: `gstack stage`, `gstack status`, `OpenSpec`
   status, and the active OpenSpec control surface when applicable
4. surface `self-improvement` only when a real event triggers recording, the
   task explicitly audits workflow hygiene, or the user asks for capture
5. execute only the smallest correct current `gstack` stage
6. when `OpenSpec` is `required` or `inherited`, use the active change and
   OpenSpec actions as a separate control surface
7. use execution light mode during implementation/debug, then return to
   `landing` when blockers are cleared
8. apply execution-quality guardrails during implementation/debug/fix work
   without turning them into a new workflow
9. treat any adopted external skill or optional model-diversity lane as an
   execution aid, not a replacement for the route decision
10. use the optional model-diversity lane only when the main thread still owns
    route selection, acceptance, final review, and merge or release decisions
11. if a delegation-heavy or parallel-dispatch launch is recommended, ask the
   user before starting it

Repository-specific mainline policy belongs in:

- the top-level `README.md`
- [openspec/specs/project-mainline-routing/spec.md](../../../openspec/specs/project-mainline-routing/spec.md)

For the thin layer model decision, see:

- [0001-thin-routing-over-full-workflow.md](decisions/0001-thin-routing-over-full-workflow.md)
- [0002-quality-first-subagent-lifecycle.md](decisions/0002-quality-first-subagent-lifecycle.md)
- [0003-event-driven-self-improvement-rail.md](decisions/0003-event-driven-self-improvement-rail.md)
- [0004-light-routing-heavy-evidence.md](decisions/0004-light-routing-heavy-evidence.md)

For the current canonical multi-agent execution shape, see:

- [multi-agent-execution.md](multi-agent-execution.md)
