# 1850
# 정수론
# 유클리드 호제법

'''
유클리드 호제법 - 최대공약수(GCD) 찾기
A % B = 나머지(C)
B % C = 나머지(D)
C % D = 나머지(E)
...
A' % B' = 0 -> 이 때의 B가 최대공약수

<Key Idea>
A & B 의 공약수 = G
1이 A번 & 1이 B번 의 공약수 = 1이 G번
'''

import sys
input = sys.stdin.readline

def GCD(a, b):
    if a%b == 0:
        return b
    else:
        return GCD(b, a%b)

a, b = map(int, input().split())

print('1'*GCD(a, b))
