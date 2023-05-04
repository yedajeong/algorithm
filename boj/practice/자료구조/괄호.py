# 9012
# 자료구조 - 스택

T = int(input())

for i in range(T):
    ps = input()
    stack = []
    finished = True
    for x in ps:
        if x == "(":
            stack.append(x)
        elif not stack:
            print('NO')
            finished = False
            break
        else:
            stack.pop()

    if finished and stack:
        print('NO')
    elif finished and not stack:
        print('YES')