def solution(n):
    prime_number = []

    if n < 2:
        return 1

    for i in range(2, n + 1):
        count = 0
        for num in prime_number:
            if (num * num) > i:  # 제곱근까지만 검사하기
                break
            if i % num == 0:  # 소수가 아니라면 count++해주고 바로 break로 빠져나오기
                count += 1
                break

        if count == 0:
            prime_number.append(i)

    return len(prime_number)
