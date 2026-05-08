from __future__ import annotations

import json
import subprocess
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _read(relative_path: str) -> str:
    return (REPO_ROOT / relative_path).read_text(encoding="utf-8")


def test_model_diversity_doc_exists_and_stays_optional() -> None:
    text = _read("docs/ops/workflow/model-diversity.md")
    compact = " ".join(text.split())

    assert "optional model-diversity lane" in text
    assert "DeepSeek Claude CLI may be a primary writer, but not the final owner." in text
    assert "primary bounded code writer" in text
    assert "does not create a new route" in text
    assert "does not replace GOI routing, OpenSpec, `gstack`, review, or QA" in compact
    assert "not the repo's default workflow" in text
    assert "bypass verification" in text
    assert "commit local secrets" in text
    assert "`code-writer` -> `deepseek-v4-pro[1m]`" in text
    assert "`code-reviewer` -> `deepseek-v4-pro[1m]`" in text
    assert "`debug-investigator` -> `deepseek-v4-pro[1m]`" in text
    assert "`docs-reviewer` -> `deepseek-v4-pro[1m]`" in text
    assert "prefer explicit model selection over `auto`" in text


def test_gitignore_blocks_local_secret_bearing_files() -> None:
    gitignore = _read(".gitignore")

    for pattern in (
        ".claude/settings.local.json",
        ".env",
        ".env.*",
        "secrets/",
    ):
        assert pattern in gitignore


def test_code_writer_agent_is_bounded_and_not_final_owner() -> None:
    text = _read(".claude/agents/code-writer.md")

    assert "accepted scope" in text
    assert "execution-quality" in text
    assert "verification" in text
    assert "scope changes" in text
    assert "blocker" in text
    assert "do not make the final merge, tag, or release decision" in text


def test_reviewer_investigator_and_docs_agents_exist_with_bounded_posture() -> None:
    reviewer = _read(".claude/agents/code-reviewer.md")
    investigator = _read(".claude/agents/debug-investigator.md")
    docs = _read(".claude/agents/docs-reviewer.md")

    assert "read-only" in reviewer
    assert "blocking" in reviewer
    assert "important" in reviewer
    assert "low" in reviewer
    assert "start by reproducing the symptom" in investigator
    assert "if the same verification fails twice, escalate to `blocker`" in investigator
    assert "read-only" in docs
    assert "README" in docs
    assert "CI workflow" in docs


def test_optional_lane_is_not_described_as_mandatory_or_new_route() -> None:
    doc = _read("docs/ops/workflow/model-diversity.md")
    routing = _read(".agents/skills/goi-workflow/SKILL.md")

    assert "mandatory workflow" not in doc
    assert "main thread still owns" in doc
    assert "assess" in routing
    assert "micro" in routing
    assert "light" in routing
    assert "full" in routing
    assert "blocker" in routing
    assert "landing" in routing


def test_example_settings_file_uses_placeholders_only() -> None:
    example = _read(".claude/settings.deepseek.example.json")
    payload = json.loads(example)
    env = payload["env"]

    assert env["ANTHROPIC_BASE_URL"] == "https://api.deepseek.com/anthropic"
    assert env["ANTHROPIC_AUTH_TOKEN"] == "<DEEPSEEK_API_KEY_FROM_LOCAL_ENV_OR_SECRET_MANAGER>"
    assert env["ANTHROPIC_MODEL"] == "deepseek-v4-pro[1m]"
    assert env["ANTHROPIC_DEFAULT_OPUS_MODEL"] == "deepseek-v4-pro[1m]"
    assert env["ANTHROPIC_DEFAULT_SONNET_MODEL"] == "deepseek-v4-pro[1m]"
    assert env["ANTHROPIC_DEFAULT_HAIKU_MODEL"] == "deepseek-v4-pro[1m]"
    assert env["CLAUDE_CODE_SUBAGENT_MODEL"] == "deepseek-v4-pro[1m]"
    assert "deepseek-v4-flash" not in example
    assert "sk-" not in example


def test_local_settings_file_is_not_tracked() -> None:
    proc = subprocess.run(
        ["git", "ls-files", "--error-unmatch", ".claude/settings.local.json"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )

    assert proc.returncode != 0


def test_indexes_and_verifier_cover_model_diversity_surfaces() -> None:
    readme = _read("README.md")
    workflow_readme = _read("docs/ops/workflow/README.md")
    checklist = _read("docs/ops/workflow/checklist.md")
    verifier = _read("scripts/verify-workflow-template.sh")

    assert "docs/ops/workflow/model-diversity.md" in readme
    assert ".claude/agents/code-writer.md" in readme
    assert "model-diversity.md" in workflow_readme
    assert "optional model-diversity lane" in workflow_readme
    assert "docs/ops/workflow/model-diversity.md" in checklist
    assert '".claude/agents/code-writer.md"' in verifier
    assert '"docs/ops/workflow/model-diversity.md"' in verifier
