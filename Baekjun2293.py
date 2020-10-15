n, k = map(int, input().split())
arr = []
dp = [0 for i in range(k+1)]
dp[0] = 1
for _ in range(n):
    arr.append(int(input()))
for value in arr:
    for i in range(1, k+1):
        if i - value >= 0:
            dp[i] += dp[i-value]
print(dp[k])