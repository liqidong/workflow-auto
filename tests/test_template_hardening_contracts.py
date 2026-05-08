from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SHORT_TRACE_FIELDS = ("Route:", "Why:", "Evidence:")
FULL_TRACE_FIELDS = (
    "Route:",
    "gstack stage:",
    "gstack status:",
    "gstack reason:",
    "OpenSpec:",
    "OpenSpec reason:",
    "OpenSpec control surface:",
    "self-improvement:",
    "self-improvement reason:",
    "Project state:",
    "Task kind:",
    "Risk level:",
    "Problem kind:",
    "Control surface:",
    "Entry:",
    "Reason:",
    "Verification required:",
)


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def test_repo_identity_is_explicit_and_consistent() -> None:
    readme = _read("README.md")
    agents = _read("AGENTS.md")
    mainline = _read("openspec/specs/project-mainline-routing/spec.md")
    pyproject = _read("pyproject.toml")

    assert "`workflow-auto` is the repository that hosts the reusable `workflow-base`" in readme
    assert "workflow-auto" in agents
    assert "workflow-base" in agents
    assert "Public repository name: `workflow-auto`" in mainline
    assert 'name = "workflow-auto"' in pyproject


def test_current_mainline_inventory_is_concrete() -> None:
    mainline = _read("openspec/specs/project-mainline-routing/spec.md")

    for heading in (
        "## Current Repository Identity",
        "## Current Mainline",
        "## Shipped Surfaces",
        "## Planned Surfaces",
        "## Evidence-only / Support Lanes",
        "## Truth Source Hierarchy",
    ):
        assert heading in mainline

    for surface in (
        ".agents/skills/goi-workflow/SKILL.md",
        ".codex/skills/goi-workflow/SKILL.md",
        ".claude/skills/goi-workflow/SKILL.md",
        "scripts/check-host-workflow-deps.sh",
        "scripts/verify-workflow-template.sh",
        "tests/",
    ):
        assert surface in mainline


def test_readme_declared_key_surfaces_exist() -> None:
    readme = _read("README.md")
    required_paths = (
        "AGENTS.md",
        ".agents/skills/goi-workflow/SKILL.md",
        ".codex/skills/goi-workflow/SKILL.md",
        ".claude/skills/goi-workflow/SKILL.md",
        "scripts/check-host-workflow-deps.sh",
        "scripts/verify-workflow-template.sh",
        "openspec/specs/workflow-routing-policy/spec.md",
        "openspec/specs/project-mainline-routing/spec.md",
    )

    for relative_path in required_paths:
        assert relative_path in readme
        assert (REPO_ROOT / relative_path).exists()


def test_short_and_full_trace_posture_is_consistent() -> None:
    surfaces = (
        "AGENTS.md",
        ".agents/skills/goi-workflow/SKILL.md",
        "docs/ops/workflow/skill-routing.md",
    )

    for surface in surfaces:
        text = _read(surface)
        for field in SHORT_TRACE_FIELDS:
            assert field in text, f"{surface} is missing short-trace field {field}"
        for field in FULL_TRACE_FIELDS:
            assert field in text, f"{surface} is missing full-trace field {field}"

        for trigger in (
            "workflow / instruction files change",
            "architecture, security, deployment, or data-contract work is in scope",
            "blocker, correction, or repeated failure conditions",
            "parallel-dispatch launch",
            "landing, release, deploy, archive, or closeout work",
            "user explicitly asks for the complete route trace",
        ):
            assert trigger in text, f"{surface} is missing trigger {trigger!r}"


def test_hard_gates_and_evidence_contract_stay_consistent() -> None:
    combined = "\n".join(
        [
            _read("AGENTS.md"),
            _read(".agents/skills/goi-workflow/SKILL.md"),
            _read("docs/ops/workflow/skill-routing.md"),
            _read("docs/ops/workflow/routing-table.md"),
            _read("docs/ops/workflow/evidence.md"),
        ]
    )

    assert "High-risk work cannot route to `micro`" in combined
    assert "Blocker, correction, or repeated-failure work must investigate before" in combined
    assert "Active OpenSpec" in combined
    assert "skipped_verification:" in combined
    for field in ("check:", "reason:", "residual_risk:", "follow_up:"):
        assert field in combined


def test_codex_and_claude_goi_shims_stay_thin() -> None:
    for path in (
        ".codex/skills/goi-workflow/SKILL.md",
        ".claude/skills/goi-workflow/SKILL.md",
    ):
        text = _read(path)
        assert ".agents/skills/goi-workflow/SKILL.md" in text
        assert "compatibility" in text.lower()
        assert len(text.splitlines()) < 80
        assert "risk_level == high" not in text
        assert "verification_evidence:" not in text
        assert "| Priority |" not in text


def test_host_dependency_script_checks_required_tooling() -> None:
    script = _read("scripts/check-host-workflow-deps.sh")

    for token in (
        "require_cmd git",
        "require_cmd rg",
        "require_cmd openspec",
        ".venv",
        "./.venv/bin/pytest",
        "python3 -m venv .venv",
    ):
        assert token in script
