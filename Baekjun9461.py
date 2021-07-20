def solution(n):
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1

    for i in range(3, n):
        dp[i] = dp[i-3] + dp[i-2]

    return dp[n-1]

t = int(input())
for _ in range(t):
    n = int(input())
    print(solution(n))