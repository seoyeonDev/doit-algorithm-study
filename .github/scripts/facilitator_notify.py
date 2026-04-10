"""
매주 수요일 실행 — 이번 주 진행자를 계산해 Discord에 알림을 보냅니다.
weeks.json의 W01~W17 순서대로 멤버를 순환(round-robin) 배정합니다.
"""

import json
import datetime
import os
import subprocess
import sys

WEEKS_JSON = "pages/weeks.json"
CONFIG_JSON = ".github/facilitator-config.json"

COLOR_GREEN = 0x7BFFC0


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def find_current_week(weeks, year):
    """오늘 날짜 기준으로 현재 진행 중인 주차 인덱스를 반환합니다."""
    today = datetime.date.today()

    thursdays = []
    for w in weeks:
        mm, dd = w["date"].split("/")
        thursdays.append(datetime.date(year, int(mm), int(dd)))

    for i, thursday in enumerate(thursdays):
        week_start = (
            thursdays[i - 1] + datetime.timedelta(days=1)
            if i > 0
            else datetime.date.min
        )
        if week_start <= today <= thursday:
            return i

    return -1


def send_discord(webhook_url, payload):
    result = subprocess.run(
        ["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}",
         "-X", "POST", webhook_url,
         "-H", "Content-Type: application/json",
         "-d", json.dumps(payload, ensure_ascii=False)],
        capture_output=True, text=True,
    )
    status = result.stdout.strip()
    if status not in ("200", "204"):
        raise RuntimeError(f"Discord webhook failed: {status}\n{result.stderr}")


def mention(member):
    if member.get("discord_id"):
        return f"<@{member['discord_id']}>"
    return member["name"]


def main():
    data = load_json(WEEKS_JSON)
    config = load_json(CONFIG_JSON)

    year = data["year"]
    # W00(오리엔테이션)은 진행자 순번에서 제외
    weeks = [w for w in data["weeks"] if w["num"] != "W00"]
    members = config["members"]

    if not members:
        print("멤버 목록이 비어 있습니다. facilitator-config.json을 확인하세요.")
        sys.exit(1)

    current_idx = find_current_week(weeks, year)

    if current_idx == -1:
        print("현재 진행 중인 주차가 없습니다. 스터디 기간 외입니다.")
        sys.exit(0)

    current_week = weeks[current_idx]
    overrides = config.get("overrides", {})

    def resolve_facilitator(up_to_idx):
        """
        W01부터 up_to_idx까지 순회하며 rotation 카운터를 계산합니다.
        - null override (쉬는 주): 카운터 유지 → 다음 주에 같은 순번 유지
        - 이름 override (교체/대타): 지정 멤버가 진행, 카운터는 올라감
        - override 없음: 순번대로 진행, 카운터 올라감
        """
        counter = 0
        for i, week in enumerate(weeks[: up_to_idx + 1]):
            override = overrides.get(week["num"])
            is_target = i == up_to_idx

            if week["num"] in overrides:
                if override is None:
                    # 쉬는 주 — 카운터 유지 (다음 주에 원래 순번 그대로)
                    if is_target:
                        return {"name": "미정", "discord_id": ""}
                    # counter 올리지 않음
                else:
                    # 대타/교체 — 카운터 올라감 (실제 진행된 세션으로 처리)
                    if is_target:
                        matched = next((m for m in members if m["name"] == override), None)
                        return matched or {"name": override, "discord_id": ""}
                    counter += 1
            else:
                # 일반 순번
                if is_target:
                    return members[counter % len(members)]
                counter += 1

        return members[counter % len(members)]

    facilitator = resolve_facilitator(current_idx)

    # 다음 주차
    next_week = weeks[current_idx + 1] if current_idx + 1 < len(weeks) else None
    next_facilitator = resolve_facilitator(current_idx + 1) if next_week else None

    mm, dd = current_week["date"].split("/")
    date_str = f"{year}년 {int(mm)}월 {int(dd)}일 (목) 20:00"

    fields = [
        {"name": "📅 날짜", "value": date_str, "inline": True},
        {"name": "🎤 진행자", "value": mention(facilitator), "inline": True},
        {"name": "📖 챕터", "value": current_week["chapter"], "inline": False},
    ]
    if next_week and next_facilitator:
        fields.append(
            {"name": "다음 주 진행자 예정", "value": mention(next_facilitator), "inline": False}
        )

    payload = {
        "embeds": [
            {
                "title": f"📢 {current_week['num']} · {current_week['title']}",
                "description": current_week["desc"],
                "color": COLOR_GREEN,
                "fields": fields,
                "footer": {"text": "Do it! 알고리즘 파이썬 스터디"},
            }
        ]
    }

    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL_NOTIFY")
    if not webhook_url:
        # 로컬 테스트 시 내용만 출력
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        print(f"\n[DRY RUN] 진행자: {facilitator['name']} ({current_week['num']})")
        return

    send_discord(webhook_url, payload)
    print(f"✅ Discord 알림 전송 완료 — {current_week['num']}: {facilitator['name']}")


if __name__ == "__main__":
    main()
