import math

def distance(startX, startY, ballX, ballY): # n세로 m가로
    return abs(startX-ballX)**2 + abs(startY-ballY)**2

def solution(m, n, startX, startY, balls):
    answer = []

    for ball in balls:
        ballX = ball[0]
        ballY = ball[1]
        candidate = []

        if not (ballX==startX and ballY > startY): # 상
            candidate.append(distance(startX, startY, ballX, ballY + (n-ballY)*2))
        if not (ballX==startX and ballY < startY): # 하
            candidate.append(distance(startX, startY, ballX, -1*ballY))
        if not (ballX<startX and ballY==startY): # 좌
            candidate.append(distance(startX, startY, -1*ballX, ballY))
        if not (ballX>startX and ballY==startY): # 우
            candidate.append(distance(startX, startY, ballX + (m-ballX)*2, ballY))

        answer.append(min(candidate))

    return answer
