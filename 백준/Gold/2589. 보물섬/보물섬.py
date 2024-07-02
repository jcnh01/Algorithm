import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().split())

words = []

for i in range(N) :
    word = list(map(str, input().strip()))
    words.append(word)

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

q = deque()

def bfs() :
    cnt = 0
    while q : 
        y, x = q.popleft()
        for i in range(4) :
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < M and 0 <= Y < N and visit[Y][X] == False and words[Y][X] == 'L':
                visit[Y][X] = True
                graph[Y][X] = graph[y][x] + 1
                cnt = max(cnt, graph[Y][X])
                q.append((Y, X))
    return cnt

result = 0

for i in range(N) :
    for j in range(M) :
        if words[i][j] == 'L' :
            graph = [[0] * M for _ in range (N)]
            visit = [[False] * M for _ in range (N)]
            visit[i][j] = True
            q.append((i, j))
            temp = bfs()
            result = max(result, temp)

print(result)