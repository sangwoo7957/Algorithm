n = int(input())
arr = list(map(int, input().split()))
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)
dp_count = max(dp)
print(dp_count)

idx = dp.index(dp_count)
s = []
while idx >= 0:
    if dp[idx] == dp_count:
        s.append(arr[idx])
        dp_count -= 1
    idx -= 1

for num in s[::-1]:
    print(num, end=" ")
print()