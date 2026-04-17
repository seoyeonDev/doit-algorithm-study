# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 프로젝트 개요

"Do it! 자료구조와 함께 배우는 알고리즘 입문 — 파이썬 편" 교재 기반 알고리즘 스터디 레포.
4명이 매주 목요일 20:00 KST에 모이며, W00(오리엔테이션) ~ W17(최종 회고)까지 총 17주 진행.

## 초기 세팅

```bash
bash setup.sh
# 또는
git config core.hooksPath .github/hooks
```

`pre-push` 훅이 활성화되어 브랜치 이름 규칙을 위반하면 push가 차단된다.

## 브랜치 네이밍 규칙

| 브랜치 | 용도 | PR 리뷰 |
|--------|------|---------|
| `summary/weekNN/이름` | 주차별 요약 | 불필요 |
| `solve/weekNN/이름` | 주차별 풀이 | **1명 이상 필수** |
| `feature/...` | 기타 작업 | - |

주차 번호는 반드시 2자리 (`week01` ✅ / `week1` ❌)

## 커밋 메시지 규칙

| prefix | 용도 |
|--------|------|
| `docs:` | 요약 파일 |
| `solve:` | 풀이 파일 |
| `fix:` | 오류 수정 |
| `chore:` | 기타 |

## 폴더 구조

```
weekNN/
├── summary/    # 멤버별 요약 마크다운
├── problem/    # 문제 설명
└── solved/     # 멤버별 Python 풀이 (.py)
pages/          # 정적 웹사이트 (Vercel 배포)
api/            # Vercel Serverless Function (GitHub API 프록시)
.github/
├── scripts/    # facilitator_notify.py, session_timer.py
├── workflows/  # GitHub Actions
├── hooks/      # pre-push 브랜치 네이밍 검사
└── facilitator-config.json
```

## GitHub Actions 워크플로우

| 워크플로우 | 트리거 | 역할 |
|-----------|--------|------|
| `run-solutions.yml` | PR (`solved/*.py` 변경 시) | 풀이 실행 후 결과를 PR 코멘트로 게시 |
| `facilitator-notify.yml` | 매주 수요일 00:00 UTC (cron) / 수동 | 이번 주 진행자를 Discord에 알림 |
| `session-timer.yml` | 수동 (`workflow_dispatch`) | 스터디 세션 중 단계별 Discord 알림 전송 |

## Automation 스크립트

### facilitator_notify.py
- `pages/weeks.json`(커리큘럼)과 `.github/facilitator-config.json`(멤버+Discord ID) 을 읽어 round-robin으로 진행자 계산
- **W00은 반드시 순번에서 제외** (`weeks = [w for w in data["weeks"] if w["num"] != "W00"]`)
- W00 포함 시 인덱스가 밀려 W01 진행자가 members[1]로 잘못 계산됨
- `overrides`: `null` = 쉬는 주(카운터 유지), 이름 문자열 = 대타(카운터 증가)
- 환경변수: `DISCORD_WEBHOOK_URL_NOTIFY`

### session_timer.py
- 세션 일정: 오프닝(0-5분) → 요약+토론(5-45분) → 코딩리뷰(45-57분) → 마무리(57-60분)
- 각 긴 세션(요약+토론, 코딩리뷰)은 **5분 전 경고 알림** 포함 (`"warning": True` 항목)
- 환경변수: `DISCORD_WEBHOOK_URL`

### Discord 멘션
- `facilitator-config.json`의 `discord_id`는 **숫자 ID** 여야 함 (`<@123456789>` 형식)
- 유저네임 문자열은 Discord에서 멘션으로 동작하지 않음

## 웹사이트 (pages/)

Vercel에 정적 배포. `weeks.json`을 기반으로 HTML 페이지가 동작함.
`api/github.js`는 Vercel Serverless Function으로 GitHub API를 프록시하며, `GH_TOKEN` 또는 `GITHUB_TOKEN` 환경변수 필요.
