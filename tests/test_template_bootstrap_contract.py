from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def test_readme_requires_copied_repo_to_replace_generic_posture() -> None:
    readme = _read("README.md")

    assert "Replace the generic sections in `README.md` with your repository's actual" in readme
    assert "product, platform, or library posture" in readme


def test_mainline_spec_requires_copied_repo_to_replace_host_identity_and_inventory() -> None:
    spec = _read("openspec/specs/project-mainline-routing/spec.md")

    assert "Copied repositories must replace this host-repo identity and current-mainline" in spec
    assert "must not continue to describe itself as the" in spec
    assert "`workflow-auto` host repo" in spec


def test_canonical_goi_skill_path_remains_agents() -> None:
    skill = _read(".agents/skills/goi-workflow/SKILL.md")

    assert "This is the canonical repo-local GOI workflow skill." in skill
    assert ".agents/skills/goi-workflow/SKILL.md" in _read(".codex/skills/goi-workflow/SKILL.md")
    assert ".agents/skills/goi-workflow/SKILL.md" in _read(".claude/skills/goi-workflow/SKILL.md")


def test_codex_and_claude_goi_shims_remain_thin() -> None:
    for path in (
        ".codex/skills/goi-workflow/SKILL.md",
        ".claude/skills/goi-workflow/SKILL.md",
    ):
        text = _read(path)
        assert "compatibility" in text.lower()
        assert len(text.splitlines()) < 80
        assert "verification_evidence:" not in text
        assert "risk_level == high" not in text


def test_generic_workflow_surfaces_do_not_identify_copied_repo_as_workflow_auto_host() -> None:
    for path in (
        ".agents/skills/goi-workflow/SKILL.md",
        "docs/ops/workflow/skill-routing.md",
        "docs/ops/workflow/README.md",
        ".codex/skills/goi-workflow/SKILL.md",
        ".claude/skills/goi-workflow/SKILL.md",
    ):
        assert "workflow-auto" not in _read(path), path


def test_github_actions_verification_workflow_exists_and_matches_local_chain() -> None:
    workflow = _read(".github/workflows/verify.yml")

    for token in (
        "push:",
        "pull_request:",
        "python -m venv .venv",
        "pip install -e '.[dev]'",
        "npm install -g @fission-ai/openspec@latest",
        "scripts/check-host-workflow-deps.sh",
        "scripts/verify-workflow-template.sh",
        "./.venv/bin/pytest -q",
        "openspec validate --specs",
    ):
        assert token in workflow
