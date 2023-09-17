from collections import deque

def solution(x, y, n):
    cal = [0] * (y+1)

    cal[x] = 0

    myDeq = deque()
    myDeq.append((x))

    # 예외처리
    if x==y:
        return 0

    while myDeq:
        x = myDeq.popleft()
        if x+n <= y:
            if cal[x+n] == 0:
                cal[x+n] = cal[x]+1
                myDeq.append(x+n)
        if x*2 <= y:
            if cal[x*2] == 0:
                cal[x*2] = cal[x]+1
                myDeq.append(x*2)
        if x*3 <= y:
            if cal[x*3] == 0:
                cal[x*3] = cal[x]+1
                myDeq.append(x*3)

    if cal[y] == 0:
        return -1
    else:
        return cal[y]
    

if __name__ == "__main__":
    x = 2
    y = 5
    n = 4

    print(solution(x, y, n))
