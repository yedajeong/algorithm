from collections import deque

def solution(board):
    answer = -1
    row = len(board)
    col = len(board[0])

    dc = [-1, 1, 0, 0] # 좌, 우, 상, 하
    dr = [0, 0, -1, 1] 

    visited = []
    for r in range(0, row):
        visited.append([0] * col)

    for i in range(0, row):
        for j in range(0, col):
            if board[i][j] == "R":
                visited[i][j] = 1
                start = (i, j)

    deq = deque()
    depth = 0
    deq.append([start, depth])

    while deq:
        node = deq.popleft()
        d = node[1]

        for r, c in zip(dr, dc):
            i = node[0][0]
            j = node[0][1]

            while i>=0 and i<row and j>=0 and j<col:
                if board[i][j] == "D":
                    break
                i += r
                j += c
            
            i -= r
            j -= c

            if visited[i][j]:
                continue
            elif board[i][j]=="G":
                return d+1
            else:
                visited[i][j] = 1
                deq.append([(i, j), d+1])

    return answer


if __name__ == "__main__":
    board = ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]
    print(solution(board))
