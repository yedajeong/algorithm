def solution(elements):
    answer = []

    S = [0] * len(elements)  # 구간합 저장
    S[0] = elements[0]
    answer.append(elements[0])

    for i in range(1, len(elements)):
        S[i] = S[i-1] + elements[i]
        answer.append(elements[i])  # 길이가 1인 연속 부분 수열

    for length in range(2, len(elements)+1):  # 길이가 2~len(elem)인 연속 부분 수열 합
        for start in range(0, len(elements)):
            end = start + length - 1
            end = (end + len(elements)) % len(elements)
            if start < end:  # start ~ end 사이 구간합
                if start == 0:
                    answer.append(S[end])
                else:
                    answer.append(S[end] - S[start-1])
            else:  # 전체합 - (end ~ start 사이 구간합)
                answer.append(S[-1] - S[start-1] + S[end])

    return len(set(answer))


if __name__ == "__main__":
    elements = [7, 9, 1, 1, 4]

    print(solution(elements))
