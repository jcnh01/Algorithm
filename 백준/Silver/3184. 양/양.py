import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N) :
    graph.append(list(map(str, input().rstrip())))

visit = [[False] * M for _ in range(N)]
q = deque()

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

v_rs = 0
o_rs = 0

def bfs() :
    global v_rs, o_rs
    v_cnt = 0
    o_cnt = 0
    while q :
        y, x = q.popleft()
        if graph[y][x] == "v" :
            v_cnt += 1
        elif graph[y][x] == "o" :
            o_cnt += 1
        for i in range(4) :
            Y, X = y + dy[i], x + dx[i]
            if 0 <= Y < N and 0 <= X < M and not visit[Y][X] and graph[Y][X] != "#" :
                visit[Y][X] = True
                q.append((Y, X))
    if not v_cnt and not o_cnt :
        return
    if v_cnt >= o_cnt :
        v_rs += v_cnt
    else :
        o_rs += o_cnt

for i in range(N) :
    for j in range(M) :
        if graph[i][j] != "#" and not visit[i][j] :
            visit[i][j] = True
            q.append((i, j))
            bfs()

print(o_rs, v_rs)