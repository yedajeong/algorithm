# 1715
# 그리디 알고리즘

# 오름차순 정렬해서 작은 것부터 더해봄
# -> 정렬 알고리즘 대신 우선순위 큐 이용

# 출력 초과 -> 기준 범위 이상의 큰 값으로 출력됨

from collections import deque
import heapq

N = int(input())
card = []

for _ in range(N):
    # heappush(리스트, 넣을 아이템)
    heapq.heappush(card, int(input()))

answer = 0

# N=1 예외처리
if N == 1:
    print(0)
else: 
    for _ in range(N-1):  # 두 개씩 꺼내서 봄
        compare = heapq.heappop(card) + heapq.heappop(card)
        answer += compare
        heapq.heappush(card, compare)

    print(answer)
