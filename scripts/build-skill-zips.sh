#!/usr/bin/env bash
# Build one zip per skill under skills/*/, with SKILL.md at the zip root
# (required by claude.ai's manual skill upload — it does not accept a
# GitHub repo reference, only a zip per skill).
#
# Usage: scripts/build-skill-zips.sh [output_dir]
#   output_dir defaults to "dist" (relative to the repo root).
#
# Each zip is named after the skill's `name:` frontmatter field in its
# SKILL.md (e.g. kuroco-app-builder.zip), not the directory name, so the
# file name always matches the skill identity even if a directory is
# renamed independently of its skill name.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR_ARG="${1:-dist}"

cd "$REPO_ROOT"

mkdir -p "$OUTPUT_DIR_ARG"
OUTPUT_DIR="$(cd "$OUTPUT_DIR_ARG" && pwd)"
rm -f "$OUTPUT_DIR"/*.zip

built=()

for skill_dir in skills/*/; do
  skill_md="${skill_dir}SKILL.md"
  if [ ! -f "$skill_md" ]; then
    echo "skip: $skill_dir (no SKILL.md)" >&2
    continue
  fi

  name="$(grep -m1 '^name:' "$skill_md" | sed 's/^name: *//; s/\r$//')"
  if [ -z "$name" ]; then
    echo "skip: $skill_dir (no name: in frontmatter)" >&2
    continue
  fi

  zip_path="$OUTPUT_DIR/${name}.zip"
  rm -f "$zip_path"

  # cd into the skill dir so SKILL.md lands at the zip root, not nested
  # under the skill's directory name.
  (
    cd "$skill_dir"
    zip -rq "$zip_path" . \
      -x ".DS_Store" -x "*/.DS_Store" -x ".git*" \
      -x "agents/openai.yaml"
  )

  built+=("${name}.zip")
  echo "built: $OUTPUT_DIR_ARG/${name}.zip"
done

# Bundle every skill zip into one archive so all skills can be downloaded
# in a single click. Each inner zip stays individually uploadable to
# claude.ai after extraction.
BUNDLE_NAME="kuroco-skills-all.zip"
if [ "${#built[@]}" -gt 0 ]; then
  (
    cd "$OUTPUT_DIR"
    zip -q "$BUNDLE_NAME" "${built[@]}"
  )
  echo "built: $OUTPUT_DIR_ARG/$BUNDLE_NAME (bundle of ${#built[@]} zips)"
fi

echo
echo "${#built[@]} skill zip(s) + 1 bundle written to $OUTPUT_DIR_ARG/"
