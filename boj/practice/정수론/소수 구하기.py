# 1929
# 정수론
# 에라토스테네스의 체

import sys
input = sys.stdin.readline

M, N = map(int, input().split())

num = [i for i in range(N+1)]

for i in range(2, N+1):
    if num[i] == -1:
        continue
    elif i >= M:
        print(i)
    for j in range(i*2, N+1, i):
        if num[j] != -1:
            num[j] = -1

