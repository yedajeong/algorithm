# 11047
# 그리디 알고리즘

N, K = map(int, input().split())

coin = []
answer = 0

for _ in range(N):
    coin.append(int(input()))

for i in range(N-1, -1, -1):
    if K == 0:
        break
    elif K < coin[i]:
        continue
    
    answer += K // coin[i]
    K %= coin[i]

print(answer)
