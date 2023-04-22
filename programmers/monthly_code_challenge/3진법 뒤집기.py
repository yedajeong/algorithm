# 시즌1
# Lv. 1

def solution(n):
    answer = 0

    # 1. 10진수 -> 3진수 (앞뒤로 뒤집기)
    tri = ""  # 뒤집어진 3진법
    while n:
        tri += str(n % 3)
        n //= 3

    # 2. 3진수 -> 10진수
    tri = str(int(tri))
    for idx, val in enumerate(tri[::-1]):
        answer += (3**idx) * int(val)

    # 2-2. int함수 사용
    answer = int(tri, 3)
    
    return answer

if __name__=="__main__":
    n = 45

    print(solution(n))
