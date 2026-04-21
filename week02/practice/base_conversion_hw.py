def base_conversion_hw(x: int, r: int) -> str:
    d = ""
    dchar = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while x > 0:
        d += dchar[x % r]
        x //= r
    return d[::-1]


if __name__ == "__main__":
    print("10진수를 n진수로 변환.")

    while True:
        while True:
            no = int(input("변환할 값으로 음이 아닌 정수를 입력 하라 :"))
            if no > 0:
                break

        while True:
            cd = int(input("어떤 진수로 변환할까요? :"))
            if 2 <= cd <= 36:
                break

        print(f"{cd}진수로는 {base_conversion_hw(no,cd)} 입니다.")

        retry = input("한 번 더 변환할까요? y/N :")
        if retry in {"N", "n"}:
            break
