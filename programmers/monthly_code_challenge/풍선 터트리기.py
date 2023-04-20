# Lv. 3

# min 함수 썼을 때 시간 초과, if문 썼을 때 같은 케이스에서 시간이 더 적게 걸리긴 하나 그래도 시간 초과
# O(N^2)
def solution_time_out(a):
    answer = 0
    for i in range(len(a)):
        min_left = 10**9
        min_right = 10**9
        for left in range(i):
            # min_left = min(min_left, a[left])
            if min_left > a[left]:
                min_left = a[left]

        for right in range(i+1, len(a)):
            # min_right = min(min_right, a[right])
            if min_right > a[right]:
                min_right = a[right]

    return answer

# O(3*N)
def solution(a):
    answer = 2  # 양 끝의 풍선은 끝까지 남을 수 있음

    if len(a)==1:
        return 1

    min_left = [a[0]] * len(a)
    min_right = [a[-1]] * len(a)

    for i in range(1, len(a)):
        min_left[i] = min(a[i], min_left[i-1])

    for i in range(len(a)-2, -1, -1):
        min_right[i] = min(a[i], min_right[i+1])

    for i in range(1, len(a)-1):
        left = min_left[i-1]
        right = min_right[i+1]

        if left < a[i] and right < a[i]:
            continue
        else:
            answer += 1


    return answer

if __name__=="__main__":
    # a = [9,-1,-5]
    a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]

    print(solution(a))
