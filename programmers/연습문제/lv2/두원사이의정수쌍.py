import math

def solution(r1, r2):
    answer = 0

    for x in range(1, r2+1):
        if x < r1:
            low_y = math.ceil(math.sqrt(r1**2 - x**2))
        else:
            low_y = 0
        high_y = math.floor(math.sqrt(r2**2 - x**2))

        answer += high_y - low_y + 1

    answer *= 4

    return answer


if __name__ == "__main__":
    r1 = 2
    r2 = 3

    print(solution(r1, r2))