from __future__ import annotations

import json
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def test_pyproject_version_matches_latest_release_docs() -> None:
    pyproject = _read("pyproject.toml")
    changelog = _read("CHANGELOG.md")

    assert 'version = "0.1.1"' in pyproject
    assert "## 0.1.1 - 2026-05-09" in changelog
    assert (REPO_ROOT / "docs" / "releases" / "v0.1.1.md").exists()


def test_readme_and_mainline_spec_cover_claude_command_surfaces() -> None:
    readme = _read("README.md")
    mainline = _read("openspec/specs/project-mainline-routing/spec.md")

    assert ".claude/commands/opsx/" in readme
    assert ".claude/commands/opsx/" in mainline
    assert ".codex` intentionally uses skills only" in mainline


def test_readme_and_checklist_call_out_badge_replacement_for_adoption() -> None:
    readme = _read("README.md")
    checklist = _read("docs/ops/workflow/checklist.md")

    assert "Replace the README badge URL" in readme
    assert "Replace the README badge URL" in checklist


def test_openspec_config_has_real_project_context_not_scaffold_examples() -> None:
    config = _read("openspec/config.yaml")

    assert "Repository: workflow-auto" in config
    assert "Purpose: host the reusable workflow-base template" in config
    assert "TypeScript, React, Node.js" not in config
    assert "e-commerce platform" not in config


def test_no_completed_changes_remain_active_in_openspec_list() -> None:
    proc = subprocess.run(
        ["openspec", "list", "--json"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    payload = json.loads(proc.stdout)
    changes = payload.get("changes", [])

    assert all(change.get("status") != "complete" for change in changes), changes
