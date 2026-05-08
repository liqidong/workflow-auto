from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
CANONICAL_SKILL = REPO_ROOT / ".agents" / "skills" / "goi-workflow" / "SKILL.md"
COMPAT_SKILL = REPO_ROOT / ".codex" / "skills" / "goi-workflow" / "SKILL.md"
CANONICAL_PACKET = (
    REPO_ROOT
    / ".agents"
    / "skills"
    / "goi-workflow"
    / "references"
    / "subagent-task-packet.md"
)
COMPAT_PACKET = (
    REPO_ROOT
    / ".codex"
    / "skills"
    / "goi-workflow"
    / "references"
    / "subagent-task-packet.md"
)


def test_goi_workflow_skill_uses_canonical_agents_path() -> None:
    skill = CANONICAL_SKILL.read_text(encoding="utf-8")

    assert "This is the canonical repo-local GOI workflow skill." in skill
    assert "light routing / heavy evidence" in skill
    for route in ("assess", "micro", "light", "full", "blocker", "landing"):
        assert f"`{route}`" in skill
    assert "Route:" in skill
    assert "gstack stage:" in skill
    assert "OpenSpec control surface:" in skill
    assert "Verification required:" in skill
    assert "verification_evidence:" in skill
    assert "skipped_verification:" in skill


def test_codex_goi_skill_is_short_compatibility_shim() -> None:
    skill = COMPAT_SKILL.read_text(encoding="utf-8")

    assert ".agents/skills/goi-workflow/SKILL.md" in skill
    assert "compatibility" in skill.lower()
    assert "does not replace, fork, or rewrite official skills" in skill
    assert len(skill.splitlines()) < 80
    assert "## Decision table" not in skill
    assert "verification_evidence:" not in skill
    assert "risk_level == high" not in skill


def test_goi_workflow_skill_carries_pre_execution_heuristics() -> None:
    skill = CANONICAL_SKILL.read_text(encoding="utf-8")

    assert "Before dispatch or non-trivial coding:" in skill
    assert "name the assumptions or unknowns that matter now" in skill
    assert "choose the simpler viable route and say why" in skill
    assert "phrase each non-trivial step as `action -> verification`" in skill
    assert "stop and ask rather" in skill


def test_subagent_task_packet_requires_assumptions_and_pass_condition() -> None:
    packet = CANONICAL_PACKET.read_text(encoding="utf-8")

    assert "Assumptions / unknowns:" in packet
    assert "Stop and ask if:" in packet
    assert "- <exact command or observable check>" in packet
    assert "- pass condition: <what counts as done>" in packet
    assert "- pass condition satisfied: yes|no" in packet


def test_codex_packet_is_only_a_compatibility_shim() -> None:
    packet = COMPAT_PACKET.read_text(encoding="utf-8")

    assert ".agents/skills/goi-workflow/references/subagent-task-packet.md" in packet
    assert "non-authoritative" in packet
    assert len(packet.splitlines()) < 30
    assert "Assumptions / unknowns:" not in packet

