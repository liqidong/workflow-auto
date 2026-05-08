from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def test_openspec_archive_wrappers_use_official_cli() -> None:
    surfaces = (
        ".codex/skills/openspec-archive-change/SKILL.md",
        ".claude/skills/openspec-archive-change/SKILL.md",
        ".claude/commands/opsx/archive.md",
    )

    for surface in surfaces:
        text = _read(surface)
        assert 'openspec archive "<name>"' in text or "openspec archive" in text
        assert "--skip-specs" in text or "skip-specs" in text
        assert "manual file moves" in text or "manual directory moves" in text


def test_openspec_wrappers_do_not_keep_stale_host_tool_references() -> None:
    surfaces = (
        ".codex/skills/openspec-explore/SKILL.md",
        ".codex/skills/openspec-propose/SKILL.md",
        ".codex/skills/openspec-apply-change/SKILL.md",
        ".codex/skills/openspec-archive-change/SKILL.md",
        ".claude/skills/openspec-explore/SKILL.md",
        ".claude/skills/openspec-propose/SKILL.md",
        ".claude/skills/openspec-apply-change/SKILL.md",
        ".claude/skills/openspec-archive-change/SKILL.md",
        ".claude/commands/opsx/explore.md",
        ".claude/commands/opsx/propose.md",
        ".claude/commands/opsx/apply.md",
        ".claude/commands/opsx/archive.md",
    )

    stale_patterns = (
        "AskUserQuestion",
        "TodoWrite",
        "Task tool",
        "openspec-sync-specs",
        "openspec-continue-change",
        "/opsx:continue",
        "connect-chrome",
    )

    for surface in surfaces:
        text = _read(surface)
        for pattern in stale_patterns:
            assert pattern not in text, f"{surface} still contains {pattern!r}"

