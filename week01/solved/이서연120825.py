def solution(my_str, n):
    answer = ""
    # for 문에서 "" 를 필터링하는 것보다 애초부터 뺴고 넣는게 더 효율적이라 생각.
    # my_str = my_str.replace('"','')
    for i in range(len(my_str)):
        ch = my_str[i]
        sen = ch * n
        answer += sen

    return answer

# "함수만" 작성해야함 
# my_str, n = input().strip().split()
# n =  int(n)

# print(solution(my_str,n))