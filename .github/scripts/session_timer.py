"""
스터디 세션 타이머 — 트리거 명령어 입력 후 단계별로 Discord에 시간 안내 알림을 전송합니다.

사용법:
    python .github/scripts/session_timer.py

환경변수:
    DISCORD_WEBHOOK_URL  — Discord 웹훅 URL (없으면 터미널 출력만)

트리거:
    실행 후 "start" 입력 → 타이머 시작
    언제든 "q" 입력 → 종료
"""

import json
import os
import subprocess
import sys
import threading
import time
from datetime import datetime, timedelta

# ── 세션 일정 ────────────────────────────────────────────────────────────────
SCHEDULE = [
    {
        "offset_min": 0,
        "title": "🟢 오프닝",
        "range": "00 — 05 min",
        "duration": "5분",
        "description": "출석 확인 · 이번 주 챕터 리마인드 · 진행자 소개",
        "color": 0xF5F0E8,
    },
    {
        "offset_min": 5,
        "title": "📚 요약 공유",
        "range": "05 — 25 min",
        "duration": "20분",
        "description": "각자 핵심 내용 2~3가지 공유 (1인 약 5분)\n사전에 GitHub에 올린 요약 기반으로 · 질문은 토론 시간에",
        "color": 0x7BFFC0,
    },
    {
        "offset_min": 25,
        "title": "💬 자유 토론",
        "range": "25 — 40 min",
        "duration": "15분",
        "description": "어려웠던 개념 · 인사이트 공유 · 사전에 정해온 토론 주제\n진행자가 흐름 조율 · 결론보다 과정이 중요",
        "color": 0xB3A8E8,
    },
    {
        "offset_min": 40,
        "title": "💻 코딩 문제 리뷰",
        "range": "40 — 55 min",
        "duration": "15분",
        "description": "문제 출제자가 문제 소개 · 각자 풀이 PR 기반으로 코드 리뷰\n못 풀었도 접근 방식 공유 · 더 나은 풀이 토론",
        "color": 0xFFDFA8,
    },
    {
        "offset_min": 55,
        "title": "🏁 마무리",
        "range": "55 — 60 min",
        "duration": "5분",
        "description": "다음 주 챕터 확인 · 진행자 · 문제 출제자 지정",
        "color": 0xF5F0E8,
    },
    {
        "offset_min": 60,
        "title": "✅ 스터디 종료",
        "range": "",
        "duration": "",
        "description": "오늘도 수고하셨습니다! 🎉",
        "color": 0x7BFFC0,
    },
]

# ── Discord 전송 ──────────────────────────────────────────────────────────────
def send_discord(webhook_url: str, payload: dict) -> None:
    result = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
         "-X", "POST", webhook_url,
         "-H", "Content-Type: application/json",
         "-d", json.dumps(payload, ensure_ascii=False)],
        capture_output=True, text=True,
    )
    status = result.stdout.strip()
    if status not in ("200", "204"):
        raise RuntimeError(f"Discord webhook 실패: {status}\n{result.stderr}")


def build_payload(session: dict, elapsed_min: int, end_time: datetime) -> dict:
    fields = []
    if session["range"]:
        fields.append({"name": "⏱ 구간", "value": session["range"], "inline": True})
    if session["duration"]:
        fields.append({"name": "⏳ 남은 시간", "value": session["duration"], "inline": True})
    fields.append({
        "name": "🕐 종료 예정",
        "value": end_time.strftime("%H:%M"),
        "inline": True,
    })

    return {
        "embeds": [
            {
                "title": session["title"],
                "description": session["description"],
                "color": session["color"],
                "fields": fields,
                "footer": {"text": "Do it! 알고리즘 파이썬 스터디"},
            }
        ]
    }


# ── 타이머 ────────────────────────────────────────────────────────────────────
stop_event = threading.Event()


def timer_thread(webhook_url: str, start_time: datetime) -> None:
    total_sessions = len(SCHEDULE)
    for i, session in enumerate(SCHEDULE):
        if stop_event.is_set():
            break

        target_time = start_time + timedelta(minutes=session["offset_min"])
        now = datetime.now()
        wait_sec = (target_time - now).total_seconds()

        if wait_sec > 0:
            print(f"  ⏳ {session['title']} 알림 대기 중... ({session['offset_min']}분 후 전송)")
            stopped = stop_event.wait(timeout=wait_sec)
            if stopped:
                break

        # 종료 예정 시간 계산
        next_offset = SCHEDULE[i + 1]["offset_min"] if i + 1 < total_sessions else session["offset_min"]
        end_time = start_time + timedelta(minutes=next_offset)

        elapsed = int((datetime.now() - start_time).total_seconds() // 60)
        payload = build_payload(session, elapsed, end_time)

        if webhook_url:
            try:
                send_discord(webhook_url, payload)
                print(f"  ✅ [{datetime.now().strftime('%H:%M:%S')}] Discord 전송: {session['title']}")
            except Exception as e:
                print(f"  ❌ 전송 실패: {e}")
        else:
            print(f"\n{'─'*50}")
            print(f"[DRY RUN] {datetime.now().strftime('%H:%M:%S')} — {session['title']}")
            print(json.dumps(payload, ensure_ascii=False, indent=2))

    print("\n🎉 세션 타이머 종료.")


# ── 메인 ─────────────────────────────────────────────────────────────────────
def main() -> None:
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL", "")

    print("=" * 55)
    print("  Do it! 알고리즘 파이썬 스터디 — 세션 타이머")
    print("=" * 55)
    if not webhook_url:
        print("  ⚠  DISCORD_WEBHOOK_URL 미설정 — 터미널 출력 모드")
    print()
    print("  세션 일정:")
    for s in SCHEDULE:
        if s["range"]:
            print(f"    {s['range']:18s} {s['title']}")
    print()
    print("  명령어: 'start' — 타이머 시작 | 'q' — 종료")
    print("=" * 55)

    while True:
        try:
            cmd = input("\n> ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\n종료합니다.")
            sys.exit(0)

        if cmd == "q":
            print("종료합니다.")
            sys.exit(0)

        if cmd == "start":
            start_time = datetime.now()
            end_time = start_time + timedelta(minutes=60)
            print(f"\n🚀 스터디 시작! {start_time.strftime('%H:%M')} → 종료 예정 {end_time.strftime('%H:%M')}")
            print("  ('q' 입력 시 타이머 중단)\n")

            t = threading.Thread(target=timer_thread, args=(webhook_url, start_time), daemon=True)
            t.start()

            # 메인 스레드에서 'q' 입력 대기
            while t.is_alive():
                try:
                    cmd = input().strip().lower()
                    if cmd == "q":
                        stop_event.set()
                        print("타이머를 중단합니다.")
                        break
                except (EOFError, KeyboardInterrupt):
                    stop_event.set()
                    break

            t.join()
            return

        print("  'start' 를 입력해 타이머를 시작하거나, 'q' 로 종료하세요.")


if __name__ == "__main__":
    main()
