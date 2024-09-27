import sys
input = sys.stdin.readline
from collections import deque
q = deque()

N = int(input())

graph = [[0] * N for _ in range(N)]

r1, c1, r2, c2 = map(int, input().split())

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

q.append((c1, r1, 0))

rs = -1

graph[c1][r1] = 1

while q :
    y, x, cnt = q.popleft()
    if y == c2 and x == r2 :
        rs = cnt
        break
    for i in range(6) :
        Y, X = y + dy[i], x + dx[i]
        if 0 <= Y < N and 0 <= X < N and graph[Y][X] == 0 :
            graph[Y][X] = 1
            q.append((Y, X, cnt + 1))

if r1 == r2 and c1 == c2 :
    print(0)
else :
    print(rs)