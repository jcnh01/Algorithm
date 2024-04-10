import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

T = int(input())

dx = [-1,0,0,1]
dy = [0,-1,1,0]

result = []

def dfs(y, x, graph, chk, M, N) :
    graph[y][x] = 2
    chk[y][x] = True
    for i in range(4) :
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < M and 0 <= Y < N and not chk[Y][X] and graph[Y][X] == 1:
            dfs(Y, X, graph, chk, M, N)

def logic() :
    M, N, K = map(int, input().split()) # M = 가로, N = 세로, K는 위치의 개수
    graph = [[0] * (M+1) for i in range(N+1)]
    chk = [[False] * (M+1) for i in range(N+1)]

    for _ in range(K) :
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    cnt = 0
    global result

    for i in range(M) :
        for j in range(N) :
            if graph[j][i] == 1 :
                dfs(j, i, graph, chk, M, N)
                cnt += 1

    result.append(cnt)


for i in range(T) :
    logic()

for res in result :
    print(res)