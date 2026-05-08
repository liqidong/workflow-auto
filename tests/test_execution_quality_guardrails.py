from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def test_execution_quality_doc_exists_and_covers_four_principles() -> None:
    doc = _read("docs/ops/workflow/execution-quality.md")

    for heading in (
        "# Execution Quality Guardrails",
        "## Think Before Coding",
        "## Simplicity First",
        "## Surgical Changes",
        "## Goal-Driven Execution",
    ):
        assert heading in doc


def test_execution_quality_doc_stays_non_routing_and_non_replacing() -> None:
    doc = _read("docs/ops/workflow/execution-quality.md")

    assert "It is not a new workflow." in doc
    assert "It does not replace:" in doc
    assert "GOI routing" in doc
    assert "OpenSpec" in doc
    assert "`gstack`" in doc
    assert "review" in doc
    assert "QA" in doc
    assert "These guardrails constrain how implementation work is executed after route" in doc


def test_execution_quality_scope_and_non_scope_are_explicit() -> None:
    doc = _read("docs/ops/workflow/execution-quality.md")

    for item in (
        "implementation",
        "debugging",
        "hardening",
        "review-finding fixes",
        "blocker fixes",
        "trivial typo or path fixes do not need the full guardrail expansion",
        "read-only `assess` work should not pretend it is executing coding guardrails",
    ):
        assert item in doc


def test_canonical_goi_skill_references_execution_quality_guardrails() -> None:
    skill = _read(".agents/skills/goi-workflow/SKILL.md")

    assert "## Execution Quality Guardrails" in skill
    assert "think before coding" in skill
    assert "simplicity first" in skill
    assert "surgical changes" in skill
    assert "goal-driven execution" in skill
    assert "do not create a new route" in skill
    assert "do not replace GOI routing, OpenSpec, `gstack`," in skill


def test_readme_workflow_readme_and_checklist_include_execution_quality_doc() -> None:
    readme = _read("README.md")
    workflow_readme = _read("docs/ops/workflow/README.md")
    checklist = _read("docs/ops/workflow/checklist.md")

    for text in (readme, workflow_readme, checklist):
        assert "docs/ops/workflow/execution-quality.md" in text or "execution-quality.md" in text


def test_workflow_control_surfaces_do_not_depend_on_external_repo_name() -> None:
    surfaces = (
        ".agents/skills/goi-workflow/SKILL.md",
        "docs/ops/workflow/README.md",
        "docs/ops/workflow/execution-quality.md",
        "docs/ops/workflow/checklist.md",
        "scripts/verify-workflow-template.sh",
    )

    for surface in surfaces:
        text = _read(surface)
        assert "andrej-karpathy-skills" not in text
