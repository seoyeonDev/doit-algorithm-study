from typing import Any, Sequence

# def seq_search(a:Sequence, key: Any) -> int:
#     i=0
#     while True:
#         if i==len(a):
#             return -1
#         if a[i] == key:
#             return i
#         i += 1

# def seq_search(a: Sequence, key: Any) -> int:
#     for i in range(len(a)):
#         if a[i] == key:
#             return i
#         return -1

# if __name__ == '__main__':
#     num = int(input('원소 수를 입력하세요: '))
#     x = [None] * num
    
#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))

#     ky = int(input('검색할 값을 입력하세요.: '))

#     idx = seq_search(x, ky)

#     if idx == -1:
#         print('검색값을 갖는 원소가 존재하지 않습니다. ')
#     else:
#         print(f'검색값은 x[{idx}]에 있습니다.')

# from ssearch_while import seq_search





# print('실수 검색 ')
# print('주의: "End" 입력 시 종료')

# number = 0
# x = []

# while True:
#     s = input(f'x[{number}]')
#     if s =='End':
#         break
#     x.append(float(s))
#     number += 1

# ky = float(input('검색 값 입력 : '))

# idx = seq_search(x, ky)
# if idx == -1:
#     print('검색 값 갖는 원소 존재하지 않음')
# else:
#     print(f'검색 값은 x[{idx}]에 있습니다.')





# t = (4,7,5.6,2,3.14,1 )
# s = 'string'
# a = ['DTS', 'AAC', 'FLAC']

# print(f'{t}에서 5.6의 인덱스는 {seq_search(t, 5.6)}')
# print(f'{s}에서 "n"의 인덱스는 {seq_search(s, "n")}')
# print(f'{a}에서 "DTS"의 인덱스는 {seq_search(a, "DTS")}')



#보초법 반영
# import copy

# def seq_search(seq: Sequence, key:Any)-> int:
#     a = copy.deepcopy(seq)
#     a.append(key)

#     i = 0
#     while True:
#         if a[i] == key:
#             break
#         i += 1
#     return -1 if i ==len(seq) else i

# if __name__ == '__main__':
#     num = int(input('원소 수 입력 : '))
#     x = [None] * num

#     for i in range(num):
#         x[i] = int(input(f'x[{i}]: '))

#     ky = int(input('검색할 값 입력 : '))

#     idx = seq_search(x, ky)

#     if idx == -1:
#         print('검색 값을 갖는 원소 존재하지 않음.')
#     else:
#         print(f'검색값은 x[{idx}]에 있습니다.')




