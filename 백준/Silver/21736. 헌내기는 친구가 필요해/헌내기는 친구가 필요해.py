import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N) :
    graph.append(list(map(str, input().rstrip())))

q = deque()

visit = [[False] * M for _ in range(N)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
answer = 0

def bfs() :
    while q :
        global answer
        y, x = q.popleft()
        for i in range(4) :
            Y, X = y + dy[i], x + dx[i]
            if 0 <= Y < N and 0 <= X < M and not visit[Y][X] and graph[Y][X] != 'X' :
                visit[Y][X] = True
                q.append((Y, X))
                if graph[Y][X] == 'P' :
                    answer += 1

for i in range(N) :
    for j in range(M) :
        if graph[i][j] == 'I' :
            visit[i][j] = True
            q.append((i, j))
            bfs()

if not answer :
    print('TT')
else :
    print(answer)