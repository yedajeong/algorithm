# 시즌1
# Lv. 2

from collections import deque

def solution(arr):
    answer = []

    s = len(arr)

    queue = deque([[(0, 0), s]])

    while queue:
        item = queue.popleft()
        x, y = item[0]
        s = item[1]

        # 더이상 쪼갤 수 없을 때
        if s == 1:
            answer.append(arr[x][y])
            continue

        # 관심 영역(2차원) 슬라이싱 해서 1차원 리스트로
        # dim_2 = arr[x:x+s][y:y+s]  # 안됨 (numpy 배열은 가능)
        dim_1 = []
        for i in range(s):
            dim_1 += arr[x+i][y:y+s]

        if sum(dim_1) == 0:
            answer.append(0)
        elif sum(dim_1) == 1*len(dim_1):
            answer.append(1)
        else:
            s //= 2  # int형으로
            queue.append([(x, y), s])
            queue.append([(x+s, y), s])
            queue.append([(x, y+s), s])
            queue.append([(x+s, y+s), s])
    
    return [answer.count(0), answer.count(1)]

if __name__=="__main__":
    # arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
    # [4, 9]
    arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
    # [10, 15]
    
    print(solution(arr))
