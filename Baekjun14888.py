def solution(cnt, result, add, sub, mul, div):
    global max_result
    global min_result

    if cnt == n:
        max_result = max(result, max_result)
        min_result = min(result, min_result)
        return

    if add:
        solution(cnt+1, result+num[cnt], add-1, sub, mul, div)
    if sub:
        solution(cnt+1, result-num[cnt], add, sub-1, mul, div)
    if mul:
        solution(cnt+1, result*num[cnt], add, sub, mul-1, div)
    if div:
        solution(cnt+1, int(result/num[cnt]), add, sub, mul, div-1)

n = int(input())
num = list(map(int, input().split()))
oper = list(map(int, input().split()))
max_result = -1000000001
min_result = 1000000001
solution(1, num[0], oper[0], oper[1], oper[2], oper[3])
print(max_result)
print(min_result)