# 10845
# 자료구조 - 큐

from collections import deque
import sys

# 빠른 입출력 -> 시간초과 해결
input = sys.stdin.readline

T = int(input())

queue = deque([])

for i in range(T):
    cmd = input().rstrip()  # 입력받을 때 줄바꿈 '\n' 제거
    if cmd.split()[0] == 'push':
        x = cmd.split()[1]
        queue.append(x)
    
    elif cmd == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue.popleft())

    elif cmd == 'size':
        print(len(queue))
    
    elif cmd == 'empty':
        if not queue:
            print(1)
        else:
            print(0)

    elif cmd == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])

    elif cmd == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
