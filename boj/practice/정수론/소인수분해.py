# 11653
# 정수론

'''
input == 1인 경우 아무것도 출력 x
'''

N = int(input())

for i in range(2, N+1):
    while N % i == 0:
        print(i)
        N //= i
