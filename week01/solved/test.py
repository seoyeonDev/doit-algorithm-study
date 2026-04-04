# 문제: 1181. 단어 정렬
# 플랫폼: 백준
# 링크: https://www.acmicpc.net/problem/1181
# 난이도: Silver 5
# 풀이: 한 줄 요약

import sys
from io import StringIO

# 백준 예제 입력
SAMPLE_INPUT = """13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours""".strip()

# 백준 예제 출력
# i
# im
# it
# no
# but
# more
# wait
# wont
# yours
# cannot
# hesitate


def solution():
    n = int(input())
    # 풀이 작성


if __name__ == "__main__":
    sys.stdin = StringIO(SAMPLE_INPUT)
    solution()
