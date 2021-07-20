def solution(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(1, n):
        dp[i+1] = dp[i] + dp[i-1]

    return dp[n]

n = int(input())
print(solution(n))