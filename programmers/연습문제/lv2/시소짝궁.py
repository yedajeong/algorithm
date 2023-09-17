from collections import Counter

def solution(weights):
    answer = 0

    counter = Counter(weights)
    for _, cnt in counter.items():
        # 1:1 비율의 짝 (cnt C 2)
        if cnt >= 2:
            answer += cnt*(cnt-1)//2

    for item, cnt in counter.items():
        # 1:2비율 (2m 4m)
        if item*(1/2) in weights:
            answer += counter[item] * counter[item*(1/2)]
        # 2:3비율 (2m 3m)
        if item*(2/3) in weights:
            answer += counter[item] * counter[item*(2/3)]
        # 3:4비율 (3m 4m)
        if item*(3/4) in weights:
            answer += counter[item] * counter[item*(3/4)]

    return answer
