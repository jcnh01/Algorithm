import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

M, N = map(int, input().split())

numbers = []
visit = [[False] * N for _ in range(M)]

for _ in range(M) :
    num = list(map(int, input().split()))
    numbers.append(num)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(y, x) :
    for i in range(8) :
        X = dx[i] + x
        Y = dy[i] + y
        if 0 <= X < N and 0 <= Y < M :
            if not visit[Y][X] and numbers[Y][X] :
                visit[Y][X] = True
                dfs(Y, X)

cnt = 0

for i in range(M) :
    for j in range(N) :
        if numbers[i][j] and not visit[i][j] :
            visit[i][j] = True
            dfs(i, j)
            cnt += 1

print(cnt)