# 스택과 큐 문제
# 17298
# 골드 5

'''
<Key Idea>
오큰수: 오른쪽에 있으면서 A보다 큰 수 중 가장 왼쪽에 있는 수 (없으면 -1)
1. 스택에 새로 들어오는 수가 top에 존재하는 수보다 크면 그 수는 오큰수
2. 오큰수를 구한 후 수열에서 오큰수가 존재하지 않는 숫자에는 -1을 출력
'''  

n = int(input())
answer = [0] * n  # 오큰수를 저장할 정답 배열
A = list(map(int, input().split()))
stack = []

for i in range(n):
    while stack and A[stack[-1]] < A[i]:  # A[i]가 A[top]의 오큰수가 됨
        top = stack.pop()  # 스택에서 삭제
        answer[top] = A[i]

    stack.append(i)

# 오큰수 지정 안된 애들(=스택에 남아있는 애들)만 뽑아서 -1 저장
while stack:
    top = stack.pop()
    answer[top] = -1

result = ""
for i in range(n):
    result += str(answer[i])+" "

print(result)
