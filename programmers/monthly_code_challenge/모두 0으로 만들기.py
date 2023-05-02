# 시즌2
# Lv.3

# list를 이용한 stack으로 품 -> 시간 초과
# deque으로 queue 구현해 풀이

# visited 표시할 때 각 인덱스(노드)의 T/F 말고 visited에 노드를 추가하는 방식으로 구현해서
# 방문 점검할 때 if node not in visited 로 하니까 visited의 길이만큼 배열 탐색 -> 여기서 O(N)이라 시간초과 났던 거 같음
# visited 구현 변경해주고 통과

from collections import deque

def solution(a, edges):
    answer = 0

    graph = {}

    # 그래프 구성하기
    for n1, n2 in edges:
        if n1 not in graph:
            graph.setdefault(n1, [n2])
        else:
            graph[n1].append(n2)

        if n2 not in graph:
            graph.setdefault(n2, [n1])
        else:
            graph[n2].append(n1)

    queue = deque([0])  # 최초에는 루트노드만 존재
    visited = [0] * len(a)
    pair = []

    while queue:
        parent = queue.popleft()
        if not visited[parent]:
            visited[parent] = 1
            if parent in graph:
                for child in graph[parent]:
                    if not visited[child]:
                        pair.append((parent, child))  # [0]: 부모 [1]: 자식
                        queue.append(child)

    for parent, child in pair[::-1]:
        a[parent] += a[child]
        answer += abs(a[child])
        a[child] = 0        

    if a[0] != 0:
        return -1
    else:
        return answer

if __name__=="__main__":
    a = [-5, 0, 2, 1, 2]
    edges = [[0,1],[3,4],[2,3],[0,3]]

    # a = [0,1,0]
    # edges = [[0,1],[1,2]]

    print(solution(a, edges))
