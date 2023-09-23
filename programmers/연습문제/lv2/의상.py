def solution(clothes):
    answer = 1
    closet = {}
    
    for _, type in clothes:
        if type not in closet.keys():
            closet[type] = 1
        else:
            closet[type] += 1

        # 혹은
        # closet[type] = closet.get(type, 0) + 1

    for type in closet.keys():
        answer *= (closet[type]+1) # 종류 개수 + 1(안입기)

    answer -= 1 # 다 안입는 경우 제외

    return answer

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
