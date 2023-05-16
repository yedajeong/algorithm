# 2667
# 그래프

import sys

input = sys.stdin.readline

N = int(input())
myMap = []
# visited = [[0] * N] * N -> shallow copy (행 동기화됨)
visited = []

for _ in range(N):
    visited.append([0] * N)

for _ in range(N):
    myMap.append(list(map(int, list(input().rstrip()))))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

stack = []
cnt = []

def DFS(row, col):
    global stack, myMap, visited

    stack.append((row, col))
    
    house = 1

    while stack:
        now_y, now_x = stack.pop()

        for x, y in zip(dx, dy):
            next_y = now_y + y
            next_x = now_x + x

            if next_y < 0 or next_y >=N or next_x < 0 or next_x >= N:
                continue
            elif visited[next_y][next_x]:
                continue
            elif myMap[next_y][next_x]:
                visited[next_y][next_x] = 1
                house += 1
                stack.append((next_y, next_x))

    return house


for y in range(N):
    for x in range(N):
        if not visited[y][x] and myMap[y][x]:
            visited[y][x] = 1
            cnt.append(DFS(y, x))


cnt.sort()

print(len(cnt))
for c in cnt:
    print(c)
