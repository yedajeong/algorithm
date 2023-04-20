# Medium

def solution(A):
    dp = [0] * len(A)
    dp[0] = A[0]
    for i in range(1, len(A)):
        # 초기화
        dp[i] = dp[i-1]+A[i]
        dice = 2
        while(dice <= 6 and i-dice >= 0):
            dp[i] = max(dp[i], dp[i-dice]+A[i])
            dice += 1

    return dp[-1]


if __name__=='__main__':
    A = [1, -2, 0, 9, -1, -2]
    print(solution(A))
