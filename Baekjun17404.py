import sys

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))

result = sys.maxsize
for color in range(3):
    dp = [[0 for _ in range(n)] for _ in range(3)]
    for i in range(3):
        if i == color:
            dp[i][0] = s[0][i]
            continue
        dp[i][0] = sys.maxsize

    for i in range(1, n):
        dp[0][i] = s[i][0] + min(dp[1][i - 1], dp[2][i - 1])
        dp[1][i] = s[i][1] + min(dp[0][i - 1], dp[2][i - 1])
        dp[2][i] = s[i][2] + min(dp[0][i - 1], dp[1][i - 1])

    for i in range(3):
        if i == color:
            continue
        result = min(result, dp[i][-1])

print(result)