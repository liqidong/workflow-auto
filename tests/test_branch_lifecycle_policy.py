from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def test_agents_and_worktree_docs_define_branch_cleanup_policy() -> None:
    agents = _read("AGENTS.md")
    worktrees = _read("docs/ops/git-worktree-layout.md")

    assert "merge the finished feature branch back to `main` only after verification" in agents
    assert "delete the local branch" in agents
    assert "delete the remote feature branch" in agents
    assert "remove its `.worktrees/...` directory" in agents
    assert "treat `lane/*` branches as explicit long-lived support lanes" in agents

    assert "merged `feat/*` branches should be cleaned up when no longer needed" in worktrees
    assert "`lane/*` branches are explicit exceptions" in worktrees
    assert "git branch -d feat/my-task" in worktrees
    assert "git push origin --delete feat/my-task" in worktrees
    assert "git worktree remove .worktrees/feat-my-task" in worktrees


def test_readme_and_checklist_preserve_feat_vs_lane_lifecycle_distinction() -> None:
    readme = _read("README.md")
    checklist = _read("docs/ops/workflow/checklist.md")
    spec = _read("openspec/specs/branch-lifecycle-policy/spec.md")

    assert "merged `feat/*` branches are cleaned up after verification and merge" in readme
    assert "long-lived `lane/*` branches are preserved" in readme
    assert "bounded `feat/*` branches are treated as short-lived and cleaned up" in checklist
    assert "long-lived `lane/*` branches are documented as exceptions" in checklist
    assert "docs/ops/git-worktree-layout.md" in readme
    assert "openspec/specs/branch-lifecycle-policy/spec.md" in readme
    assert "long-lived `lane/*`" in spec
    assert "remote feature branch deletion when no longer needed" in spec
