## Context

The repo already has the right high-level posture:

- thin routing
- heavy evidence
- canonical `.agents` routing
- compatibility shims rather than duplicated workflows

The gap is not missing methodology. The gap is template operability:

- repo identity is ambiguous between `workflow-auto` and `workflow-base`
- mainline inventory exists only as abstract policy
- README promises and actual surfaces can drift
- shell verification is mostly grep-level
- route reporting is verbose enough to become ritual on routine tasks

This change hardens those edges without introducing a new orchestration layer.

## Goals / Non-Goals

**Goals:**

- make the host repo identity explicit and stable
- make the current template inventory concrete and easy to inspect
- ensure README claims match actual files
- improve machine verification depth with pytest contract tests
- reduce route-trace ceremony for routine tasks while preserving the full trace
  for high-risk or closeout work
- add practical recovery and learning-capture guidance where repeated drift is
  likely

**Non-Goals:**

- introducing new route modes
- creating a second workflow runtime or schema system
- importing a foreign mandatory methodology
- replacing human review with parsers or generators

## Decisions

### 1. Public repo identity and template identity stay distinct

The repository will identify itself as `workflow-auto`, while documenting that
it hosts the reusable `workflow-base` template.

Why:

- The git remote and local clone name are already `workflow-auto`.
- The template artifact name still matters for adopters and copied surfaces.

### 2. Current mainline inventory belongs in the live mainline spec

`openspec/specs/project-mainline-routing/spec.md` will carry both the abstract
requirements and the current live inventory for this repo.

Why:

- New readers need the real current state, not only the policy for future
  adopters.

### 3. Short trace is the default; full trace is conditional

Routine non-high-risk work uses a short visible trace:

- `Route`
- `Why`
- `Evidence`

The full GOI trace remains the requirement for workflow-sensitive, high-risk,
blocker, multi-agent, landing, or explicitly requested work.

Why:

- This keeps observability while reducing empty ceremony on routine tasks.

### 4. Verification hardening should stay simple and local

Instead of adding a parser-heavy validator, the repo will combine:

- a host dependency checker
- an updated shell verifier
- focused pytest contract tests

Why:

- The failure modes here are mostly consistency and surface drift.
- Simple targeted tests are easier to audit than a generated policy engine.

### 5. Recovery and learning guidance should be compact and concrete

The repo will add recovery rules for multi-agent conflicts and a small
learning-capture decision table for `.learnings/`.

Why:

- These are high-value repeated failure points.
- They improve reuse without changing the route model.

## Risks / Trade-offs

- [Identity churn] Some older docs or assumptions may still expect
  `workflow-base` everywhere. -> Mitigation: keep the template name explicit
  while making the repo name primary.
- [Test brittleness] Text-based contract tests can overfit headings. ->
  Mitigation: test stable phrases and invariants only.
- [Verifier overlap] Shell and pytest checks overlap somewhat. -> Mitigation:
  shell checks file presence and obvious invariants; pytest checks deeper
  consistency.

## Migration Plan

1. Add OpenSpec change artifacts for identity, inventory, and verification
   hardening.
2. Update README, AGENTS, workflow docs, and specs.
3. Add `.claude` GOI shim and host dependency checker.
4. Strengthen pytest contracts and shell verifier.
5. Run the full local verification chain and record evidence.
