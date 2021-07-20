def solution(n, start, mid, end):
    if n == 1:
        print(start, end)
    else:
        solution(n-1, start, end, mid)
        print(start, end)
        solution(n-1, mid, start, end)

n = int(input())
sum = 1
for i in range(n-1):
    sum = 2*sum + 1

print(sum)
solution(n, 1, 2, 3)