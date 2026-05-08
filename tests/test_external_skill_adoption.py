from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def test_superpowers_analysis_lives_outside_workflow_control_surface() -> None:
    analysis = _read("docs/ops/superpowers-capability-adoption.md")

    assert "descriptive analysis" in analysis
    assert "obra/superpowers" in analysis
    assert "docs/ops/workflow/*" in analysis


def test_workflow_control_surfaces_describe_external_skill_posture_generically() -> None:
    combined = "\n".join(
        [
            _read("README.md"),
            _read("AGENTS.md"),
            _read("docs/ops/workflow/README.md"),
            _read("docs/ops/workflow/skill-routing.md"),
        ]
    )

    assert "external skill" in combined
    assert "mandatory" in combined
    assert "route selection" in combined

    workflow_control = "\n".join(
        [
            _read("AGENTS.md"),
            _read("docs/ops/workflow/README.md"),
            _read("docs/ops/workflow/skill-routing.md"),
        ]
    )
    assert "obra/superpowers" not in workflow_control


def test_superpowers_compatibility_wrappers_stay_thin() -> None:
    wrapper_paths = (
        ".codex/skills/brainstorming/SKILL.md",
        ".codex/skills/subagent-driven-development/SKILL.md",
        ".codex/skills/dispatching-parallel-agents/SKILL.md",
        ".codex/skills/test-driven-development/SKILL.md",
        ".codex/skills/using-git-worktrees/SKILL.md",
        ".codex/skills/writing-plans/SKILL.md",
        ".codex/skills/systematic-debugging/SKILL.md",
        ".codex/skills/requesting-code-review/SKILL.md",
        ".codex/skills/receiving-code-review/SKILL.md",
        ".codex/skills/verification-before-completion/SKILL.md",
    )

    for path in wrapper_paths:
        text = _read(path)
        assert "compatibility" in text.lower()
        assert len(text.splitlines()) < 60
        assert "mandatory foreign workflow chain" in text or "mandatory" in text


def test_capability_matrix_records_exclusions_for_conflicting_superpowers_flows() -> None:
    analysis = _read("docs/ops/superpowers-capability-adoption.md")

    assert "`subagent-driven-development`" in analysis
    assert "`dispatching-parallel-agents`" in analysis
    assert "`adopted`" in analysis
    assert "opt-in launch mode" in analysis


def test_test_driven_development_wrapper_points_to_repo_local_pytest_entrypoint() -> None:
    wrapper = _read(".codex/skills/test-driven-development/SKILL.md")
    analysis = _read("docs/ops/superpowers-capability-adoption.md")
    checklist = _read("docs/ops/workflow/checklist.md")
    readme = _read("README.md")

    assert "./.venv/bin/pytest -q" in wrapper
    assert "not mandatory" in wrapper
    assert "`test-driven-development`" in analysis
    assert "./.venv/bin/pytest -q" in analysis
    assert "./.venv/bin/pytest -q" in checklist
    assert "./.venv/bin/pytest -q" in readme
