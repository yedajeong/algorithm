# 사다리꼴 넓이: (a+b)*h / 2
# a, b는 우박수열 그래프의 y값, h는 x값(=1)
def solution(k, ranges):
    answer = []
    sequence = []  # 우박수열

    # 1. 우박수열 전체 구하기
    sequence.append((0, k))
    x = 0
    while k > 1:
        if k % 2 == 0:
            k //= 2
        elif k % 2 == 1:
            k *= 3
            k += 1
        x += 1
        sequence.append((x, k))
    n = x

    print(sequence)

    for a, b in ranges:
        result = 0
        if n+b < a:
            result = -1*1.0
        else:
            for i in range(a, n+b):
                w1 = sequence[i][1]
                w2 = sequence[i+1][1]
                result += (w1 + w2) / 2
        answer.append(result)

    return answer


if __name__ == "__main__":
    k = 5
    ranges = [[0,0],[0,-1],[2,-3],[3,-3]]	
    print(solution(k, ranges))
