from functools import cmp_to_key

def solution(numbers):
    # 두 수를 이어붙인 결과를 비교하기
    def compare(a, b):
        ab = str(a) + str(b)
        ba = str(b) + str(a)
        if ab > ba:
            return -1
        elif ab < ba:
            return 1
        else:
            return 0

    # compare 기준으로 내림차순 정렬
    numbers.sort(key=cmp_to_key(compare))

    answer = ''

    for value in numbers:
        answer = answer + str(value)

    # 처음이 0부터 시작하면 000... 이므로 '0'만 반환
    if answer[0] == '0':
        return '0'

    return answer