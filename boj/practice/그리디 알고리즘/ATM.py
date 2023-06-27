# 11399
# 그리디 알고리즘

import sys

input = sys.stdin.readline

N = int(input())
P = list(map(int, input().rstrip().split()))
line = list(enumerate(P))

line.sort(key=lambda x: x[1])

answer = 0
waiting = 0
for _, time in line:
    waiting += time
    answer += waiting

print(answer)
