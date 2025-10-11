from collections import deque

R, C = map(int, input().split())
maps = [[s for s in input()] for _ in range(R)]

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(x, y):
    cnt = {'.': 0, 'o': 0, 'v': 0}
    q = deque([(x, y)])
    visited[x][y] = True
    
    while q:
        x, y = q.popleft()
        cnt[maps[x][y]] += 1
        
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < R and 0 <= ny < C
                and not visited[nx][ny]
            ):
                q.append((nx, ny))
                visited[nx][ny] = True
    
    if cnt['o'] == cnt['v'] == 0:
        return '.', 0
    elif cnt['o'] > cnt['v']:
        return 'o', cnt['o']
    else:
        return 'v', cnt['v']
    
    
res = {'.': 0, 'o': 0, 'v': 0}
visited = [[maps[i][j] == '#' for j in range(C)] for i in range(R)]

for i in range(R):
    for j in range(C):
        if visited[i][j]:
            continue
        r, c = bfs(i, j)
        res[r] += c
print(res['o'], res['v'])

"""
### 최적화
* deque를 set으로 변환 O(|q|) > 모든 구간에서 반복 O(N²) > visited 배열 생성하기
* pop 시 방문처리 > 같은 칸 중복 enqueue > 방문 처리는 euqueue 때
"""