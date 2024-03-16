import sys
import copy
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())

graph = []

for _ in range(N):
    row = list(map(str, sys.stdin.readline().rstrip()))
    graph.append(row)   

graph2 = copy.deepcopy(graph)

dy=[0,1,-1,0]
dx=[1,0,0,-1]

def dfs(x, y, color) :
    graph[x][y] = '0'
    for i in range(4) :
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < N and 0 <= Y < N and graph[X][Y] == color:
            dfs(X, Y, color)
        
def dfs2(x, y, color) :
    graph2[x][y] = '0'
    for i in range(4) :
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < N and 0 <= Y < N and graph2[X][Y] == color:
            dfs2(X, Y, color)

cnt = 0

for x in range(N) :
    for y in range(N) :
        if graph[x][y] != '0' :
            dfs(x, y, graph[x][y])
            cnt += 1

cnt2 = 0

for x in range(N) :
    for y in range(N) :
        if graph2[x][y] == 'R' :
            graph2[x][y] = 'G'

for x in range(N) :
    for y in range(N) :
        if graph2[x][y] != '0' :
            dfs2(x, y, graph2[x][y])
            cnt2 += 1

print(cnt, end = " ")
print(cnt2)