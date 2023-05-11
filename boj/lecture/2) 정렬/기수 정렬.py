# 기수 정렬 직접 코드로 구현해보기

from collections import deque

N = int(input())
A = input().split()


myQue = []
for i in range(10):
    myQue.append(deque([]))

length = 1
while True:
    idx = -1 * length

    for a in A:
        if length > len(a):
            myQue[0].append(a)
        else:
            myQue[int(a[idx])].append(a)
        
    if len(myQue[0]) >= N:
        break

    length += 1

    A = []
    for i in range(10):
        while myQue[i]:
            A.append(myQue[i].popleft())


answer = []
for i in range(10):
    while myQue[i]:
        answer.append(myQue[i].popleft())

print(' '.join(answer))
