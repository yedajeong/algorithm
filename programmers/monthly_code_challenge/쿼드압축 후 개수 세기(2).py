# 시즌1
# Lv. 2
# 라이브러리 쓰지 않고 재귀함수로 구현

def solution(arr):
    answer = [0, 0]

    s = len(arr)

    def check(y, x, s):
        # 더이상 쪼갤 수 없을 때
        if s == 1:
            answer[arr[y][x]] += 1  # index 0 or 1
            return
        
        else:
            item = arr[y][x]

            for i in range(s):
                for j in range(s):
                    if item != arr[y+i][x+j]:
                        s //= 2
                        check(y, x, s)
                        check(y+s, x, s)
                        check(y, x+s, s)
                        check(y+s, x+s, s)
                        return

            answer[item] += 1

    check(0, 0, len(arr))

    return answer

if __name__=="__main__":
    # arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
    arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]

    print(solution(arr))
