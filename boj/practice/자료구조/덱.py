# 10866
# 자료구조 - 덱

from collections import deque
import sys

# 빠른 입출력 -> 시간초과 해결
input = sys.stdin.readline

T = int(input())

myDeq = deque([])

for i in range(T):
    cmd = input().rstrip()  # 입력받을 때 줄바꿈 '\n' 제거
    if cmd.split()[0] == 'push_front':
        x = cmd.split()[1]
        myDeq.appendleft(x)
    
    elif cmd.split()[0] == 'push_back':
        x = cmd.split()[1]
        myDeq.append(x)

    elif cmd == 'pop_front':
        if not myDeq:
            print(-1)
        else:
            print(myDeq.popleft())

    elif cmd == 'pop_back':
        if not myDeq:
            print(-1)
        else:
            print(myDeq.pop())

    elif cmd == 'size':
        print(len(myDeq))
    
    elif cmd == 'empty':
        if not myDeq:
            print(1)
        else:
            print(0)

    elif cmd == 'front':
        if not myDeq:
            print(-1)
        else:
            print(myDeq[0])

    elif cmd == 'back':
        if not myDeq:
            print(-1)
        else:
            print(myDeq[-1])
