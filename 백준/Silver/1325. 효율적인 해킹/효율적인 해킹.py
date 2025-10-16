N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

visited = [0] * (N + 1)

def dfs(start):
    cnt = 0
    stack = [start]
    if visited[start] != start:
        visited[start] = start
        cnt += 1
    while stack:
        x = stack.pop()
        for y in graph[x]:
            if visited[y] != start:
                visited[y] = start
                cnt += 1
                stack.append(y)
    return cnt

cnts = [0] * (N + 1)
for i in range(1, N + 1):
    cnts[i] = dfs(i)

max_cnt = max(cnts)
res = [i for i in range(1, N + 1) if cnts[i] == max_cnt]
print(*res)