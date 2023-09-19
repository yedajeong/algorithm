def win(board, t):
    for i in range(3):
        # 가로
        if board[i] == t+t+t:
            return True
        # 세로
        if board[0][i]+board[1][i]+board[2][i] == t+t+t:
            return True
    
    # 대각선
    if board[0][0]+board[1][1]+board[2][2] == t+t+t:
        return True
    if board[2][0]+board[1][1]+board[0][2] == t+t+t:
        return True
    
    return False

def solution(board):
    answer = 1
    first = 0
    second = 0

    for i in range(0, 3):
        for j in range(0, 3):
            if board[i][j] == "O":
                first += 1
            elif board[i][j] == "X":
                second += 1

    first_win = win(board, "O")
    second_win = win(board, "X")
    
    # 둘 다 이겼을 때
    if first_win and second_win:
        answer = 0
    # 선공이 이겼으면 선공이 한 개 더 많아야 함
    elif first_win and first != second+1:
        answer = 0
    # 후공이 이겼으면 선공 후공 개수 똑같아야 함
    elif second_win and first != second:
        answer = 0
    # 후공이 선공보다 개수 많을 때
    elif second > first:
        answer = 0
    # 선공이 후공보다 2개 이상으로 많을 때 (꼭 한 개까지만 차이나야 함)
    elif first >= second+2:
        answer = 0
    

    return answer

if __name__ == "__main__":
    board = ["OXX", "OOX", "OXO"]
    print(solution(board))
