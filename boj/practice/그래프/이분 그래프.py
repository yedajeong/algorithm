# 1707
# 그래프

import sys

input = sys.stdin.readline

def DFS(root):
    global graph, color

    stack = [root]
    color[root] = 1

    while stack:
        n1 = stack.pop()

        if n1 not in graph.keys():
            continue

        for n2 in graph[n1]:
            if not color[n2]:
                color[n2] = -1 * color[n1]
                stack.append(n2)

            elif color[n2] != -1 * color[n1]:
                return False

    return True


# main
K = int(input())

for _ in range(K):
    V, E = map(int, input().split())

    # 매 테케마다 초기화
    graph = {}
    result = False
    color = [0] * (1+V)

    for _ in range(E):
        n1, n2 = map(int, input().split())
        if n1 not in graph.keys():
            graph[n1] = []
        if n2 not in graph.keys():
            graph[n2] = []

        graph[n1].append(n2)
        graph[n2].append(n1)

    for i in range(1, V+1):
        if not color[i]:
            result = DFS(i)

            # result가 False인 즉시 (비연결 그래프의 경우) 다른 노드 탐색 x
            if not result:
                break

    if result: print("YES")
    else: print("NO")
