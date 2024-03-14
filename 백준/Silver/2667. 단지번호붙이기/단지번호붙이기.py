import sys

N = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(x, y, cnt):
    graph[y][x] = 0
    for i in range(4):
        X, Y = x + dx[i], y + dy[i]
        if 0 <= X < N and 0 <= Y < N and graph[Y][X]:
            cnt = dfs(X, Y, cnt+1)
    return cnt

cnt_arr = []

for y in range(N):
    for x in range(N):
        if graph[y][x] == 1:
            cnt_arr.append(dfs(x, y, 1))

cnt_arr.sort()

print(len(cnt_arr))

for cnt in cnt_arr:
    print(cnt)