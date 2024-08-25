import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = []
for i in range(N) :
    graph.append(list(map(int, input().split())))

q = deque()

visit = [[False] * M for _ in range(N)] 

def bfs() :
    while q :
        y, x = q.popleft()
        dy = [-1, 0, 0, 1]
        dx = [0, -1, 1, 0]
        for i in range(4) :
            Y, X = y + dy[i], x + dx[i]
            if 0 <= Y < N and 0 <= X < M and not visit[Y][X] and graph[Y][X] == 1 :
                graph[Y][X] = graph[y][x] + 1
                q.append((Y, X))
                visit[Y][X] = True

st = True

for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 2 :
            graph[i][j] = 0
            q.append((i, j))
            visit[i][j] = True
            bfs()
            st = False
            break
    if not st :
        break
    
for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 1 and not visit[i][j] :
            graph[i][j] = -1

for i in range(N) :
    for j in range(M) :
        print(graph[i][j], end = " ")
    print()