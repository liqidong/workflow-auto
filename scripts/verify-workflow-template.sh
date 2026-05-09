#!/usr/bin/env bash
set -euo pipefail

required_files=(
  "AGENTS.md"
  "README.md"
  "CHANGELOG.md"
  "docs/releases/v0.1.0.md"
  "docs/releases/v0.1.1.md"
  ".github/workflows/verify.yml"
  ".agents/skills/goi-workflow/SKILL.md"
  ".codex/skills/goi-workflow/SKILL.md"
  ".claude/skills/goi-workflow/SKILL.md"
  ".claude/commands/opsx/explore.md"
  ".claude/commands/opsx/propose.md"
  ".claude/commands/opsx/apply.md"
  ".claude/commands/opsx/archive.md"
  "docs/ops/workflow/README.md"
  "docs/ops/workflow/skill-routing.md"
  "docs/ops/workflow/routing-table.md"
  "docs/ops/workflow/evidence.md"
  "docs/ops/workflow/routing-checks.md"
  "docs/ops/workflow/execution-quality.md"
  "docs/ops/workflow/multi-agent-execution.md"
  "docs/ops/workflow/checklist.md"
  "docs/ops/git-worktree-layout.md"
  "docs/ops/superpowers-capability-adoption.md"
  "scripts/check-host-workflow-deps.sh"
  "openspec/specs/branch-lifecycle-policy/spec.md"
  "openspec/specs/workflow-routing-policy/spec.md"
  "openspec/specs/project-mainline-routing/spec.md"
)

for path in "${required_files[@]}"; do
  test -f "$path"
done

grep -q "light routing / heavy evidence" .agents/skills/goi-workflow/SKILL.md
grep -q "gstack stage:" AGENTS.md
grep -q "workflow-auto" README.md
grep -q "workflow-base" README.md
grep -q "badge.svg" README.md
grep -q "lane/\\*" README.md
grep -q 'version = "0.1.1"' pyproject.toml
grep -q "## 0.1.1 - 2026-05-09" CHANGELOG.md
grep -q "0.1.0 - 2026-05-09" CHANGELOG.md
grep -q "## What this release is" docs/releases/v0.1.0.md
grep -q "## What this release is" docs/releases/v0.1.1.md
grep -q ".claude/commands/opsx/" README.md
grep -q "pull_request" .github/workflows/verify.yml
grep -q "openspec validate --specs" .github/workflows/verify.yml
grep -q "ripgrep" .github/workflows/verify.yml
grep -q "@fission-ai/openspec@1.3.1" .github/workflows/verify.yml
grep -q "## Current Mainline" openspec/specs/project-mainline-routing/spec.md
grep -q "## Shipped Surfaces" openspec/specs/project-mainline-routing/spec.md
grep -q "## Truth Source Hierarchy" openspec/specs/project-mainline-routing/spec.md
grep -q ".claude/commands/opsx/" openspec/specs/project-mainline-routing/spec.md
grep -q "Think Before Coding" docs/ops/workflow/execution-quality.md
grep -q "do not replace" docs/ops/workflow/execution-quality.md
grep -q "do not create a new route" .agents/skills/goi-workflow/SKILL.md
grep -q "compatibility shim" .claude/skills/goi-workflow/SKILL.md
grep -q "openspec archive" .codex/skills/openspec-archive-change/SKILL.md
grep -q "descriptive analysis" docs/ops/superpowers-capability-adoption.md
grep -q "Repository: workflow-auto" openspec/config.yaml
grep -q "delete the local branch" AGENTS.md
grep -q "lane/\\*" AGENTS.md
grep -q "git worktree remove .worktrees/feat-my-task" docs/ops/git-worktree-layout.md
grep -q "feature branches SHALL have an explicit cleanup policy" openspec/specs/branch-lifecycle-policy/spec.md

if rg -n "TypeScript, React, Node.js|e-commerce platform" openspec/config.yaml >/dev/null; then
  echo "Found OpenSpec scaffold residue in openspec/config.yaml" >&2
  exit 1
fi

if rg -n "obra/superpowers" docs/ops/workflow AGENTS.md >/dev/null; then
  echo "Found external methodology name in workflow control surface" >&2
  exit 1
fi

for stale in "avatar_pipeline" "KaoLRM" "single_image_service" "direct_multiview_service" "openspec-sync-specs"; do
  if rg -n "$stale" \
    .agents .codex .claude docs/ops/workflow openspec/specs README.md AGENTS.md \
    --glob '!tests/**' \
    --glob '!scripts/verify-workflow-template.sh' >/dev/null; then
    echo "Found stale source residue: $stale" >&2
    exit 1
  fi
done

echo "workflow-auto template verification passed"
