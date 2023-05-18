# 4963
# 섬의 개수

import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def BFS(row, col):
    global graph, visited, dx, dy, w, h

    queue = deque([(row, col)])

    land = 1

    while queue:
        y, x = queue.popleft()
        visited[y][x] = 1

        for xx, yy in zip(dx, dy):
            new_x = x + xx
            new_y = y + yy
            
            if new_x < 0 or new_x >= w or new_y < 0 or new_y >= h:
                continue

            elif visited[new_y][new_x]:
                continue

            elif graph[new_y][new_x] == 1:
                visited[new_y][new_x] = 1
                land += 1
                queue.append((new_y, new_x))

    return land


w, h = map(int, input().split())

while w>0 and h>0:
    graph = []
    visited = []

    island = 0

    for _ in range(h):
        graph.append(list(map(int, input().split())))
        visited.append([0] * w)

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and graph[i][j]:
                if BFS(i, j) > 0:
                    island += 1

    print(island)

    w, h = map(int, input().split())

