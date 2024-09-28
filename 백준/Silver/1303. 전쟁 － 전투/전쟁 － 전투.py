import sys
input = sys.stdin.readline
from collections import deque
q = deque()

N, M = map(int, input().split())

graph = []

for _ in range(M) :
    graph.append(list(map(str, input().rstrip())))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

visit = [[False] * N for _ in range(M)]

def bfs_w(cnt) :
    while q :
        y, x = q.popleft()
        cnt += 1
        for i in range(4) :
            Y, X = y + dy[i], x + dx[i]
            if 0 <= Y < M and 0 <= X < N and not visit[Y][X] and graph[Y][X] == 'W' :
                visit[Y][X] = True
                q.append((Y, X))
    return cnt

cnt_w = 0

for i in range(M) :
    for j in range(N) :
        if graph[i][j] == 'W' and not visit[i][j] :
            cnt = 0
            q.append((i, j))
            visit[i][j] = True
            rs = bfs_w(cnt)
            cnt_w += rs ** 2

def bfs_b(cnt) :
    while q :
        y, x = q.popleft()
        cnt += 1
        for i in range(4) :
            Y, X = y + dy[i], x + dx[i]
            if 0 <= Y < M and 0 <= X < N and not visit[Y][X] and graph[Y][X] == 'B' :
                visit[Y][X] = True
                q.append((Y, X))
    return cnt

cnt_b = 0

for i in range(M) :
    for j in range(N) :
        if graph[i][j] == 'B' and not visit[i][j] :
            cnt = 0
            visit[i][j] = True
            q.append((i, j))
            rs = bfs_b(cnt)
            cnt_b += rs * rs

print(cnt_w, cnt_b)