def solution(numbers):
    answer = [0] * len(numbers)
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            top = stack.pop()
            answer[top] = numbers[i]
        
        stack.append(i)

    while stack:
        idx = stack.pop()
        answer[idx] = -1

    return answer


if __name__ == "__main__":
    numbers = [2, 3, 3, 5]
    print(solution(numbers))
