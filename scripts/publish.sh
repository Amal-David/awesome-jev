#!/usr/bin/env bash
# Publish only generated directory files. Never force-push or overwrite a conflict.
set -euo pipefail

branch="${DEFAULT_BRANCH:-main}"
git check-ref-format "refs/heads/$branch" >/dev/null

report() {
  printf '%s\n' "$1"
  if [[ -n "${GITHUB_STEP_SUMMARY:-}" ]]; then
    printf '%s\n' "$1" >> "$GITHUB_STEP_SUMMARY"
  fi
}

git config user.name 'github-actions[bot]'
git config user.email '41898282+github-actions[bot]@users.noreply.github.com'
git add -- README.md data/catalog.json docs/CATALOG.md data/discoveries.json
if git diff --cached --quiet; then
  report 'No directory changes.'
  exit 0
fi
# An unrelated staged file must never slip into the bot's commit.
while IFS= read -r -d '' path; do
  case "$path" in
    README.md|data/catalog.json|docs/CATALOG.md|data/discoveries.json) ;;
    *) printf 'Refusing to commit unexpected staged file: %s\n' "$path" >&2; exit 1 ;;
  esac
done < <(git diff --cached --name-only -z)
git commit -m 'chore: refresh Jev directory and source metadata'

for attempt in 1 2 3; do
  git fetch --no-tags origin "refs/heads/$branch"
  if git merge-base --is-ancestor HEAD FETCH_HEAD; then
    report "Directory commit already present remotely: $(git rev-parse --short HEAD)"
    exit 0
  fi
  if ! git rebase FETCH_HEAD; then
    git rebase --abort || true
    report 'Publish stopped: concurrent changes conflict. No force-push was attempted.'
    exit 1
  fi
  # The transport may report failure after the server has accepted the ref update.
  # Verify actual remote ancestry after either result, rather than trusting its exit code.
  if ! git push origin "HEAD:refs/heads/$branch"; then
    printf 'Push attempt %s reported an error; checking remote state.\n' "$attempt" >&2
  fi
  git fetch --no-tags origin "refs/heads/$branch"
  if git merge-base --is-ancestor HEAD FETCH_HEAD; then
    report "Published and verified directory update: $(git rev-parse --short HEAD)"
    exit 0
  fi
done
report 'Publish failed after three verified attempts. Local changes were not force-pushed.'
exit 1
