N, T = map(int, input().split())
text = input()
order = [text[i] for i in range(len(text))]
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

x, y = N // 2, N // 2
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
move_dir = 2
cnt = graph[x][y]


for i in range(T):
    if order[i] == 'L':
        if move_dir == 0:
            move_dir = 1
        elif move_dir == 1:
            move_dir = 2
        elif move_dir == 2:
            move_dir = 3
        else:
            move_dir = 0
    
    elif order[i] == 'R':
        if move_dir == 0:
            move_dir = 3
        elif move_dir == 1:
            move_dir = 0
        elif move_dir == 2:
            move_dir = 1
        else:
            move_dir = 2
    
    else:
        nx, ny = x + dxs[move_dir], y + dys[move_dir]
        if 0 <= nx < N and 0 <= ny < N:
            x, y = nx, ny
            cnt += graph[x][y]
print(cnt)