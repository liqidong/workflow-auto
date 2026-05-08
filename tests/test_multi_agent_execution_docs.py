from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def test_multi_agent_execution_doc_exists_and_covers_five_patterns() -> None:
    doc = (REPO_ROOT / "docs" / "ops" / "workflow" / "multi-agent-execution.md").read_text(
        encoding="utf-8"
    )

    for heading in (
        "### Prompt chaining",
        "### Routing",
        "### Parallelization",
        "### Orchestrator-workers",
        "### Evaluator-optimizer",
    ):
        assert heading in doc

    assert "```mermaid" in doc
    assert "one writer" in doc
    assert "fresh read-only reviewer" in doc
    assert "separate worktrees" in doc
    assert "Inference note:" in doc
    assert "https://code.claude.com/docs/en/sub-agents" in doc
    assert "https://developers.openai.com/codex/use-cases" in doc
    assert "https://github.com/openai/skills" in doc
    assert "avatar_pipeline" not in doc
    assert "/data/" not in doc


def test_multi_agent_execution_doc_is_linked_from_operating_surfaces() -> None:
    required_link = "docs/ops/workflow/multi-agent-execution.md"

    workflow_readme = (REPO_ROOT / "docs" / "ops" / "workflow" / "README.md").read_text(
        encoding="utf-8"
    )
    agents = (REPO_ROOT / "AGENTS.md").read_text(encoding="utf-8")
    feedback_log = (REPO_ROOT / "docs" / "ops" / "agent-orchestration-feedback.md").read_text(
        encoding="utf-8"
    )

    assert "multi-agent-execution.md" in workflow_readme
    assert required_link in agents
    assert required_link in feedback_log
    assert "not the primary operating guide" in feedback_log


def test_template_includes_lightweight_checklist_and_worktree_doc() -> None:
    checklist = (REPO_ROOT / "docs" / "ops" / "workflow" / "checklist.md").read_text(
        encoding="utf-8"
    )
    worktree = (REPO_ROOT / "docs" / "ops" / "git-worktree-layout.md").read_text(
        encoding="utf-8"
    )

    assert "scripts/verify-workflow-template.sh" in checklist
    assert "pytest -q" in checklist
    assert "openspec validate --specs" in checklist
    assert "main -> feat/* -> main" in worktree
    assert ".worktrees/" in worktree

