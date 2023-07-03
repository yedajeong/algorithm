# 1676
# 수학

N = int(input())

five = 0
two = 0

for i in range(2, N+1):
    tmp = i
    while tmp % 5 == 0:
        five += 1
        tmp //= 5
    while tmp % 2 == 0:
        two += 1
        tmp //= 2

print(min(five, two))
