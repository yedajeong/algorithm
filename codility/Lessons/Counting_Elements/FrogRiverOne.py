# Easy

def solution(X, A):
    leaf = []
    for idx, item in enumerate(A):
        leaf.append((idx, item))

    print(leaf)

    leaf = sorted(leaf, key=lambda x: x[1])

    print(leaf)

    x = 1
    sec = -1
    for idx, item in leaf:
        if item == x:
            x+=1
            sec = max(sec, idx)
            if x > X:
                return sec
            
    return -1


if __name__=='__main__':
    X = 3
    A = [1, 3, 1, 3, 2, 1, 3]
    print(solution(X, A))
