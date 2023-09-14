def solution(sequence, k):
    answer = []
    length = len(sequence)

    end = length-1
    total = 0

    for start in range(length-1, -1, -1):
        total += sequence[start]

        if total > k:
            total -= sequence[end]
            end -= 1
        
        if total == k:
            s = start
            e = end
            while s > 0:
                total -= sequence[e]
                e -= 1
                s -= 1
                total += sequence[s]
                if total == k:
                    start = s
                    end = e
                else:
                    break
            answer = [start, end]
            break

    return answer


if __name__ == "__main__":
    sequence = list(map(int, input().split()))
    k = int(input())

    print(solution(sequence, k))
