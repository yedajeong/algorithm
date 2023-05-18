# 11724
# 그래프

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

graph = {}
visited = [0] * (N+1)

for _ in range(M):
    n1, n2 = map(int, input().split())
    if n1 not in graph.keys():
        graph[n1] = []
    if n2 not in graph.keys():
        graph[n2] = []

    graph[n1].append(n2)
    graph[n2].append(n1)


def DFS(root):
    global graph, visited

    stack = [root]
    visited[root] = 1

    while stack:
        n1 = stack.pop()
        
        if n1 not in graph.keys():  # 아무 노드에도 연결되지 않았을 때 예외처리
            continue
        
        for n2 in graph[n1]:
            if not visited[n2]:
                stack.append(n2)
                visited[n2] = 1


connect = 0
for i in range(1, N+1):
    if not visited[i]:
        connect += 1
        DFS(i)


print(connect)
