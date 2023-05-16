# 2178
# 그래프

# 최단경로 -> BFS

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maze = []

for _ in range(N):
    maze.append(list(map(int, list(input().rstrip()))))


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

path = 0
def BFS(input_y, input_x):
    global N, M, maze, dx, dy, path

    myQue = deque([(input_y, input_x)])

    while myQue:
        now_y, now_x = myQue.popleft()

        for x, y in zip(dx, dy):
            child_x = now_x + x
            child_y = now_y + y
            if child_x < 0 or child_x >= M or child_y < 0 or child_y >= N:
                continue
            
            if maze[child_y][child_x] == 1:
                maze[child_y][child_x] = maze[now_y][now_x] + 1
                myQue.append((child_y, child_x))

    return maze[N-1][M-1]


print(BFS(0, 0))

