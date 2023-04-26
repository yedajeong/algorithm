# 시즌1
# Lv. 1

def solution(a, b):
    answer = 0

    for i in range(len(a)):
        answer += a[i] * b[i]

    return answer

if __name__=="__main__":
    a = [1, 2, 3, 4]
    b = [-3, -1, 0, 2]

    print(solution(a, b))
