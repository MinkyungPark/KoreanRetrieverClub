N, M = map(int, input().split())
maps = [[s for s in input()] for _ in range(M)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

visited = [[0] * N for _ in range(M)]

def dfs(x, y, cnt):
    visited[x][y] = 1
    cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (
            0 <= nx < M and 
            0 <= ny < N and 
            not visited[nx][ny] and
            maps[nx][ny] == maps[x][y]
        ):
            cnt = dfs(nx, ny, cnt)
    
    return cnt

res = {'W': 0, 'B': 0}
for i in range(M):
    for j in range(N):
        if visited[i][j]:
            continue
        t = maps[i][j]
        res[t] += dfs(i, j, 0)**2

print(res['W'], res['B'])