import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = []

for i in range(N) :
    number = list(map(int, input().rstrip()))
    numbers.append(number)

graph = [[0] * M for i in range(N)]

dx=[0,1,-1,0]
dy=[1,0,0,-1]

from collections import deque
q = deque()

def bfs() :
    while q:
        y, x = q.popleft()
        for i in range(4) :
            Y = y + dy[i]
            X = x + dx[i]
            if 0 <= Y < N and 0 <= X < M and numbers[Y][X] == 1:
                numbers[Y][X] = 0
                graph[Y][X] = graph[y][x] + 1
                q.append((Y, X))

numbers[0][0] = 0
q.append((0, 0))
bfs()

print(graph[N-1][M-1] +1)