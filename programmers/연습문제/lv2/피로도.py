from itertools import permutations

answer = 0

def dfs(k, cnt, dungeons, visited):
    global answer

    answer = max(answer, cnt)
    
    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k-dungeons[i][1], cnt+1, dungeons, visited)
            visited[i] = False

def solution(k, dungeons):
    global answer
    answer = -1
    visited = [0] * len(dungeons)
    dfs(k, 0, dungeons, visited)

    return answer

def solution2(k, dungeons):
    answer = 0

    for p in permutations(dungeons, len(dungeons)):
        tired = k
        cnt = 0

        for need, subtr in p:
            if tired >= need:
                tired -= subtr
                cnt += 1
        
        answer = max(answer, cnt)
    
    return answer


if __name__ == "__main__":
    k = 80
    dungeons = [[80,20],[50,40],[30,10]]
    print(solution2(k, dungeons))
