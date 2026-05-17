def solution(participant, completion):
    # participant 해시 테이블에 leo: 1, kiki: 1, mislav: 2 를 저장
    # completion for문을 돌면서 데이터 마이너스 해주기 
    # 하나가 남은 게 정답 
    hash_data = {}
    
    for p in participant:
        if p in hash_data:
            hash_data[p] += 1
        else:
            hash_data[p] = 1
    
    for c in completion:
        if c in hash_data:
            hash_data[c] -= 1
    
    for name, count in hash_data.items():
        if count > 0:
            return name