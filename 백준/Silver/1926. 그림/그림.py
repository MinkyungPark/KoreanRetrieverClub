from collections import deque

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

def bfs(x, y):
    cnt = 1
    q = deque([(x, y)])
    paper[x][y] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n and 0 <= ny < m
                and paper[nx][ny]
            ):
                q.append((nx, ny))
                paper[nx][ny] = 0
                cnt += 1
    return cnt

count, max_size = 0, 0
for i in range(n):
    for j in range(m):
        if not paper[i][j]:
            continue
        count += 1
        max_size = max(max_size, bfs(i, j))

print(count)
print(max_size)