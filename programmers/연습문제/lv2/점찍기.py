import math

def solution(k, d):
    answer = 0
    for x in range(d+1):
        if x % k != 0:  # k의 배수인지 확인
            continue
        y = math.floor(math.sqrt(d**2 - x**2))
        
        answer += y//k + 1

    return answer

if __name__ == "__main__":
    k = 1
    d = 5
    print(solution(k, d))
