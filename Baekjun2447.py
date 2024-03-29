def solution(n):
    matrix = []
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return list(matrix)

star = ["***", "* *", "***"]
n = int(input())
k = 0
while n != 3:
    n = n // 3
    k += 1

for i in range(k):
    star = solution(star)
for i in star:
    print(i)