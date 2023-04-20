# Medium

# O(N+M)으로도 풀이 가능..!
def solution(N, A):
    save_max = 0
    max_counter = 0
    counter = [0] * N  # [0]으로 초기화된 배열
    for idx in A:
        if idx > N:
            save_max = max_counter
        else:
            if counter[idx-1] < save_max:
                counter[idx-1] = save_max
            counter[idx-1] += 1
            max_counter = max(max_counter, counter[idx-1])

    for i in range(N):
        if counter[i] < save_max:
            counter[i] = save_max

    return counter


if __name__=='__main__':
    N = 5
    A = [3, 4, 4, 6, 1, 4, 4]
    print(solution(N, A))
