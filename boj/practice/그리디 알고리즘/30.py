# 10610
# 그리디 알고리즘
# 정수론

# N = 100,000자리 수

N = list(map(int, input()))

# 예외처리
if 0 not in N:
    print(-1)
    exit()

num_sum = sum(N)

if num_sum % 3 != 0:
    print(-1)
else:
    num_sorted = sorted(N, reverse=True)  # 큰 수 찾기 -> 정렬
    answer = "".join(list(map(str, num_sorted)))
    print(answer)
