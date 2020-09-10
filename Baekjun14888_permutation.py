from collections import deque
from itertools import permutations
import copy
import sys

def solve(n, num, oper):
    op = ['+', '-', '*', '//']
    oper_list = []
    max_num = -sys.maxsize - 1
    min_num = sys.maxsize
    for i in range(4):
        operation = op[i]
        count = oper[i]
        temp = [operation] * count
        oper_list.extend(temp)

    case_list= set(permutations(oper_list, n-1))

    for case in case_list:
        temp_list = deque(copy.deepcopy(num))
        idx = -1
        result = temp_list.popleft()
        while temp_list:
            idx += 1
            next_num = temp_list.popleft()
            current_op = case[idx]

            if current_op == '+':
                result += next_num
            elif current_op == '-':
                result -= next_num
            elif current_op == '*':
                result *= next_num
            else:
                if result < 0:
                    result = -(result)
                    result //= next_num
                    result = -(result)
                else:
                    result //= next_num

        if result < min_num:
            min_num = result
        if max_num < result:
            max_num = result

    return max_num, min_num

n = int(input())
num = deque(list(map(int, input().split())))
oper = deque(list(map(int, input().split())))

max_result, min_result = solve(n, num, oper)
print(max_result)
print(min_result)
