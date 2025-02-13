N = int(input())
x, y = 0, 0
dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]


graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

def in_graph(x, y):
    return 0 <= x  and x < N and 0 <= y and y < N


def count_num(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_graph(nx, ny) and graph[nx][ny] == 1:
            cnt += 1
    
    return cnt

result = 0
for i in range(N):
    for j in range(N):
        if count_num(i, j) >= 3:
            result += 1

print(result)