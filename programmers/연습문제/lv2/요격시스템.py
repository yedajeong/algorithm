
def solution(targets):
    answer = 0

    targets.sort(key = lambda x: [x[1], x[0]])

    s = e = 0

    for target in targets:
        if target[0] >= e:  # 현재 start가 이전 end보다 앞에 있으면 추가 미사일 필요 없음
            answer += 1
            e = target[1]

    return answer


if __name__=="__main__":
    targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]

    print(solution(targets))
