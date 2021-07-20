def solution():
    for i in range(1, n):
        for j in range(len(tri_arr[i])):
            if j == 0:
                tri_arr[i][j] = tri_arr[i][j] + tri_arr[i-1][j]
            elif i == j:
                tri_arr[i][j] = tri_arr[i][j] + tri_arr[i-1][j-1]
            else:
                tri_arr[i][j] = max(tri_arr[i-1][j-1], tri_arr[i-1][j]) + tri_arr[i][j]

    return (max(tri_arr[n-1]))



n = int(input())
tri_arr = []
for i in range(n):
    num = list(map(int, input().split()))
    tri_arr.append(num)

print(solution())