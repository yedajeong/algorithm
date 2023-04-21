# 시즌 1
# Lv.2 

def solution(n):
    answer = [[0 for j in range(1, i+1)] for i in range(1, n+1)]

    num = 1
    row, col = -1, 0  # 처음 시작은 아래로 -> [0][0]부터 시작

    for turn in range(n):
        for i in range(n-turn):
            if turn % 3 == 0:  # 아래로
                row += 1

            elif turn % 3 == 1:  # 오른쪽으로
                col += 1

            elif turn % 3 == 2:  # 위로
                row -= 1
                col -= 1

            answer[row][col] = num
            num += 1
    
    return sum(answer, [])  # 2차원 리스트 1차원으로 펴기

if __name__=="__main__":
    n = 6

    print(solution(n))
