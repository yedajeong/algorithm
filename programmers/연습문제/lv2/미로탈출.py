from collections import deque

dc = [0, 0, -1, 1]
dr = [-1, 1, 0, 0] # 상, 하, 좌, 우

def lever(maps, visited, i, j, d):
    row = len(maps)
    col = len(maps[0])
    myDeq = deque()
    myDeq.append([(i, j), d])

    while(myDeq):
        now = myDeq.popleft()
        i = now[0][0]
        j = now[0][1]
        d = now[1]

        for r, c in zip(dr, dc):
            next_i = i+r
            next_j = j+c
            if next_i>=0 and next_i<row and next_j>=0 and next_j<col:
                if not visited[next_i][next_j]:
                    if maps[next_i][next_j]=="O" or maps[next_i][next_j]=="E":
                        visited[next_i][next_j] = 1
                        myDeq.append([(next_i, next_j), d+1])
                    elif maps[next_i][next_j]=="L":
                        return [(next_i, next_j), d+1]
                    
    return [(-1, -1), -1]

def exit(maps, visited, i, j, d):
    row = len(maps)
    col = len(maps[0])
    myDeq = deque()
    myDeq.append([(i, j), d])

    while(myDeq):
        now = myDeq.popleft()
        i = now[0][0]
        j = now[0][1]
        d = now[1]

        for r, c in zip(dr, dc):
            next_i = i+r
            next_j = j+c

            if next_i>=0 and next_i<row and next_j>=0 and next_j<col:
                if not visited[next_i][next_j]:
                    if maps[next_i][next_j]=="O" or maps[next_i][next_j]=="S":
                        visited[next_i][next_j] = 1
                        myDeq.append([(next_i, next_j), d+1])
                    elif maps[next_i][next_j]=="E":
                        return [(next_i, next_j), d+1]
                    
    return [(-1, -1), -1]


def solution(maps):
    row = len(maps)
    col = len(maps[0])
    visited = []
    for i in range(row):
        visited.append([0]*col)

    for i in range(row):
        for j in range(col):
            if maps[i][j]=="S":
                visited[i][j] = 1
                result = lever(maps, visited, i, j, 0)
                break

    if result[0][0]==-1:
        return -1
    else:
        # 방문배열 초기화
        visited = []
        for i in range(row):
            visited.append([0]*col)
        # 레버 ~ 출구
        visited[result[0][0]][result[0][1]] = 1
        result = exit(maps, visited, result[0][0], result[0][1], result[1])

    if result[0][0]==-1:
        return -1
    else:
        return result[1]
    

if __name__ == "__main__":
    maps = 	["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]
    print(solution(maps))
