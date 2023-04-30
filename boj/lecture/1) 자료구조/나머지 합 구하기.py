# 구간 합 실전 문제
# 10986
# 골드 3

'''
1 <= N <= 10e6  : 연속된 수의 개수
2 <= M <= 10e3  : M으로 나누어떨어지는 구간

<Key Idea>
1. (A + B) % C == ((A % C) + (B % C)) % C
즉, 이 구간 합의 나머지 연산 == 특정 구간 수들의 나머지 연산을 더해 나머지 연산을 한 값
2. 구간 합 배열 S[i] - S[j] == i~j까지의 구간 합
3. if S[i] % M == S[j] % M: (S[i]-S[j]) % M == 0 임
즉, 구간 합 배열의 원소를 M으로 나눈 나머지로 업데이트하고 S[i], S[j]가 같은 (i, j)쌍을 찾으면 
원본 리스트에서 j+1~i 까지의 구간 합이 M으로 나눠떨어짐
'''

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * n
cnt = [0] * m  # 합배열 S를 M으로 나눈 나머지로 업데이트 한 후, 같은 값을 갖는 i, j를 찾기 위한 배열, 길이: m으로 나눈 나머지, 즉 m
answer = 0

# 합배열 S 구성
S[0] = A[0]
for i in range(1, n):
    S[i] = S[i-1] + A[i]

# 합배열 업데이트 (현재 합배열을 M으로 나눈 나머지로)
for i in range(n):
    mod = S[i] % m

    # 나머지가 0이면 index 0~i까지의 구간 합이 M으로 나눈 나머지 0 (I=0, J=i 인 순서쌍 하나 발견)
    if mod == 0:
        answer += 1 
    
    # 같은 값을 갖는 애가 몇 개인지 카운팅
    cnt[mod] += 1

for i in range(m):
    if cnt[i] > 1:
        # 조합 계산 -> iC2 = (i * (i-1)) // 2
        answer += (cnt[i] * (cnt[i]-1)) // 2  # int형으로 반환하기 위해 / 대신 //

print(answer)
