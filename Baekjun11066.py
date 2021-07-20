import sys

t = int(input())
for _ in range(t):
    K = int(input())
    file_list = list(map(int, sys.stdin.readline().split()))
    dp = [[0 for _ in range(K)] for _ in range(K)]
    sum = [0] * (K + 1)
    for i in range(1, K + 1):
        sum[i] = sum[i - 1] + file_list[i - 1]

    knuth = [[0 for _ in range(K)] for _ in range(K)]
    for i in range(K):
        knuth[i][i] = i

    for x in range(1, K):
        for i in range(K - x):
            j = i + x
            dp[i][j] = 999999999999
            for k in range(knuth[i][j - 1], knuth[i + 1][j] + 1):
                if k < K - 1 and dp[i][j] > dp[i][k] + dp[k + 1][j] + sum[j + 1] - sum[i]:
                    dp[i][j] = dp[i][k] + dp[k + 1][j] + sum[j + 1] - sum[i]
                    knuth[i][j] = k

    print(dp[0][K - 1])