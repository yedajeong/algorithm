# 보조 컨테이너: stack

def solution(order):
    answer = 0
    container = []
    i = 0
    box = 1

    while box <= len(order):
        if box == order[i]:
            answer += 1
            i += 1
            box += 1
        elif not container:
            container.append(box)
            box += 1
        elif container[-1] == order[i]:
            container.pop()
            answer += 1
            i += 1
        else:
            container.append(box)
            box += 1

    while i < len(order):
        if not container:
            break
        if container[-1] == order[i]:
            container.pop()
            answer += 1
            i += 1
        else:
            break

    return answer


if __name__ == "__main__":
    order = [3, 2, 1, 4, 5]
    print(solution(order))
