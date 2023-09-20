def solution(n, left, right):
    answer = []

    l_row = left // n
    l_col = left % n
    r_row = right // n
    r_col = right % n

    if l_row == r_row:
        for col in range(l_col, r_col+1):
            answer.append(max(l_row, col) + 1)
    else:
        for col in range(l_col, n):
            answer.append(max(l_row, col) + 1)

    if l_row+2 <= r_row:
        for row in range(l_row+1, r_row):
            for col in range(0, n):
                answer.append(max(row, col) + 1)
        for col in range(0, r_col+1):
            answer.append(max(r_row, col) + 1)

    elif l_row+1 == r_row:
        for col in range(0, r_col+1):
            answer.append(max(r_row, col) + 1)

    return answer


if __name__ == "__main__":
    n = 4
    left = 7
    right = 14
    print(solution(n, left, right))
