def solution(n):
    answer = 0
    
# 범위 안의 배수 제거 
    # 범위 값을 boolean 배열 안에 담기
    # i부터 숫자 n 까지 반복
        # num = 2 부터 num * num <= n 까지 반복
            # false 인 수들만 다시 확인 
                # num 의 배수 체크 
                    # 배수 삭제
                    
    my_list = [True] * (n+1) # 리스트 곱셈 연산
    
    for i in range(2,n+1,1):
        if my_list[i] == True:
            for j in range(i * i,n + 1, i):
                my_list[j] = False
            
    for i in range(2, len(my_list), 1):
        if my_list[i] == True:
            answer += 1
    
    return answer