## Context

`obra/superpowers` is published as a complete coding-agent methodology with
automatic or mandatory workflow activation across design, planning,
subagent-driven execution, test-first implementation, and review. That is
useful as a capability source, but it conflicts with this repo's current
posture: repo-local `goi-workflow` chooses the route, OpenSpec controls change
scope, and downstream skills stay conditional.

The repo already has part of the required capability set through existing local
skills, plugin skills, and global host skills. The missing piece is not "install
everything"; it is a thin adoption strategy that says what can be reused, under
what names, with what provenance, and under what constraints.

Constraints:

- `goi-workflow` remains the canonical routing skill.
- Workflow control surfaces stay thin and supply-chain-sensitive.
- Detailed skill commentary should not be merged into normative
  `docs/ops/workflow/*` unless it changes policy.
- Some desired capabilities may already exist under different local or host
  names.
- Direct installation of a mandatory methodology is out of bounds for this
  change.

## Goals / Non-Goals

**Goals:**

- Preserve repo-local routing authority while enabling superpowers-inspired
  skill coverage.
- Make external skill adoption explicit, auditable, and reversible.
- Distinguish clearly between installed, mapped, wrapped, and excluded skills.
- Support a descriptive route-to-skill guide without turning it into workflow
  law.
- Leave the repo ready to implement selective wrappers or vendored skills in a
  later apply phase.

**Non-Goals:**

- Installing the full `superpowers` plugin and accepting its automatic
  methodology.
- Replacing `goi-workflow`, `gstack`, or OpenSpec with superpowers terminology.
- Promising one-to-one parity for every superpowers skill.
- Copying a full mandatory chain such as brainstorming -> worktree creation ->
  writing plans -> subagent execution into repo-local workflow control docs.

## Decisions

### 1. Treat external skills as capabilities, not as workflow owners

The repo will reason about external skills by capability class:

- `adopted`: the repo intentionally uses the same or vendored skill
- `equivalent`: an existing repo or host skill already covers the capability
- `excluded`: intentionally not adopted because it conflicts with thin routing
- `pending`: worth revisiting later, but not part of the current backbone

Why:

- This lets the repo benefit from external skill ecosystems without binding the
  repo to a foreign top-level methodology.

Alternative considered:

- Directly install `superpowers` and let its triggers run.
- Rejected because the upstream system explicitly describes a complete,
  mandatory workflow chain, which would compete with repo-local routing.

### 2. Keep detailed skill analysis outside the normative workflow control surface

Expanded route-to-skill mapping, capability inventory, provenance notes, and
skill comparison tables will live in `docs/ops/` or another descriptive
surface, not inside `docs/ops/workflow/*`.

Why:

- The repo already treats `docs/ops/workflow/*` as a control surface and
  instruction files as supply-chain-sensitive.
- The detailed mapping will change more often than the normative route model.

Alternative considered:

- Put full route-to-skill chains into `docs/ops/workflow/skill-routing.md`.
- Rejected because it would turn the thin layer into a second orchestration
  runtime.

### 3. Allow only thin compatibility wrappers

If specific superpowers names create repeated friction, the repo may add thin
local wrappers or aliases. Those wrappers must:

- point to canonical local entrypoints
- preserve repo-local route selection
- avoid embedding a full downstream methodology
- stay short enough to audit easily

Why:

- This gives callers a familiar entrypoint without forking the workflow model.

Alternative considered:

- Copy full external skill instructions into local control surfaces.
- Rejected because it duplicates logic, increases drift, and weakens local
  ownership.

### 4. Prefer mapping to existing host skills before vendoring

The repo should first try to map desired capabilities to existing local or host
skills such as `investigate`, `review`, `qa`, `ship`, `land-and-deploy`,
`browse`, and the existing OpenSpec wrappers. Vendoring from external sources
should happen only when there is a repeated high-value gap and no credible
existing equivalent.

Why:

- This keeps the adoption set smaller and reduces maintenance cost.

Alternative considered:

- Vendor every useful-looking superpowers skill up front.
- Rejected because it adds bulk before real usage proves the need.

## Risks / Trade-offs

- [Capability drift] The external skill source may evolve while the repo's
  mapping snapshot stays stale. -> Mitigation: record provenance and keep an
  explicit capability matrix.
- [Wrapper bloat] Too many compatibility aliases could recreate the external
  workflow indirectly. -> Mitigation: require repeated friction and keep
  wrappers thin.
- [User confusion] Callers may assume "mapped" means "installed". ->
  Mitigation: classify each capability explicitly and document the difference.
- [Control-surface creep] Descriptive docs may start acting like policy. ->
  Mitigation: keep normative requirements in specs and keep analysis outside
  `docs/ops/workflow/*`.

## Migration Plan

1. Create the capability matrix and descriptive analysis surface.
2. Update only the minimum normative workflow surfaces needed to preserve
   routing authority and define adoption constraints.
3. Add thin wrappers only for approved high-friction names.
4. Add tests or checks that prove the repo still follows thin routing.

Rollback is straightforward: remove the added analysis docs, wrappers, and
references without changing the underlying six-route model.

## Open Questions

- Which superpowers capabilities are high-value enough to justify local wrappers
  instead of pure documentation mapping?
- Should the capability matrix live as Markdown only, or also have a
  machine-readable form?
- Which exclusions should be explicit on day one, especially around mandatory
  plan/execution chains?
