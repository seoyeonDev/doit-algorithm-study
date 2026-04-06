#!/bin/bash
git config core.hooksPath .github/hooks
chmod +x .github/hooks/pre-push
echo "✅ Git hooks 설정 완료"

git pull