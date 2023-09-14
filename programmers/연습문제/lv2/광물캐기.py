def solution(picks, minerals):
    answer = 0

    # [i][j] = i번째 곡괭이로 j번째 광물 캘 때 피로도
    tired = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]

    # 못 캐는 광물 버림
    avail = picks[0]*5 + picks[1]*5 + picks[2]*5
    if len(minerals) > avail:
        minerals = minerals[:avail]

    mine_sort = []
    for i in range(0, len(minerals), 5):
        end = i+4
        if end > len(minerals)-1:
            end = len(minerals)-1

        tmp = []
        total = 0
        for idx in range(i, end+1):
            if minerals[idx]=="diamond":
                tmp.append(0)
                total += 25
            elif minerals[idx]=="iron":
                tmp.append(1)
                total += 5
            elif minerals[idx]=="stone":
                tmp.append(2)
                total += 1
        tmp.append(total)
        mine_sort.append(tmp)

    mine_sort.sort(key = lambda x : -1 * x[-1])

    print(mine_sort)

    for mine in mine_sort:
        if picks[0] > 0:
            i = 0
            picks[0] -= 1
        elif picks[1] > 0:
            i = 1
            picks[1] -= 1
        elif picks[2] > 0:
            i = 2
            picks[2] -= 1

        for j in range(0, len(mine)-1):
            answer += tired[i][mine[j]]

    return answer


if __name__ == "__main__":
    picks = [1, 3, 2]
    minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]

    print(solution(picks, minerals))
