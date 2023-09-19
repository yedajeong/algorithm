from collections import Counter

def solution(topping):
    answer = 0
    length = 0
    
    back = Counter(topping)
    front = {}

    for top in topping:
        if top in front:
            front[top] += 1
        else:
            front[top] = 1
        back[top] -= 1

        if back[top] == 0:
            del back[top]

        if len(front) == len(back):
            answer += 1 

    return answer
