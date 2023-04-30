# 슬라이딩 윈도우 실전 문제
# 플래티넘

'''
<Key Idea>
자료구조 'Deque(덱)' 이용
1. 최솟값 가능성이 없는 데이터 삭제
2. window 크기(L) 밖의 데이터 삭제
''' 

import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
mydeque = deque()  # [0]: value  [1]: idx 인 tuple
now = list(map(int, input().split))  # 입력받아 탐색할 리스트

for i in range(N):
    # 1. 나보다 큰 데이터 삭제하기
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()  # 가장 끝 삭제

    mydeque.append((now[i], i))

    # 2. 슬라이딩 윈도우 벗어난 데이터 삭제
    if mydeque[0][1] <= i-L:
        mydeque.popleft()

    print(mydeque[0][0], end=' ')  # 윈도우 내의 가장 작은 값 출력

