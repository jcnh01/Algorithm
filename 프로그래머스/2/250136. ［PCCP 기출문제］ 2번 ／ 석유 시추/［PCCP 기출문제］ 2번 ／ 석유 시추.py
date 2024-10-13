from collections import deque
q = deque()

visit = [[False] * 500 for _ in range(500)]
rs = [0] * 500

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

def bfs(n, m, land, visit, rs) :
    vis = set()
    cnt = 0
    while q :
        y, x = q.popleft()
        vis.add(x)
        cnt += 1
        for i in range(4) :
            Y, X = y + dy[i], x + dx[i]
            if 0 <= Y < n and 0 <= X < m and not visit[Y][X] and land[Y][X] :
                visit[Y][X] = True
                q.append((Y, X))
    for v in vis :
        rs[v] += cnt

def solution(land):
    n = len(land)
    m = len(land[0])
    
    for i in range(m) :
        for j in range(n) :
            if land[j][i] == 1 and not visit[j][i] :
                visit[j][i] = True
                q.append((j, i))
                c = bfs(n, m, land, visit, rs)
    
    return max(rs)