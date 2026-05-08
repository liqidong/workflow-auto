from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def test_goi_workflow_requires_user_confirmation_for_optional_launch_modes() -> None:
    skill = _read(".agents/skills/goi-workflow/SKILL.md")

    assert "Optional Launch Modes" in skill
    assert "ask the user before launching" in skill
    assert "write sets are disjoint" in skill
    assert "separate worktree" in skill or "separate worktrees" in skill


def test_subagent_task_packet_includes_acceptance_and_parallel_metadata() -> None:
    packet = _read(".agents/skills/goi-workflow/references/subagent-task-packet.md")

    for field in (
        "Acceptance source:",
        "Review mode:",
        "Checkpoint trigger:",
        "Parallel-safe:",
    ):
        assert field in packet


def test_multi_agent_doc_and_routing_checks_encode_optional_launch_gates() -> None:
    multi = _read("docs/ops/workflow/multi-agent-execution.md")
    checks = _read("docs/ops/workflow/routing-checks.md")

    assert "ask the user before launch" in multi
    assert "Parallel dispatch checklist" in multi
    assert "Delegation-heavy launch candidate" in checks
    assert "refuse parallel dispatch" in checks


def test_optional_dispatch_wrappers_stay_thin_and_non_default() -> None:
    for path in (
        ".codex/skills/subagent-driven-development/SKILL.md",
        ".codex/skills/dispatching-parallel-agents/SKILL.md",
    ):
        text = _read(path)
        assert "compatibility" in text.lower()
        assert len(text.splitlines()) < 40
        assert "Ask the user before launching this mode." in text
