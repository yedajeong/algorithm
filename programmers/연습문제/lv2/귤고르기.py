from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    count = list(count.values())
    count.sort(reverse=True)

    if count[0] >= k:
        return 1
    
    for cnt in count:
        if k >= cnt:
            k -= cnt
            answer += 1
        elif k > 0 and k < cnt:
            k = 0
            answer += 1
            break
        elif k == 0:
            break
    
    return answer

if __name__ == "__main__":
    k = 6
    tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

    print(solution(k, tangerine))
