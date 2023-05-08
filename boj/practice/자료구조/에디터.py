# 1406
# 자료구조 - 스택, 연결 리스트(linked list)

# 시간초과...
# c++은 구조체로 노드 만들어서 링크드 리스트로 풀이
# python -> deque의 내부 구현이 LL로 돼있지만 insert연산 O(n)의 시간복잡도 -> 시간초과
    # 따라서 커서 기준 왼쪽/오른쪽 두 개의 스택으로 나눠 구현

from collections import deque
import sys

input = sys.stdin.readline

a = input().rstrip()
M = int(input().rstrip())

left = deque(list(a))
right = deque([])

for i in range(M):
    cmd = input().rstrip()
    if cmd.split()[0] == 'P':
        x = cmd.split()[1]
        left.append(x)  
    
    elif cmd.split()[0] == 'L':
        if left:
            x = left.pop()
            right.appendleft(x)

    elif cmd.split()[0] == 'D':
        if right:
            x = right.popleft()
            left.append(x)

    elif cmd.split()[0] == 'B':
        if left:
            left.pop()

'''
# deque 하나로 -> 시간초과
myDeq = deque(list(a))
cursor = len(a)-1

for i in range(M):
    cmd = input().rstrip()
    if cmd.split()[0] == 'P':
        x = cmd.split()[1]
        cursor += 1
        myDeq.insert(cursor, x)  
    
    elif cmd.split()[0] == 'L':
        if cursor > -1:
            cursor -= 1

    elif cmd.split()[0] == 'D':
        if cursor < len(myDeq)-1:
            cursor += 1

    elif cmd.split()[0] == 'B':
        if cursor > -1:
            del myDeq[cursor]
            cursor -= 1


print(''.join(myDeq))
'''

print(''.join(left) + ''.join(right))
