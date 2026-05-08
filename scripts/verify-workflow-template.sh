#!/usr/bin/env bash
set -euo pipefail

required_files=(
  "AGENTS.md"
  "README.md"
  ".agents/skills/goi-workflow/SKILL.md"
  ".codex/skills/goi-workflow/SKILL.md"
  ".claude/skills/goi-workflow/SKILL.md"
  "docs/ops/workflow/README.md"
  "docs/ops/workflow/skill-routing.md"
  "docs/ops/workflow/routing-table.md"
  "docs/ops/workflow/evidence.md"
  "docs/ops/workflow/routing-checks.md"
  "docs/ops/workflow/multi-agent-execution.md"
  "docs/ops/workflow/checklist.md"
  "docs/ops/superpowers-capability-adoption.md"
  "scripts/check-host-workflow-deps.sh"
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
grep -q "## Current Mainline" openspec/specs/project-mainline-routing/spec.md
grep -q "## Shipped Surfaces" openspec/specs/project-mainline-routing/spec.md
grep -q "## Truth Source Hierarchy" openspec/specs/project-mainline-routing/spec.md
grep -q "compatibility shim" .claude/skills/goi-workflow/SKILL.md
grep -q "openspec archive" .codex/skills/openspec-archive-change/SKILL.md
grep -q "descriptive analysis" docs/ops/superpowers-capability-adoption.md

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
