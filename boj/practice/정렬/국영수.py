# 10825
# 정렬

import sys

input = sys.stdin.readline

N = int(input())
A = []

for _ in range(N):
    name, kor, eng, math = input().split()
    A.append((name, int(kor), int(eng), int(math)))

A = sorted(A, key=lambda x: (-1 * x[1], x[2], -1 * x[3], x[0]))

for name, _, _, _ in A:
    print(name)
