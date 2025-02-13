N = input()
x, y = 0, 0
nx, ny = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_num = 3

for i in range(len(N)):
    if N[i] == 'R':
        if dir_num == 0:
            dir_num = 1
        elif dir_num == 1:
            dir_num = 2
        elif dir_num == 2:
            dir_num = 3
        else:
            dir_num = 0
    
    elif N[i] == 'L':
        if dir_num == 0:
            dir_num = 3
        elif dir_num == 3:
            dir_num = 2
        elif dir_num == 2:
            dir_num = 1
        else:
            dir_num = 0

    else:
        if dir_num == 0:
            nx, ny = x + dx[0], y + dy[0]
        elif dir_num == 1:
            nx, ny = x + dx[1], y + dy[1]
        elif dir_num == 2:
            nx, ny = x + dx[2], y + dy[2]
        else:
            nx, ny = x + dx[3], y + dy[3]
    
    x, y = nx, ny

print(x, y)
    