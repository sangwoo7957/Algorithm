def solution():
    dp = [cost[0]]
    for i in range(1, n):
        temp = []
        temp.append(min(dp[i-1][1], dp[i-1][2]) + cost[i][0])
        temp.append(min(dp[i-1][0], dp[i-1][2]) + cost[i][1])
        temp.append(min(dp[i-1][0], dp[i-1][1]) + cost[i][2])
        dp.append(temp)
    return(min(dp[n-1]))

n = int(input())
cost = []
for i in range(n):
    r, g, b = map(int, input().split())
    cost.append([r, g, b])

print(solution())