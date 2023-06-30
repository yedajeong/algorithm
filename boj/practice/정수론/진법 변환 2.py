# 11005
# 수학

'''
10진수 -> B진수
10진수 수를 B로 나눈 후 마지막 몫과 나머지들을 역순으로 읽어주기
'''

import sys

input = sys.stdin.readline

N, B = map(int, input().split())

answer = ''
a = 65

while N // B > 0:
    if N % B >= 10:
        answer += chr(a + (N % B - 10))
    else:
        answer += str(N % B)
    
    N //= B

if N >= 10:
    answer += chr(a + (N-10))
else:
    answer += str(N)

answer = answer[::-1]
print(answer)
