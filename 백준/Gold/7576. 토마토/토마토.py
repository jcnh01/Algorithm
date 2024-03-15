import sys
input = sys.stdin.readline

M, N = map(int, input().split())

graph = []

for _ in range(N) :
    a = list(map(int, input().split()))
    graph.append(a)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

from collections import deque
q = deque()

def bfs() :
    while q :
        x, y = q.popleft()
        for i in range(4) :
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < N and 0 <= Y < M and graph[X][Y] == 0 :
                graph[X][Y] = graph[x][y] + 1
                q.append((X, Y))

for y in range(N):
    for x in range(M):
        if graph[y][x] == 1:
            q.append((y, x))

bfs()

result = 0

for y in range(N):
    for x in range(M):
        if graph[y][x] == 0:
            print(-1)
            quit()
        result = max(result, graph[y][x])

print(result-1)