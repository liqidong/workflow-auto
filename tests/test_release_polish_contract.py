from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def test_readme_has_verify_badge() -> None:
    readme = _read("README.md")

    assert "[![Verify](https://github.com/liqidong/workflow-auto/actions/workflows/verify.yml/badge.svg)]" in readme
    assert "(https://github.com/liqidong/workflow-auto/actions/workflows/verify.yml)" in readme


def test_changelog_exists_with_v010_entry() -> None:
    changelog = _read("CHANGELOG.md")

    assert "# Changelog" in changelog
    assert "## 0.1.0 - 2026-05-09" in changelog
    assert "GitHub Actions verification" in changelog
    assert "bootstrap contract coverage" in changelog
    assert "@fission-ai/openspec@1.3.1" in changelog


def test_release_note_exists_and_covers_required_sections() -> None:
    release = _read("docs/releases/v0.1.0.md")

    for heading in (
        "## What this release is",
        "## What is included",
        "## How to verify locally",
        "## How to copy or adopt the template",
        "## Known residual risks",
        "## Next recommended work",
    ):
        assert heading in release


def test_verify_workflow_pins_openspec_and_installs_ripgrep() -> None:
    workflow = _read(".github/workflows/verify.yml")

    assert "sudo apt-get update && sudo apt-get install -y ripgrep" in workflow
    assert "npm install -g @fission-ai/openspec@1.3.1" in workflow


def test_release_docs_are_wired_into_repo_surfaces() -> None:
    readme = _read("README.md")
    verifier = _read("scripts/verify-workflow-template.sh")

    assert "CHANGELOG.md" in readme
    assert "docs/releases/v0.1.0.md" in readme
    assert '"CHANGELOG.md"' in verifier
    assert '"docs/releases/v0.1.0.md"' in verifier
