# 1744
# 그리디 알고리즘

N = int(input())
pos = []
neg = []
answer = 0

for _ in range(N):
    n = int(input())
    if n == 1:
        answer += 1
    elif n > 0:
        pos.append(n)
    else:
        neg.append(n)

pos.sort(reverse=True)
neg.sort()


end = len(pos)-1
if len(pos) % 2:
    end -= 1
    answer += pos[-1]

for i in range(0, end, 2):
    answer += pos[i] * pos[i+1]

end = len(neg)-1
if len(neg) % 2:
    end -= 1
    answer += neg[-1]

for i in range(0, end, 2):
    answer += neg[i] * neg[i+1]

print(answer)
