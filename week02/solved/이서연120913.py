def solution(my_str, n):
    answer = []
    # my_str 을 n 만큼씩 잘라서 answer에 담기
        # 처음부터 n 간격으로 이동, my_str이 끝날때까지  
        # 자른 문자열 answer 배열에 할당 
    for i in range(0, len(my_str), n):
        sliced_str = my_str[i:n + i]
        answer.append(sliced_str)
    
    
    return answer

my_str, n = input().strip().split()
n =  int(n)

print(solution(my_str,n))