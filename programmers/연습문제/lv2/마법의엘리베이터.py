def solution(storey):
    answer = 0
    div = 10

    while storey != 0:
        # 5일 때 하나 더 앞자리까지 보기
        if (storey % div) == 5:
            # 올라가서 6이상 되면 올라가기
            if (storey // div) % div >= 5:
                answer += 5
                storey //= div
                storey += 1
            # 아니면 그냥 내려가기
            else:
                answer += 5
                storey //= div
        # 내려가기
        elif (storey % div) < 5:
            answer += storey % div
            storey //= div
        # 올라갔다(storey += 1) 내려오기 (10-나머지)
        else:
            answer += 10 - (storey % div)
            storey //= div
            storey += 1

    return answer


if __name__ == "__main__":
    storey = 965
    print(solution(storey))
