# 구간 합 실전 문제
# 구간 합 구하기 2
# 실버 1

'''
1 <= N <= 1024  표 크기 (N by N)
1 <= M <= 100,000  질의 개수
-> 표 크기는 그닥 크지 않으나 질의 최대 개수가 큰 경우
-> 한 번 정답판을 만들어놓고 질의가 오면 바로 답을 출력하는 형태

-> 질의마다 합을 구하면 안되고, 구간 합 배열을 이용해야 한다!
'''

'''
2차원 구간 합 배열 D[X][Y]의 정의
원본 배열의 (0, 0)부터 (X, Y)까지의 사각형 영역 안에 있는 수의 합
D[1][j] = D[1][j-1] + A[1][j]
D[i][1] = D[i-1][1] + A[i][1]
D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
겹치는 부분 D[i-1][j-1] 빼기
'''  

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# 1 based indexing -> n+1 길이로 만들어줌
A = [[0] * (n+1)]  # 1차원 리스트로 초기화 -> row로 입력받아 append하면서 2차원 배열로 만들기
D = [[0]*(n+1) for _ in range(n+1)]

# 원본 배열 A 구성
for i in range(n):
    # row로 한번에 입력받기
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

# 구간 합 배열 D 구성
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

# m번만큼 질의 처리
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)