# 11656
# 정렬

S = input()
A = []

for i in range(len(S)-1, -1, -1):
    A.append(S[i:])

A.sort()

for a in A:
    print(a)
