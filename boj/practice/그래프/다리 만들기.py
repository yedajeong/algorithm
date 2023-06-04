# 2146
# 그래프

import sys
from collections import deque

input = sys.stdin.readline

def mark_island(y, x, num):
    global island, visited, N

    stack = [(y, x)]

    while stack:
        now_y, now_x = stack.pop()
        visited[now_y][now_x] = 1
        island[now_y][now_x] = num

        for yy, xx in zip(dy, dx):
            next_y = now_y + yy
            next_x = now_x + xx

            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                continue
            elif not visited[next_y][next_x] and island[next_y][next_x] == 1:
                stack.append((next_y, next_x))


def BFS(num):
    global island, visited, N

    queue = deque()
    result = 0

    for i in range(N):
        for j in range(N):
            if island[i][j] == num:
                visited[i][j] = 1
                queue.append((i, j))

    while queue:
        # 이번 레벨에서 탐색할 노드 개수 == q_size
        q_size = len(queue)

        for _ in range(q_size):
            now_y, now_x = queue.popleft()

            for yy, xx in zip(dy, dx):
                next_y = now_y + yy
                next_x = now_x + xx

                if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:
                    continue

                elif island[next_y][next_x] == 0 and not visited[next_y][next_x]:
                    queue.append((next_y, next_x))
                    visited[next_y][next_x] = 1

                elif island[next_y][next_x] != num and island[next_y][next_x] != 0:
                    # 제일 먼저 다른 섬에 도달하는 경우 바로 result 반환
                    return result
        
        # 같은 레벨에서 그다음 레벨로 갈 노드들 모두 탐색 후 큐에 집어넣고 경로 1 추가
        result += 1

    return result


N = int(input())
island = []
visited = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 입력 받기
for _ in range(N):
    island.append(list(map(int, input().rstrip().split())))
    visited.append([0] * N)


# 섬 넘버링
num = 0
for i in range(N):
    for j in range(N):
        if island[i][j] == 1:
            num -= 1
            mark_island(i, j, num)


# 다리 놓기
result = N*N
land_num = -1
while land_num >= num:
    # 방문 기록 초기화
    visited = []
    for _ in range(N):
        visited.append([0] * N)

    result = min(result, BFS(land_num))

    land_num -= 1

print(result)


# tc
# 10           
# 1 1 1 0 0 0 0 1 1 1
# 1 1 1 1 0 0 0 0 1 1
# 1 0 1 1 0 0 0 0 1 1
# 0 0 1 1 1 0 0 0 0 1
# 0 0 0 1 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 1
# 0 0 0 0 0 0 0 0 0 0
# 0 0 0 0 1 1 0 0 0 0
# 0 0 0 0 1 1 1 0 0 0
# 0 0 0 0 0 0 0 0 0 0
