m = list(input())
n = list(input())
dp = [[0] * (len(n) + 1) for i in range(len(m) + 1)]
for i in range(len(m)):
    for j in range(len(n)):
        if m[i] == n[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
print(dp[len(m)][len(n)])