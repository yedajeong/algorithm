# 10989

# O(nlogn) 정렬 -> 메모리 초과
# 입력을 모두 배열에 저장하면 x (short로 해도 메모리 초과)
# 1 <= N <= 10,000,000
# 1 <= A[i] <= 10,000  -> 수의 크기는 그리 크지 않음..

# 시간 초과 -> 빠른입출력

import sys
input = sys.stdin.readline

N = int(input())
A = [0] * 10001

for i in range(N):
    A[int(input())] += 1

for i in range(1, 10001):
    for _ in range(A[i]):
        print(i)
