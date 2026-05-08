#!/usr/bin/env bash
set -euo pipefail

failures=0

ok() {
  printf 'ok: %s\n' "$1"
}

warn() {
  printf 'warn: %s\n' "$1"
}

fail() {
  printf 'missing: %s\n' "$1" >&2
  failures=1
}

require_cmd() {
  local cmd="$1"
  if command -v "$cmd" >/dev/null 2>&1; then
    ok "command '$cmd'"
  else
    fail "command '$cmd' on PATH"
  fi
}

require_cmd git
require_cmd rg
require_cmd openspec

if command -v python3 >/dev/null 2>&1; then
  ok "command 'python3'"
elif command -v python >/dev/null 2>&1; then
  ok "command 'python'"
else
  fail "python3 or python on PATH"
fi

if [ -d ".venv" ]; then
  ok "local virtualenv '.venv/'"
else
  fail "local virtualenv '.venv/'"
  printf "hint: python3 -m venv .venv && ./.venv/bin/pip install -e '.[dev]'\n" >&2
fi

if [ -x "./.venv/bin/python" ]; then
  ok "local interpreter './.venv/bin/python'"
else
  fail "local interpreter './.venv/bin/python'"
fi

if [ -x "./.venv/bin/pytest" ]; then
  ok "local pytest './.venv/bin/pytest'"
else
  fail "local pytest './.venv/bin/pytest'"
  printf "hint: ./.venv/bin/pip install -e '.[dev]'\n" >&2
fi

for path in ".agents/skills" ".codex/skills" ".claude/skills"; do
  if [ -d "$path" ]; then
    ok "skill discovery path '$path'"
  else
    warn "optional skill discovery path '$path' not found"
  fi
done

if [ "$failures" -ne 0 ]; then
  exit 1
fi

echo "host workflow dependency check passed"
