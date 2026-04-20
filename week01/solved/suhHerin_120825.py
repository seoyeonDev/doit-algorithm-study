def solution(my_string, n):
    answer = ''

    for cha in my_string:
        answer += cha * n

    return answer

import re

text = input()

s = re.search(r'[a-zA-Z]+', text).group()	#문자열 정규식
n = int(re.search(r'\d+', text).group()) 	#정수형 정규식

print(solution(s, n))