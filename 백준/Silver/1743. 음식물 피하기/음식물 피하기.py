import sys

n, m, k = map(int, sys.stdin.readline().split())

graph = [([0] * (m+1))for _ in range(n+1)]

for i in range(k) :
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1

from collections import deque
q = deque()

dy=[0,1,-1,0]
dx=[1,0,0,-1]

def bfs(y, x) :
    cnt = 1
    q.append((y, x))
    graph[y][x] = 0
    while q :
        y, x = q.popleft()
        for i in range(4) :
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < m+1 and 0 <= Y < n+1 and graph[Y][X] :
                graph[Y][X] = 0
                q.append((Y, X))
                cnt += 1
    return cnt

li_cnt = []

for i in range(1, m+1) :
    for j in range(1, n+1) :
        if graph[j][i] == 1 :
            li_cnt.append(bfs(j, i))

print(max(li_cnt))