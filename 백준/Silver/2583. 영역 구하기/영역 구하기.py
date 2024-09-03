import sys
input = sys.stdin.readline
from collections import deque

M, N, K = map(int, input().split())

graph = [[0] * N for _ in range(M)]

for _ in range(K) :
    x, y, X, Y = list(map(int, input().split()))
    for i in range(Y - y) :
        for j in range(X - x) :
            graph[y+i][x+j] = 1

q = deque()

cnt = 0
rs = []

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

visit = [[False] * N for _ in range(M)]

def bfs() :
    a = 0
    while q :
        y, x = q.popleft()
        for i in range(4) :
            Y, X = y + dy[i], x + dx[i]
            if 0 <= Y < M and 0 <= X < N and not visit[Y][X] and not graph[Y][X] :
                a += 1
                visit[Y][X] = True
                q.append((Y, X))
    if not a :
        return 1
    return a

for i in range(M) :
    for j in range(N) :
        if graph[i][j] == 0 and not visit[i][j]:
            q.append((i, j))
            cnt += 1
            a = bfs()
            rs.append(a)

print(cnt)
rs.sort()

for i in rs :
    print(i, end = " ")