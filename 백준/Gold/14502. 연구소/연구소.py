import sys
input = sys.stdin.readline
from itertools import combinations
import copy
from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N) :
    graph.append(list(map(int, input().split())))

block = []

for i in range(N) :
    for j in range(M) :
        if not graph[i][j] :
            block.append((i, j))

li = list(combinations(block, 3))

q = deque()

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

rs = 0

def bfs(visit, graph2, cnt) :
    while q :
        y, x = q.popleft()
        for i in range(4) :
            Y, X = y + dy[i], x + dx[i]
            if 0 <= Y < N and 0 <= X < M and not visit[Y][X] and (graph2[Y][X] == 2 or not graph2[Y][X]) :
                visit[Y][X] = True
                graph2[Y][X] = 2
                q.append((Y, X))
    return cnt

for l in li:
    cnt = 0
    graph2 = copy.deepcopy(graph)
    visit = [[False] * M for _ in range(N)]
    for a in l :
        graph2[a[0]][a[1]] = 1
    for i in range(N) :
        for j in range(M) :
            if graph2[i][j] == 2 and not visit[i][j] :
                q.append((i, j))
                visit[i][j] = True
                bfs(visit, graph2, cnt)

    for i in range(N) :
        for j in range(M) :
            if not graph2[i][j] :
                cnt += 1
    rs = max(rs, cnt)

print(rs)