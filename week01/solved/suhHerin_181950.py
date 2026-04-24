import re

text = input()

s = re.search(r'[a-zA-Z]+', text).group()	#문자열 정규식
n = int(re.search(r'\d+', text).group()) 	#정수형 정규식

print(s * n)