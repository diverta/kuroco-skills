#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
cd "$repo_root"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

skill_count="$(find skills -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
[ "$skill_count" = "11" ] || fail "expected 11 canonical skills, found $skill_count"

for skill_dir in skills/*; do
  [ -f "$skill_dir/SKILL.md" ] || fail "$skill_dir has no SKILL.md"

  skill_name="$(sed -n 's/^name: *//p' "$skill_dir/SKILL.md" | head -n 1)"
  [ -n "$skill_name" ] || fail "$skill_dir has no frontmatter name"

  metadata="$skill_dir/agents/openai.yaml"
  [ -f "$metadata" ] || fail "$metadata is missing"
  grep -q '^  display_name: "' "$metadata" || fail "$metadata has no display_name"
  grep -q '^  short_description: "' "$metadata" || fail "$metadata has no short_description"
  grep -Fq "\$$skill_name" "$metadata" || fail "$metadata default_prompt does not mention \$$skill_name"
done

if find skills -type f -name '*.md' ! -path 'skills/kuroco-docs/docs/*' -print0 \
  | xargs -0 grep -nF '${CLAUDE_SKILL_DIR}'; then
  fail "Claude-specific skill directory variable found"
fi

grep -q -- '-x "agents/openai.yaml"' scripts/build-skill-zips.sh \
  || fail "Claude ZIP exclusion for openai.yaml is missing"

echo "PASS: $skill_count canonical skills have portable Codex metadata"
