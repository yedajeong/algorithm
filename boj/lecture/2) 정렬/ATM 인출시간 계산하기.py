# 삽입 정렬 실전문제
# 11399
# 실버 3

N = int(input())
A = list(map(int, input().split()))
S = [0] * N  # 합 배열 (대기 시간의 누적합)

# 삽입 정렬
for i in range(1, N):
    insert_point = 0  # 현재 값보다 더 작은 애가 없는 경우 == 현재 값이 제일 작음 == 제일 앞(idx=0)에 위치
    insert_value = A[i]
    for j in range(i-1, -1, -1):  # 뒤에서부터 탐색
        if A[j] < A[i]:
            insert_point = j+1  # 나보다 작은 애의 뒷자리에 놓아야 함
            break
    # 한 칸씩 뒤로 shifting
    for j in range(i-1, insert_point-1, -1):
        A[j+1] = A[j]
    A[insert_point] = insert_value

# 합 배열 만들기
S[0] = A[0]
answer = S[0]
for i in range(1, N):
    S[i] = S[i-1] + A[i]
    answer += S[i]

print(answer)
