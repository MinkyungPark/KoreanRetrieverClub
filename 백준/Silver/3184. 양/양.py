from collections import deque

R, C = map(int, input().split())
maps = [[s for s in input()] for _ in range(R)]

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y):
    q = deque([(x, y)])
    cnt = {'.': 0, 'o': 0, 'v': 0}
    while q:
        x, y = q.popleft()
        cnt[maps[x][y]] += 1
        maps[x][y] = '#'
        
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < R and 0 <= ny < C
                and maps[nx][ny] != '#'
                and not (set(q) & set([(nx, ny)]))
            ):
                q.append((nx, ny))
    
    if cnt['o'] == cnt['v'] == 0:
        return '.', 0
    elif cnt['o'] > cnt['v']:
        return 'o', cnt['o']
    else:
        return 'v', cnt['v']
    
    
res = {'.': 0, 'o': 0, 'v': 0}
for i in range(R):
    for j in range(C):
        if maps[i][j] == '#':
            continue
        r, c = bfs(i, j)
        res[r] += c
print(res['o'], res['v'])