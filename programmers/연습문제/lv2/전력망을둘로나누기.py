from collections import deque

def bfs(s, visited, graph):
    cnt = 0
    que = deque()
    que.append(s)
    visited[s] = True

    while que:
        now = que.popleft()
        cnt += 1
        for next in graph[now]:
            if not visited[next]:
                visited[next] = True
                que.append(next)

    return cnt

def solution(n, wires):
    answer = 100
    graph = []
    for _ in range(0, n+1):
        graph.append([])

    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)

    for s, e in wires:
        visited = [0] * (n+1)
        graph[s].remove(e)
        graph[e].remove(s)
        tmp = []

        for node in range(1, n+1):
            if not visited[node]:
                tmp.append(bfs(node, visited, graph))

        answer = min(answer, abs(tmp[0]-tmp[1]))

        graph[s].append(e)
        graph[e].append(s)

    return answer

if __name__ == "__main__":
    n = 9
    wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	
    print(solution(n, wires))
