# Lv. 1

def solution(price, money, count):
    answer = -1
    need = 0
    
    for i in range(1, count+1):
        need += price * i
    
    if (money - need) < 0:
        answer = need - money
    else:
        answer = 0

    return answer
