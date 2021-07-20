import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [[-1000000001, -1]]
trace = [0] * n

for i in range(n):
    low = 0
    high = len(dp) - 1
    while low <= high:
        mid = (low + high) // 2
        if dp[mid][0] < arr[i]:
            low = mid + 1
        else:
            high = mid - 1

    if low >= len(dp):
        trace[i] = dp[low-1][1]
        dp.append([arr[i], i])
    else:
        dp[low][0] = arr[i]
        dp[low][1] = i
        trace[i] = dp[low-1][1]
print(len(dp) - 1)

result = []
cur_index = dp[len(dp)-1][1]
while cur_index != -1:
    result.append(arr[cur_index])
    cur_index = trace[cur_index]

for i in range(len(result)-1, -1, -1):
    print(result[i], end=" ")