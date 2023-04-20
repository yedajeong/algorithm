# Easy

def solution(A):
    A.sort()
    if A == list(range(1, len(A)+1)):
        return 1
    else:
        return 0


if __name__=='__main__':
    A = [4, 1, 3]
    print(solution(A))
