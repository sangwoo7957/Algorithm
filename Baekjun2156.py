n = int(input())
dp = [0 for _ in range(10001)]
check = [False for _ in range(n+1)]
arr = []
for _ in range(n):
    arr.append(int(input()))

dp[1] = arr[0]
if n > 1:
    dp[2] = arr[0] + arr[1]
for i in range(3, n+1):
    dp[i] = max(dp[i-1], dp[i-3] + arr[i-2] + arr[i-1], dp[i-2] + arr[i-1])

print(dp[n])