# Rule Reduction Checklist

Status: historical reduction reference
Purpose: preserve the reduction checklist that shaped the thin workflow layer; this is not a current operating surface

This checklist is based on:

- current repo rules in [AGENTS.md](../../../AGENTS.md)
- current canonical repo routing skill in [goi-workflow/SKILL.md](../../../.agents/skills/goi-workflow/SKILL.md)
- compatibility shim in [.codex/skills/goi-workflow/SKILL.md](../../../.codex/skills/goi-workflow/SKILL.md)
- current routing table in [docs/ops/workflow/skill-routing.md](skill-routing.md)
- upstream source review of `gstack`
- upstream source review of `OpenSpec`

Reference policy for this checklist:
- avoid brittle line anchors while reduction is still in flight
- reference stable section intent and file-level surfaces instead

## Decision Standard

Use this rule for every workflow paragraph:

- keep it only if it is repo-specific operating guidance
- move it if it is rationale or a durable decision
- delete or shrink it if it duplicates upstream `gstack` or `OpenSpec`

## AGENTS.md

### Keep

- short default GOI backbone:
  - `gstack`
  - `OpenSpec`
  - `self-improvement`
- process gating:
  - when full workflow is needed
  - when trivial skip is allowed
- short implementation-light rule:
  - active change is canonical
  - primary surfaces are code/tests/smoke/classified review
  - docs/tracker/archive are secondary during live blockers
- current project lock and control-first implication
- orchestration source-of-truth rule:
  - OpenSpec changes/tasks and repo artifacts
  - `.learnings`
  - no second control-plane runtime

### Downscope

- keep AGENTS as policy-level guidance; do not re-expand into execution graph detail
- do not move heavy roster/fallback mechanics into `goi-workflow` or `skill-routing`
- if heavy execution mechanics are still needed, keep them in decision artifacts, not operating surfaces

### Move To Decision Layer

- detailed rationale embedded in implementation-light wording
- historical justification for why multi-agent/default roster rules were added
- any future explanation of why the repo chose routing-over-graph

### Delete If Still Present After Downscope

- duplicated roster shape/model/fallback details in repo-main operating docs
- any wording that reads like a full stage-by-stage workflow graph

## goi-workflow/SKILL.md

### Keep

- core rule:
  - thin orchestration layer
  - do not replace official skills
- required GOI decision shape with explicit triad routing:
  - `gstack stage/status/reason`
  - `OpenSpec required|inherited|skipped` with reason
  - `self-improvement triggered|not-triggered` with reason
- thin handoff rule:
  - choose smallest current gate
  - explain continue/stop/inherited/skipped
- thin implementation-light routing rule
- official-skill source-of-truth rule
- current project lock
- concise research preflight rule
- short routing pointer to `skill-routing.md`
- short repo-specific execution flow and operator guardrails

### Downscope Hard

- do not keep a broad skill-family catalog in this file
- do not recreate heavy phase graphs (for `gstack` or `OpenSpec`)
- keep routing concise and stage-local; deep flow belongs to official skills

### Move To Decision Layer

- detailed phase rationale
- why the phase order evolved this way
- why the repo chose a fixed roster per slice
- historical reasoning behind archive defaults

### Delete Or Collapse

- broad catalogs of optional `gstack` families
- execution planning details that duplicate OpenSpec task surfaces
- long subagent lifecycle mechanics in operating docs
- full verification ladders that compete with official verification skills
- long close-out graphs that restate official close-out skills
- long quick-checklist and red-flag prose once short guardrails exist

## docs/ops/workflow/skill-routing.md

### Keep

- GOI routing rule with explicit triad decisions:
  - smallest `gstack` entry gate
  - `OpenSpec required|inherited|skipped`
  - `self-improvement triggered|not-triggered`
- mode-to-entry-gate routing (`Program`, `Change`, `Execution`, `Landing`)
- conditional skill groups that are not always-on backbone
- anti-duplication rule against mirroring official skill internals

### Downscope

- do not mirror the full linked `gstack` graph
- do not mirror the full `OpenSpec` lifecycle
- keep mode guidance short and entry-gate oriented

## What Should Exist After Reduction

### Operating Surfaces

- `AGENTS.md`
  - short repo defaults
  - short gating
  - short implementation-light rule
  - current project lock
- `goi-workflow/SKILL.md`
  - GOI triad decision format
  - six route names: `assess`, `micro`, `light`, `full`, `blocker`, `landing`
  - smallest-gate routing rule
  - explicit `OpenSpec` and `self-improvement` routing
  - implementation-light routing
  - official-source-of-truth rule
  - concise research-preflight rule
- `docs/ops/workflow/skill-routing.md`
  - mode-to-entry-gate routing
  - conditional skill groups
- `docs/ops/workflow/routing-table.md`
  - declarative route precedence and hard gates
- `docs/ops/workflow/evidence.md`
  - minimum evidence and skipped-verification contract
- `docs/ops/workflow/routing-checks.md`
  - snapshot cases that prevent route drift

### State Surfaces

- program tracker
- active OpenSpec change
- `.learnings/`

### Decision Surfaces

- `docs/ops/workflow/decisions/*.md`

## Acceptance Check

The reduction is successful only if all are true:

1. repo docs no longer mirror the full `gstack` linked graph
2. repo docs no longer mirror the OpenSpec lifecycle
3. one reader can find:
   - current gate
   - current canonical artifact
   - next bounded move
   in under two file hops
4. rationale is separated from operating instructions
