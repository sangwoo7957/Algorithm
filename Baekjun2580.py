import sys
sdk = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i, j) for i in range(9) for j in range(9) if sdk[i][j] == 0]

def solution(index):
    if index == len(zeros):
        for row in sdk:
            print(*row)
        sys.exit(0)

    else:
        x = zeros[index][0]
        y = zeros[index][1]
        dx = (x//3) * 3
        dy = (y//3) * 3
        num_list = [False] + [True for _ in range(9)]

        for j in range(9):
            if (sdk[x][j]):
                num_list[sdk[x][j]] = False
            if (sdk[j][y]):
                num_list[sdk[j][y]] = False

        for i in range(dx, dx+3):
            for j in range(dy, dy + 3):
                check_num = sdk[i][j]
                if check_num:
                    num_list[check_num] = False

        answer_list = [i for i, k in enumerate(num_list) if k]
        for num in answer_list:
            sdk[x][y] = num
            solution(index + 1)
            sdk[x][y] = 0

solution(0)