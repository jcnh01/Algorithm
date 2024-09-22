import sys
input = sys.stdin.readline

from collections import deque
q = deque()

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, 1, -1, -1, 0, 1]

def bfs(w, h, visit) :
    while q :
        y, x = q.popleft()
        for i in range(8) :
            Y = y + dy[i]
            X = x + dx[i]
            if 0 <= Y < h and 0 <= X < w and not visit[Y][X] and graph[Y][X] :
                visit[Y][X] = True
                q.append((Y, X))

rs = []

while True :
    w, h = list(map(int, input().split()))
    if not w and not h :
        break

    graph = []
    visit = [[False] * w for _ in range(h)]

    for i in range(h) :
        graph.append(list(map(int, input().split())))

    cnt = 0
    
    for i in range(h) :
        for j in range(w) :
            if graph[i][j] and not visit[i][j] :
                q.append((i, j))
                bfs(w, h, visit)
                cnt += 1

    rs.append(cnt)

for r in rs :
    print(r)