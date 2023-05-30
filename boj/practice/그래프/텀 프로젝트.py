# 9466
# 그래프

# 시간초과 유의

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 더 깊게 탐색

def DFS(node):
    global answer, visited

    visited[node] = 1
    cycle.append(node)
    next = graph[node]

    if visited[next] == 1:
        if next in cycle:
            next_idx = cycle.index(next)
            answer -= len(cycle[next_idx:])
        return
    
    else:
        DFS(next)


T = int(input())
graph = []
visited = []
answer = 0

for _ in range(T):
    n = int(input())
    answer = n

    graph = [0]
    graph.extend(list(map(int, input().rstrip().split())))

    visited = [0] * (n+1)

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            DFS(i)

    print(answer)
