# 1783
# 그리디 알고리즘

import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

if N == 1 or M == 1:
    print(1)
elif N == 2:
    print(min(4, (M-1)//2 + 1))
elif M <= 6:
    print(min(4, M))
else:
    print(M-2)
