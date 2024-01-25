n, m = map(int, input().split())
graph = []

for i in range(n + 1):
    if i == 0:
        row = [0] * (m + 1)
    else:
        row = [0]
        row.extend(list(map(int, input())))
    graph.append(row)

dy = [-1, 1, 0, 0]  # 상하
dx = [0, 0, -1, 1]  # 좌우

def isInrange(y, x):
    return x >= 1 and y >= 1 and x <= m and y <= n

def dfs(y, x):
    if not isInrange(y, x) or graph[y][x] == 0:
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if isInrange(ny, nx) and graph[ny][nx] == 1:
            graph[ny][nx] = graph[y][x] + 1
            dfs(ny, nx)

dfs(1, 1)
print(graph[n][m])
