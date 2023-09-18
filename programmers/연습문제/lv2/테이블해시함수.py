def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key = lambda x: [x[col-1], -1 * x[0]])

    for i in range(row_begin, row_end+1):
        s = 0
        for item in data[i-1]:
            s += (item % i)

        answer ^= s

    return answer

if __name__ == "__main__":
    data = [[2, 2, 6],
            [1, 5, 10],
            [4, 2, 9],
            [3, 8, 3]]
    print(solution(data, 2, 2, 3))
