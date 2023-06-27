# 2873
# 그리디 알고리즘

import sys

input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
park = []  # R, C가 모두 짝수일 때만 실질적으로 사용됨

for _ in range(R):
    park.append(list(map(int, input().rstrip().split())))

row = 0
col = 0
answer = ""

# row가 홀수
if R % 2 == 1:
    lr = 'R'
    dir = 1
    while row < R and col < C:
        col += dir
        answer += lr

        if row == R-1 and col == C-1:
            break
        elif col == C-1:
            answer += 'D'
            dir = -1
            lr = 'L'
            row += 1
        elif col == 0:
            answer += 'D'
            dir = 1
            lr = 'R'
            row += 1

# col이 홀수
elif C % 2 == 1:
    ud = 'D'
    dir = 1
    while row < R and col < C:
        row += dir
        answer += ud

        if row == R-1 and col == C-1:
            break
        elif row == R-1:
            answer += 'R'
            dir = -1
            ud = 'U'
            col += 1
        elif row == 0:
            answer += 'R'
            dir = 1
            ud = 'D'
            col += 1

# row, col 짝수 _ 수정
else:
    # [min_row][min_col] 지나면 안됨
    minimum = park[0][1]
    min_row = 0
    min_col = 1
    for row in range(R):
        for col in range(C):
            if (row+col)%2 and park[row][col] < minimum:
                minimum = park[row][col]
                min_row = row
                min_col = col

    # 두 행씩 나눠서 minimum 위치한 쌍은 지그재그, 나머지는 수평하게 이동
    zigzag = False
    for row in range(0, R, 2):
        if row != 0:
            answer += 'D'

        if min_row == row or min_row == row + 1:
            ud = False  # T: up F: down
            zigzag = True
            if min_col != 0:
                answer += 'D'
                ud = True
            for col in range(1, C):
                if min_col == col:
                    answer += 'R'
                    continue
                elif ud:
                    answer += 'RU'
                else:
                    answer += 'RD'
                ud = not ud

        else:
            if zigzag:
                answer += 'L'*(C-1)
                answer += 'D'
                answer += 'R'*(C-1)
            else:
                answer += 'R'*(C-1)
                answer += 'D'
                answer += 'L'*(C-1)
            

# row, col 짝수 _ 시간초과..
'''
else:
    # [min_row][min_col] 지나면 안됨
    minimum = park[0][1]
    min_row = 0
    min_col = 1
    for row in range(R):
        for col in range(C):
            if (row+col)%2 and park[row][col] < minimum:
                minimum = park[row][col]
                min_row = row
                min_col = col
    
    # print(min_row, min_col)
    # print(park[min_row][min_col])
    
    # 방향 우선순위: 좌 / 하 / 상 / 우
    dr = [0, 1, -1, 0]
    dc = [-1, 0, 0, 1]
    direction = ['L', 'D', 'U', 'R']

    row = 0
    col = 0
    park[0][0] = -1  # 방문 점검(음수_o/양수_x)

    while row < R and col < C:
        if row == R-1 and col == C-1:
            break

        # 오른쪽 끝 두 col을 지날 때는 예외처리 (지그재그로 방향 바꾸기)
        elif row == 0 and col == C-2 and min_col >= C-2:
            dr = [0, 0, 1]
            dc = [1, -1, 0]
            direction = ['R', 'L', 'D']

        for rr, cc, dir in zip(dr, dc, direction):
            next_row = row + rr
            next_col = col + cc

            # index out of range
            if next_row < 0 or next_col < 0 or next_row >= R or next_col >= C:
                continue

            # 이미 방문
            elif park[next_row][next_col] == -1:
                continue

            # 최솟값 피해가기
            elif next_row == min_row and next_col == min_col:
                if dir in ['U', 'D']:
                    next_col = col + 1
                    answer += 'R' + dir
                    park[row][col+1] = -1
                    park[next_row][next_col] = -1
                    park[min_row][min_col] = -1
                    break

                elif dir == 'R':
                    next_row = row + 1
                    answer += 'D' + dir
                    park[row+1][col] = -1
                    park[next_row][next_col] = -1
                    park[min_row][min_col] = -1
                    break

            # 새로 방문
            else:
                park[next_row][next_col] = -1
                answer += dir
                break  # 이동했으니까 for문 빠져나오기
        
        row = next_row
        col = next_col
'''

print(answer)
