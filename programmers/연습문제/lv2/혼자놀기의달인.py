def dfs(card, visited, cards):
    stack = []
    stack.append(card)
    cycle = 0

    while stack:
        next = stack.pop()
        if not visited[next]:
            visited[next] = 1
            cycle += 1
            stack.append(cards[next-1])

    return cycle


def solution(cards):
    answer = []
    visited = [0] * (len(cards)+1)

    for card in cards:
        if not visited[card]:
            answer.append(dfs(card, visited, cards))

    answer.sort(reverse=True)

    if len(answer)==1:
        return 0

    return answer[0] * answer[1]


if __name__ == "__main__":
    cards = [2, 1]

    print(solution(cards))
