n = int(input())
arr = []
arr_b = []
dp = [0 for i in range(n)]
for i in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x:x[0])

for i in range(n):
    arr_b.append(arr[i][1])
for i in range(n):
    for j in range(i):
        if arr_b[i] > arr_b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp))