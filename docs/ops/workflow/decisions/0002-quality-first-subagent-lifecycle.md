# 0002: Quality-First Subagent Lifecycle

Status: accepted
Date: 2026-04-17

## Context

The repo already reduced its workflow to a thin GOI routing/state/decision model.

The remaining execution-side ambiguity is subagent lifecycle:

- how long a writer should stay alive
- whether a reviewer should be reused
- when parallel writers are justified
- how wide the repo-local Codex thread cap should be

Recent repo defaults still leaned too far toward a persistent roster per slice.
That preserved context for the writer, but it also kept reviewers alive too long and made
it too easy to treat subagents as a standing team instead of bounded roles.

## Decision

The quality-first default for write-heavy work is:

- one long-lived main thread
- one writer for one coherent milestone
- one fresh read-only reviewer per checkpoint
- explorer/docs agents only on demand

Additional rules:

1. A writer may be reused only while the milestone remains coherent.
2. When the milestone closes, pauses, or changes direction materially, close the writer.
3. A reviewer should be fresh for each checkpoint and then closed after findings are consumed.
4. Review should be checkpoint-based, not a perpetual loop.
5. Parallel writers remain exceptional and require:
   - separate worktrees
   - disjoint write sets
   - explicit ownership
6. Repo-local Codex config should cap live subagent width to this quality-first default ceiling.

## Consequences

Positive:

- lower context rot in long-lived reviewer threads
- less review-loop churn
- clearer separation between implementation continuity and independent audit
- tighter default concurrency for write-heavy work

Negative:

- more deliberate reviewer respawn at checkpoints
- less convenience for conversational reviewer continuity

## Rules Implied By This Decision

1. The main thread remains the durable owner of requirements, boundaries, acceptance, and final decisions.
2. Reviewer continuity is no longer the default optimization target; reviewer independence is.
3. The repo should prefer one writer over many unless the parallel-write preconditions are already satisfied.
4. The repo should keep `agents.max_depth = 1`.
5. Repo docs should describe this as a quality-first default, not an absolute ban on other topologies.

## Review Trigger

Revisit this decision if:

- repeated real rounds show that fresh reviewers create more churn than value
- the repo accumulates enough disjoint write-heavy work to justify a different writer cap
- upstream Codex multi-agent capabilities materially change
