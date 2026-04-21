from week02.practice.max_of_hw import max_of

print("배열의 최댓값 구하기 :")
print("주의 : END를 입력하면 종료 ")

number = 0
x = []

while True:
    s = input(f"x[{number}]값을 입력:")
    if s == "END":
        break
    x.append(int(s))
    number += 1

print(f"{number}개를 입력했다")
print(f"최댓값은 {max_of(x)}입니다.")
