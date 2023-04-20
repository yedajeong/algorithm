# Medium

def solution(A):
    A = list(set(A))
    A.sort()
    A = [i for i in A if i > 0]

    if len(A) == 0:
        return 1
    elif A[0] > 1:
        return 1
    
    for i in range(len(A)-1):
        if A[i]+1 != A[i+1]:
            return A[i]+1
    
    return A[-1]+1

if __name__=='__main__':
    A = [1]
    print(solution(A))
