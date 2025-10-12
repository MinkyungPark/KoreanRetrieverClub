from collections import deque

N, M, K = map(int, input().split())
visited = [[True] * M for _ in range(N)]
c = []
for _ in range(K):
    x, y = map(int, input().split())
    visited[x-1][y-1] = False
    c.append((x-1, y-1))

def bfs(x, y):
    cnt = 0
    q = deque([(x, y)])
    visited[x][y] = True
    cnt += 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < N and 0 <= ny < M
                and not visited[nx][ny]
            ):
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1

    return cnt

res = 0
for i, j in c:
    if visited[i][j]:
        continue
    res = max(res, bfs(i, j))
print(res)