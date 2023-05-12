# 11652
# 정렬

N = int(input())
D = {}

for _ in range(N):
    x = int(input())

    if x not in D.keys():
        D[x] = 1
    else:
        D[x] += 1


D = sorted(D.items(), key=lambda x: (-1 * x[1], x[0]))

print(D[0][0])
