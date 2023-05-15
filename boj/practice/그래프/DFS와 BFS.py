# 1260
# 그래프

import sys
from collections import deque

input = sys.stdin.readline


N, M, V = map(int, input().split())

graph = {}
visited = []


# 깊이우선 _ 재귀 or 스택
def DFS(parent):
    global graph, visited

    # 예외처리
    if parent not in graph.keys():
        print(parent, end=' ')
        return

    print(parent, end=' ')

    for child in graph[parent]:
        if not visited[child]:
            visited[child] = 1
            DFS(child)
        else:
            continue


# 너비우선 _ 큐
def BFS(root):
    global graph, visited

    # 예외처리
    if root not in graph.keys():
        print(root, end=' ')
        return

    myDeq = deque([root])

    while myDeq:
        parent = myDeq.popleft()

        print(parent, end=' ')

        for child in graph[parent]:
            if not visited[child]:
                visited[child] = 1
                myDeq.append(child)


# 그래프 구성
for _ in range(M):
    n1, n2 = map(int, input().split())
    if n1 not in graph.keys():
        graph[n1] = []
    
    if n2 not in graph.keys():
        graph[n2] = []

    graph[n1].append(n2)
    graph[n2].append(n1)


# 노드 번호 작은 것부터 방문 -> 미리 정렬
for key in graph.keys():
    graph[key] = sorted(graph[key])

visited = [0] * (N+1)
visited[V] = 1
DFS(V)

print()

visited = [0] * (N+1)
visited[V] = 1
BFS(V)
