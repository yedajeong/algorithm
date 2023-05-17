import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

box = []

for _ in range(N):
    box.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(tomato):
    global box, dx, dy

    days = -1

    adjust = deque([])

    while tomato:

        while tomato:
            y, x = tomato.pop()
            adjust.append((y, x))

        while adjust:
            y, x = adjust.popleft()

            for yy, xx in zip(dy, dx):
                next_y = y + yy
                next_x = x + xx

                if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
                    continue
                elif box[next_y][next_x] == 0:
                    box[next_y][next_x] = 1
                    tomato.append((next_y, next_x))

        days += 1
    
    return days


# main
tomato = []

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomato.append((i, j))

answer = BFS(tomato)

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            print(-1)
            exit()

print(answer)

