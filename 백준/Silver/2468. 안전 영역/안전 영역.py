import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
numbers = []

for i in range(n) :
    numbers.append(list(map(int, input().split())))

max_height = 0

for i in range(n) :
    for j in range(n) :
        max_height = max(max_height, numbers[i][j])

dx = [-1,0,0,1]
dy = [0,-1,1,0]

def dfs(y, x, height) :
    chk[y][x] = True
    for i in range(4) :
        X = x + dx[i]
        Y = y + dy[i]
        if 0 <= X < n and 0 <= Y < n and numbers[Y][X] > height and not chk[Y][X]:
            dfs(Y, X, height)

max_cnt = 0

for height in range(max_height) :
    chk = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n) :
        for j in range(n) :
            if numbers[i][j] > height and not chk[i][j]:
                dfs(i, j, height)
                cnt += 1
    max_cnt = max(max_cnt, cnt)
            
print(max_cnt)