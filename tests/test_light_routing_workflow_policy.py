from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def test_six_route_modes_are_defined_on_operating_surfaces() -> None:
    surfaces = (
        ".agents/skills/goi-workflow/SKILL.md",
        "AGENTS.md",
        "docs/ops/workflow/skill-routing.md",
        "docs/ops/workflow/routing-table.md",
    )

    for surface in surfaces:
        text = _read(surface)
        for route in ("assess", "micro", "light", "full", "blocker", "landing"):
            assert f"`{route}`" in text, f"{surface} is missing {route}"


def test_non_trivial_route_trace_template_is_present() -> None:
    combined = "\n".join(
        [
            _read("AGENTS.md"),
            _read(".agents/skills/goi-workflow/SKILL.md"),
            _read("docs/ops/workflow/skill-routing.md"),
        ]
    )

    for field in ("Route:", "Why:", "Evidence:"):
        assert field in combined

    for field in (
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
    ):
        assert field in combined


def test_hard_gates_prevent_unsafe_light_routing() -> None:
    surfaces = (
        "AGENTS.md",
        ".agents/skills/goi-workflow/SKILL.md",
        "docs/ops/workflow/skill-routing.md",
        "docs/ops/workflow/routing-table.md",
    )

    combined = "\n".join(_read(surface) for surface in surfaces) + _read(
        "docs/ops/workflow/routing-checks.md"
    )

    assert "High-risk work cannot route to `micro`" in combined
    assert "Blocker, correction, or repeated-failure work must investigate before implementation" in combined
    assert "active OpenSpec" in combined
    assert "inherit" in combined.lower()


def test_skipped_verification_requires_reason_risk_and_followup() -> None:
    combined = "\n".join(
        [
            _read("AGENTS.md"),
            _read(".agents/skills/goi-workflow/SKILL.md"),
            _read("docs/ops/workflow/evidence.md"),
        ]
    )

    assert "skipped_verification:" in combined
    for field in ("check:", "reason:", "residual_risk:", "follow_up:"):
        assert field in combined


def test_instruction_files_are_supply_chain_sensitive() -> None:
    combined = "\n".join(
        [
            _read("AGENTS.md"),
            _read(".agents/skills/goi-workflow/SKILL.md"),
            _read("docs/ops/workflow/skill-routing.md"),
        ]
    )

    assert "supply-chain sensitive" in combined
    assert ".agents/skills/**" in combined
    assert ".codex/skills/**" in combined
    assert "docs/ops/workflow/**" in combined


def test_routing_predicates_stay_declarative() -> None:
    combined = "\n".join(
        [
            _read("AGENTS.md"),
            _read(".agents/skills/goi-workflow/SKILL.md"),
            _read("docs/ops/workflow/skill-routing.md"),
            _read("docs/ops/workflow/routing-table.md"),
            _read("docs/ops/workflow/routing-checks.md"),
        ]
    )

    forbidden = (
        "eval(",
        "exec(",
        "subprocess",
        "shell interpolation",
        "generated Python",
    )
    for pattern in forbidden:
        assert pattern not in combined


def test_codex_compatibility_surface_does_not_duplicate_router() -> None:
    compat = _read(".codex/skills/goi-workflow/SKILL.md")

    assert ".agents/skills/goi-workflow/SKILL.md" in compat
    assert len(compat.splitlines()) < 80
    assert "risk_level == high" not in compat
    assert "verification_evidence:" not in compat
    assert "| Priority |" not in compat


def test_routing_checks_cover_required_snapshot_cases() -> None:
    checks = _read("docs/ops/workflow/routing-checks.md")

    for case in (
        "High-risk workflow rule change",
        "Active OpenSpec implementation",
        "Active OpenSpec scope expansion",
        "Failing smoke",
        "Same test fails twice",
        "User asks",
        "README typo",
        "Architecture boundary change",
        "Release/archive",
        "Unknown project state",
        "Spec/code mismatch",
        "Small local code cleanup",
    ):
        assert case in checks


def test_workflow_surfaces_are_generic_and_path_safe() -> None:
    surfaces = (
        "AGENTS.md",
        ".agents/skills/goi-workflow/SKILL.md",
        ".codex/skills/goi-workflow/SKILL.md",
        "docs/ops/workflow/README.md",
        "docs/ops/workflow/skill-routing.md",
        "docs/ops/workflow/rule-reduction-checklist.md",
        "docs/ops/workflow/decisions/0003-event-driven-self-improvement-rail.md",
    )

    forbidden_patterns = (
        "avatar_pipeline",
        "KaoLRM",
        "single_image_service",
        "direct_multiview_service",
        "bridge_then_multiview_service",
        "/data/",
    )

    for surface in surfaces:
        text = _read(surface)
        for pattern in forbidden_patterns:
            assert pattern not in text, f"{surface} still contains {pattern!r}"


def test_live_workflow_specs_are_not_placeholders() -> None:
    routing_spec = _read("openspec/specs/workflow-routing-policy/spec.md")
    mainline_spec = _read("openspec/specs/project-mainline-routing/spec.md")
    placeholder = "T" + "BD"

    assert "## Purpose" in routing_spec
    assert placeholder not in routing_spec
    assert "light-routing/heavy-evidence workflow policy" in routing_spec

    assert "## Purpose" in mainline_spec
    assert placeholder not in mainline_spec
    assert "current mainline" in mainline_spec
    assert "truth-source hierarchy" in mainline_spec
    assert "## Current Mainline" in mainline_spec
    assert "## Shipped Surfaces" in mainline_spec
