# 1158
# 자료구조 - 큐

from collections import deque
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

myDeq = deque(list(range(1, N+1)))
answer = []

for _ in range(N):
    for _ in range(K-1):
        x = myDeq.popleft()
        myDeq.append(x)
    answer.append(myDeq.popleft())

print('<' + ', '.join(map(str, answer)) + '>')
