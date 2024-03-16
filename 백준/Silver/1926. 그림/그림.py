import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dy=[0,1,-1,0]
dx=[1,0,0,-1]

def dfs(x, y, cnt) :
    graph[y][x] = 0
    for i in range(4) :
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < m and 0 <= Y < n and graph[Y][X] :
            cnt = dfs(X, Y, cnt+1)
    return cnt

result = []
result_cnt = 0

for i in range(m) :
    for j in range(n) :
        if graph[j][i] == 1 :
            result.append(dfs(i, j, 1))
            result_cnt += 1

print(result_cnt)
if result:
    print(max(result))
else:
    print(0)