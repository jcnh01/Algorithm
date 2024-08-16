import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

from collections import deque
q = deque()

t = int(input())

def bfs() :
    while q :
        global N, graph, visit, A, B
        y, x = q.popleft()
        dx = [-2, -1, 1, 2, 2, 1, -1, -2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        for i in range(8) :
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= X < N and 0 <= Y < N and not visit[Y][X] :
                graph[Y][X] = graph[y][x] + 1
                visit[Y][X] = True
                q.append((Y, X))
                if Y == B and X == A :
                    q.clear()

def find() :
    global N, graph, visit, A, B
    N = int(input())

    visit = [[False] * N for _ in range(N)]
    graph = [[0] * N for _ in range(N)]

    a, b = map(int, input().split())
    A, B = map(int, input().split())

    q.append((b, a))
    visit[b][a] = True

    bfs()

    print(graph[B][A])

for i in range(t) :
    find()