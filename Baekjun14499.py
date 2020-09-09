def dice_solve(n):
    if n == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif n == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif n == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    else:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]


move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
dice = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
n, m, x, y, k = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
for oper in list(map(int, input().split())):
    moved_x = move[oper-1][0] + x
    moved_y = move[oper-1][1] + y

    if (0 <= moved_x < n) and (0 <= moved_y < n):
        x, y = moved_x, moved_y
        dice_solve(oper)
        if arr[x][y] != 0:
            dice[6] = arr[x][y]
            arr[x][y] = 0
        else:
            arr[x][y] = dice[6]
        print(dice[1])