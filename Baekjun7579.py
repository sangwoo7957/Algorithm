n, m = map(int, input().split())
arr = list(map(int, input().split()))
cost = list(map(int, input().split()))
cost_max = sum(cost) + 1
dp = [-1] * cost_max
dp[0] = 0
for i in range(n):
    for j in range(cost_max - cost[i] - 1, -1, -1):
        if dp[j] != -1:
            dp[j + cost[i]] = max(dp[j + cost[i]], dp[j] + arr[i])

for i in range(cost_max):
    if dp[i] >= m:
        print(i)
        break