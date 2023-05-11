# 11650
# 정렬

import sys

input = sys.stdin.readline

N = int(input())
point = []

for _ in range(N):
    x, y = map(int, input().split())
    point.append((x, y))

point = sorted(point, key=lambda x: (x[0], x[1]))

for x, y in point:
    print(x, y)
