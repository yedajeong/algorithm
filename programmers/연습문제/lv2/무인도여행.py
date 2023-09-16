from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def island(maps, visited, i, j):
    food = 0
    row = len(maps)
    col = len(maps[0])
    myDeq = deque()
    myDeq.append([i, j])
    
    while myDeq:
        now = myDeq.popleft()
        now_i = now[0]
        now_j = now[1]
        food += int(maps[now_i][now_j])

        for ii, jj in zip(dr, dc):
            next_i = now_i + ii
            next_j = now_j + jj
            if next_i>=0 and next_i<row and next_j>=0 and next_j<col:
                if not visited[next_i][next_j] and maps[next_i][next_j] != "X":
                    visited[next_i][next_j] = 1
                    myDeq.append([next_i, next_j])

    return food

def solution(maps):
    answer = []

    row = len(maps)
    col = len(maps[0])

    visited = []
    for i in range(row):
        visited.append([0]*col)
    
    for i in range(row):
        for j in range(col):
            if maps[i][j] != "X" and not visited[i][j]:
                visited[i][j] = 1
                answer.append(island(maps, visited, i, j))

    if not answer:
        return [-1]
    
    answer.sort(reverse=False)

    return answer
