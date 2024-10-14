import sys
input = sys.stdin.readline
from collections import deque
q = deque()

R, C = map(int, input().split())

graph = []
for _ in range(R) :
    graph.append(list(map(str, input().rstrip())))

visit = [[False] * C for _ in range(R)]

dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

k_rs = 0
v_rs = 0

def bfs() :
    global k_rs, v_rs
    v_count = 0
    k_count = 0
    while q :
        y, x = q.popleft()
        if graph[y][x] == "v" :
            v_count += 1
        elif graph[y][x] == "k" :
            k_count += 1
        for i in range(4) :
            Y, X = y + dy[i], x + dx[i]
            if 0 <= Y < R and 0 <= X < C and not visit[Y][X] and graph[Y][X] != "#" :
                visit[Y][X] = True
                q.append((Y, X))
    if k_count > v_count :
        k_rs += k_count
    else :
        v_rs += v_count

for i in range(R) :
    for j in range(C) :
        if graph[i][j] != "#" and not visit[i][j] :
            visit[i][j] = True
            q.append((i, j))
            bfs()

print(k_rs, v_rs)