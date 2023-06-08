# 1931
# 그리디 알고리즘

import sys

input = sys.stdin.readline

N = int(input())
time = []

for _ in range(N):
    time.append(tuple(map(int, input().rstrip().split())))

time.sort(key=lambda x: (x[1], x[0]))

answer = 0
now = 0

for start, end in time:
    if now <= start:
        answer += 1
        now = end

print(answer)
