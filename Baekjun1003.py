'''
n = int(input())
zero = [1, 0, 1]
one = [0, 1, 1]

def one_two_count(n):
    init_len = len(zero)
    if (init_len <= n):
        for i in range(init_len, n + 1):
            add_0 = zero[i - 2] + zero[i - 1]
            add_1 = one[i - 2] + one[i - 1]
            zero.append(add_0)
            one.append(add_1)
    print('{} {}'.format(zero[n], one[n]))

for _ in range(n):
    one_two_count(int(input()))
'''
t = int(input())
for i in range(t):
    n = int(input())
    zero = 1
    one = 0
    tmp = 0
    for _ in range(n):
        tmp = one
        one = one + zero
        zero = tmp
    print(zero, one)