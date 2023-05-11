# 2751
# 정렬
# 빠른 입출력

import sys

input = sys.stdin.readline

N = int(input())
A = []

for _ in range(N):
    A.append(int(input()))

A.sort()

for a in A:
    print(a)
