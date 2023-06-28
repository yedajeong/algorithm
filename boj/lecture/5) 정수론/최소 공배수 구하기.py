# 유클리드 호제법 실전문제
# 1934
# 실버 5

'''
<Key Idea>
A, B의 최소 공배수 = A * B / A, B의 최대 공약수
최대 공약수 -> 유클리드 호제법으로 구함

A, B 사이에 대소관계 구분 없이 (큰수, 작은수) 하지 않아도 됨
-> A(작) % B(큼) = 나머지 -> (B, 나머지(==A)) 로 입력될 때 자동으로 swap됨
'''

import sys

input = sys.stdin.readline

T = int(input())

def GCD(A, B):
    if A % B == 0:
        return B
    else:
        return GCD(B, A%B)

for _ in range(T):
    A, B = map(int, input().rstrip().split())
    
    # print(A * B / GCD(A, B))  : float로 출력
    print(A * B // GCD(A, B))  # : int로 출력
