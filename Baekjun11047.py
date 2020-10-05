n, k = map(int, input().split())
a = []
for _ in range(n):
    a.append(int(input()))

num = 0
for i in range(n-1, -1, -1):
    if k == 0:
        break
    if a[i] > k:
        continue
    num += k // a[i]
    k %= a[i]
print(num)