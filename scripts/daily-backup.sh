#!/usr/bin/env bash
set -euo pipefail

WORKSPACE="/root/.openclaw/workspace"
BRANCH="main"
TIMESTAMP="$(date -u +'%Y-%m-%d %H:%M:%S UTC')"

cd "$WORKSPACE"

# Garante que há mudanças antes de commitar
git add -A

if git diff --cached --quiet; then
  echo "[$TIMESTAMP] Nenhuma mudança para backup."
  exit 0
fi

git commit -m "chore(backup): snapshot ${TIMESTAMP}"
git push origin "$BRANCH"

echo "[$TIMESTAMP] Backup enviado com sucesso."
