def solution(my_string, n):
    answer = ""
    stringList = list(my_string)

    for i in range(len(stringList)):
        answer += stringList[i] * n

    return answer

    # 아래와 같이 요소를 바로 꺼내서 사용할 수 있음.
    # answer = ''

    # for char in my_string:
    #    answer += char * n

    # return answer
