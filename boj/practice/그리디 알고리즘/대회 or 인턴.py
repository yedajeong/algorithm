# 2875
# 그리디 알고리즘

N, M, K = map(int, input().split())

left = N+M

answer = 0
while left >= K:
    N -= 2
    M -= 1

    if N < 0 or M < 0:
        break

    answer += 1
    left = N+M

if left >= K:
    print(answer)
elif left < K:
    print(answer-1)
