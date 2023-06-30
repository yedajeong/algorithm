# 11576
# 수학
# 정수론

'''
N진수 -> 10진수
sum(N진수의 n번째 자리의 수 * N**n)

10진수 -> N진수
10진수 % N ~ 마지막 (0이 아닌) 몫 -> 역순으로 이어붙이기
'''

import sys

input = sys.stdin.readline

# A진법 -> 10진법
def ToDec(num, A):
    exp = len(num) - 1
    result = 0

    for n in num:
        result += n * A**exp
        exp -= 1

    return result

# 10진법 -> B진법
def FromDec(num, B):
    result = []
    while num // B > 0:
        result.append(str(num % B))
        num //= B
    
    result.append(str(num))
    result = result[::-1]

    return " ".join(result)

A, B = map(int, input().rstrip().split())
m = int(input())
num = list(map(int, input().rstrip().split()))

num_dec = ToDec(num, A)
num_B = FromDec(num_dec, B)

print(num_B)


